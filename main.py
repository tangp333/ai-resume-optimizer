from openai import OpenAI
from dotenv import load_dotenv
import os
import gradio as gr

# 文件解析
from docx import Document
from PyPDF2 import PdfReader

# 加载环境变量
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)


def read_file(file) -> str:
    """读取上传的文件内容（支持 txt/docx/pdf）"""
    if file is None:
        return ""

    filepath = file.name if hasattr(file, "name") else file
    ext = os.path.splitext(filepath)[1].lower()

    try:
        if ext == ".txt":
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        elif ext == ".docx":
            doc = Document(filepath)
            return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
        elif ext == ".pdf":
            reader = PdfReader(filepath)
            return "\n".join([page.extract_text() or "" for page in reader.pages])
        else:
            return f"不支持的文件格式：{ext}"
    except Exception as e:
        return f"读取文件失败：{str(e)}"


def optimize_resume(resume_text: str, resume_file, job_description: str) -> str:
    """把简历和岗位JD发给大模型，返回优化建议"""

    # 优先使用上传的文件，否则用文本框内容
    if resume_file is not None:
        resume = read_file(resume_file)
        if resume.startswith("不支持") or resume.startswith("读取文件失败"):
            return f"⚠️ {resume}"
    else:
        resume = resume_text

    if not resume.strip():
        return "⚠️ 请先输入或上传你的简历"
    if not job_description.strip():
        return "⚠️ 请先输入目标岗位的 JD"

    prompt = f"""你是一位资深HR和简历优化专家。

请根据以下目标岗位的要求，分析这份简历，并给出：

## 一、简历优缺点分析
从岗位匹配度、技能覆盖、经历描述等方面分析

## 二、针对性修改建议
给出具体的、可执行的修改建议

## 三、优化后的简历内容
直接给出修改后的完整简历

## 目标岗位JD：
{job_description}

## 当前简历：
{resume}

请用中文回答，使用 Markdown 格式，层次分明。"""

    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "deepseek-chat"),
            messages=[
                {"role": "system", "content": "你是一位专业的简历优化顾问，擅长根据岗位要求优化简历内容。请用结构清晰的格式回答，使用标题、列表等Markdown元素。回答要专业、具体、有针对性。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ 调用失败：{str(e)}"


# ========== 网页界面 ==========
with gr.Blocks(title="AI 简历优化器", theme=gr.themes.Soft()) as demo:

    gr.Markdown("# 📄 AI 简历优化器")
    gr.Markdown("输入简历和目标岗位 JD，AI 帮你分析并生成优化建议  |  支持上传 Word / PDF 文件")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📝 你的简历")
            with gr.Tab("手动输入"):
                resume_text = gr.Textbox(
                    placeholder="在这里粘贴你的简历内容...",
                    lines=12,
                    show_label=False,
                )
            with gr.Tab("上传文件"):
                resume_file = gr.File(
                    label="上传简历（支持 .txt / .docx / .pdf）",
                    file_types=[".txt", ".docx", ".pdf"],
                )

        with gr.Column(scale=1):
            gr.Markdown("### 🎯 目标岗位 JD")
            jd_input = gr.Textbox(
                placeholder="在这里粘贴目标岗位的职位描述...",
                lines=16,
                show_label=False,
            )

    submit_btn = gr.Button("🚀 开始优化", variant="primary", size="large")

    gr.Markdown("---")
    gr.Markdown("### 💡 优化建议")
    output = gr.Markdown(value="> 等待输入...")

    gr.Markdown(
        "<div style='text-align:center;color:#999;margin-top:16px;'>"
        "⭐ 觉得好用？欢迎到 <a href='https://github.com/tangp333/ai-resume-optimizer' target='_blank'>GitHub</a> 点个 Star"
        "</div>"
    )

    submit_btn.click(
        fn=optimize_resume,
        inputs=[resume_text, resume_file, jd_input],
        outputs=output,
    )

if __name__ == "__main__":
    demo.launch(share=True)
