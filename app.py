import gradio as gr

from SCVD_Professional_GUI import CSS, demo


if __name__ == "__main__":
    demo.launch(
        theme=gr.themes.Base(primary_hue="blue", neutral_hue="slate"),
        css=CSS,
    )
