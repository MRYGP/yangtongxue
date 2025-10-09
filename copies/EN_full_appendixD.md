: AVP Measurement Protocol (Simplified Version)

### D.1 Pre-Measurement Checklist

**Applicability Confirmation**:

- [ ] Task type: Cognitive-intensive, learnable (non-purely instrumental tasks)
- [ ] Independent completion has value (non-compensatory exoskeleton scenarios, see Section 3.0.6 Boundary Conditions Anchor B5)
- [ ] Unplugged window can be set (no high-risk consequences)

**Baseline Design**:

- [ ] Design baseline tasks (moderate difficulty, completion time 30–120 minutes)
- [ ] Recruit participants (minimum N=30, recommended $N \geq 50$)
- [ ] Record: $B_0$ score, completion time, subjective difficulty (1–10 scale)
- [ ] Questionnaire: Cognitive load (NASA-TLX), task motivation

**Parallel Test Preparation**:

- [ ] Ensure task equivalence (IRT calibration or expert evaluation)
- [ ] Prepare $\geq 2$ sets of backup tasks (prevent leakage)
- [ ] Pilot test verify difficulty consistency (pilot $N \geq 10$)
- [ ] Calculate inter-rater reliability (target **ICC ≥ 0.75**, working assumption); if ICC < 0.75: retrain raters or refine the rubric.

**Parameter Determination**:

- [ ] $\delta$: $\geq 0.3\,\mathrm{SD}$ or 10% (working assumption; requires cross-domain/task calibration)
- [ ] W window: 4–8 weeks (default 6 weeks; working assumption)
- [ ] Follow-up time: Recommend testing 3 months after $T_3$ (retention assessment; optional)
- [ ] Ethics review: Obtain IRB/ethics committee approval

### D.2 Measurement Execution Protocol

**Phase 1: Baseline Measurement ($T_0$ - Week 0)**

- Participants complete standard tasks without AI assistance
- Record: Raw scores, completion time, error types
- Questionnaire: Subjective difficulty, cognitive load (NASA-TLX), self-efficacy
- Scoring: By $\geq 2$ independent raters blind to experimental hypothesis
- Calculate inter-rater reliability (target **ICC ≥ 0.75**, working assumption); if ICC < 0.75: retrain raters or refine the rubric.
- Take average as $B_0$
- Quality control: Check ceiling/floor effects (if >80% or <20% reach extreme scores, adjust difficulty)

**Phase 2: Training Period ($T_1$→$T_2$ - Weeks 1–8)**

- Experimental group: EML conditions

- Beneficial friction: Target success rate 50$\text{–}$70% (working assumption; cross-domain/task calibrated; individual adaptation required)
- Systematic reduction: $S(t)$ from 0.8→0 according to reduction curve
- Bi-weekly embedded micro-tests (10% tasks without support)

- Control group: Standard AI assistance or no AI

- No friction design (complete support)
- No reduction mechanism ($S(t)$ constant)

- Record data: Usage frequency, help requests, weekly task volume, weekly success rate, user satisfaction (bi-weekly)

- Fidelity check execution:

- Confirm experimental group friction intensity at 50$\text{–}$70% (allow ±5% fluctuation)
- Confirm reduction curve executed as planned
- Monitor control group for accidental friction introduction

**Phase 3: Unplugged Window (W - Weeks 9–14, default 6 weeks)**

- Completely disable AI assistance (technical blocking + self-report)
- Can continue daily tasks, but no system support
- Monitoring:
- Weekly self-report (whether AI was used in violation)
- Behavioral log sampling (e.g., code commit records, writing trace analysis)
- Violation handling:
- Minor violations (1–2 times, non-critical tasks): Record but retain data, sensitivity analysis
- Major violations ($\geq 3$ times or critical tasks): Exclude participant data

**Phase 4: Post-test ($T_3$ - After unplugged window)**

- Use equivalent parallel tests (same difficulty as $T_0$ but different content)
- Scoring: By $\geq 2$ independent raters blind to experimental hypothesis
- Calculate $P_2$, determine AVP result:
- $P_2 \geq B_0 + \delta$: Success (Cognitive Endosymbiosis)
- $P_2 \approx B_0$: Neutral
- $P_2 < B_0$: Failure (Cognitive Exoskeleton)

### D.3 Key Considerations

**Equivalence Assurance**:

- $T_0$ and $T_3$ tests have consistent difficulty (IRT calibration or expert evaluation)
- Different content (prevent practice effects)
- Same testing environment (time, location, instructions)

**Blind Rating Requirements**:

- Raters unaware of participant group (experimental/control)
- Raters unaware of test time point ($T_0$/$T_3$)
- Scoring criteria predetermined and trained

**Violation Handling**:

- Minor violations: Retain data, mark as "violation," exclude in sensitivity analysis
- Major violations: Direct exclusion, not included in final analysis

**Attrition Management**:

- Intent-to-treat analysis (ITT): Retain all randomized participant data
- Per-protocol analysis (PP): Only analyze participants completing full process
- If attrition rate >30%: Analyze causes, may need to shorten W or increase incentives

**Ethical Considerations**:

- Informed consent: Participants understand experiment purpose and unplugged testing
- No harm principle: Unplugged testing not for high-risk tasks
- Privacy protection: AVP results confidential, not for employment/education discrimination
- Right to withdraw: Participants can exit research at any time
