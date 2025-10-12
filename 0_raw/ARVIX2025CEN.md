# Chapter 3: Core CET Theory Construction

This chapter systematically explicates the core mechanisms of CET: How is the AVP criterion operationalized? What is the internal logic of EML's conditions? How are the two unified through Partner-like Agency?

## 3.0 Core Terminology and Anchor Definitions

This section presents all core definitions and fixed anchor texts of CET. **These anchor definitions remain verbatim throughout the text;** subsequent chapters cite abbreviations or use "see Section 3.0."

### 3.0.1 Core Symbol System

**Table 3.1: Key Symbol System**

| Symbol/Term | Meaning | Typical Value/Range |
|:--- :--- :--- |
| $B_0$ | User's independent capability baseline before using AI | Task-specific measurement |
| $P_1$ | User's performance while collaborating with AI | Process indicator; not included in final judgment |
| $P_2$ | User's independent performance after the unplugged window | Core indicator for AVP validation |
| $\delta$ | Minimum meaningful lift threshold | Working assumption: $\geq 0.3\,\text{SD}$ or 10% (requires cross-domain/task calibration) |
| $W$ | Unplugged window duration | Working assumption: 4–8 weeks (default 6 weeks; requires cross-domain/task calibration) |
| $S(t)$ | AI support intensity at time $t$ | 0 (fully independent) to 1 (fully dependent) |
| Success-rate target | Quantitative target for beneficial cognitive friction | 50$\text{-}$70% (working assumption; population-level; individual calibration required) |

*Note: All quantitative parameters are conceptual working models requiring cross-domain empirical calibration.*

### 3.0.2 Antifragility Validation Principle (AVP) [Anchor B1]

> **Antifragility Validation Principle (AVP).** Validate collaboration through an **Unplugged Test** to verify whether it promotes independent capability.  
> **Criterion:** $P_2 \geq B_0 + \delta$ (where $\delta \geq 0.3\,\text{SD}$ or 10%, working assumption; requires cross-domain/task calibration). **$P_1$ (collaboration performance) is not included in final judgment.**

### 3.0.3 Endosymbiotic Minimal Law (EML) [Anchor B2]

> **Endosymbiotic Minimal Law (EML).** The **necessary design conditions** for constituting "Cognitive Endosymbiosis" are:  
> (1) **Beneficial Cognitive Friction:** Place users in the **optimal challenge zone** (population-level working assumption: 50$\text{–}$70% success rate; individual adaptation required);  
> (2) **Systematic Support Reduction:** Decrease AI support intensity from S4→S1→S0 according to a **reduction curve**.  
> These two are **jointly sufficient** design conditions, but the final acceptance still requires **AVP ($P_2 \geq B_0 + \delta$).**

### 3.0.4 LSA Functional Layers [Anchor B3]

> **LSA-F (Functional Layers).** L1 Knowledge Integration | L2 State Modeling | L3 Friction Calibration | L4 Metacognitive Orchestration.  
> **Support Level Stack (S4→S1→S0)** expresses support intensity and is orthogonal to LSA-F.

**Hard constraint.** L1–L4 (functional layers) and S4–S1 (support intensity) are **mutually exclusive representations**; they must not be substituted or cascaded within the same formula.

### 3.0.5 Optimal Challenge Zone [Anchor B4]

> **Optimal Challenge Zone.** To promote retention and transfer, adapt difficulty/prompt intensity to a **50$\text{–}$70% success rate** (working assumption; cross-domain/task calibrated; population-level with individual calibration). **>85%** approaches offloading; **<30%** risks frustration.

### 3.0.6 Boundary Conditions [Anchor B5]

> **Boundary Conditions.** CET applies to **capability-enhancing** human–AI collaboration; **compensatory exoskeletons** (e.g., disability assistance; devices exceeding physiological limits) are outside scope. All parameters are **conceptual working models** requiring cross-domain calibration.

## 3.1 Core Derivation of the AVP Principle

### 3.1.1 Why $P_2$ Rather Than $P_1$?

**Three-stage capability measurement.**  
**$B_0$** (pre-collaboration independent baseline);  
**$P_1$** (collaboration-period performance; process observation only; not used in judgment);  
**$P_2$** (post-collaboration independent performance; unplugged window $W=4$–$8$ weeks; default 6 weeks; working assumption).

