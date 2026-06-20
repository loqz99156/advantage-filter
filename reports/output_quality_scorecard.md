# Output Quality Scorecard

Skill: `advantage-filter`  
Mode: Local

**Note:** This scorecard is a human reviewer artifact. The model should use `verification.md`, output self-checks, and the `confirmed:/hypothesis:/needs validation:` evidence taxonomy in SKILL.md for in-process output quality.

Use this scorecard when reviewing generated positioning outputs.

## Scoring rubric

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Current bottleneck | Not identified | Mentioned vaguely | Clearly names one largest bottleneck |
| Evidence separation | Mixes facts and assumptions | Some distinction | Labels confirmed / hypothesis / needs validation |
| Demand logic | No buyer/user demand | Assumed demand | Names demand evidence or demand gap |
| Trait externalization | Uses abstract traits | Gives examples | Converts to content, user benefit, service/product, validation |
| Funnel discipline | No filtering | Partial filtering | Applies truth, demand, spread, stability, commercial gates |
| Commercial handoff | Generic monetization | Broad path | Specific minimal handoff or next commercial test |
| Validation action | None | Vague “test content” | 1-3 concrete actions with pass/stop signals |
| Boundary clarity | Overclaims | Some caveats | Names what not to do / not touch yet |

Maximum score: 16

## Quality threshold

- 13-16: usable output.
- 9-12: needs revision before user-facing final answer.
- 0-8: failed output; downgrade to diagnostic or ask for missing evidence.

## Automatic fail conditions

Any one of these fails the output regardless of score:

- Invents personal facts, achievements, audience feedback, sales, or market proof.
- Turns abstract traits into final positioning without externalization.
- Gives a complete plan when demand/trust/delivery evidence is missing and unmarked.
- Recommends broad topic mixing for a new account without label-training rationale.
- Provides monetization advice without naming buyer, use case, or trust path.

## Review evidence

- Baseline review: `reports/baseline-behavior.md`
- Trigger review: `reports/trigger-eval-report.md`
- Blind reviewer: `missing evidence`
