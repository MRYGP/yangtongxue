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

## 3-Step 读取流程

### Step 1: 读取 SYNC 快照
**Raw URL**:
```
https://raw.githubusercontent.com/MRYGP/yangtongxue/main/00_admin/SYNC.md
```

SYNC.md 包含:
- `last_updated`: 最后更新日期
- `week`: 当前周数
- `weekly_plan_path`: 本周计划文件路径
- `last_retro_path`: 上周复盘文件路径
- `active_projects`: 活跃项目列表

### Step 2: 读取周计划（Plan）
根据 SYNC 中的 `weekly_plan_path` 读取本周计划。

**如果无法直接打开**，使用搜索解锁:
```
site:raw.githubusercontent.com MRYGP/yangtongxue "<file_path>"
site:github.com MRYGP/yangtongxue "<file_path>"
```

### Step 3: 读取周复盘（Retro）
根据 SYNC 中的 `last_retro_path` 读取上周复盘。

**如果搜索解锁仍失败**: 粘贴文件正文片段给 AI，AI 可以基于片段继续工作。

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

## URL 解锁方法

某些 AI 环境存在"只能打开用户消息/搜索结果出现过的 URL"的限制。

**搜索模板**:
```
site:raw.githubusercontent.com MRYGP/yangtongxue "02_plans/2025-W52-plan.md"
site:github.com MRYGP/yangtongxue "02_plans/2025-W52-plan.md"
```

替换文件路径即可。

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
4. **URL 解锁机制**: 遇到无法打开的文件，先用搜索解锁
5. **每周日更新 SYNC**: 确保指针始终指向最新文件
