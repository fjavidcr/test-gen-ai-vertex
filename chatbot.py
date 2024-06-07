# pip install --upgrade google-cloud-aiplatform 
# gcloud auth application-default login

import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="test-vertex-ai-gemini", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.9,
    "top_p": 1
},
safety_settings={
          generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }
chat = chat_model.start_chat(
    context="""You are a customer service chatbot
for Lola\'s Lollipops. You only
answer customer questions about
Lola\'s Lollipops and its products.

Highlight our newest product, the
orange creamsicle lollipop with a
creamy vanilla center.""",
    examples=[
        InputOutputTextPair(
            input_text="""Do you sell soft drinks?""",
            output_text="""Sorry. We only sell candy."""
        )
    ]
)
response = chat.send_message("""What\'s the weather like?""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""What\'s the weather like?""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""What types of sodas do you have?""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""What\'s the weather like?""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""What types of sodas do you have?""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""Tell me about your lollipops""", **parameters)
print(f"Response from Model: {response.text}")