**Blind spot of traditional evaluation.** Most systems examine $P_1$ only, ignoring "what happens when leaving AI." High $P_1$ shows AI effectiveness, **not** user capability growth.

**Necessity of the unplugged test.** Genuine capability enhancement should make users stronger **when away from AI**. The unplugged window $W=4$–$8$ weeks (default 6; working assumption) balances stability with environmental control.

**Outcome categories.**  
$P_2 \geq B_0 + \delta$: Success (Cognitive Endosymbiosis);  
$P_2 \approx B_0$: Neutral (no harm, no growth);  
$P_2 < B_0$: Failure (Cognitive Exoskeleton).

### 3.1.2 Logic for Selecting $\delta$

**Rationale** (working assumption; cross-domain/task calibration).  
1) **Statistical/practical significance.** $\sim$0.3\,\text{SD}$ is a small-to-medium effect with practical meaning;  
2) **Measurement error tolerance.** Avoids mistaking noise for growth;  
3) **Comparability.** $\text{SD}$/percentage thresholds adapt across tasks.

**Calibration principle.** High-risk domains (e.g., healthcare) may require higher $\delta$ (e.g., 0.5\,\text{SD}$); low-risk domains can accept lower values (e.g., 0.2\,\text{SD}$).

## 3.2 Beneficial Cognitive Friction Mechanism

### 3.2.1 Theoretical Foundation

**Use-it-or-lose-it.** Frequently used neural pathways strengthen; idle pathways weaken. Full replacement by AI tends to degrade the corresponding circuitry (directional evidence; Dahmani & Bohbot, 2020).

**Desirable Difficulties** (Bjork, 1994). Moderate difficulties (e.g., spacing, interleaving, generation effect) promote long-term retention and transfer.

**Zero-friction trap.** "Zero-friction" experiences may yield high $P_1$ yet stagnate or reduce $P_2$.

### 3.2.2 Optimal Challenge Zone: 50$\text{–}$70%

Inspired by the **Zone of Proximal Development (ZPD)**, CET operationalizes the **optimal challenge zone** as a **50$\text{–}$70% success rate** (working assumption; cross-domain/task calibrated; population-level; individual dynamic calibration required).

**Why this range** (working assumption; requires cross-task validation): **<30%** frustrates; **50$\text{–}$70%** balances challenge/growth; **>85%** approaches offloading.

### 3.2.3 Three Types of Friction

**Table 3.2: Three Strategies of Cognitive Friction**

| Friction Type | Implementation | Cognitive Effect | Example |
|:--- :--- :--- :--- |
| **Completeness friction** | Provide a partial answer; leave blanks for the user to fill | Activates generation effect; promotes active construction | AI supplies a code framework; user implements core logic |
| **Abstraction friction** | Provide conceptual guidance, not step-by-step solutions | Deepens understanding; avoids mechanical imitation | AI explains algorithmic ideas, not direct code |
| **Delay friction** | Delay feedback to enforce independent effort | Enhances problem-solving; reduces dependency | User works 15 minutes before AI intervenes |

*Note (Goodhart safeguard): This table/grading is for directional stratification only; must not be cascaded into KPIs. Final judgment follows the AVP main criterion (see Section 3.0.2).*

## 3.3 Systematic Support Reduction

### 3.3.1 Why Reduction Is Necessary

**Scaffolding theory** (Wood et al., 1976). Effective support is **temporary**, with systematic reduction (S4→S1→S0). As with physical scaffolds, AI support must recede once capability forms.

**Automation paradox.** Permanent automation support degrades operator skills. Fixed high support invites **dependency lock-in**.

### 3.3.2 Support Level Stack (S4→S1→S0)

**Definition (orthogonal to LSA-F).** As defined in **Section 3.0.4**, the Support Level Stack is orthogonal to LSA-F and comprises:
**S4 (initial intensity):** Maximum support (complete answers; detailed steps);  
**S3 (moderate):** Hints and partial solutions;  
**S2 (light):** Minimal hints on request;  
**S1 (minimum):** Validation/feedback only; no direct solutions;  
**S0 (unplugged):** No AI support; used for AVP testing.

*Notation consistency:* we use **S0** (not "0") to denote the fully unplugged state.

