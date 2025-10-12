
# Chapter 4: Cross-Scale Extensions: From Individual to Organization to Society

The first three chapters focused on individual-level human-AI interaction, but AI's impact extends beyond individuals. When multiple people collaborate, organizations operate, and societies evolve, what emergent effects do individual-level cognitive offloading produce? This chapter demonstrates how CET scales from microscopic mechanisms to macroscopic phenomena.

## 4.1 I/T/O/S Four-Layer System: The Scale Ladder

### 4.1.1 Individual Layer (I-AVP): Foundation

**Core criterion**: $P_2 \geq B_0 + \delta$ (capability after unplugging exceeds baseline)

**Key mechanisms**: Beneficial friction (50–70% success rate, working assumption) + Systematic support reduction (S4→S1→S0)

**Applicable scenarios**: Learning tools, skill training, personal productivity tools

### 4.1.2 Team Layer (T-AVP): Collaborative Capability

**Core finding**: Even when all members pass I-AVP, the team level may still fail ($P_{2,\mathrm{team}} < B_{0,\mathrm{team}}$)

**Three failure modes**:

1. **Capability polarization**: Some members highly dependent on AI, others completely independent, team overall fragile
2. **Tacit knowledge loss**: Members all ask AI rather than communicate with each other, team collective intelligence not accumulated
3. **Role rigidity**: Over-specialization, loss of mutual backup capability

**T-AVP Definition**

**Criterion**: $P_{2,\mathrm{team}} \geq B_{0,\mathrm{team}} + \delta_{\mathrm{team}}$

**Where**:
- $\delta_{\mathrm{team}} \geq 0.3\,\mathrm{SD}$ (working assumption; requires cross-domain calibration)
- Team performance $\neq$ simple sum of individual performance (collaborative emergence)

**Measurement protocol (simplified)**:

1. **Baseline**: Team completes a standard project without AI
2. **AI usage period**: 8–12 weeks of normal AI use
3. **Unplugged window**: $W = 4\text{–}8$ weeks (default 6; working assumption)
4. **Team Unplugged Test**: Complete an equivalent project without AI
5. **Judgment**: $P_{2,\mathrm{team}} \geq B_{0,\mathrm{team}} + \delta_{\mathrm{team}}$?

**Design insights**:

- Regular "no-AI discussion sessions" promote knowledge flow
- Role rotation avoids over-specialization
- Institutionalized capability construction (e.g., "Friday No-AI Day")

### 4.1.3 Organizational Layer (O-AVP): System Resilience

**Three major organizational risks**:

1. **Critical capability hollowing**: Certain skills completely disappear from the organization (veteran employees degrade, new employees never master)
2. **Knowledge transmission rupture**: New employees learn from AI rather than veteran employees, tacit knowledge lost
3. **Cognitive infrastructure single point of failure**: AI outage → business paralysis

**O-AVP Definition (dual-threshold model)**

**O-AVP Formula**: $\mathrm{O\text{-}AVP} = \mathrm{BCI} \times 0.4 + \mathrm{ICR} \times 0.6$

**Dual thresholds** (working assumption):
- **Alert**: $\geq 0.70$ (triggers risk investigation)
- **Target**: $\geq 0.85$ (healthy-organization standard)

**Where**:
- **BCI (Business Continuity Index)**: Sustainability of core business under 48h no-AI conditions
- **ICR (Independent Capability Retention)**: Share of employees who complete critical tasks without AI
- Weights 0.4/0.6 are working assumptions and require calibration & sensitivity analysis

**48-hour outage drill (measurement protocol)**:

1. Baseline metrics under normal AI support
2. Simulate a 48h complete AI outage
3. Assess continuity: what stops vs. what barely sustains
4. Compute O-AVP: $\mathrm{BCI} \times 0.4 + \mathrm{ICR} \times 0.6$
5. Judge against dual thresholds

**Organizational design recommendations**:

- Establish "cognitive reserve" mechanisms
- Regular "no-AI duty system"
- Critical position independent capability certification
- Quarterly outage drills (like fire drills)

### 4.1.4 Societal Layer (S-AVP): Generational Divide

**Core challenge**: Society cannot directly "unplug test," must rely on proxy indicators

**S-AVP proxy indicator set (working assumption)**:

1. **Generational capability differences**: $T_0$ (1980–2000) vs. $T_1$ (2000–2015) vs. $T_2$ (2015– )
2. **Industry baselines**: O-AVP distributions across critical industries
3. **Education signals**: No-AI academic performance trends
4. **Labor-market signals**: Demand for "independent capability"

**Tragedy of the cognitive commons**:

- **Individual rationality**: Using AI improves efficiency (short-term optimal)
- **Collective irrationality**: Society-wide independent capability decline (long-term risk)
- **Path dependence reinforcement**: After generational transmission rupture, lack of teachers and role models, recovery cost rises exponentially

**Window period warning**: 2025–2035 is a critical 10-year window (working assumption)
- $T_0$ generation still working, knowledge transmission can still be salvaged
- AI penetration rate approximately 30–50%, not yet at irreversible point
- Institutional intervention can still be established

## 4.2 Cross-Scale Mechanisms: Emergence and Cascade

### 4.2.1 Unified Core Mechanisms

**Scale invariance**: AVP principle has isomorphism across different scales

- All require "Unplugged Test" (or proxy measurement)
- All focus on "independent capability" rather than "collaboration efficiency"
- All use "baseline + increment" as standard

**Triple commonality**:

1. **Antifragility essence**: Temporary stress → capability improvement (individual/organization/society)
2. **Dependency lock-in commonality**: Permanent support → capability atrophy (skill degradation/institutional fragility/generational divide)
3. **Validation logic consistency**: Unified framework of baseline $B_0$ + improvement $\delta$

