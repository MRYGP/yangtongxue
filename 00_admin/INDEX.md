# INDEX（项目索引）

## 开机读取入口（v2.3）

### 3-step 读取顺序
1. SYNC：读取当前周与指针（只读 raw 文本）
2. weekly_plan：优先打开 weekly_plan_api_url（解码 content） → raw 兜底 → blob
3. last_retro：优先打开 last_retro_api_url（解码 content） → raw 兜底 → blob

### SYNC Raw URL
- https://raw.githubusercontent.com/MRYGP/yangtongxue/main/00_admin/SYNC.md

### 本周关键指针（来自 SYNC）
- weekly_plan_raw_url: https://raw.githubusercontent.com/MRYGP/yangtongxue/main/02_plans/2025-W52-plan.md
- last_retro_raw_url: https://raw.githubusercontent.com/MRYGP/yangtongxue/main/03_logs/2025-W51-review.md
- metrics_dictionary_raw_url: https://raw.githubusercontent.com/MRYGP/yangtongxue/main/00_admin/metrics_dictionary.md

## 本周 MVP
本周完成"每日运动打卡机制"上线 + 科创项目选题确认（1个）并入库

## 进行中项目
- project-demo: 04_projects/project-demo/charter.md

## 最近四周复盘
- 2025-W51: 03_logs/2025-W51-review.md
- 2025-W50: （若存在则补链接；否则删除该行）

## 最大风险/阻塞（写实）
- 运动打卡启动失败（抵触/忘记/阈值过高）
- 选题拖延导致项目无法立项
