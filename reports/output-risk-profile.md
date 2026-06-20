# Output Risk Profile

Skill: `advantage-filter`  
Mode: Local

## Primary output risks

| Risk | Failure mode | Guardrail |
| --- | --- | --- |
| 空泛人设 | 把用户材料包装成“温暖、通透、有力量”之类的漂亮词 | 抽象特质必须转成内容表达、用户收益、产品/服务线索或验证动作 |
| 伪市场需求 | 把用户想做账号、想卖服务当成市场会买 | 每个定位判断必须指出需求证据或需求缺口 |
| 过度完整方案 | 信息不足时仍输出完整定位资产 | 低证据时降级为反证诊断卡或最小追问卡 |
| 叙事滥用 | 强行制造谷底、卖惨或夸大经历 | 反差叙事是放大器，不是必经路径；没有真实证据不做主叙事 |
| 标签稀释 | 同时推荐多个主标签，导致账号训练失败 | 早期只保留一个主标签，副标签必须等主标签稳定后扩展 |
| 商业跳步 | 直接设计课程、产品或高价服务 | 先确认需求、信任路径和交付证据，再谈产品化 |
| 缺验证动作 | 输出定位语但没有下一步 | 每个判断卡必须包含 1-3 个最小验证动作和通过/停止信号 |

## High-risk prompt patterns

- “我不知道适合做什么账号”但没有经历、反馈或服务对象。
- “我很自信/通透/坚韧”但没有可展示外显物。
- “我经历很多”但每个方向都没有需求证据。
- “帮我做完整方案”但缺少信任证据、需求证据或交付能力。
- “怎么涨粉/起号/爆款”实际是平台运营请求，不是定位判断。

## Required downgrade behavior

When trust evidence, demand evidence, or delivery evidence is missing, output must mark recommendations as:

- `confirmed`: directly supported by user material or external feedback.
- `hypothesis`: plausible but unverified.
- `needs validation`: cannot be used as main positioning until tested.

## Missing evidence

- Blind review status: `missing evidence`
- Historical pass rate: `missing evidence`
- Telemetry: `missing evidence`
