# ====== 配置 ======
$REPO_URL="https://github.com/MRYGP/yangtongxue.git"
# =================================

$ErrorActionPreference="Stop"

# 检查是否已有 git 仓库
if (Test-Path .git) {
    Write-Host "检测到已有 git 仓库，拉取最新内容..."
    git pull origin main -q
} else {
    Write-Host "初始化 git 仓库..."
    git init
    git branch -M main
    git remote add origin $REPO_URL
    git pull origin main --allow-unrelated-histories -q 2>$null
}

# 目录结构
"00_admin","01_people","02_plans","03_logs","04_projects","05_assets","06_reports" | ForEach-Object {
  New-Item -ItemType Directory -Force -Path $_ | Out-Null
}

# 基础文件（如果不存在则创建）
if (-not (Test-Path README.md)) {
    @"
# 立体教育研究仓库（GitHub 驱动）
这是一个"研究化 + 项目化"的家庭教育长期项目仓库。
唯一事实源：本仓库内容（计划 / 日志 / 复盘 / 产出）。

建议从 /00_admin/INDEX.md 开始。
"@ | Set-Content -Encoding UTF8 README.md
}

@"
# INDEX（项目索引）

## 当前主线（五条）
- 身体发育与运动：
- AI 素养与工具能力：
- 学业与基础能力：
- 创新与科创项目：
- 表达与传播：

## 本周最小目标（MVP）
- 

## 正在进行的项目（/04_projects）
- 

## 最近四周复盘（/03_logs）
- 

## 下一步（本周行动清单）
- 
"@ | Set-Content -Encoding UTF8 00_admin\INDEX.md

@"
# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/

# Logs
*.log

# Secrets
.env
"@ | Set-Content -Encoding UTF8 .gitignore

# 添加所有文件
git add .

# 检查是否有变更
$status = git status --porcelain
if ($status) {
    git commit -m "init: scaffold repo structure + templates"
    Write-Host "提交变更..."
} else {
    Write-Host "没有新变更需要提交。"
}

# 推送（如果远程不存在则添加）
$remoteExists = git remote | Select-String -Pattern "origin" -Quiet
if (-not $remoteExists) {
    git remote add origin $REPO_URL
}

# 推送到远程
Write-Host "推送到 GitHub..."
git push -u origin main

Write-Host "✅ Done. 已创建并同步到 GitHub：$REPO_URL"

