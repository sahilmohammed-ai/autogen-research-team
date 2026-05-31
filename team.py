from autogen import ConversableAgent, GroupChat, GroupChatManager
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

llm_config = {
    "config_list": [
        {
            "model": "claude-sonnet-4-20250514",
            "api_key": api_key,
            "api_type": "anthropic"
        }
    ]
}

print("Config loaded successfully")

researcher = ConversableAgent(
    name="Researcher",
    system_message="""
    You are a researcher. 
    Your job is to gather information on a specified topic thoroughly and then present findings clearly with sources cited.
    Make sure that your output is structured well and accurate enough to be handed off to a fact checker agent.
    """,
    llm_config=llm_config,
    human_input_mode="NEVER"
)

fact_checker = ConversableAgent(
    name="Fact Checker",
    system_message="""
    You are a fact checker.
    Your job is to challenge the claims/information from the researcher and flag any unsupported statements.
    Make sure that your output contains both the researcher's claims and your insights with enough context to be handed off to an report generator agent.
    Structure:
    Researcher's Information - ...
    Fact Checker's Insights - ...
    """,
    llm_config=llm_config,
    human_input_mode="NEVER"
)

writer = ConversableAgent(
    name="Writer",
    system_message="""
    You are a writer.
    Your job is to generate a structured report on the researcher's claims while also taking into account the insights given from the fact checker.
    """,
    llm_config=llm_config,
    human_input_mode="NEVER"
)

editor = ConversableAgent(
    name="Editor",
    system_message="""
    You are a editor.
    Your job is the clean the researcher report draft. Review thoroughly for clarity, flow, and completeness.
    The output should be well structured and ready for publishing/viewing.
    """,
    llm_config=llm_config,
    human_input_mode="NEVER"
)

manager = ConversableAgent(
    name="Manager",
    system_message="""
    You are a research team manager.
    Your job is to coordinate and kick off the conversation within a team of research agents.
    Give the research topic to the researcher; hand off output to fact checker; then that output to writer; then that output to editor.
    The conversation should wrap up when the editor generates a clean report on the researcher topic.
    When the report is complete, end your message with: REPORT COMPLETE
    """,
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "REPORT COMPLETE" in msg.get("content", "")
)

group_chat = GroupChat(
    agents=[manager, researcher, fact_checker, writer, editor],
    messages=[],
    max_round=20
)

chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config
)

manager.initiate_chat(
    chat_manager,
    message="Research the viability of AI engineering as a career path in 2032 and produce a structured report."
)