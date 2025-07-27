import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub

load_dotenv()

class PMAgent:
    def __init__(self):
        self.llm = self._initialize_llm()
        self.tools = self._initialize_tools()
        self.memory = self._initialize_memory()
        self.agent_executor = self._initialize_agent()

    def _initialize_llm(self):
        # Prioritize Groq for speed and reliability
        return ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"))

    def _initialize_tools(self):
        # Initialize basic tools for now
        tools = [
            TavilySearchResults(max_results=5)
        ]
        return tools

    def _initialize_memory(self):
        return ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    def _initialize_agent(self):
        # Use the default react-chat prompt from hub
        prompt = hub.pull("hwchase17/react-chat")

        agent = create_react_agent(self.llm, self.tools, prompt)
        return AgentExecutor(agent=agent, tools=self.tools, memory=self.memory, verbose=True, handle_parsing_errors=True)

    def run(self, user_input):
        return self.agent_executor.invoke({"input": user_input})

    def generate_product_brief(self, requirements):
        """Generate a product brief using the LLM directly"""
        prompt = f"""
        Based on the following requirements, create a comprehensive Product Brief:

        Requirements: {requirements}

        Please structure the Product Brief with the following sections:

        # PRODUCT BRIEF

        ## Product Name
        [Provide a clear, memorable product name]

        ## Product Description
        [2-3 sentence overview of what the product is and does]

        ## Target Audience
        [Define primary and secondary target audiences with demographics and psychographics]

        ## Key Features
        [List 5-7 core features that deliver the most value]

        ## Value Proposition
        [Clear statement of unique value and benefits]

        ## Success Metrics
        [Define how success will be measured - KPIs, metrics, goals]

        ## Competitive Advantage
        [What makes this product unique in the market]

        ## Technical Requirements (High-Level)
        [Brief overview of technical considerations]

        ## Timeline & Milestones
        [High-level development timeline with key milestones]

        Make sure the brief is comprehensive, actionable, and aligned with business objectives.
        """
        response = self.llm.invoke(prompt)
        return response.content

    def generate_brd(self, requirements):
        """Generate a BRD using the LLM directly"""
        prompt = f"""
        Based on the following requirements, create a detailed Business Requirements Document (BRD):

        Requirements: {requirements}

        Please structure the BRD with the following sections:

        # BUSINESS REQUIREMENTS DOCUMENT (BRD)

        ## 1. Executive Summary
        [Brief overview of the project and its business value]

        ## 2. Project Overview
        ### 2.1 Project Name
        ### 2.2 Project Description
        ### 2.3 Project Scope
        ### 2.4 Project Objectives

        ## 3. Business Objectives
        [Detailed business goals and expected outcomes]

        ## 4. Stakeholders
        ### 4.1 Primary Stakeholders
        ### 4.2 Secondary Stakeholders
        ### 4.3 Roles and Responsibilities

        ## 5. Functional Requirements
        ### 5.1 Core Features
        ### 5.2 User Stories
        ### 5.3 Use Cases

        ## 6. Non-Functional Requirements
        ### 6.1 Performance Requirements
        ### 6.2 Security Requirements
        ### 6.3 Scalability Requirements
        ### 6.4 Usability Requirements

        ## 7. Business Rules
        [Define business logic and constraints]

        ## 8. Data Requirements
        [Data sources, storage, and management needs]

        ## 9. Integration Requirements
        [External systems and APIs]

        ## 10. Assumptions and Dependencies
        [Key assumptions and external dependencies]

        ## 11. Risks and Mitigation
        [Identified risks and mitigation strategies]

        ## 12. Success Criteria
        [Measurable criteria for project success]

        ## 13. Timeline and Milestones
        [Detailed project timeline with deliverables]

        Ensure the BRD is detailed, technically sound, and provides clear guidance for development teams.
        """
        response = self.llm.invoke(prompt)
        return response.content

    def generate_market_research(self, product_info, market_data=""):
        """Generate market research using the LLM directly"""
        prompt = f"""
        Based on the following product information, create a comprehensive Market Research Report:

        Product Information: {product_info}
        Market Data: {market_data}

        Please structure the Market Research Report with the following sections:

        # MARKET RESEARCH REPORT

        ## 1. Executive Summary
        [Key findings and recommendations]

        ## 2. Market Overview
        ### 2.1 Market Size and Growth
        ### 2.2 Market Trends
        ### 2.3 Market Drivers

        ## 3. Target Market Analysis
        ### 3.1 Market Segmentation
        ### 3.2 Customer Demographics
        ### 3.3 Customer Needs and Pain Points

        ## 4. Competitive Analysis
        ### 4.1 Direct Competitors
        ### 4.2 Indirect Competitors
        ### 4.3 Competitive Positioning
        ### 4.4 SWOT Analysis

        ## 5. Market Opportunity
        ### 5.1 Market Gap Analysis
        ### 5.2 Opportunity Size
        ### 5.3 Entry Strategy

        ## 6. Customer Insights
        ### 6.1 Customer Behavior
        ### 6.2 Purchase Drivers
        ### 6.3 Customer Journey

        ## 7. Pricing Analysis
        ### 7.1 Competitive Pricing
        ### 7.2 Price Sensitivity
        ### 7.3 Pricing Strategy Recommendations

        ## 8. Market Entry Barriers
        [Challenges and obstacles to market entry]

        ## 9. Regulatory Environment
        [Relevant regulations and compliance requirements]

        ## 10. Technology Trends
        [Relevant technology trends affecting the market]

        ## 11. Recommendations
        ### 11.1 Go-to-Market Strategy
        ### 11.2 Product Positioning
        ### 11.3 Marketing Strategy

        ## 12. Conclusion
        [Summary of key insights and next steps]

        Ensure the report is data-driven, insightful, and provides actionable recommendations.
        """
        response = self.llm.invoke(prompt)
        return response.content