### 4.2.2 Cascading Vulnerability Propagation Paths

**Cascading mechanism**: Low-scale vulnerability propagates upward

```
Individual dependency (I-AVP failure 30%)
↓ Emergence effect
Team fragility (T-AVP failure 50%) ← Nonlinear amplification
↓ Institutionalization
Organizational crisis (O-AVP = 0.65 < 0.70) ← Systemic fragility
↓ Accumulation
Societal risk (S-AVP yellow warning) ← Generational divide
```

**Amplification mechanisms**:

1. **Nonlinearity of emergence**: 10% individual dependency ≠ 10% organizational risk, may amplify to 30–50% risk (due to network effects)
2. **Time lag in repair**: Individuals can recover in months, organizations take years, society may require a generation
3. **Path dependence reinforcement**: Low scales reversible (individuals can retrain), high scales have strong path dependence, recovery cost rises exponentially

### 4.2.3 Multi-Scale Coordinated Design

**Limitations of single-scale intervention**:

- Only change individuals: Organizational inertia pulls back
- Only change organizations: Social environment does not support
- **Requires multi-scale coordination**

**Coordination essentials**:

1. **Bottom-up**: Individual capability is foundation (I-AVP must pass)
2. **Top-down**: Organizational systems create environment (O-AVP drills, no-AI days)
3. **Horizontal linkage**: Industry standards, social norms (policy guidance)

## 4.3 Key Tables (Simplified Version)

**Table 4.1: Cross-Scale AVP System Comparison**

| Scale | AVP Variant | Key Criterion | Measurement Method | Primary Risk |
|:--- :--- :--- :--- :--- |
| **Individual** | I-AVP | $P_2 \geq B_0 + \delta$ | Unplugged Test ($W = 4\text{-}8$ weeks) | Capability degradation |
| **Team** | T-AVP | $P_{2,\mathrm{team}} \geq B_{0,\mathrm{team}} + \delta_{\mathrm{team}}$ | Collective Unplugged Test (drill) | Capability polarization |
| **Organization** | O-AVP | $\mathrm{BCI} \times 0.4 + \mathrm{ICR} \times 0.6 \geq 0.70\;(\text{alert});\; \geq 0.85\;(\text{target})$ | 48h outage drill | System fragility |
| **Society** | S-AVP | Proxy-indicator set healthy | Generational-difference monitoring | Generational divide |

*Note (Goodhart safeguard): This table is for direction & quality stratification only; it must not be pushed down as KPIs. Final judgment follows the AVP main criterion (see Section 3.0.2). All parameters are working assumptions requiring cross-domain/task calibration.*

## 4.4 Core Contributions of This Chapter

### Theoretical Extension

- CET extends from individual theory to cross-scale framework
- AVP principle has scale invariance
- Proposes conceptual system of T-AVP, O-AVP, S-AVP

### Mechanism Revelation

- **Team layer**: Capability polarization, knowledge loss, role rigidity
- **Organizational layer**: Institutional dependency, cognitive infrastructure degradation
- **Societal layer**: Tragedy of the cognitive commons, generational divide

### Practical Guidance

- Provides operationalizable measurement protocols (T-AVP, O-AVP)
- Identifies key risk signals (e.g., O-AVP < 0.70 alert threshold)
- Proposes multi-scale coordination directions (bottom-up + top-down + horizontal linkage)

### Theoretical Urgency

What this chapter reveals is **current reality**, not distant risk:

- Team level: Some organizations already report "new hires cannot work independently"
- Organizational level: AI outage incidents expose fragility
- Societal level: Generational capability differences beginning to emerge

**CET's mission**: Within the 2025–2035 window period, provide theoretical foundation and practical guidance to avoid the tragedy of the cognitive commons with strong path dependence and exponentially rising recovery costs.

# References

1. Bainbridge, L. (1983). Ironies of automation. *Automatica*, 19(6), 775–779. https://doi.org/10.1016/0005-1098(83)90046-8
2. Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.
3. Clark, A., & Chalmers, D. (1998). The extended mind. *Analysis*, 58(1), 7–19. https://doi.org/10.1093/analys/58.1.7
4. Dahmani, L., & Bohbot, V. D. (2020). Habitual use of GPS negatively impacts spatial memory during self-guided navigation. *Scientific Reports*, 10(1), 6310. https://doi.org/10.1038/s41598-020-62877-0
5. Engelbart, D. C. (1962). *Augmenting human intellect: A conceptual framework.* SRI Summary Report AFOSR-3223. Stanford Research Institute.
6. Liao, Q. V., Gruen, D., & Miller, S. (2024). Designing LLM chains by adapting techniques from crowdsourcing workflows. *arXiv preprint* arXiv:2312.11681. https://arxiv.org/abs/2312.11681
7. Maguire, E. A., Gadian, D. G., Johnsrude, I. S., Good, C. D., Ashburner, J., Frackowiak, R. S. J., & Frith, C. D. (2000). Navigation-related structural change in the hippocampi of taxi drivers. *Proceedings of the National Academy of Sciences*, 97(8), 4398–4403. https://doi.org/10.1073/pnas.070039597
8. Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors*, 39(2), 230–253. https://doi.org/10.1518/001872097778543886
9. Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences*, 20(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002
10. Sparrow, B., Liu, J., & Wegner, D. M. (2011). Google effects on memory: Cognitive consequences of having information at our fingertips. *Science*, 333(6043), 776–778. https://doi.org/10.1126/science.1207745
11. Taleb, N. N. (2012). *Antifragile: Things that gain from disorder.* Random House. ISBN: 978-1400067824
12. Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes.* Harvard University Press. ISBN: 978-0674576292
13. Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89–100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x
