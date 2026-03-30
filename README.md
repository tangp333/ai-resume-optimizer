# 📄 AI 简历优化器 v2.0

输入你的简历和目标岗位 JD，AI 帮你全方位分析并优化简历。

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Gradio](https://img.shields.io/badge/Gradio-4.0+-green)
![Version](https://img.shields.io/badge/Version-2.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ 五大功能

| 功能 | 说明 |
|------|------|
| 📊 **智能评分** | 综合评分 + 多维度分析（技能匹配、经验匹配、教育背景、表达质量） |
| 🔑 **ATS 关键词匹配** | 分析简历与 JD 的关键词覆盖率，找出缺失关键词 |
| 💡 **详细优化建议** | 简历优缺点分析 + 针对性修改建议 + 优化后简历内容 |
| ⚖️ **多岗位对比** | 一份简历对比 1-3 个岗位，分析最佳匹配 |
| 📥 **PDF 导出** | 一键导出完整的分析报告为 PDF 文件 |

## 🛠️ 技术栈

| 组件 | 技术 |
|------|------|
| 后端 | Python 3.10+ |
| 前端 | Gradio |
| AI 模型 | OpenAI API 兼容（DeepSeek / 硅基流动 / OpenAI） |
| 文件解析 | python-docx / PyPDF2 |
| PDF 导出 | fpdf2 |

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/tangp333/ai-resume-optimizer.git
cd ai-resume-optimizer
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制 `.env.example` 为 `.env`，填入你的 API Key：

```env
OPENAI_API_KEY=你的API密钥
OPENAI_BASE_URL=https://api.siliconflow.cn/v1
OPENAI_MODEL=Qwen/Qwen2.5-7B-Instruct
```

> 支持任何 OpenAI 兼容的 API 服务（DeepSeek、硅基流动、OpenAI 等）

### 4. 运行

```bash
python main.py
```

浏览器会自动打开 `http://127.0.0.1:7860`。

## 📖 使用方法

1. **输入简历** — 左侧输入框粘贴，或上传 Word / PDF 文件
2. **输入 JD** — 右侧输入目标岗位（最多3个）
3. **点击分析** — AI 自动完成评分、关键词分析、优化建议、多岗对比
4. **导出报告** — 一键下载 PDF 分析报告

## 📁 项目结构

```
ai-resume-optimizer/
├── main.py              # 主程序（五大功能）
├── requirements.txt     # 依赖列表
├── .env.example         # 环境变量模板
├── .env                 # 环境变量（不提交）
├── .gitignore           # Git 忽略文件
└── README.md            # 项目说明
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

MIT License
