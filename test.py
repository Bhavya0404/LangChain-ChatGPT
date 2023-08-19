import openai
from constants import openai_key as api_key
import streamlit as st

# Set your OpenAI API key here


# Initialize the OpenAI API client
openai.api_key = api_key
st.title("Convo")
def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="davinci",  # You can also use "curie" for a smaller model
        prompt=prompt,
        max_tokens=50  # Adjust the response length as needed
    )
    return response.choices[0].text.strip()
key = 1
print("Chat with the AI bot. Type 'exit' to end the conversation.")
user_input = st.text_input("You: ", key=key)
while True:
    key += 1
    if user_input.lower() == 'exit':
        break
    conversation_history = f"You: {user_input}\nBot:"
    bot_response = chat_with_bot(conversation_history)
    st.write(bot_response)
    # print(f"Bot: {bot_response}")
