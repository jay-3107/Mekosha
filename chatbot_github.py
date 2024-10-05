import streamlit as st

# Define a function to process the conversation and then clear the input
def process_and_clear_text():
    # Get the user input
    user_input = st.session_state.get('user_input', '')

    if user_input:
        # Append user's message to conversation
        st.session_state['conversation'].append({"role": "user", "content": user_input})

        # Placeholder bot response for now
        bot_response = f"I am a bot, and you said: {user_input}"

        # Append bot's response to conversation
        st.session_state['conversation'].append({"role": "bot", "content": bot_response})

        # Clear the input text box by resetting the session state
        st.session_state['user_input'] = ''  # Reset input field

# Inject custom CSS for left/right alignment of messages and readable text colors
st.markdown("""
    <style>
    .user-message {
        background-color: #D3EE98;
        color: black;  /* Black text for user messages */
        padding: 8px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 60%;
        text-align: right;
        float: right;
        clear: both;
    }

    .bot-message {
        background-color: #72BF78;
        color: black;  /* Black text for bot messages */
        padding: 8px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 60%;
        text-align: left;
        float: left;
        clear: both;
    }

    .container {
        display: flex;
        flex-direction: column;
    }

    .icon {
        display: inline-block;
        vertical-align: middle;
        margin-right: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("Mekosha Law Project Chatbot")

# Store conversation history
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

# Input form for user message
user_input = st.text_input("Type your message here...", key="user_input")

# Button to send user message with callback to process conversation and clear input
st.button("Send", on_click=process_and_clear_text)

# Function to display chat bubbles with left/right alignment and icons
def display_chat():
    for message in st.session_state['conversation']:
        if message['role'] == 'user':
            st.markdown(f"""
                <div class="user-message">
                    <span class="icon">👤</span>{message['content']}  <!-- User icon -->
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="bot-message">
                    <span class="icon">🤖</span>{message['content']}  <!-- Bot icon -->
                </div>
            """, unsafe_allow_html=True)

# Display chat history after processing input
st.write("## Conversation")
display_chat()
