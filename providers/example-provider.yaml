schema_version: "0.2"

id: example-provider
name: Example Provider

description: Example AI model provider entry for Model Router Hub.

website: https://example.com
register_url: https://example.com/register
pricing_url: https://example.com/pricing
documentation_url: https://example.com/docs

status: active

api_regions:
  - Global

mainland_accessible: true
proxy_required: false

protocols:
  - openai-compatible

auth:
  type: bearer

endpoints:
  - name: Global API
    base_url: https://api.example.com/v1
    region: Global
    protocol: openai-compatible
    status: active

models:
  - canonical_id: example-video-model
    upstream_id: Example-Video-Model

    capabilities:
      - video-generation

    pricing:
      - currency: CNY
        unit: second
        value: 0.09
        availability: available
        source_url: https://example.com/pricing

        conditions:
          resolution: 1080P
          variant: standard
          notes: Example pricing only.
