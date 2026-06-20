# Baseline Behavior Report

Skill: `advantage-filter`  
Source fixture: `个人优势定位方法论反向抽象.md`  
Mode: Local baseline before source-method upgrade

## Baseline finding

The current skill is conceptually strong: it already treats personal advantage positioning as evidence-based market positioning rather than persona packaging. It has useful route rules, evidence branching, method cards, and a complete-plan path.

The main quality gaps are operational rather than conceptual:

1. The frontmatter description is long and process-heavy, which can encourage shallow route compliance instead of full skill reading.
2. The main skill and method cards use inconsistent funnel language: the entrypoint uses `真实性 -> 需求性 -> 传播性 -> 稳定性 -> 商业性`, while method cards still show the source document's four-layer funnel `真实性 -> 传播性 -> 稳定性 -> 商业性`.
3. The skill mentions `AskUserQuestion` as a hard interaction rule, which is not portable across all agent runtimes.
4. Existing evals cover common cases but miss low-evidence account direction, abstract trait externalization, complete-plan downgrade behavior, and near-neighbor platform-growth prompts.
5. Complete-plan mode is strong but needs an explicit downgrade rule so thin evidence becomes staged hypotheses rather than confident final positioning.

## Pressure scenarios

### 1. “我适合做什么账号” with little evidence

Likely current behavior:

- Correctly avoids producing a polished persona immediately.
- Likely outputs minimal questions or a反证诊断卡.

Gap:

- May ask too many framework questions before giving a useful next move.
- Needs a stronger default: identify the largest missing evidence point, offer 2-3 provisional hypotheses only if clearly labeled, and ask for one decisive fact.

Improvement:

- Add low-evidence triage guidance and eval coverage.

### 2. Abstract traits: “自信 / 通透 / 坚韧”

Likely current behavior:

- Rejects abstract traits as final positioning.
- Uses externalization examples: confidence expression, decision judgment, adversity recovery.

Gap:

- May produce generic examples without forcing a lead trait.

Improvement:

- Add selection rule: rank traits by audience perceptibility, topic production potential, and paid-demand connection; choose one lead trait and demote the rest to supporting material.

### 3. Many experiences, scattered direction

Likely current behavior:

- Enters material extraction and funnel filtering.
- Avoids instantly packaging all experiences into a persona.

Gap:

- May list too many candidate angles without pruning.

Improvement:

- Cap candidate directions at three and rank by proof strength, audience clarity, repeatable content, monetization path, and failure risk.

### 4. Account topics are scattered

Likely current behavior:

- Correctly diagnoses platform label confusion.
- Uses single-label training before 1+2 expansion.

Gap:

- Needs a smaller default sprint output: one main label, three content pillars, five immediate test topics, and short-term “do not post” boundaries.

Improvement:

- Add eval case and output-quality gate for label-training requests.

### 5. User asks for a complete positioning plan

Likely current behavior:

- Enters a structured complete path.
- Produces a comprehensive positioning package.

Gap:

- If evidence is thin, the output can still sound too final.

Improvement:

- Add a downgrade rule: missing trust, demand, or delivery evidence must be marked as `confirmed`, `hypothesis`, or `needs validation`.

## Required changes

- Tighten frontmatter description to trigger conditions only.
- Resolve funnel rule drift by explicitly documenting the source four-layer funnel and the skill's optional demand gate.
- Replace hard `AskUserQuestion` dependency with portable wording: use structured choices when the runtime supports them; otherwise ask concise numbered questions.
- Add stronger low-evidence triage and candidate ranking rules.
- Expand eval coverage for abstract traits, weak evidence, complete-plan downgrade, platform-growth near-neighbors, and commercial-service prompts.

## Evidence status

- Baseline is based on file-backed fixture review and simulated pressure scenarios.
- No live model eval harness existed before this local skill pass.
- Reviewer identity, blind review, telemetry, and historical pass rates: `missing evidence`.
