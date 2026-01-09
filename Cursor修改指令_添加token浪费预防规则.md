# Cursor修改指令：添加Token浪费预防规则

## 任务
在 `立体教育培养助手v5.0.md` 中添加Token浪费预防规则

## 修改位置
在第54行（第一个`---`分隔符后）插入新内容

## 具体步骤

### Step 1: 打开文件
```bash
code 立体教育培养助手v5.0.md
```

### Step 2: 定位插入位置
找到第54行：
```
```

### Step 3: 在第54行后插入以下内容
```markdown
## ⚠️ TOKEN WASTE PREVENTION RULES (Claude Projects Only)

**CRITICAL: These actions are FORBIDDEN - they waste tokens with near-zero success rate:**

### 🚫 禁止的操作

#### 1. ❌ 不要用 web_search 搜索 GitHub 文件
```
错误示例：
web_search("site:github.com MRYGP yangtongxue 立体教育培养助手v5.0")

为什么禁止：
- 成功率 <5%（私有仓库/小众仓库不被搜索引擎索引）
- 返回大量无关结果（浪费token解析）
- GitHub有429速率限制

正确做法：
→ 先检查uploads
→ uploads没有 → 直接问用户："请上传该文件"
```

#### 2. ❌ 不要多次重试同一个失败的URL
```
错误示例：
TRY 1: curl https://api.github.com/... → 403
TRY 2: curl https://api.github.com/... (不同参数) → 403
TRY 3: curl https://raw.githubusercontent.com/... → 空返回
TRY 4: web_fetch(...) → 403

为什么禁止：
- 网络配置限制不会因重试改变
- 每次失败浪费1-2次tool call

正确做法：
→ 第一次失败 → 立即切换策略
→ api.github.com失败 → 不要再试raw或blob
→ 直接要求用户上传
```

#### 3. ❌ 不要尝试访问不在白名单的域名
```
已知受限域名（会失败）：
- api.github.com (403错误)
- raw.githubusercontent.com (空返回/blocked)

唯一可访问的GitHub域名：
- github.com (仅网页，不能读取文件内容)

正确做法：
→ 不要浪费时间尝试受限域名
→ 发现文件不在uploads → 立即要求用户上传
```

#### 4. ❌ 不要在失败后继续"探索其他可能性"
```
错误模式（常见错误）：
uploads没有 → 试GitHub API → 失败
→ "让我试试raw URL" → 失败
→ "让我试试web_search" → 失败
→ "让我试试blob URL" → 失败
→ 浪费4-5次tool call，最终还是要用户上传

正确模式（快速失败 Fail Fast）：
uploads没有 → 试GitHub API → 失败
→ "该文件不在我的uploads目录，GitHub访问也失败了。
   请上传文件，或粘贴文件内容前100行。"
→ 只用了2次tool call，节省60-80% token
```

---

### ✅ 正确的文件读取流程（复习）

```
用户提到文件 / 上传文件
    ↓
STEP 1: 检查 uploads
    view /mnt/user-data/uploads
    ↓
文件在uploads？
    ├─ YES → 直接使用 (view /mnt/user-data/uploads/filename) ✅
    │        停在这里，工作完成
    │
    └─ NO → STEP 2: 问用户
            "该文件不在我的uploads目录。
             请上传文件，或粘贴关键内容。"
            停在这里，等用户响应 ✅

不要做：
❌ 试GitHub API
❌ 试raw URL  
❌ web_search搜索
❌ 多次重试
❌ "探索其他可能性"

为什么不做：
→ 成功率极低（<5%）
→ 浪费大量token
→ 最终还是要用户上传
→ 不如一开始就直接问用户
```

---

### 📊 Token节省效果对比

| 场景 | 错误做法（token消耗） | 正确做法（token消耗） | 节省 |
|------|--------------------|--------------------|----|
| 读取文件 | uploads → API → raw → web_search → 最终上传<br>约5-8次tool call，~3000 tokens | uploads → 直接要求上传<br>1次tool call，~500 tokens | **83%** |
| 验证URL | 尝试3-4种URL格式<br>约4次tool call，~2000 tokens | 第一次失败立即停止<br>1次tool call，~500 tokens | **75%** |
| 搜索文件 | web_search返回10个无关结果<br>~1500 tokens | 不搜索，直接问用户<br>~200 tokens | **87%** |

**平均节省：75-85% token** ⚡

---

### 🎯 实施检查清单

在执行任何文件读取操作前，自问：

- [ ] 我检查了uploads目录吗？
- [ ] 如果第一次失败，我是否立即停止了？
- [ ] 我是否避免了web_search？
- [ ] 我是否避免了多次重试同一URL？
- [ ] 我是否直接要求用户帮助？

**如果有任何"否"→ 你在浪费token，立即停止，切换策略。**

---

### 📝 示例对话（正确vs错误）

#### ❌ 错误示例（浪费5次tool call）
```
用户："读取立体教育培养助手v5.0.md"
Assistant: 
  → view /mnt/user-data/uploads (没找到)
  → curl api.github.com/... (403)
  → curl raw.githubusercontent.com/... (空返回)
  → web_search("site:github.com ...") (无关结果)
  → web_fetch("github.com/blob/...") (403)
  → "请上传文件" 
  
结果：浪费5次tool call，~3000 tokens
```

#### ✅ 正确示例（只用1次tool call）
```
用户："读取立体教育培养助手v5.0.md"
Assistant:
  → view /mnt/user-data/uploads (没找到)
  → "该文件不在我的uploads目录。请上传文件或粘贴内容。"
  
结果：只用1次tool call，~500 tokens，节省83%
```

---

**本规则生效日期**：立即生效  
**适用对象**：Claude Projects only  
**更新者**：用户基于2025-01-09对话反馈

```

### Step 4: 保存并提交
```bash
git add 立体教育培养助手v5.0.md
git commit -m "添加Token浪费预防规则 禁止web_search搜索GitHub 快速失败策略"
git push origin main
```

---

## 预期效果

添加此规则后，Claude Projects将：

✅ 避免用web_search搜索GitHub文件（节省~1500 tokens/次）
✅ 第一次URL失败后立即停止（节省~2000 tokens/次）
✅ 不再尝试受限域名（节省~1000 tokens/次）
✅ 快速失败，直接要求用户上传（节省75-85% token）

**总体token节省率：75-85%** ⚡

---

## 验证步骤

修改完成后，测试以下场景：

### 测试1：读取不存在的文件
```
用户："读取某个不存在的文件.md"
期望：
1. 检查uploads
2. 没找到 → 立即要求用户上传
3. 不尝试GitHub/web_search
```

### 测试2：读取GitHub上的文件
```
用户："读取GitHub上的SYNC.md"
期望：
1. 检查uploads
2. 没找到 → 询问："应该从GitHub读取还是等你上传？"
3. 如果用户说GitHub → 尝试一次 → 失败 → 要求上传
```

### 测试3：用户上传文件
```
用户：上传文件
期望：
1. 立即从uploads读取
2. 不尝试GitHub
```

---

## 问题排查

如果修改后仍然浪费token：

1. 检查是否在第54行正确插入
2. 检查Markdown格式是否正确（特别是代码块）
3. 确认已推送到GitHub
4. 在Claude Projects中刷新知识库
