from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

PROVIDER_SCHEMA_PATH = ROOT / "schema" / "provider.schema.json"
MODEL_SCHEMA_PATH = ROOT / "schema" / "model.schema.json"

PROVIDERS_DIR = ROOT / "providers"
MODELS_DIR = ROOT / "models"


def load_json(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_yaml_file(file_path, validator):
    try:
        data = load_yaml(file_path)
    except Exception as exc:
        print(f"  ERROR: Invalid YAML: {exc}")
        return None, True

    if not isinstance(data, dict):
        print("  ERROR: File must contain a YAML object.")
        return None, True

    errors = sorted(
        validator.iter_errors(data),
        key=lambda e: list(e.absolute_path)
    )

    if errors:
        for error in errors:
            path = ".".join(str(x) for x in error.absolute_path)
            location = path if path else "<root>"
            print(f"  ERROR [{location}]: {error.message}")

        return data, True

    return data, False


def validate_models():
    print("\n=== Validating Model Registry ===")

    schema = load_json(MODEL_SCHEMA_PATH)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker()
    )

    files = sorted(MODELS_DIR.glob("*.yaml"))

    if not files:
        print("ERROR: No model YAML files found.")
        return {}, True

    failed = False
    model_ids = {}

    for file_path in files:
        print(f"\nValidating model: {file_path.relative_to(ROOT)}")

        data, file_failed = validate_yaml_file(file_path, validator)

        if file_failed:
            failed = True
            continue

        model_id = data.get("id")

        if model_id in model_ids:
            print(
                f"  ERROR: Duplicate model id '{model_id}'. "
                f"Already used by {model_ids[model_id]}"
            )
            failed = True
            continue

        model_ids[model_id] = file_path.name

        print("  OK")

    return model_ids, failed


def validate_providers(model_ids):
    print("\n=== Validating Provider Registry ===")

    schema = load_json(PROVIDER_SCHEMA_PATH)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker()
    )

    files = sorted(PROVIDERS_DIR.glob("*.yaml"))

    if not files:
        print("ERROR: No provider YAML files found.")
        return True

    failed = False
    provider_ids = {}

    for file_path in files:
        print(f"\nValidating provider: {file_path.relative_to(ROOT)}")

        data, file_failed = validate_yaml_file(file_path, validator)

        if file_failed:
            failed = True
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

        provider_failed = False

        for index, model in enumerate(data.get("models", [])):
            canonical_id = model.get("canonical_id")

            if canonical_id not in model_ids:
                print(
                    f"  ERROR [models.{index}.canonical_id]: "
                    f"Unknown canonical model id '{canonical_id}'. "
                    f"Add it to models/ before using it in a Provider."
                )
                provider_failed = True

        if provider_failed:
            failed = True
            continue

        print("  OK")

    return failed


def main():
    model_ids, models_failed = validate_models()

    providers_failed = validate_providers(model_ids)

    print("\n----------------------------------------")

    if models_failed or providers_failed:
        print("Model Router Registry validation FAILED.")
        return 1

    print(
        f"Model Router Registry validation PASSED. "
        f"{len(model_ids)} canonical model(s) registered."
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
