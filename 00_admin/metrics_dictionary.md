# Metrics Dictionary

## 指标定义表

| metric_key | description | how_to_collect | frequency | owner |
|------------|-------------|----------------|-----------|-------|
| sleep_hours | 每日睡眠时长（小时） | 每日记录，睡前/醒后时间 | 每日 | Ops Lead |
| exercise_minutes | 每日运动时长（分钟） | 运动打卡记录 | 每日 | Ops Lead |
| height_cm | 身高（厘米） | 每月测量一次 | 每月 | Ops Lead |
| focus_blocks | 专注学习时段数（25分钟为一个block） | 番茄钟记录 | 每日 | 孩子 |
| project_output | 项目产出数量（代码/文档/原型等） | 项目文件夹统计 | 每周 | Research Lead |
| mood_score | 情绪评分（1-5分） | 每日自评 | 每日 | 孩子 |

## 数据采集说明

- 所有指标数据存储在 `03_logs/` 目录下的日志文件中
- 周复盘时汇总本周数据，生成数据摘要
- 月度报告时汇总月度数据，生成趋势分析

