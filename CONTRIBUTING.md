# Contributing to Model Router Registry

[English](#english) | [中文](#中文)

---

# English

Thank you for contributing to the Model Router Hub Provider Registry.

Model Router Hub is an open registry for discovering and comparing AI model providers.

Provider operators and community contributors are welcome to submit new providers or update existing provider information.

## What you can submit

You may submit public and verifiable provider information, including:

- Provider name
- Official website
- Registration URL
- Pricing URL
- Operating region
- API regions
- Supported protocols
- Supported models
- Model identifiers
- Public pricing
- Mainland China accessibility
- Proxy requirements

## What providers cannot submit

Providers must not submit or modify their own:

- Ranking
- Overall score
- Benchmark score
- Success rate
- Latency
- P50 / P95
- Stability score
- Verified status
- Recommended status

These metrics are generated independently by Model Router Hub benchmark systems.

**Providers provide information. Model Router Hub provides evaluation.**

## How to add a provider

1. Fork this repository.
2. Copy:

   `providers/example-provider.yaml`

3. Rename the file using your Provider ID, for example:

   `providers/example-ai.yaml`

4. Complete the Provider information.
5. Submit a Pull Request.
6. Automated validation will check the submitted data.
7. Model Router Hub maintainers will review the Pull Request.

## Provider ID rules

Provider IDs must:

- Use lowercase letters
- Use numbers when necessary
- Use hyphens instead of spaces
- Be unique

Examples:

`example-provider`

`abc-ai`

`router-123`

## Pricing

Pricing submitted by providers must reflect publicly available pricing.

Whenever possible, include an official pricing URL.

Provider-declared pricing may be displayed separately from independently observed benchmark data.

## Registration and payment

Registration, payment and account management take place on the Provider's own website.

Model Router Hub does not:

- Sell AI credits
- Resell model usage
- Process Provider payments
- Hold customer balances
- Store customer Provider API keys

## API Keys

Never submit API keys, secrets, passwords, tokens, credentials or other private information to this repository.

Users configure their own API keys inside their own self-hosted Model Router.

## Accuracy

Submitted information should be accurate and verifiable.

Providers and community contributors are encouraged to update entries when:

- Pricing changes
- Models are added or removed
- API endpoints change
- Service regions change
- Provider status changes

## Review

Submission does not guarantee listing.

Model Router Hub maintainers may reject, request changes to, suspend or remove entries that are:

- Incorrect
- Misleading
- Duplicate
- Unverifiable
- Malicious
- Abandoned
- Incompatible with the Registry Schema

## Disclaimer

Third-party Providers are independently operated.

Listing in Model Router Hub does not constitute endorsement, warranty or guarantee of a Provider's service quality, availability, legality or security.

---

# 中文

感谢你参与 Model Router Hub Provider Registry。

Model Router Hub 是一个用于发现、比较和连接 AI 模型服务商的开放 Registry。

我们欢迎 Provider 运营方以及社区贡献者提交新的 Provider，或更新已有 Provider 的公开信息。

## 可以提交的信息

可以提交公开且可验证的 Provider 信息，包括：

- Provider 名称
- 官方网站
- 注册链接
- 价格页面
- 运营地区
- API 服务地区
- 支持协议
- 支持模型
- 模型 ID
- 公开价格
- 中国大陆是否可直连
- 是否需要代理

## Provider 不允许自行提交的数据

Provider 不得自行填写或修改以下数据：

- 排名
- 综合评分
- Benchmark 分数
- 成功率
- 延迟
- P50 / P95
- 稳定性评分
- Verified 状态
- 推荐状态

这些指标由 Model Router Hub 的独立 Benchmark 系统产生。

**Provider 提供资料，Model Router Hub 提供评价。**

## 如何提交 Provider

1. Fork 本仓库。
2. 复制：

   `providers/example-provider.yaml`

3. 使用你的 Provider ID 重命名文件，例如：

   `providers/example-ai.yaml`

4. 填写 Provider 信息。
5. 提交 Pull Request。
6. GitHub 自动校验提交数据。
7. 等待 Model Router Hub 维护者审核。

## Provider ID 规则

Provider ID 必须：

- 使用小写英文字母
- 必要时可以包含数字
- 使用 `-` 代替空格
- 全局唯一

例如：

`example-provider`

`abc-ai`

`router-123`

## 价格

Provider 提交的价格必须与公开价格一致。

建议同时提供官方价格页面。

Provider 自己声明的价格，可以与 Model Router Hub 独立实测价格分开显示。

## 注册与充值

用户注册、充值以及账号管理，均在 Provider 自己的官方网站完成。

Model Router Hub 不：

- 销售 AI 额度
- 转售模型调用
- 代收 Provider 费用
- 保存用户余额
- 保存用户的 Provider API Key

## API Key

请勿向本仓库提交：

- API Key
- Secret
- Password
- Token
- Credential
- 其他任何私密信息

用户应当把自己的 API Key 配置在自己部署的 Model Router 中。

## 数据准确性

提交的信息应当真实、准确并且可以验证。

以下信息发生变化时，Provider 或社区贡献者应及时更新：

- 价格
- 模型
- API Endpoint
- 服务地区
- Provider 状态

## 审核

提交并不代表一定会被收录。

对于以下情况，Model Router Hub 维护者有权要求修改、拒绝、暂停或移除：

- 信息错误
- 误导性信息
- 重复 Provider
- 无法验证
- 恶意提交
- 长期无人维护
- 不符合 Registry Schema

## 免责声明

第三方 Provider 均由其各自独立运营。

被 Model Router Hub 收录，不代表 Model Router Hub 对该 Provider 的服务质量、可用性、合法性或安全性作出背书、保证或担保。
