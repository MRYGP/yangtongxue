: Frequently Asked Questions (FAQ)

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