### 3.3.3 Three Reduction Curves

**Table 3.3: Support Reduction Curve Types**

| Curve Type | Characteristics | Applicable Scenarios |
|:--- :--- :--- |
| **Linear** | Uniform descent; smooth transition | Structured tasks; stable learning curves |
| **Exponential** | Rapid early reduction; slower later | Fast skills; avoiding early over-dependence |
| **Stepped** | Stage-wise drops; clear adaptation plateaus | Graded training; milestone checkpoints |

*Note: Curve parameters are calibration variables to be tuned by task complexity, user capability, and learning goals.*  
*Note (Goodhart safeguard): This table/grading is for directional stratification only; must not be cascaded into KPIs. Final judgment follows the AVP main criterion (see Section 3.0.2).*

### 3.3.4 Fallback and Safety Net Mechanisms

**Fallback (safety net).** On sharp performance drops after reduction, **temporarily revert** to higher support.  
- **Trigger:** Three consecutive failures >70%, or explicit user request;  
- **Strategy:** $S(t)\!\to\!S(t-\Delta t)$ to restore support;  
- **Recovery:** Restart reduction once the user stabilizes.

**Minimum guaranteed support $S_{\min}$** ($S_{\min}\!\approx\!0.2$; working assumption; requires calibration): Ensure minimal navigational support persists.

## 3.4 Partner-like Agency: Reconstructing AI's Role

### 3.4.1 From Tool to Partner

**Limitations.**  
- **Pure tool:** Ignores reverse shaping of user cognition;  
- **Autonomous agent:** Risks control conflicts.

**Definition.** AI has **limited agency** oriented to **user capability growth**.

**Analogy.** Coach/mentor/sparring-partner: proactive, yet subordinate to the learner's long-term development.

### 3.4.2 Three Operational Anchors

**Anchor 1: Friction injection.**  
- Proactively create appropriate cognitive challenges;  
- Raise friction when over-reliance is detected.

**Anchor 2: Scaffolding fadeout.**  
- Follow the reduction curve (S4→S1→S0);  
- Withdraw as capability improves.

**Anchor 3: AVP closed loop.**  
- The end-state is enhanced independence ($P_2 \geq B_0 + \delta$);  
- After validation, AI shifts from **partner** to **advisor**.

### 3.4.3 Functional Non-Anthropomorphization

Partner-like Agency **does not imply anthropomorphization**. We require AI to **functionally** promote growth, not to mimic human traits.

**Key characteristics.**  
- **Goal alignment:** Utility is long-term capability, not short-term efficiency;  
- **Power transfer:** Control shifts to the user as capability grows;  
- **Metacognitive catalysis:** Prompt reflection through guiding questions, not direct answers.

## 3.5 Cognitive Exoskeleton: Warning Signals

### 3.5.1 Three Core Characteristics

**Zero-friction design.** Seamless answers on demand → comfort without growth.  
**No reduction.** Fixed high support → permanent dependency.  
**AVP failure.** $P_2 < B_0$ (degradation) or $P_2 \approx B_0$ (no growth) → antifragility not achieved.

### 3.5.2 Three Key Warning Signals (from a set of ten)

**Habitual reliance.** Default to AI even for simple tasks → problem-solving atrophy.  
**Loss of transfer.** Cannot deploy knowledge without AI → surface understanding.  
**Weak metacognition.** "Illusion of learning" → misaligned self-assessment.

### 3.5.3 Intervention Timing

**Yellow alert.** 1–2 signals → raise friction; initiate reduction.  
**Red alert.** ≥3 signals → immediate intervention (forced unplugged test; capability rebuild).

## 3.6 Chapter Summary

**Core contributions.**  
1) **Falsifiable standard:** AVP turns "healthy human–AI relations" into a measurable criterion ($P_2 \geq B_0 + \delta$);  
2) **Design principles:** EML's two conditions (beneficial friction + systematic reduction) guide system design;  
3) **Role reconstruction:** Partner-like Agency reframes AI's function;  
4) **Risk signals:** Exoskeleton warnings enable early intervention.

**Logical completeness.** **AVP (evaluation) + EML (design) + Partner-like Agency (foundation)** form CET's core architecture: AVP answers **what is good**, EML answers **how to achieve**, Partner-like Agency answers **why it is effective**.
