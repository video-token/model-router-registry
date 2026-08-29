from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "provider.schema.json"
PROVIDERS_DIR = ROOT / "providers"


def main():
    with SCHEMA_PATH.open("r", encoding="utf-8") as f:
        schema = json.load(f)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker()
    )

    files = sorted(PROVIDERS_DIR.glob("*.yaml"))

    if not files:
        print("ERROR: No provider YAML files found.")
        return 1

    failed = False
    provider_ids = {}

    for file_path in files:
        print(f"\nValidating: {file_path.relative_to(ROOT)}")

        try:
            with file_path.open("r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except Exception as exc:
            print(f"  ERROR: Invalid YAML: {exc}")
            failed = True
            continue

        if not isinstance(data, dict):
            print("  ERROR: Provider file must contain a YAML object.")
            failed = True
            continue

        errors = sorted(
            validator.iter_errors(data),
            key=lambda e: list(e.absolute_path)
        )

        if errors:
            failed = True

            for error in errors:
                path = ".".join(str(x) for x in error.absolute_path)
                location = path if path else "<root>"
                print(f"  ERROR [{location}]: {error.message}")

            continue

        provider_id = data.get("id")

        if provider_id in provider_ids:
            print(
                f"  ERROR: Duplicate provider id '{provider_id}'. "
                f"Already used by {provider_ids[provider_id]}"
            )
            failed = True
            continue

        provider_ids[provider_id] = file_path.name

        expected_filename = f"{provider_id}.yaml"

        if file_path.name != expected_filename:
            print(
                f"  ERROR: File name must match provider id. "
                f"Expected '{expected_filename}', got '{file_path.name}'."
            )
            failed = True
            continue

        print("  OK")

    print("\n----------------------------------------")

    if failed:
        print("Provider registry validation FAILED.")
        return 1

    print(
        f"Provider registry validation PASSED. "
        f"{len(files)} provider file(s) validated."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
