# 仓库协作手册（Repo Playbook）

## 系统架构

### SSOT = GitHub 仓库
- **作用**: 存放所有计划、日志、复盘、项目材料、指标定义
- **定位**: 唯一事实源，所有决策和产出都以这里为准
- **特点**: 可追踪、可复盘、可协作

### AI = 推理与产出引擎
- **作用**: 基于仓库内容进行推理、生成计划、复盘分析
- **输入**: 从仓库读取的 SYNC、Plan、Retro 等文件
- **输出**: 生成新的计划、复盘、文档，沉淀回仓库

## 读取规程 v2.3

### 3-Step 读取流程
1. **Step 1**: 读取 SYNC 快照（Raw URL）
2. **Step 2**: 使用 SYNC 中的 `weekly_plan_raw_url` 读取本周计划
3. **Step 3**: 使用 SYNC 中的 `last_retro_raw_url` 读取上周复盘

### URL 获取与解锁 v2.3（四级策略）

#### A. SYNC 直给（优先）
- 直接从 SYNC.md 读取 `*_raw_url` 字段
- 格式: `https://raw.githubusercontent.com/MRYGP/yangtongxue/main/<file_path>`
- **禁止依赖搜索引擎收录**（不要写 site:raw 作为主路径）

#### B. API 兜底（如果 raw_url 失败）
- 使用 SYNC 中的 `*_api_url` 字段
- 调用 GitHub API: `https://api.github.com/repos/MRYGP/yangtongxue/contents/<file_path>?ref=main`
- 从响应 JSON 中提取 `download_url` 字段
- 使用 `download_url` 读取文件内容

#### C. Blob URL（备选）
- 使用 SYNC 中的 `*_blob_url` 字段
- 格式: `https://github.com/MRYGP/yangtongxue/blob/main/<file_path>`
- 注意: 可能需要解析 HTML 或使用 GitHub 的 Raw 按钮

#### D. 粘贴降级（最后手段）
- 如果所有 URL 方式都失败，要求用户粘贴文件正文片段
- AI 基于片段继续工作

### 校验规则
- **Plan/Retro 前 25 行校验**: 检查是否包含关键字段（week, primary, secondary, mvp, owner, due, data, insights, adjustments）
- **若文件 <25 行**: 则全文校验
- **校验不通过**: 输出缺失字段清单 + 修复入库稿片段

## 周节奏（Mon/Wed/Sun）

### 周一（Mon）: 周计划
- **输入**: 上周复盘、INDEX 当前状态
- **工具**: GPTS 生成周计划模板
- **输出**: `02_plans/YYYY-Www-plan.md`
- **更新**: 同步更新 SYNC.md 和 INDEX.md

### 周三（Wed）: 检查点
- **检查**: 任务进度、识别阻塞
- **记录**: 如有调整，记录在日志中

### 周日（Sun）: 周复盘
- **输入**: 本周计划、执行记录、关键数据
- **工具**: Claude Projects 进行深度复盘分析
- **输出**: `03_logs/YYYY-Www-review.md`
- **更新**: 同步更新 SYNC.md（last_updated/week/plan/retro 指针）和 INDEX.md

## 隐私脱敏规则

### 必须脱敏
- 真实姓名（用代号或"孩子A"）
- 学校名称（用"某小学"或"目标学校"）
- 具体住址（用"长沙市某区"）
- 可识别照片（面部打码或使用示意图）

### 不入库
- 未脱敏的个人信息
- 健康诊断记录（只记录观察和习惯建议）
- 家庭内部敏感对话
- 涉及隐私的心理评估细节

## 文件路径规范

- **周计划**: `02_plans/YYYY-Www-plan.md`
- **周复盘**: `03_logs/YYYY-Www-review.md`
- **日打卡**: `03_logs/YYYY-MM-DD-daily.md`
- **项目文档**: `04_projects/<project_slug>/charter.md`

## 关键原则

1. **仓库是唯一事实源**: 所有决策和产出必须入库
2. **SYNC 是开机入口**: AI 每次工作前先读 SYNC
3. **Plan → Retro 循环**: 每周完成"计划→执行→复盘"闭环
4. **URL 四级策略**: A SYNC直给 → B API → C Blob → D 粘贴降级
5. **每周日更新 SYNC**: 确保指针始终指向最新文件
6. **禁止依赖搜索引擎**: 不要使用 site:raw 作为主路径
