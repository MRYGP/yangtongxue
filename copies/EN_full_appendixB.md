: Parameter Registry (SSOT)

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
