from openai import OpenAI
import streamlit as st

def app():
    """This function handles the chatbot page"""
    
    # Sidebar for API key input & Model Selection
    with st.sidebar:
        openai_api_key = st.text_input("🔑 OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

        st.subheader("⚙️ Chatbot Settings")
        model_choice = st.radio("Choose AI Model:", ["GPT-3.5", "GPT-4"])
        model = "gpt-4" if model_choice == "GPT-4" else "gpt-3.5-turbo"

    # Display the chatbot page content only when the API key is provided
    if openai_api_key:
        # Streamlit UI setup
        st.title("💙 Health Chatbot")
        st.caption("❤️ My Health Consultant - Ask me anything about heart health!")

        # Define the system message to establish chatbot's role (INVISIBLE to user)
        system_message = {
            "role": "system",
            "content": (
                "You are an experienced Medical Professional specializing in Cardiology. "
                "Your responses must be clear, informative, and patient-friendly, always prioritizing medical accuracy. "
                "If a user asks about heart attack symptoms, explain them in detail and when they should seek medical attention. "
                "If they ask about treatments, provide general knowledge but always advise consulting a doctor for specific cases. "
                "Do NOT redirect users to mental health support unless they explicitly mention mental health concerns."
            )
        }

        # Initialize session state for chat history (ensuring system message is stored but NOT displayed)
        if "messages" not in st.session_state:
            st.session_state["messages"] = [system_message]  # Store system message for AI context

        # Function to handle AI responses
        def get_ai_response():
            """Calls OpenAI API and updates chat history with assistant response."""
            client = OpenAI(api_key=openai_api_key)

            with st.spinner("🤖 Thinking..."):
                response = client.chat.completions.create(
                    model=model,  # User-selected model (GPT-3.5 or GPT-4)
                    messages=st.session_state.messages,  # System message included for context
                )

            bot_message = response.choices[0].message.content  # Extract response

            # Append assistant's response to session history
            st.session_state.messages.append({"role": "assistant", "content": bot_message})
            st.chat_message("assistant", avatar="🩺").write(bot_message)

        # Display quick suggested questions & trigger response
        st.write("💡 **Quick Questions:** Click below to ask")
        col1, col2 = st.columns(2)

        if col1.button("Early Heart Attack Signs"):
            st.session_state.messages.append({"role": "user", "content": "What are the early signs of a heart attack?"})
            st.chat_message("user", avatar="👤").write("What are the early signs of a heart attack?")
            get_ai_response()

        if col2.button("💓 How High BP Affects Heart"):
            st.session_state.messages.append({"role": "user", "content": "How does high blood pressure affect heart health?"})
            st.chat_message("user", avatar="👤").write("How does high blood pressure affect heart health?")
            get_ai_response()

        # Display chat history (skip system message)
        avatars = {
            "user": "👤",
            "assistant": "🩺"
        }

        for msg in st.session_state.messages[1:]:  # Skip system message in display
            st.chat_message(msg["role"], avatar=avatars[msg["role"]]).write(msg["content"])

        # User input handling
        if prompt := st.chat_input("Ask me about heart health, symptoms, treatments, or prevention..."):
            if not openai_api_key:
                st.info("🚨 Please enter your OpenAI API key to continue.")
                st.stop()

            # Append user message to session history
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user", avatar="👤").write(prompt)

            get_ai_response()  # Trigger AI response

    else:
        # Prompt the user to input the API key
        st.info("Please provide your OpenAI API key to access the chatbot.")





# # #python3 -m venv - creates environment
# # #source ./venv/bin/activate - activates environment
# # # streamlit run Chatbot.py

# from openai import OpenAI
# import streamlit as st

# # Sidebar for API key input & Model Selection
# with st.sidebar:
#     openai_api_key = st.text_input("🔑 OpenAI API Key", key="chatbot_api_key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

#     st.subheader("⚙️ Chatbot Settings")
#     model_choice = st.radio("Choose AI Model:", ["GPT-3.5", "GPT-4"])
#     model = "gpt-4" if model_choice == "GPT-4" else "gpt-3.5-turbo"

# # Streamlit UI setup
# st.title("💙 Health Chatbot")
# st.caption("❤️ Your Cardiology Assistant - Ask me anything about heart health!")

# # Define the system message to establish chatbot's role (INVISIBLE to user)
# system_message = {
#     "role": "system",
#     "content": (
#         "You are an experienced Medical Professional specializing in Cardiology. "
#         "Your responses must be clear, informative, and patient-friendly, always prioritizing medical accuracy. "
#         "If a user asks about heart attack symptoms, explain them in detail and when they should seek medical attention. "
#         "If they ask about treatments, provide general knowledge but always advise consulting a doctor for specific cases. "
#         "Do NOT redirect users to mental health support unless they explicitly mention mental health concerns."
#     )
# }

# # Initialize session state for chat history (ensuring system message is stored but NOT displayed)
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [system_message]  # Store system message for AI context

# # Display quick suggested questions
# st.write("💡 **Quick Questions:** Click below to ask")
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("🩺 Early Heart Attack Signs"):
#         st.session_state.messages.append({"role": "user", "content": "What are the early signs of a heart attack?"})
# with col2:
#     if st.button("💓 How High BP Affects Heart"):
#         st.session_state.messages.append({"role": "user", "content": "How does high blood pressure affect heart health?"})

# # Display chat history (skip system message)
# avatars = {
#     "user": "👤",
#     "assistant": "🩺"
# }

# for msg in st.session_state.messages[1:]:  # Skip system message in display
#     st.chat_message(msg["role"], avatar=avatars[msg["role"]]).write(msg["content"])

# # User input handling
# if prompt := st.chat_input("Ask me about heart health, symptoms, treatments, or prevention..."):
#     if not openai_api_key:
#         st.info("🚨 Please enter your OpenAI API key to continue.")
#         st.stop()

#     # Append user message to session history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user", avatar="👤").write(prompt)

#     try:
#         # OpenAI API call with history (including system message but NOT displayed)
#         client = OpenAI(api_key=openai_api_key)
        
#         with st.spinner("🤖 Thinking..."):
#             response = client.chat.completions.create(
#                 model=model,  # User-selected model (GPT-3.5 or GPT-4)
#                 messages=st.session_state.messages,  # System message included for context
#             )

#         bot_message = response.choices[0].message.content  # Extract response

#         # Append assistant's response to session history
#         st.session_state.messages.append({"role": "assistant", "content": bot_message})
#         st.chat_message("assistant", avatar="🩺").write(bot_message)

#     except Exception as e:
#         st.error(f"❌ Error occurred: {e}")

