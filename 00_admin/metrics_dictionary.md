# Metrics Dictionary

## 指标定义

### sleep_hours
- name: sleep_hours
- definition: 每日睡眠时长（小时）
- how_to_collect: 每日记录，睡前/醒后时间
- frequency: 每日
- owner: Ops Lead

### exercise_minutes
- name: exercise_minutes
- definition: 每日运动时长（分钟）
- how_to_collect: 运动打卡记录
- frequency: 每日
- owner: Ops Lead

### height_cm
- name: height_cm
- definition: 身高（厘米）
- how_to_collect: 每月测量一次
- frequency: 每月
- owner: Ops Lead

### focus_blocks
- name: focus_blocks
- definition: 专注学习时段数（25分钟为一个block）
- how_to_collect: 番茄钟记录
- frequency: 每日
- owner: 孩子

### project_output
- name: project_output
- definition: 项目产出数量（代码/文档/原型等）
- how_to_collect: 项目文件夹统计
- frequency: 每周
- owner: Research Lead

### mood_score
- name: mood_score
- definition: 情绪评分（1-5分）
- how_to_collect: 每日自评
- frequency: 每日
- owner: 孩子

### schulte_time
- name: schulte_time
- definition: 舒尔特表完成时间（秒）
- how_to_collect: 每次课开头记录
- frequency: 每次课
- owner: Ops Lead
- target: 40秒以内（5x5表）

## 五维能力经验值

### 身体发育力经验值
- name: 身体发育力经验值
- definition: 运动完成度、连续打卡天数、睡眠达标的综合评分
- how_to_collect: 每次课后自动计算
- frequency: 每次课后
- owner: Ops Lead

### AI协作力经验值
- name: AI协作力经验值
- definition: 独立使用AI次数、AI工具熟练度的综合评分
- how_to_collect: 每次课后自动计算
- frequency: 每次课后
- owner: Ops Lead

### 学业掌握度经验值
- name: 学业掌握度经验值
- definition: 错题攻克率、知识点理解深度的综合评分
- how_to_collect: 每次课后自动计算
- frequency: 每次课后
- owner: Ops Lead

### 创新思维力经验值
- name: 创新思维力经验值
- definition: 项目推进步骤、独立解决问题次数的综合评分
- how_to_collect: 每次课后自动计算
- frequency: 每次课后
- owner: Ops Lead

### 表达清晰度经验值
- name: 表达清晰度经验值
- definition: 讲解流畅度、表达结构化程度的综合评分
- how_to_collect: 每次课后自动计算
- frequency: 每次课后
- owner: Ops Lead

## 数据采集说明

- 所有指标数据存储在 `03_logs/` 目录下的日志文件中
- 周复盘时汇总本周数据，生成数据摘要
- 月度报告时汇总月度数据，生成趋势分析
- 五维能力经验值存储在 `00_admin/ability-levels.md` 中，每次课后自动更新
