### MSO (Multi-Scale Orchestrator, 多尺度编排器)

Multi-Scale Orchestrator, an L4 layer module of LSA. Function: coordinate individual, team, and organizational-level goals, ensure system adheres to ethical constraints. Strategy management: organizational strategy → team strategy → individual strategy → F(t)/S(t) parameters. Coordination mechanisms: ① Bottom-up (individual aggregation) ② Top-down (goal decomposition) ③ Conflict resolution (long-term resilience > short-term efficiency). First appearance: Section 5.5.

------

## Organizational Indicators

### BCI (Business Continuity Index, 业务连续性指数)

Business Continuity Index: sustainability of core business under 48h no-AI conditions (adjustable to 24/48/72h by sectoral risk level; working assumption). Measurement method: 48-hour outage drill simulates complete AI service interruption, assesses which businesses stop and which barely sustain. Used in O-AVP formula: BCI×0.4 + ICR×0.6. First appearance: Section 4.2.

### ICR (Independent Capability Retention, 独立能力保持率)

Independent Capability Retention: the proportion of employees who can complete critical tasks without AI. Measurement method: random sampling of employees, testing whether they can independently complete core work tasks (without AI assistance). Used in O-AVP formula: BCI×0.4 + ICR×0.6. First appearance: Section 4.2.

------

## Key Mechanisms

### Dependency Lock-in (依赖锁定)

A pathological state where users form permanent reliance on AI and cannot function independently. Characteristics: ① Habitual reliance even for simple tasks ② Loss of transfer capability ③ Weak metacognition ④ AVP failure (P₂ < B₀). Prevention mechanisms: beneficial friction + systematic support reduction + periodic Unplugged Tests. First appearance: Section 3.3.

### Equivalent Effort Principle (等效努力原则)

A fairness principle in human-AI collaboration: adjust **task format** without lowering **challenge intensity**; assess by **relative improvement** rather than absolute level; (if involving accessibility) **challenge budget conservation**. Purpose: ensure users with different baselines all experience moderate cognitive effort, avoiding both over-protection and excessive frustration. First appearance: Section 5.5.

### Weakest-Link Effects (短板效应/最弱环效应)

In team collaboration, overall team capability is limited by members with the lowest capability (weakest link), not the simple sum of all members' capabilities. When some members highly depend on AI while others maintain independence, team resilience becomes fragile. Prevention: role rotation, knowledge sharing, regular team-level Unplugged Tests. First appearance: Section 5.5.

### Tragedy of the Cognitive Commons (认知公地悲剧)

At the societal level: individual rationality (using AI to improve efficiency) leads to collective irrationality (society-wide independent capability decline). Characteristics: ① Short-term individual optimization ② Long-term collective risk ③ Path dependence reinforcement ④ Exponentially rising recovery costs. Window period: 2025–2035 (working assumption) is the critical intervention period. First appearance: Section 4.3.

### Generational Divide (代际鸿沟)

