# Model Router Registry

[English](#english) | [中文](#中文)

Open registry for AI model providers, models, pricing, regions and capabilities.

Part of the **Model Router Hub** ecosystem.

Official website: https://www.video-token.com

---

# English

## What is Model Router Registry?

Model Router Registry is the public Provider registry used by Model Router Hub.

It contains structured and publicly verifiable information about AI model providers, including:

- Provider information
- Supported models
- Public pricing
- API protocols
- Service regions
- Mainland China accessibility
- Proxy requirements
- Model capabilities

The Registry does **not** store API keys, customer credentials or customer balances.

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
User registers and obtains API Key
      ↓
Self-hosted Model Router
      ↓
XiaoFei / Other AI Applications
```

## Repository structure

```text
model-router-registry/

├── schema/
│   └── provider.schema.json
│
├── providers/
│   └── example-provider.yaml
│
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Provider submissions

Provider operators and community contributors may submit public and verifiable information such as:

- Provider name
- Official website
- Registration URL
- Pricing URL
- Operating region
- API regions
- Supported protocols
- Supported models
- Public pricing
- Mainland China accessibility
- Proxy requirements

## Independent benchmark data

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

## Add your Provider

To submit a Provider, please read:

[CONTRIBUTING.md](./CONTRIBUTING.md)

Start from the example:

`providers/example-provider.yaml`

## Security

Never commit:

- API Keys
- Passwords
- Access Tokens
- Secrets
- Customer Credentials

Users configure their own API keys inside their own self-hosted Model Router.

## Registration and payment

Users register, purchase and recharge directly on third-party Provider websites.

Model Router Hub does not:

- Sell AI credits
- Resell model usage
- Process Provider payments
- Hold customer balances
- Store customer Provider API keys

## License

Registry data is released under the license included in this repository.

---

# 中文

## Model Router Registry 是什么？

Model Router Registry 是 Model Router Hub 使用的公开 Provider 注册库。

它负责维护 AI 模型服务商公开、结构化且可以验证的信息，包括：

- Provider 基本信息
- 支持模型
- 公开价格
- API 协议
- 服务地区
- 中国大陆是否可直连
- 是否需要代理
- 模型能力

Registry **不保存用户 API Key、用户 Credential 或用户余额**。

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
小啡 / 其他 AI 应用
```

## 仓库结构

```text
model-router-registry/

├── schema/
│   └── provider.schema.json
│
├── providers/
│   └── example-provider.yaml
│
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Provider 可以提交的信息

Provider 运营方和社区贡献者可以提交公开且可以验证的信息，例如：

- Provider 名称
- 官方网站
- 注册链接
- 价格页面
- 运营地区
- API 服务地区
- 支持协议
- 支持模型
- 公开价格
- 中国大陆是否可直连
- 是否需要代理

## 独立 Benchmark

Provider 不允许自行提交或修改：

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

## 提交 Provider

如果你是 Provider 运营方或社区贡献者，请先阅读：

[CONTRIBUTING.md](./CONTRIBUTING.md)

可以从示例文件开始：

`providers/example-provider.yaml`

## 安全

请勿向本仓库提交：

- API Key
- Password
- Access Token
- Secret
- Customer Credential

用户自己的 API Key 应配置在用户自己部署的 Model Router 中。

## 注册与充值

用户应直接前往第三方 Provider 官网注册、购买或充值。

Model Router Hub 不：

- 销售 AI 额度
- 转售模型调用
- 代收 Provider 费用
- 保存用户余额
- 保存用户 Provider API Key

## License

Registry 数据按照本仓库中的 License 开放。
