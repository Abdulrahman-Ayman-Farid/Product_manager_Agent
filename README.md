# Product Manager Agent

A comprehensive Product Manager Agent built with Streamlit and LangChain that helps users gather requirements, generate product briefs, create Business Requirements Documents (BRDs), and conduct market research through a conversational interface.

## Features

- **Conversational Interface**: Chat-based interaction for natural requirement gathering
- **Product Brief Generation**: Automated creation of comprehensive product briefs
- **BRD Creation**: Detailed Business Requirements Document generation
- **Market Research**: Comprehensive market analysis and research reports
- **Document Export**: Download generated documents in text format
- **LangChain Integration**: Powered by advanced language models for intelligent responses
- **Groq LLM**: Fast and reliable language model for quick responses

## Architecture

The application consists of several key components:

- **Streamlit Frontend**: Interactive web interface with chat functionality
- **LangChain Agent**: Core AI agent for conversation management and tool orchestration
- **Document Generation**: Specialized methods for creating structured documents
- **API Integration**: Groq for LLM capabilities and Tavily for web search

## Installation

### Prerequisites

- Python 3.8 or higher
- Groq API key
- Tavily API key (for market research)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd product_manager_agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env file with your API keys
```

4. Run the application:
```bash
streamlit run streamlit_app.py
```

## Usage

### Getting Started

1. **Initialize the Agent**: 
   - Enter your Groq API key and Tavily API key in the sidebar
   - Click "Initialize Agent" to set up the system

2. **Start a Conversation**:
   - Use the chat interface to discuss your product ideas
   - The agent will ask strategic questions to gather requirements

3. **Generate Documents**:
   - Use the sidebar tasks to generate specific documents
   - Choose from Product Brief, BRD, or Market Research
   - Documents are automatically saved and available for download

### Available Tasks

- **Start Requirement Gathering**: Begin a structured conversation to collect product requirements
- **Generate Product Brief**: Create a comprehensive product brief based on conversation history
- **Generate BRD**: Generate a detailed Business Requirements Document
- **Perform Market Research**: Conduct market analysis and create research reports
- **General Chat**: Open conversation for any product management questions

### Document Types

#### Product Brief
Includes:
- Product name and description
- Target audience analysis
- Key features and functionality
- Value proposition
- Success metrics
- Competitive advantage
- Technical requirements
- Timeline and milestones

#### Business Requirements Document (BRD)
Comprehensive document covering:
- Executive summary
- Project overview and objectives
- Stakeholder analysis
- Functional and non-functional requirements
- Business rules and data requirements
- Integration requirements
- Risk assessment and mitigation
- Success criteria and timeline

#### Market Research Report
Detailed analysis including:
- Market overview and trends
- Target market analysis
- Competitive landscape
- Market opportunities
- Customer insights
- Pricing analysis
- Regulatory environment
- Strategic recommendations

## API Configuration

### Groq API Key
1. Sign up at [Groq Console](https://console.groq.com/)
2. Create a new API key
3. Add the key to your environment variables or enter it in the Streamlit interface

### Tavily API Key
1. Sign up at [Tavily](https://tavily.com/)
2. Get your API key from the dashboard
3. Add the key to your environment variables or enter it in the Streamlit interface

## Deployment

### Local Deployment
The application runs locally on port 8501 by default:
```bash
streamlit run streamlit_app.py
```

### Streamlit Community Cloud Deployment

1. **Prepare Repository**:
   - Ensure all files are committed to a GitHub repository
   - Include `requirements.txt` and `streamlit_app.py` in the root directory

2. **Deploy to Streamlit Cloud**:
   - Visit [Streamlit Community Cloud](https://streamlit.io/cloud)
   - Connect your GitHub account
   - Select your repository
   - Configure the app settings

3. **Environment Variables**:
   - In Streamlit Cloud, go to app settings
   - Add your API keys as secrets:
     - `GROQ_API_KEY`
     - `TAVILY_API_KEY`

4. **Access Your App**:
   - Your app will be available at a Streamlit-provided URL
   - Share the URL with users for access

## File Structure

```
product_manager_agent/
├── app/
│   ├── __init__.py
│   └── agent.py              # Core agent implementation
├── streamlit_app.py          # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── README.md                # This documentation
└── todo.md                  # Development progress tracking
```

## Dependencies

- `langchain`: Framework for LLM applications
- `streamlit`: Web application framework
- `python-dotenv`: Environment variable management
- `langchain-groq`: Groq integration for LangChain
- `langchain-community`: Community tools for LangChain
- `tavily-python`: Web search capabilities

## Troubleshooting

### Common Issues

1. **API Key Errors**:
   - Ensure API keys are correctly entered
   - Check that keys have sufficient credits/quota
   - Verify network connectivity

2. **Import Errors**:
   - Ensure all dependencies are installed
   - Check Python version compatibility

3. **Streamlit Issues**:
   - Clear browser cache
   - Restart the Streamlit server
   - Check for port conflicts

### Support

For issues and questions:
1. Check the troubleshooting section above
2. Review the API provider documentation
3. Ensure all dependencies are up to date

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://langchain.com/)
- LLM capabilities provided by [Groq](https://groq.com/)
- Web search powered by [Tavily](https://tavily.com/)

