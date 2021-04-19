# coding : utf-8

"""
Sentiment Analysis with Textblob
I just use Textblob to analyze the input text
"""

import gradio as gr
from textblob import TextBlob


def analyze(input_text):
	blob = TextBlob(input_text)
	polarity = blob.sentiment.polarity
	probas = round(0.5*polarity + 0.5, 3)

	return f"Polarity: {probas}"


gr.Interface(
    fn=analyze,
    inputs=gr.inputs.Textbox(lines=8, placeholder="Put your text here..."),
    outputs="text",
    title="Sentiment Analysis with Textblob",
    # description="Put your text in the Negative < 0.5 > Positive",
	server_name="0.0.0.0"
    ).launch()
