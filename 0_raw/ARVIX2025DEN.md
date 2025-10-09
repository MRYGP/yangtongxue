## Appendix B: Parameter Registry (SSOT)

**Description**: This table serves as the Single Source of Truth (SSOT) for all parameters throughout the paper. If cross-chapter parameter inconsistencies are found, this table takes precedence and other chapters should be corrected accordingly.

| Parameter Symbol | Default Specification | Maintenance Location | First Definition | Cross-Chapter References | Calibration Direction |
|------------------|----------------------|---------------------|------------------|-------------------------|----------------------|
| **AVP Criterion** | $P_2 \geq B_0 + \delta$ | Section 3.0.2 | Section 3.0.2 | Throughout | - |
| **$\delta$ Threshold** | $\geq 0.3\,\mathrm{SD}$ or 10% (working assumption; requires cross-domain/task calibration) | Section 3.0.2 | Section 3.0.2 | Throughout | Procedural tasks 0.2–0.3; Creative tasks 0.4–0.5 |
| **W Window** | 4–8 weeks (default 6 weeks; working assumption) | Section 3.0.2 | Section 3.0.2 | 3.1/4.1/Appendix D | Fast skills 4 weeks; Complex skills 8–12 weeks |
| **Optimal Challenge Zone** | 50$\text{–}$70% success rate (working assumption; cross-domain/task calibrated; population-level; individual calibration required) | Section 3.2.1 | Section 3.2.1 | 5.2/Appendix D | Individual adaptation; task-specific calibration |
| **$S_0$ Starting Point** | 0.8 (80% support; working assumption) | Section 3.3.1 | Section 3.3.1 | 5.3 | High-risk tasks 0.6; Novice-friendly 0.9 |
| **$S_{\min}$ Lower Bound** | $\approx 0.2$ (working assumption; requires calibration) | Section 3.3.2 | Section 3.3.2 | 5.3.3 | Experts ≈0.1; Novices ≥0.3 |
| **Reduction Rate $\lambda$** | Task-specific (working assumption) | Section 3.3.1 | Section 3.3.1 | 5.3 | Linear/exponential/S-curve optimization |
| **T-AVP Criterion** | $P_{2,\mathrm{team}} \geq B_{0,\mathrm{team}} + \delta_{\mathrm{team}}$ | Section 4.1.3 | Section 4.1.3 | 4.1 | - |
| **$\delta_{\mathrm{team}}$ Threshold** | $\geq 0.3\,\mathrm{SD}$ (working assumption; domain-calibrated) | Section 4.1.3 | Section 4.1.3 | 4.1 | Larger teams/critical tasks may require $\geq 0.5\,\mathrm{SD}$ |
| **O-AVP Weighting** | $\mathrm{BCI}\times0.4 + \mathrm{ICR}\times0.6$ (working assumption; sensitivity test) | Section 4.2.2 | Section 4.2.2 | 4.2/6.2 | Weight sweep & ablation |
| **O-AVP Threshold** | Alert $\geq 0.70$, Target $\geq 0.85$ (working assumption) | Section 4.2.3 | Section 4.2.3 | 4.2/6.2 | Adjust by industry risk tolerance |
| **48h Exercise Window** | 48 hours (adjustable 24/72h; working assumption) | Section 4.2.2 | Section 4.2.2 | 4.2 | Adjust by business criticality |
| **Generational Window** | 10 years (2025–2035; conceptual placeholder) | Section 4.3.2 | Section 4.3.2 | 6.3.3 | Longitudinal study calibration; cross-cultural validation |
| **Ability Vector Dimensions** | 5–20 dimensions (exploratory hypothesis) | Section 5.4.3 | Section 5.4.3 | 5.4 | Domain definition; IRT modeling |
| **Alert Threshold** | Green/Yellow/Red/Black (working assumption) | Section 5.4.4 | Section 5.4.4 | 5.4 | Adjust by risk tolerance |

*Note (Goodhart safeguard): This table/grading is for **directional and stratified** purposes only; **must not be cascaded into KPIs**. Final judgment follows the **AVP main criterion (see Section 3.0.2)**.*

**Usage Rules**:

1. **Modification Process**: If any parameter's default value needs adjustment, it must first be modified in the corresponding "Maintenance Location" section, then this table updated
2. **Citation Format**: When referencing parameters, use "(see Section X.Y, Parameter Registry Appendix B)"
3. **Version Control**: This table updates synchronously with the main text, version number consistent with paper version
4. **Specification Conservation Commitment**: If cross-chapter parameter inconsistencies are found, this table takes precedence and other chapters should be corrected accordingly

## Appendix C: Selected Case Studies

### Case 1: Programming Education Platform (Success Case)

**Background**: An online programming education platform designed an AI-assisted learning system for Python beginners, with 100 students (aged 18–25), 8-week learning cycle, aiming to master basic Python programming skills.

**AVP Test Results**:

$B_0$ (baseline): Completed 3 programming tasks without AI assistance, average score 62/100
Collaboration period (8 weeks): Used EML-designed AI teaching assistant
W (unplugged window): 6 weeks completely without AI
$P_2$ (post-unplugged): Completed equivalent tasks, average score 78/100
**Judgment**: Define the capability increment as **$\Delta C = P_2 - B_0$**. ΔC = $P_2$ - $B_0$ = 16 points > $\delta$(10 points, $\approx 0.3\,\mathrm{SD}$) → **AVP Passed**

**EML Analysis**:

**Beneficial friction**: AI did not provide direct code, but:
- Weeks 1–2: Provided code framework, students filled core logic (completeness friction)
- Weeks 3–4: Only gave algorithmic ideas, students implemented independently (abstraction friction)
- Weeks 5–6: Students tried for 15 minutes before AI intervened (delay friction)
- Maintained success rate 55–65% (close to target 50$\text{–}$70%)
- Systematic support reduction:

- Adopted S-curve reduction: $S_0$=0.8 → slow reduction in first 2 weeks → rapid reduction in middle → later approaching $S_{\min}$=0.2
- Fallback mechanism: 2 students triggered fallback due to consecutive failures, temporarily increased support then recovered

**Success Factors**:

1. **Friction and Reduction Synergy**: Not using friction or reduction alone, but implementing both simultaneously with complementary effects
2. **Personalized Adjustment**: Dynamically adjusted friction intensity and reduction speed based on students' C(t) (ability vector)
3. **Safety Net Mechanism**: $S_{\min}$=0.2 ensured students wouldn't be completely lost, enhancing confidence
4. **Sufficient Unplugged Window**: 6-week window was sufficient for ability to stabilize and internalize

**Transferable Insights**:

- EML dual conditions (friction + reduction) are **jointly necessary**, neither can be omitted
- 50$\text{–}$70% success rate (working assumption) is the key balance point: challenging but not frustrating
- S-curve reduction outperforms linear: adapts to learning curve's non-linear characteristics
- Personalized adjustment is more effective than fixed strategies (but higher implementation cost)

**Red Flag Warning**: Don't mistake "reducing AI assistance" for "lowering teaching quality." Friction is to promote active learning, not to deliberately make things difficult for students. If teams resist, start with "partial tasks" or "advanced students" as pilot.

### Case 2: Software Team Comparative Experiment (Team-Level Comparison)

**Background**: Two software development teams at a tech company (8 people each, comparable abilities), 6-month AI-assisted programming experiment. Group A (experimental): implemented "Friday No-AI Day" policy; Group B (control): unlimited use of AI programming assistants.

**AVP Test Results**:

- Individual level (I-AVP):

- Group A: All 8 people passed I-AVP ($P_2 \geq B_0 + \delta$)
- Group B: Only 3 passed, 5 failed ($P_2 < B_0$ or $P_2 \approx B_0$)

- Team level (T-AVP):

- Group A: After 3 days unplugged, team independently completed medium-scale feature ($P_{2,\mathrm{team}}=80$ points > $B_{0,\mathrm{team}}=68$ points+$\delta$) → **T-AVP Passed**
- Group B: After 3 days unplugged, team efficiency significantly declined ($P_{2,\mathrm{team}}=55$ points < $B_{0,\mathrm{team}}=65$ points) → **T-AVP Failed**

**Failure Patterns (Group B)**:

1. **Capability Polarization**: 3 senior members maintained ability, 5 juniors completely dependent on AI, team overall fragile
2. **Knowledge Loss**: Team no longer shared experience internally (all asked AI), tacit knowledge not transmitted
3. **Poor Architecture Understanding**: Over-reliance on AI-generated code, insufficient understanding of overall system, difficult to locate bugs when they occurred

**Quantitative Evidence**:

- Group A "interpersonal code review": Average 48 times/person over 6 months
- Group B "interpersonal code review": Average 12 times/person over 6 months
- Group A Slack technical discussions: 15 posts/day average
- Group B Slack technical discussions: 5 posts/day average

**Transferable Insights**:

1. **"No-AI Day" is a simple and effective T-AVP safeguard mechanism**: Low cost (policy only), highly operable (fixed weekly day), minimal side effects (no impact on overall efficiency)
2. **Team capability $\neq$ sum of individual capabilities**: I-AVP passed $\neq$ T-AVP necessarily passed (emergence)
3. **Junior members are T-AVP's vulnerability point**: Most prone to dependency, need special protection (e.g., disable AI for first 3 months)
4. **Interpersonal communication is the foundation of team resilience**: AI cannot replace "tacit knowledge" transmission; code review, technical sharing sessions, pair programming become more valuable in the AI era

**Management Decision**: Based on this experiment, the company decided: ① Company-wide rollout of "Friday No-AI Day" ② New employees disabled AI for first 3 months (build basic capabilities) ③ Quarterly T-AVP exercises (simulate AI downtime scenarios) ④ Performance evaluation added "interpersonal collaboration" dimension.

**Red Flag Warning**: Don't understand "Friday No-AI Day" as "punishment" or "going backwards." Correct positioning: this is a **capability training day**, similar to "weight training" at the gym. If teams resist, start with "monthly" to reduce frequency, or choose non-critical tasks for unplugged testing.

## Appendix D: AVP Measurement Protocol (Simplified Version)

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

## Appendix E: Frequently Asked Questions (FAQ)

**Q1: Is AVP applicable to all AI tools?**

No. AVP only applies to "capability-enhancing" human–AI collaboration, not "compensatory exoskeletons" (see Section 3.0.6 Boundary Conditions Anchor B5).

**Applicable Scenarios**:

- ✓ Learning tools (e.g., programming assistants, writing tutors)
- ✓ Skill training (e.g., design software, data analysis tools)
- ✓ Cognitive enhancement (e.g., decision support systems)

**Non-Applicable Scenarios**:

- ✗ Disability assistance (e.g., screen readers, prosthetic control)
- ✗ Beyond physiological limits (e.g., night vision devices, gravity-assist exoskeletons)
- ✗ Purely instrumental tasks (e.g., calculator for basic arithmetic, no capability-building goal)

**Judgment Standard**: If the tool's goal is "compensation" rather than "enhancement," then AVP is not applicable.

**Q2: How to determine the $\delta$ threshold?**

$\delta$ (minimum meaningful lift threshold) has a default working assumption of $\geq 0.3\,\mathrm{SD}$ or 10%, but needs calibration based on domain characteristics:

**General Principles**:

- **Statistical/practical significance**: 0.3 SD is typically considered a "small-to-medium effect" in psychometrics, with practical meaning
- **Measurement error tolerance**: Avoids mistaking measurement noise for capability enhancement
- **Cross-domain comparability**: Relative thresholds (SD or percentage) adapt to different tasks

**Domain Differences** (working assumption; requires empirical validation):

- **Cognitive skills** (e.g., programming, writing): $\delta \geq 0.3\,\mathrm{SD}$ or 10%
- **Motor skills** (e.g., typing speed): May require larger threshold ($\delta \geq 0.5\,\mathrm{SD}$) because muscle memory is more stable
- **Creative tasks** (e.g., artistic creation): May require qualitative assessment rather than single $\delta$

**Calibration Process**:

1. Pilot study: Small sample testing to determine preliminary parameters
2. Sensitivity analysis: Test impact of $\delta$ changes on judgment results
3. Domain expert consultation: Adjust based on practical experience
4. Iterative optimization: Adjust parameters based on feedback

