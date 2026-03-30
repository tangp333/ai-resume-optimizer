from openai import OpenAI
from dotenv import load_dotenv
import os
import gradio as gr

# 加载环境变量
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)


def optimize_resume(resume: str, job_description: str) -> str:
    """把简历和岗位JD发给大模型，返回优化建议"""

    if not resume.strip():
        return "请先输入你的简历内容"
    if not job_description.strip():
        return "请先输入目标岗位的JD"

    prompt = f"""你是一位资深HR和简历优化专家。

请根据以下目标岗位的要求，分析这份简历，并给出：
1. 简历的优缺点分析
2. 针对这个岗位的具体修改建议
3. 优化后的简历内容

## 目标岗位JD：
{job_description}

## 当前简历：
{resume}

请用中文回答，格式清晰。"""

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "deepseek-chat"),
        messages=[
            {"role": "system", "content": "你是一位专业的简历优化顾问，擅长根据岗位要求优化简历内容。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content


# ========== 网页界面 ==========
demo = gr.Interface(
    fn=optimize_resume,
    inputs=[
        gr.Textbox(
            label="你的简历",
            placeholder="在这里粘贴你的简历内容...",
            lines=10,
        ),
        gr.Textbox(
            label="目标岗位JD",
            placeholder="在这里粘贴目标岗位的职位描述...",
            lines=8,
        ),
    ],
    outputs=gr.Textbox(
        label="优化建议",
        lines=20,
    ),
    title="AI 简历优化器",
    description="输入你的简历和目标岗位JD，AI帮你分析并优化简历内容。",
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch(share=True)