Significant capability differences between generations due to different technology usage patterns. T₀ generation (1980–2000): pre-AI era, strong independent capability. T₁ generation (2000–2015): AI transition period, mixed capability. T₂ generation (2015–): AI native, risk of independent capability deficiency. H8 hypothesis predicts: by 2035–2040, T₂ generation will have significantly lower independent capability than T₀ generation (Cohen's d > 0.3). First appearance: Section 4.3.

------

## Falsifiable Hypotheses (H1–H8)

### H1: AVP-Basic Hypothesis

**Statement**: In procedural cognitive tasks, AI tools designed with beneficial friction (50–70% success rate, working assumption) + systematic support reduction (S4→S1→S0) will result in users' independent performance significantly exceeding baseline after W weeks of collaboration (P₂ ≥ B₀ + δ; see §3.0.2).

**Falsification condition**: Under rigorous RCT design, experimental and control groups show no significant P₂ difference (Cohen's d < 0.2), or P₂ < B₀.

**Validation method**: 2×2 factorial RCT, N ≥ 200, multi-domain replication.

First appearance: Section 6.2.

### H2: Beneficial Friction Hypothesis

**Statement**: An "optimal challenge zone" exists (50–70% success rate, working assumption); within this zone, user capability enhancement (P₂ - B₀) is maximized.

**Falsification condition**: Prove friction intensity and capability enhancement have a linear relationship (no inverted-U curve), or optimal zone significantly deviates from 50–70%.

**Validation method**: Multi-arm trial, 5–7 friction levels, N ≥ 300.

First appearance: Section 6.2.

### H3: Systematic Reduction Hypothesis

**Statement**: Systematic support reduction (S4→S1→S0) outperforms fixed support; systematic reduction group has significantly higher AVP pass rate and long-term retention.

**Falsification condition**: Fixed support group P₂ performance not inferior to reduction group.

**Validation method**: 3×2 factorial experiment, N ≥ 240.

First appearance: Section 6.2.

### H4: Team Capability Polarization Hypothesis

**Statement**: Under AI use without EML constraints, capability polarization emerges within teams; T-AVP declines.

**Falsification condition**: Within-team capability variance shows no significant change, or low-capability individuals also gain enhancement.

**Validation method**: Natural experiment, 50–100 teams, 6–12 months.

First appearance: Section 6.2.

### H5: Organizational Resilience Hypothesis

**Statement**: Organizations with O-AVP < 0.70 (alert threshold; working assumption) have significantly longer recovery times after AI disruption.

**Falsification condition**: Find organizations with O-AVP < 0.70 but rapid recovery (<12h), or target thresho# Appendix A: Core Terminology Glossary

## Theoretical Core Concepts

### Cognitive Endosymbiosis (认知内共生)

An AI-as-cognitive-partner collaboration pattern that promotes independent capability enhancement through beneficial friction and systematic support reduction. Characteristics: ① Beneficial Cognitive Friction ② Systematic Support Reduction ③ AVP validation passed (P₂ ≥ B₀ + δ). First appearance: Section 1.3, complete definition: Section 3.0.3 (EML definition Anchor B2). Contrast: Cognitive Exoskeleton (pathological pattern).

### Cognitive Exoskeleton (认知外骨骼)

A pathological pattern where over-reliance on AI leads to independent capability degradation. Characteristics: ① Zero-friction design ② No support reduction ③ AVP failure (P₂ < B₀). Users perform well during collaboration (P₁ high) but capability declines after unplugging (P₂ < B₀). First appearance: Section 1.2, detailed definition: Section 3.0.6. Contrast: Cognitive Endosymbiosis (target pattern).

### Antifragility Validation Principle (AVP, 反脆弱性验证原则)

An assessment standard that uses the Unplugged Test to verify whether human-AI collaboration promotes independent capability. Core criterion: P₂ ≥ B₀ + δ, where B₀ is baseline capability, P₂ is independent performance after unplugging, and δ is minimum meaningful lift threshold (Cohen's d ≥ 0.3 or relative improvement ≥ 10%, working assumption). P₁ (collaboration performance) does not participate in final judgment. First appearance: Section 1.3, complete definition: Section 3.0.2 (AVP definition Anchor B1).

### Endosymbiotic Minimal Law (EML, 内共生最小法则)

Design necessary conditions for constituting Cognitive Endosymbiosis: ① Beneficial Cognitive Friction (optimal challenge zone, 50–70% success rate, working assumption) ② Systematic Support Reduction (S4→S1→S0). These two constitute jointly sufficient design conditions, but ultimately still require AVP (P₂ ≥ B₀ + δ) as the necessary acceptance criterion. First appearance: Section 1.3, complete definition: Section 3.0.3 (EML definition Anchor B2).

### Partner-like Agency (伙伴式主体性)

The ideal role positioning of AI as a cognitive partner. AI has limited agency oriented toward promoting user capability growth, can act proactively but always serves the user's long-term development. Three operationalizable anchors: ① Friction injection ② Scaffolding fadeout ③ AVP closed loop. Characteristics: functional non-anthropomorphization, goal alignment, power transfer. First appearance: Section 1.3, detailed exposition: Section 3.4.

### Unplugged Test (拔线测试)

A standardized testing method that measures independent capability in an AI-free environment. Key elements: ① Equivalence (same task difficulty) ② Unplugged window W (4–8 weeks, default 6 weeks, working assumption) ③ Violation monitoring. Purpose: validate whether AI collaboration promotes capability internalization. First appearance: Section 3.1, measurement protocol: Appendix D.

------

## Design Mechanism Terms

### Beneficial Cognitive Friction (有益认知摩擦)

A design strategy where moderate challenge (target success rate 50–70%, working assumption; requires cross-domain/task calibration; individual adaptation required) promotes capability growth. Three types: ① Completeness friction (leave blanks for users to fill) ② Abstraction friction (provide concepts rather than steps) ③ Delayed-feedback friction (delay feedback to enforce independent thinking). Theoretical foundation: flow theory + Zone of Proximal Development (ZPD). First appearance: Section 3.2.

### Systematic Support Reduction (系统性支持削减)

A design strategy where AI support intensity gradually decreases from S4→S1→S0 according to a predetermined reduction curve. Purpose: ensure extension is temporary scaffolding rather than a permanent crutch. Reduction curve types: linear, exponential, stepped, adaptive. Key mechanisms: fallback and minimum guaranteed support (S_min). First appearance: Section 3.3.

### Optimal Challenge Zone (最优挑战区)

To promote long-term retention and transfer, the system should adaptively adjust task difficulty/prompt intensity to a 50–70% success rate (working assumption; requires cross-domain/task calibration; population-level; individual calibration required). >85% approaches offloading, <30% risks frustration, 50–70% optimal balance. Theoretical source: Vygotsky's Zone of Proximal Development (ZPD). First appearance: Section 3.2, definition anchor: Section 3.0.5 (B4).

### Support-Intensity Stack (支持档位栈, S4→S1→S0)

A graded system expressing support intensity. S4 (maximum support) → S3 (moderate support) → S2 (light support) → S1 (minimum support) → S0 (complete unplugging, used for AVP testing). Orthogonal dimension to LSA-F's L1–L4 functional layers. First appearance: Section 3.3, definition anchor: Section 3.0.4 (B3).

### Reduction Curve (削减曲线)

The function of support intensity S(t) changing over time t. Types: ① Linear (uniform descent) ② Exponential (fast early, slow late) ③ Stepped (stage-wise drops) ④ S-curve (slow early, fast middle, slow late) ⑤ Adaptive (dynamically adjusts based on user state). Selection basis: task complexity, user capability, learning goals. First appearance: Section 3.3, implementation: Section 5.3 (SGS).

### Fallback Mechanism (回退机制, Safety Net)

A safety mechanism where the system temporarily reverts to a higher support level when detecting sharp performance decline after reduction. Trigger conditions: three consecutive failures >70% or explicit user request. Fallback strategy: S(t) → S(t-Δt). Recovery path: restart reduction after user stabilizes. First appearance: Section 3.3, implementation: Section 5.3.

### Minimum Guaranteed Support (保底支持, S_min)

The minimum support intensity threshold during reduction (working assumption ≈ 0.2; requires calibration), ensuring users always have minimal navigational support and are never completely "stuck." Implementation: maintained by LSA's L2 friction calibration engine and L4 metacognitive coordination layer. First appearance: Section 3.3, implementation: Sections 5.3–5.5.

------

## Measurement Parameter Terms

### Baseline Capability (基线能力, B₀)

User's independent capability level before using AI, obtained through standardized testing at time T₀. Measurement requirements: AI-free environment, standard tasks, blind evaluation. Unit: task-specific scoring (e.g., percentage, IRT θ value). First appearance: Section 3.0.2.

### Performance during Collaboration (协作期表现, P₁)

User's task performance while collaborating with AI, a process indicator. High P₁ only indicates AI effectiveness, cannot judge whether capability improved, thus does not participate in AVP final judgment. Can be used for friction intensity calibration. First appearance: Section 3.0.2.

### Post-Unplugged Performance (拔线后能力, P₂)

User's independent task performance after the unplugged window (W = 4–8 weeks, default 6 weeks; working assumption), the core indicator of AVP validation. Measurement requirements: equivalent parallel test, AI-free environment, blind evaluation. Judgment: P₂ ≥ B₀ + δ is success. First appearance: Section 3.0.2.

### Minimum Meaningful Lift Threshold (最小提升阈值, δ)

The minimum threshold for judging whether capability improvement is meaningful. Working assumption: Cohen's d ≥ 0.3 or relative improvement ≥ 10% (requires cross-domain/task calibration). Selection basis: ① Statistical significance (small-to-medium effect) ② Measurement error tolerance ③ Cross-domain comparability. Different tasks may require adjustment: high-risk tasks Cohen's d ≥ 0.5, low-risk tasks ≥ 0.2. First appearance: Section 3.0.2, calibration: Section 3.1.

### Unplugged Window (拔线窗口, W)

The time window for complete cessation of AI use, used to measure whether capability is internalized. Working assumption: 4–8 weeks (default 6 weeks; requires cross-domain/task calibration). Selection basis: balance capability stability with environmental factor control. Different tasks may require adjustment: fast skills 4 weeks, complex skills 8–12 weeks, professional capabilities several months. First appearance: Section 3.0.2, calibration: Section 3.1.

### Capability Vector (能力向量, C(t))

A multi-dimensional vector representation of user capability state that changes over time t. Typical dimensions (5–20 dimensions; requires domain definition): problem decomposition, implementation skill, debugging capability, metacognition, etc. Data sources: ① P₂ Unplugged Test (reference standard) ② Daily task performance (indirect inference) ③ Self-report (auxiliary) ④ Peer evaluation (team layer). First appearance: Section 5.4.

------

## Cross-Scale Concept Terms

### I-AVP (Individual-level AVP, 个体层反脆弱性验证)

Individual-level antifragility validation. Core criterion: P₂ ≥ B₀ + δ. Applicable scenarios: learning tools, skill training, personal productivity tools. Measurement method: standard Unplugged Test (W = 4–8 weeks). This is CET's foundational scale; other scales extend from this. First appearance: Section 4.1.

### T-AVP (Team-level AVP, 团队层反脆弱性验证)

Team-level antifragility validation. Core criterion: P₂,team ≥ B₀,team + δ_team (Cohen's d ≥ 0.3; population-level; working assumption). Key finding: even when all members pass I-AVP, team level may still fail (emergence). Failure modes: capability polarization, tacit knowledge loss, role rigidity. Measurement method: collective Unplugged Test (W = 4–8 weeks). First appearance: Section 4.1.

### O-AVP (Organizational-level AVP, 组织层反脆弱性验证)

Organizational-level antifragility validation. Core criterion: BCI×0.4 + ICR×0.6 ≥ threshold (alert ≥ 0.70, target ≥ 0.85; working assumption). BCI = Business Continuity Index, ICR = Independent Capability Retention. Measurement method: 48-hour outage drill (adjustable to 24/48/72h by sector). Organizational risks: critical capability hollowing, knowledge transmission rupture, cognitive infrastructure single point of failure. First appearance: Section 4.2.

### S-AVP (Societal-level AVP, 社会层认知资本指标)

Societal-level cognitive capital indicators. Cannot directly unplug test; must rely on proxy indicator set: ① Generational capability differences (T₀ vs. T₁ vs. T₂; defined in Chapter 4) ② Industry independent capability baselines ③ Education system indicators ④ Labor market signals. Core concerns: tragedy of the cognitive commons, generational divide, window period (2025–2035; working assumption). First appearance: Section 4.3.

### Cascading Vulnerability (级联脆弱)

The phenomenon where low-scale vulnerability propagates upward with nonlinear amplification. Path: individual dependency (I-AVP failure 30%) → team fragility (T-AVP failure 50%) → organizational crisis (O-AVP < 0.70) → societal risk (S-AVP yellow alert). Amplification mechanisms: ① Emergence nonlinearity ② Repair time lag ③ Path dependence reinforcement. First appearance: Section 4.4.

------

## Architecture-Related Terms

### Layered Symbiosis Architecture (分层共生架构, LSA)

A four-layer technical architecture for implementing CET theory. L1 (Foundation AI Layer): model access, knowledge base. L2 (Friction & Reduction Layer): CFE Cognitive Friction Engine + SGS Support Graduation Scheduler. L3 (Monitoring & Feedback Layer): AVP-TM Telemetry Module + alert system. L4 (Orchestration & Governance Layer): Multi-Scale Orchestrator MSO + ethical governance. First appearance: Section 5.1, definition anchor: Section 3.0.4 (B3).

### CFE (Cognitive Friction Engine, 认知摩擦引擎)

Cognitive Friction Engine, an L2 layer module of LSA. Function: dynamically adjust AI response's completeness, abstraction, and delay based on user capability, maintaining 50–70% success rate (working assumption). Strategies: ① Completeness friction (partial answers) ② Abstraction friction (conceptual guidance) ③ Delayed-feedback friction (delayed feedback) ④ Adaptive friction (adjust based on C(t)). First appearance: Section 5.2.

### SGS (Support Graduation Scheduler, 支持削减调度器)

Support Graduation Scheduler, an L2 layer module of LSA. Function: manage support intensity S(t) reduction curve from S₀ to S0. Mechanisms: ① Curve selection (linear/exponential/stepped/S-curve) ② Fallback trigger (consecutive failures > threshold) ③ Minimum guaranteed support (S_min ≈ 0.2; working assumption) ④ Recovery path (restart reduction after stabilization). First appearance: Section 5.3.

### AVP-TM (AVP Telemetry Module, AVP遥测模块)

AVP Telemetry Module, an L3 layer module of LSA. Function: continuously assess user capability C(t), detect dependency lock-in risks, trigger intervention mechanisms. Data sources: task logs, collaboration records, drill data. Alert system: green (healthy) → yellow (stagnant) → red (degradation) → black (AVP failure). First appearance: Section 5.4.

### MSO (Multi-Scale Orchestrator, 多尺度编排器)

Multi-Scale Orchestrator, an L4 layer module of LSA. Function: coordinate individual, team, and organizational-level goals, ensure system adheres to ethical constraints. Strategy management: organizational strategy → team strategy → individual strategy → F(t)/S(t) parameters. Coordination mechanisms: ① Bottom-up (individual aggregation) ② Top-down (goal decomposition) ③ Conflict resolution (long-term resilience > short-term efficiency). First appearance: Section 5.5.