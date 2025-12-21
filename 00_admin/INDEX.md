# INDEX（项目索引）

## 开机读取入口（v2.3）

### 3-Step 读取流程
1. SYNC：读取 SYNC 快照获取当前状态
2. weekly_plan：使用 SYNC 中的 weekly_plan_raw_url 读取本周计划
3. last_retro：使用 SYNC 中的 last_retro_raw_url 读取上周复盘

### URL 优先级
- 优先使用：SYNC 中的 *_raw_url（直接可读）
- raw_url 失败：使用 *_api_url → 提取 download_url
- 不依赖：搜索引擎收录

### SYNC Raw URL
- https://raw.githubusercontent.com/MRYGP/yangtongxue/main/00_admin/SYNC.md

## 本周最小目标（MVP）
- 建立每日运动打卡机制并完成第一个科创项目的选题确认。

## 正在进行的项目（/04_projects）
- project-demo：04_projects/project-demo/charter.md

## 最近四周复盘（/03_logs）
- 2025-W51：03_logs/2025-W51-review.md
- 2025-W50：03_logs/2025-W50-review.md

## 最大风险/阻塞
- 风险1：孩子对打卡机制有抵触情绪
  - 应对：降低初始目标，先建立习惯
- 风险2：项目选题时间不足
  - 应对：提前准备 3 个候选方案，缩短讨论时间

## 本周仓库待更新清单
- [ ] 00_admin/SYNC.md - 更新 week 和路径指针
- [ ] 00_admin/INDEX.md - 更新本周MVP和项目状态
- [ ] 02_plans/2025-W52-plan.md - 生成下周计划
- [ ] 03_logs/2025-W51-review.md - 完成本周复盘

## 当前主线（五条）
- 身体发育与运动
- AI 素养与工具能力
- 学业与基础能力
- 创新与科创项目
- 表达与传播

## 下一步（本周行动清单）
- [ ] 设计每日运动打卡表（跳绳500个 + 拉伸10分钟）
- [ ] 教孩子使用 ChatGPT 辅助学习（错题分析）
- [ ] 完成项目选题确认（3个候选方案 → 1个确定）
- [ ] 用 AI 工具分析本周错题，生成错题本
- [ ] 让孩子对 AI 讲解本周学习内容（5分钟）

## 项目运行与 AI 手册

### 运行手册
- [OPS.md](OPS.md) - 运行手册（每周节奏、交付物、角色分工、隐私边界）

### AI 协作
- [AI_PLAYBOOK.md](AI_PLAYBOOK.md) - AI 协作手册（GPTS / Claude Projects 使用指南）
- [GPTS_SPEC.md](GPTS_SPEC.md) - GPTS 规格说明（版本与变更记录）
