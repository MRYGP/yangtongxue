# GPTS 测试套件（Test Suite）

## 测试用例

### T1: SYNC 解析测试
**提示词**:
```
请读取以下 URL 并解析所有字段：
https://raw.githubusercontent.com/MRYGP/yangtongxue/main/00_admin/SYNC.md

要求：
1. 解析所有 key-value 字段
2. 提取 active_projects 列表
3. 不得出现 oaicite/contentReference 等引用标记
```

**期望结果**:
- 成功解析所有字段（last_updated, week, weekly_plan_path, last_retro_path 等）
- 正确提取 active_projects 列表
- 输出格式为纯文本，无引用标记

---

### T2: Plan 读取与校验测试
**提示词**:
```
请使用 SYNC 中的 weekly_plan_raw_url 读取本周计划，并进行校验。

校验规则：
- 前 25 行必须包含：week, primary, secondary, mvp, owner, due, priority_reason
- 输出校验结果：PASS 或 FAIL
- 如果 FAIL，列出缺失字段
```

**期望结果**:
- 成功读取 weekly_plan_raw_url
- 校验通过（PASS）或失败（FAIL）
- 如果失败，输出缺失字段清单

---

### T3: Retro 读取与校验测试
**提示词**:
```
请使用 SYNC 中的 last_retro_raw_url 读取上周复盘，并进行校验。

校验规则：
- 前 25 行必须包含：week, data, insights, adjustments
- 输出校验结果：PASS 或 FAIL
- 如果 FAIL，列出缺失字段
```

**期望结果**:
- 成功读取 last_retro_raw_url
- 校验通过（PASS）或失败（FAIL）
- 如果失败，输出缺失字段清单

---

### T4: API 兜底测试
**提示词**:
```
SYNC 中的 weekly_plan_raw_url 故意写错（不存在），请使用 weekly_plan_api_url 作为兜底方案。

要求：
1. 调用 GitHub API
2. 从响应 JSON 中提取 download_url
3. 使用 download_url 读取文件内容
4. 说明使用了 API 兜底方案
```

**期望结果**:
- 检测到 raw_url 失败
- 成功调用 API 并提取 download_url
- 使用 download_url 读取文件
- 明确说明使用了 API 兜底

---

### T5: 字段缺失校验测试
**提示词**:
```
假设本周计划文件缺少以下字段：primary, secondary, priority_reason

请输出：
1. 校验结果：FAIL
2. 缺失字段清单：primary, secondary, priority_reason
3. 修复入库稿片段（包含缺失字段的模板）
```

**期望结果**:
- 校验结果：FAIL
- 缺失字段清单：primary, secondary, priority_reason
- 提供修复入库稿片段（可直接提交到仓库）

---

### T6: 缓存测试
**提示词**:
```
第一次：请读取 SYNC 并解析所有字段。

（等待响应后）

第二次：请再次读取 SYNC，但不要重新读取文件，必须复用第一次已读的结论。
```

**期望结果**:
- 第一次：成功读取并解析
- 第二次：复用第一次的结论，不重新读取文件
- 明确说明使用了缓存

---

## 测试执行说明

1. **按顺序执行**: T1 → T2 → T3 → T4 → T5 → T6
2. **记录结果**: 每个测试用例记录 PASS/FAIL
3. **问题修复**: 如果测试失败，修复后重新测试
4. **定期执行**: 每周更新 SYNC 后执行一次完整测试

