# Model Router Hub Evidence

[English](#english) | [中文](#中文)

---

# English

## What is Evidence?

The `evidence/` directory stores public sources and review records used to support information published in the Model Router Registry.

Evidence is separate from:

- Provider-submitted registry data
- Model Router Hub benchmark data
- User reviews

The purpose of Evidence is traceability.

## Directory structure

```text
evidence/

└── providers/
    ├── easyrouter.md
    ├── example-provider.md
    └── ...
```

Each Provider should use:

```text
evidence/providers/<provider-id>.md
```

The filename must match the Provider ID.

Example:

```text
Provider ID:
easyrouter

Evidence:
evidence/providers/easyrouter.md
```

## Evidence may support

Evidence may be used to verify:

- Official website
- Registration URL
- Pricing URL
- Documentation URL
- API Base URL
- Authentication method
- Supported models
- Upstream model IDs
- Public pricing
- Availability
- Service regions
- Mainland China accessibility
- Public Provider policies

## Evidence cannot define

Evidence files must not be used to manually assign:

- Ranking
- Overall score
- Benchmark score
- Success rate
- Latency
- P50 / P95
- Stability score
- Verified status
- Recommended status

These metrics belong to the independent Model Router Hub benchmark system.

## Source priority

Prefer sources in this order:

1. Official Provider documentation
2. Official Provider pricing page
3. Official Provider website
4. Official Provider announcement
5. Public API response or reproducible test
6. Other reliable public sources

Community posts, screenshots and third-party discussions may be useful as supporting material, but should not replace official sources when official information exists.

## Review date

Every Evidence file should include:

```text
Last reviewed: YYYY-MM-DD
```

Provider information changes frequently.

Evidence should be reviewed again when:

- Pricing changes
- Models change
- API endpoints change
- Provider policies change
- Availability changes
- Existing information is disputed

## Provider data vs Benchmark data

Provider Registry data answers:

> What does the Provider publicly claim or document?

Benchmark data answers:

> What did Model Router Hub independently observe?

These must remain separate.

> **Provider information is sourced. Performance is measured.**

---

# 中文

## Evidence 是什么？

`evidence/` 用来保存支持 Model Router Registry 公开数据的来源与审核记录。

Evidence 与以下数据相互独立：

- Provider 自己提交的 Registry 数据
- Model Router Hub 独立 Benchmark 数据
- 用户评价

它最重要的作用是：

> **可追溯。**

以后有人问：

“为什么 EasyRouter 的 MiniMax H3 写这个价格？”

我们可以直接找到对应 Evidence。

## 目录结构

统一使用：

```text
evidence/

└── providers/
    ├── easyrouter.md
    ├── example-provider.md
    └── ...
```

每一家 Provider 对应：

```text
evidence/providers/<provider-id>.md
```

文件名必须和 Provider ID 一致。

例如：

```text
Provider ID：
easyrouter

Evidence：
evidence/providers/easyrouter.md
```

## Evidence 可以证明什么？

Evidence 可以用于支持：

- 官方网站
- 注册链接
- 价格页面
- API 文档
- API Base URL
- 鉴权方式
- 支持模型
- Provider 实际模型 ID
- 公开价格
- 可用状态
- 服务地区
- 中国大陆是否可访问
- Provider 公开政策

## Evidence 不能决定什么？

Evidence 文件不得人工填写或决定：

- 排名
- 综合评分
- Benchmark 分数
- 成功率
- 延迟
- P50 / P95
- 稳定性评分
- Verified 状态
- 推荐状态

这些数据属于 Model Router Hub 的独立 Benchmark 系统。

## 来源优先级

优先采用：

1. Provider 官方 API 文档
2. Provider 官方价格页面
3. Provider 官方网站
4. Provider 官方公告
5. 可复现的公开 API 测试
6. 其他可信公开来源

社区帖子、截图、论坛讨论可以作为辅助信息，但如果存在官方资料，不应使用第三方资料代替官方资料。

## 审核日期

每一份 Evidence 都应包含：

```text
Last reviewed: YYYY-MM-DD
```

因为 Provider 信息变化很快。

出现以下情况时应重新审核：

- 价格变化
- 新增或删除模型
- API Endpoint 改变
- Provider 政策改变
- 可用状态改变
- 有人质疑现有数据

## Provider 数据与 Benchmark 数据

Provider Registry 回答的是：

> Provider 官方公开说了什么？

Benchmark 回答的是：

> Model Router Hub 实际测到了什么？

两者必须分开。

> **Provider 信息有来源，性能数据靠实测。**
