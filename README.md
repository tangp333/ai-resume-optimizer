# 📄 AI 简历优化器

输入你的简历和目标岗位 JD，AI 帮你分析并生成优化建议。

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Gradio](https://img.shields.io/badge/Gradio-4.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ 功能特性

- 📝 **智能分析** — 自动分析简历与目标岗位的匹配度
- 💡 **优化建议** — 针对性地给出具体修改建议
- 📄 **优化简历** — 直接生成优化后的简历内容
- 📂 **文件上传** — 支持上传 Word (.docx) / PDF / TXT 文件
- 🌐 **网页界面** — 基于 Gradio，开箱即用
- 🔗 **分享链接** — 一键生成公开访问链接

## 🛠️ 技术栈

| 组件 | 技术 |
|------|------|
| 后端 | Python 3.10+ |
| 前端 | Gradio |
| AI 模型 | OpenAI API 兼容（DeepSeek / 硅基流动 / OpenAI） |
| 文件解析 | python-docx / PyPDF2 |

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

```bash
cp .env.example .env
```

编辑 `.env`：

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

浏览器会自动打开 `http://127.0.0.1:7860`，即可使用。

## 📖 使用方法

1. **输入简历**：在左侧输入框粘贴简历内容，或上传 Word / PDF 文件
2. **输入 JD**：在右侧输入框粘贴目标岗位的职位描述
3. **点击优化**：AI 会自动分析并生成优化建议

## 📁 项目结构

```
ai-resume-optimizer/
├── main.py              # 主程序
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
