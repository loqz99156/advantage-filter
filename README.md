# 个人优势定位方法 Skill

把真实经历、稳定能力和高频被求助场景，过滤成可验证、可内容化、可商业承接的个人优势定位。

这个 skill 适合个人 IP、自媒体账号、知识服务、咨询服务和个人品牌定位。它不帮你包装一个好听的人设，而是先判断目标市场、需求证据和信任路径，再决定什么优势值得成为主定位。

## 它解决什么问题

很多定位问题不是表达问题，而是证据问题：

- 你有很多经历，但不知道哪一段能变成内容资产。

- 你知道自己有优势，但说出来像抽象形容词。

- 账号内容很散，用户和平台都记不住你。

- 你想做咨询、服务、课程或陪跑，但不确定谁会买单。

- 你有一个方向，但缺少需求证据、信任证据或商业承接路径。

Advantage Filter 会把定位拆成四个硬条件：

```text
真实支点 × 可识别需求 × 内容证明 × 商业承接
```

它会优先判断方向是否成立，而不是直接输出漂亮标签。

## 适用场景

适合用它处理：

- 个人 IP 定位

- 自媒体账号定位

- 小红书、抖音、视频号、公众号、X/Twitter 等账号的主标签判断

- 知识服务、咨询服务、陪跑服务的定位初筛

- 个人经历、能力、行业经验、审美判断的优势提炼

- 内容太散、商业路径不清、受众不清的问题诊断

- 主页简介、一句话定位、账号表达的局部改写

不适合用它处理：

- 纯流量打法、爆款标题、平台运营技巧

- 心理测评或职业性格测试

- 情绪疗愈类咨询

- 没有任何市场验证的直接产品包装

- 虚构谷底、夸大履历、包装脆弱经历

## 安装

### Claude Code：安装到个人 skills

适合你想在 Claude Code 的所有项目里使用这个 skill。

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/loqz99156/advantage-filter.git ~/.claude/skills/advantage-filter
```

### Claude Code：安装到当前项目

适合你只想在某个 Claude Code 项目里使用它。

```bash
mkdir -p .claude/skills
git clone https://github.com/loqz99156/advantage-filter.git .claude/skills/advantage-filter
```

### Codex：安装到个人 skills

适合你想在 Codex 里使用同一套定位方法。

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/loqz99156/advantage-filter.git ~/.agents/skills/advantage-filter
```

仓库地址已经指向 `loqz99156/advantage-filter`。

安装后，重新打开 Claude Code 或 Codex，或开启一个新会话，让客户端重新发现本地 skills。

## 使用方法

### Claude Code

在 Claude Code 里直接调用：

```text
/advantage-filter 我是一名 B2B SaaS 产品顾问，想做个人 IP，过去主要帮创业公司梳理增长和产品定价，怎么定位？
```

也可以用自然语言提出局部问题：

```text
/advantage-filter 帮我判断“AI 工作流顾问”这个定位能不能做
```

```text
/advantage-filter 我现在内容很散，既讲职业成长，又讲 AI 工具，还讲读书，帮我收敛主标签
```

```text
/advantage-filter 帮我改一下主页简介：独立顾问，帮企业做 AI 转型
```

### Codex

在 Codex 里说明要使用 `advantage-filter`，再写你的问题：

```text
使用 advantage-filter：我是一名 B2B SaaS 产品顾问，想做个人 IP，过去主要帮创业公司梳理增长和产品定价，怎么定位？
```

```text
使用 advantage-filter：帮我判断“AI 工作流顾问”这个定位能不能做
```

如果你的 Codex 运行环境支持 slash command，也可以用：

```text
/advantage-filter 帮我收敛账号主标签
```

## 输入什么效果最好

你不用一次性写完整方案。先给能改变判断的事实：

- 你现在的身份、行业和主要经历

- 别人经常因为什么问题找你

- 你做成过什么案例、项目或结果

- 你已有的内容反馈、私信、咨询、成交或转介绍

- 你想服务谁，不想服务谁

- 你希望最后承接什么：咨询、服务、课程、陪跑、职业机会或商业合作

如果证据不足，skill 会先输出缺口和验证动作，而不是强行给定位。

## 输出形式

Advantage Filter 会根据当前问题选择最小有用输出。

### 定位判断卡

当受众、需求证据、信任路径和下一步动作基本明确时，它会输出：

- 结论

- 为什么可能成立

- 当前最大断点

- 建议表达

- 先验证的动作

- 通过 / 停止信号

### 反证诊断卡

当方向可能不成立、证据不足或风险很高时，它会输出：

- 为什么现在不该直接定定位

- 最大风险

- 不能直接采用的假设

- 可能路径

- 现在只验证一个事实

### 最小追问卡

当缺失信息会改变判断时，它只追问关键问题，不跑完整访谈流程。

### 完整定位方案

只有你明确要求“完整定位方案 / 账号方案 / 重定位方案 / 系统梳理”时，它才会进入完整方案路径，输出：

- 需求初筛

- 定位目标

- 人生素材矩阵

- 主支点判断

- 外显物转换

- 定位过滤表

- 账号定位结构

- 内容栏目与种子选题

- 商业承接路径

- 风险边界

## 示例

### 判断定位能不能做

```text
/advantage-filter 我想做“普通人的 AI 自动化教练”，目前没有课程，但有 3 个朋友让我帮他们搭过 Notion + Claude 工作流，这个方向能做吗？
```

你会得到一个判断：它可能成立在哪里、缺什么证据、先用什么动作验证，而不是直接收到一套课程包装。

### 从很多经历里提炼主线

```text
/advantage-filter 我做过品牌、电商、AI 工具和自由职业，现在想做账号，但不知道该讲哪条线。我有几个客户问过我怎么用 AI 提高内容产出。
```

你会得到候选方向排序，并看到每个方向的证据强度、受众清晰度、内容持续性和商业承接风险。

## 方法原则

这个 skill 遵守几条硬规则：

- 先判断市场需求，再挖个人故事。

- 兴趣不能直接当定位，外部需求证据更重要。

- 抽象优势必须翻译成内容栏目、用户收益和商业线索。

- 没有信任证据时，先补证明链，不包装专家人设。

- 反差叙事只是放大器，不是必选项。

- 每个定位建议都要说明：为什么可能成立、为什么可能不成立、哪个事实会推翻它。

## 目录结构

```text
advantage-filter/
├── SKILL.md                    # skill 主入口
├── manifest.json               # 元信息、边界和验证门槛
├── agents/interface.yaml       # agent 接口说明
├── references/                 # 方法卡、执行、验证和压力测试参考
├── evals/evals.json            # 评估样例
├── reports/                    # 基线行为和质量报告
└── scripts/                    # 本地验证脚本
```

## 本地验证

如果你修改了 skill 内容，建议在提交前运行：

```bash
python scripts/validate_skill.py
python scripts/resource_boundary_check.py
python scripts/trigger_eval.py
```

这些脚本会检查结构、资源边界和触发规则。

## License

MIT License
