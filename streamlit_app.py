import streamlit as st
import os
from app.agent import PMAgent

# Page configuration
st.set_page_config(
    page_title="Product Manager Agent",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent" not in st.session_state:
    st.session_state.agent = None
if "documents" not in st.session_state:
    st.session_state.documents = {}

def extract_requirements_from_conversation():
    """Extract requirements from conversation history"""
    conversation_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
    return conversation_text

# Sidebar for configuration and tasks
with st.sidebar:
    st.title("🚀 Product Manager Agent")
    st.markdown("---")
    
    # API Key Configuration
    st.subheader("Configuration")
    groq_api_key = st.text_input("Groq API Key", type="password", value=os.getenv("GROQ_API_KEY", ""))
    tavily_api_key = st.text_input("Tavily API Key", type="password", value=os.getenv("TAVILY_API_KEY", ""))
    
    if st.button("Initialize Agent"):
        if groq_api_key and tavily_api_key:
            os.environ["GROQ_API_KEY"] = groq_api_key
            os.environ["TAVILY_API_KEY"] = tavily_api_key
            try:
                st.session_state.agent = PMAgent()
                st.success("Agent initialized successfully!")
            except Exception as e:
                st.error(f"Error initializing agent: {str(e)}")
        else:
            st.error("Please provide both API keys")
    
    st.markdown("---")
    
    # Task Selection
    st.subheader("Tasks")
    task_options = [
        "Start Requirement Gathering",
        "Generate Product Brief",
        "Generate BRD",
        "Perform Market Research",
        "General Chat"
    ]
    
    selected_task = st.selectbox("Select a task:", task_options)
    
    if st.button("Start Task"):
        if st.session_state.agent:
            if selected_task == "Generate Product Brief":
                requirements = extract_requirements_from_conversation()
                if requirements:
                    try:
                        brief = st.session_state.agent.generate_product_brief(requirements)
                        st.session_state.documents["Product Brief"] = brief
                        st.session_state.messages.append({"role": "assistant", "content": brief})
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error generating product brief: {str(e)}")
                else:
                    st.error("No conversation history found. Please discuss your product requirements first.")
            
            elif selected_task == "Generate BRD":
                requirements = extract_requirements_from_conversation()
                if requirements:
                    try:
                        brd = st.session_state.agent.generate_brd(requirements)
                        st.session_state.documents["BRD"] = brd
                        st.session_state.messages.append({"role": "assistant", "content": brd})
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error generating BRD: {str(e)}")
                else:
                    st.error("No conversation history found. Please discuss your product requirements first.")
            
            elif selected_task == "Perform Market Research":
                requirements = extract_requirements_from_conversation()
                if requirements:
                    try:
                        research = st.session_state.agent.generate_market_research(requirements)
                        st.session_state.documents["Market Research Report"] = research
                        st.session_state.messages.append({"role": "assistant", "content": research})
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error generating market research: {str(e)}")
                else:
                    st.error("No conversation history found. Please discuss your product requirements first.")
            
            else:
                # For other tasks, use the agent's conversational interface
                task_prompts = {
                    "Start Requirement Gathering": "I want to start gathering requirements for a new product. Please guide me through the process by asking relevant questions about the product idea, target audience, key features, and business objectives.",
                    "General Chat": "Hello! I'm ready to help you with product management tasks. What would you like to work on today?"
                }
                
                prompt = task_prompts.get(selected_task, "Hello! How can I help you today?")
                st.session_state.messages.append({"role": "user", "content": prompt})
                
                # Get agent response
                try:
                    response = st.session_state.agent.run(prompt)
                    st.session_state.messages.append({"role": "assistant", "content": response["output"]})
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.error("Please initialize the agent first")
    
    st.markdown("---")
    
    # Document Downloads
    st.subheader("Generated Documents")
    if st.session_state.documents:
        for doc_type, content in st.session_state.documents.items():
            st.download_button(
                label=f"Download {doc_type}",
                data=content,
                file_name=f"{doc_type.lower().replace(' ', '_')}.txt",
                mime="text/plain"
            )
    else:
        st.info("No documents generated yet")

# Main chat interface
st.title("💬 Product Manager Chat")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    if st.session_state.agent:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get agent response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.agent.run(prompt)
                    response_text = response["output"]
                    st.markdown(response_text)
                    
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                        
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    else:
        st.error("Please initialize the agent first using the sidebar")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and LangChain")

