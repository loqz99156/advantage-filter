# Trigger Eval Report

Skill: `advantage-filter`

## Route boundary

Use this skill for personal advantage positioning: finding a true, audience-legible, content-provable, commercially supportable positioning direction from real experience, stable ability, high-frequency help scenarios, or account label confusion.

Do not route here as the primary skill when the user asks only for platform growth tactics, publishing operations, visual assets, article ingestion, transcription, or pure formatting.

## Positive trigger examples

| Prompt pattern | Expected route reason |
| --- | --- |
| “我适合做什么账号？” | Core low-evidence positioning diagnosis |
| “我的经历很多但方向很散” | Material extraction and funnel filtering |
| “我很通透/自信/坚韧，怎么做成内容？” | Abstract trait externalization |
| “账号内容太散，平台识别不了我” | Single-label training and account positioning |
| “我想把个人优势做成咨询/服务” | Commercial handoff and demand validation |

## Negative / near-neighbor examples

| Prompt pattern | Preferred route |
| --- | --- |
| “帮我做小红书 30 天涨粉计划” | xiaohongshu-account-launch-expert unless positioning is the bottleneck |
| “帮我排版公众号文章” | gongzhonghao-typeset |
| “把这个视频转文字” | relevant transcribe skill |
| “生成小红书封面图” | guizang-social-card-skill |
| “给我 100 个爆款标题” | content/platform strategy skill, not this skill unless tied to positioning validation |

## Confusion risks

- Full account/positioning plan requests should enter this skill's complete path only when explicitly requested; do not overproduce on partial requests.
- Creator-system or platform-growth requests overlap in audience but should stay here only when the bottleneck is advantage positioning or evidence filtering.
- platform launch experts: own platform-specific growth mechanics after positioning is clear.

## Eval coverage status

- Positive trigger evals: present and expanded in `evals/evals.json`.
- Negative trigger evals: added as expected-output cases in `evals/evals.json`.
- Automated semantic route judging: `missing evidence`.
- Blind holdout: `missing evidence`.
