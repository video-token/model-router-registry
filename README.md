# Model Router Registry

[English](#english) | [中文](#中文)

Open registry for AI model providers, canonical models, pricing, regions and capabilities.

Part of the **Model Router Hub** ecosystem.

Official website: https://www.video-token.com

Current Provider Schema: **v0.2**

---

# English

## What is Model Router Registry?

Model Router Registry is the public data registry used by Model Router Hub.

It maintains structured and publicly verifiable information about:

- AI Providers
- Canonical models
- Public pricing
- API protocols
- API endpoints
- Authentication methods
- Service regions
- Model capabilities

The Registry does **not** store customer API Keys, credentials or balances.

## How it works

```text
Model Router Hub
      ↓
Discover / Compare / Benchmark
      ↓
Provider Registry
      ↓
Third-party Provider website
      ↓
User registers, pays and obtains API Key
      ↓
Self-hosted Model Router
      ↓
ArcReel,xiaofei,AIYT9,OpenMontage  / Other AI Applications
```

## Repository structure

```text
model-router-registry/

├── models/
│   ├── example-model.yaml
│   ├── minimax-h3.yaml
│   ├── seedance-2-0.yaml
│   └── gpt-image-2.yaml
│
├── providers/
│   └── example-provider.yaml
│
├── schema/
│   ├── model.schema.json
│   └── provider.schema.json
│
├── scripts/
│   └── validate_providers.py
│
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Provider Schema v0.2

Provider Schema v0.2 supports:

- Provider identity
- Official website
- Registration and pricing URLs
- Documentation URL
- API regions
- Mainland China accessibility
- Proxy requirements
- API protocols
- Authentication method
- Public API endpoints
- Supported models
- Provider-specific upstream model IDs
- Multiple pricing entries per model

## Canonical Models

Model Router Hub uses canonical model IDs.

Example:

```yaml
canonical_id: minimax-h3
upstream_id: MiniMax-H3
```

`canonical_id` is the Model Router Hub standard model identifier.

`upstream_id` is the actual model identifier used by a Provider.

This allows different Providers to expose different upstream names while Model Router uses one common model ID.

## Pricing

Provider Schema v0.2 supports multiple prices for the same model.

Example:

```yaml
pricing:
  - currency: USD
    unit: second
    value: 0.13
    availability: available

    conditions:
      resolution: 2K
      variant: standard

  - currency: USD
    unit: second
    value: 0.09
    availability: unavailable

    conditions:
      resolution: 768P
```

This allows Model Router Hub to compare pricing by:

- Resolution
- Quality
- Variant
- Duration
- Availability

## Independent Benchmark

Providers may submit public Provider information.

Providers cannot submit or modify their own:

- Ranking
- Overall score
- Benchmark score
- Success rate
- Latency
- P50 / P95
- Stability score
- Verified status
- Recommended status

These metrics are generated independently by Model Router Hub.

> **Providers provide information. Model Router Hub provides evaluation.**

## Security

Never commit:

- API Keys
- Passwords
- Access Tokens
- Secrets
- Private Credentials
- Customer information

Users configure their own Provider API Keys inside their own self-hosted Model Router.

## Registration and payment

Users register, purchase and recharge directly on third-party Provider websites.

Model Router Hub does not:

- Sell AI credits
- Resell model usage
- Process Provider payments
- Hold customer balances
- Store customer Provider API Keys

## Add your Provider

See:

[CONTRIBUTING.md](./CONTRIBUTING.md)

Start with:

`providers/example-provider.yaml`

---

# 中文

## Model Router Registry 是什么？

Model Router Registry 是 Model Router Hub 使用的公开数据注册库。

它负责维护公开、结构化且可以验证的数据，包括：

- AI Provider
- 标准模型
- 公开价格
- API 协议
- API Endpoint
- 鉴权方式
- 服务地区
- 模型能力

Registry **不保存用户 API Key、Credential 或用户余额**。

## 工作方式

```text
Model Router Hub
      ↓
发现 / 比较 / 跑分
      ↓
Provider Registry
      ↓
第三方 Provider 官网
      ↓
用户自行注册、充值并获得 API Key
      ↓
用户自部署 Model Router
      ↓
ArcReel,xiaofei,AIYT9,OpenMontage / 其他一键成片或 AI 应用
```

## Provider Schema v0.2

当前 Provider Schema 版本：

`0.2`

v0.2 可以描述：

- Provider 基本资料
- 官方网站
- 注册链接
- 价格页面
- API 文档
- API 服务地区
- 中国大陆是否可直连
- 是否需要代理
- API 协议
- 鉴权方式
- API Base URL
- 支持模型
- Provider 实际模型 ID
- 一个模型的多档价格

## Canonical Model

Model Router Hub 使用统一的标准模型 ID。

例如：

```yaml
canonical_id: minimax-h3
upstream_id: MiniMax-H3
```

其中：

`canonical_id`

是 Model Router Hub 定义的标准模型 ID。

`upstream_id`

是 Provider API 实际使用的模型名称。

因此不同 Provider 即使模型名称不同，也可以统一映射到同一个标准模型。

## 多档价格

Schema v0.2 支持同一个模型存在不同价格：

```yaml
pricing:
  - currency: USD
    unit: second
    value: 0.13
    availability: available

    conditions:
      resolution: 2K
      variant: standard
```

未来可以按照：

- 分辨率
- 画质
- 模型版本
- 时长
- 可用状态

分别比较价格。

## 独立 Benchmark

Provider 可以提交公开资料，但不能自行提交或修改：

- 排名
- 综合评分
- Benchmark 分数
- 成功率
- 延迟
- P50 / P95
- 稳定性评分
- Verified 状态
- 推荐状态

这些数据由 Model Router Hub 独立 Benchmark 系统产生。

> **Provider 提供资料，Model Router Hub 提供评价。**

## 安全

严禁向 Registry 提交：

- API Key
- Password
- Access Token
- Secret
- 私有 Credential
- 客户信息

用户自己的 Provider API Key 只配置在用户自己部署的 Model Router 中。

## 注册与充值

用户直接前往第三方 Provider 官网：

```text
注册
 ↓
充值
 ↓
获得 API Key
 ↓
填写到自己的 Model Router
```

Model Router Hub 不：

- 销售 AI 额度
- 转售模型调用
- 代收 Provider 费用
- 保存用户余额
- 保存用户 Provider API Key

## 提交 Provider

请阅读：

[CONTRIBUTING.md](./CONTRIBUTING.md)

提交模板：

`providers/example-provider.yaml`
