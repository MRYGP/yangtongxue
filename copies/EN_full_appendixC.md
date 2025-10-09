: Selected Case Studies

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
