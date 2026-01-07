import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,  # Function to call
    inputs=["text", "slider"],  # Input components
    outputs=["text"],  # Output components
    api_name="predict"  # API endpoint name
)

demo.launch() # Launch the interface
