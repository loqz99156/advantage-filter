# Prompt Quality Profile

Skill: `advantage-filter`

## Explicit user need

Users ask for personal IP, creator account, knowledge-service, or personal brand positioning. The recurring job is to identify a positioning direction that is true, legible to an audience, content-provable, and commercially supportable.

## Implicit user need

Users often ask “我适合做什么” but actually need one of these narrower outcomes:

- identify the current largest positioning bottleneck;
- separate evidence-backed strengths from self-image;
- choose one main label from scattered materials;
- translate abstract traits into audience-facing assets;
- design a minimal validation action before expanding effort.

## Role design

The skill should behave like a positioning diagnostician, not a motivational coach or persona copywriter.

It should:

- state assumptions;
- distinguish confirmed evidence from hypotheses;
- challenge weak demand claims;
- avoid flattering but unverifiable labels;
- give the smallest useful next output.

## Task family

Primary task family: advisory diagnosis with structured output.  
Secondary task family: method application and content/business translation.

## Output format expectations

Use one of these shapes, not all at once:

- 定位判断卡
- 反证诊断卡
- 最小追问卡
- 表达改写
- 完整定位资产（only when explicitly requested）

## Quality checks

| Dimension | Standard |
| --- | --- |
| Completeness | Solves the current largest positioning bottleneck, not every possible problem |
| Clarity | Names audience, demand, evidence, and next action plainly |
| Consistency | Uses the same funnel logic across entrypoint and references |
| Practicality | Includes a content, private-message, homepage, or small-sale validation action |
| Specificity | Avoids generic labels unless tied to evidence and externalization |

## Known prompt risks

- Over-answering when a minimal diagnostic card is enough.
- Asking interview questions indefinitely instead of offering a next action.
- Confusing platform growth with positioning.
- Treating user goals as market proof.

## Missing evidence

- User interview transcripts: `missing evidence`
- Blind prompt evaluation: `missing evidence`
- Cross-runtime adapter testing: `missing evidence`
