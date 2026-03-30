# AI 简历优化器

输入你的简历和目标岗位JD，AI 帮你分析并优化简历内容。

## 功能

- 简历优缺点分析
- 针对目标岗位的修改建议
- 生成优化后的简历内容
- 网页界面，即开即用

## 技术栈

- Python
- OpenAI API（兼容 DeepSeek / 硅基流动等）
- Gradio（网页界面）

## 快速开始

```bash
# 1. 克隆项目
git clone https://github.com/你的用户名/ai-resume-optimizer.git
cd ai-resume-optimizer

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
# 复制 .env.example 为 .env，填入你的 API Key
cp .env.example .env

# 4. 运行
python main.py
```

## 环境变量

在 `.env` 文件中配置：

```
OPENAI_API_KEY=你的API密钥
OPENAI_BASE_URL=https://api.siliconflow.cn/v1
OPENAI_MODEL=Qwen/Qwen2.5-7B-Instruct
```

支持任何 OpenAI 兼容的 API 服务。

## 效果预览

输入简历和岗位JD后，AI 会输出：
1. 简历优缺点分析
2. 针对性修改建议
3. 优化后的简历内容

## License

MIT