**Q3: How to choose the unplugged window W?**

W (unplugged window) has a default working assumption of 4–8 weeks (default 6 weeks), but needs adjustment based on task complexity:

**Task Differences** (working assumption; requires empirical validation):

- **Fast skills** (e.g., math calculation, simple programming): W=4 weeks may be sufficient
- **Complex skills** (e.g., second language learning, advanced programming): W=8–12 weeks
- **Professional abilities** (e.g., surgery, architectural design): W may require months or even years

**Selection Criteria**:

- **Capability stability**: W needs to be long enough for ability to transition from "short-term memory" to "long-term retention"
- **Environmental factor control**: W should not be too long, otherwise confounding variables increase (e.g., other learning, life changes)
- **Practical feasibility**: Consider participant attrition rate, research resources

**Red Flag**: If W is too short (<2 weeks), may only measure short-term memory residue, unable to verify true capability internalization. If W is too long (>12 weeks), environmental factors confound, difficult to attribute to AI collaboration.

**Q4: Why are compensatory exoskeletons not applicable to AVP?**

Compensatory exoskeletons (e.g., disability assistance devices, tools beyond physiological limits) have fundamentally different goals from capability-enhancing AI:

**Compensatory Exoskeletons**:

- Goal: Compensate for missing or impaired functions
- Expectation: Users continue to depend on tools (this is the design goal, not a defect)
- Evaluation standard: Whether tools enable users to achieve "equivalent function" (rather than "capability enhancement")
- Examples: Blind people using screen readers, amputees using prosthetics, elderly using walkers

**Capability-Enhancing AI**:

- Goal: Promote user capability growth
- Expectation: Users gradually become independent (this is the design goal)
- Evaluation standard: Whether capability improves after unplugging (AVP)
- Examples: Learning programming, improving writing, enhancing decision-making

**Why Not Applicable to AVP**:

- "Unplugged testing" for compensatory tools is unreasonable (e.g., asking blind people to remove screen readers to read)
- Compensatory tools' goal is not "independence," but "functional equivalence"

**Fairness Principle** (see Section 3.0.6):

- For individuals who truly need assistive tools (e.g., screen reader users), adjust **task format** without reducing **challenge intensity**
- Evaluation based on **relative improvement** rather than absolute level
- AVP's $\delta$ threshold can be personalized (e.g., based on individual's $B_0$)

**Q5: How to avoid the Goodhart's Law trap?**

Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure." If AVP is misused as a KPI, it may lead to:

**Risk Scenarios**:

- A company uses AVP for employee promotion evaluation → employees artificially manipulate baseline $B_0$ (intentionally low scores), use AI during unplugged period → AVP completely fails
- An educational institution uses AVP for teacher performance evaluation → teachers only teach "easy-to-improve" skills, ignoring important but difficult-to-achieve-short-term capabilities

**Goodhart Safeguard Mechanisms** (see Section 3.0.2 Note 2, Section 5.5.1):

1. **Correct AVP Positioning**:

- AVP is an **acceptance criterion**, not a **management tool**
- AVP is for **quality judgment**, not **benefit distribution**

2. **Non-KPI Grading**:

- AVP grading (Basic/Retention/Transfer) is only for **quality stratification**
- Prohibit using AVP scores for personnel assessment, performance ranking, resource allocation
- Any scenario involving benefit distribution must not use AVP as the sole criterion

3. **Fixed Footnote Template** (use under all threshold tables):

> *Note (Goodhart safeguard): This table/grading is for **directional and stratified** purposes only; **must not be cascaded into KPIs**. Final judgment follows the **AVP main criterion (see Section 3.0.2)**.*

4. **Separation of Monitoring and Warning**:

- Monitoring data (e.g., C(t) ability vector) is only for system improvement
- Not linked to personal benefits
- Anonymized processing to protect user privacy

**Correct AVP Usage**:

- ✓ For evaluating AI tool design quality
- ✓ For research verification of theoretical hypotheses
- ✓ For educational institutions to evaluate teaching methods

**Incorrect AVP Usage**:

- ✗ For employee performance evaluation
- ✗ For student ranking/class assignment
- ✗ For AI tool marketing KPIs
