import streamlit as st

st.set_page_config(page_title="AI-Driven Agile Development", layout="wide")

# Header
st.title("AI-Driven Agile Development: Save Money, Build Smart")
st.subheader("A Breakthrough Method for Cost-Effective App Development")

# Introduction
st.markdown("""
Welcome to the future of app development! This method leverages AI agents to meticulously plan and build your application step-by-step, saving you tons of money by getting the initial project setup right. We'll guide you through each phase—keeping costs low and the process fun!
""")

# Sidebar for navigation
st.sidebar.title("Development Phases")
phases = [
    "1. Business Analyst (BA)",
    "2. Project Manager (PM)",
    "3. Architect",
    "4. Product Owner (PO)",
    "5. Scrum Master",
    "6. Developer Agent"
]
selected_phase = st.sidebar.radio("Navigate Phases", phases)

# Phase Content
def display_phase(phase_title, description, outputs):
    st.header(phase_title)
    st.write(description)
    st.subheader("Key Outputs")
    for output in outputs:
        st.markdown(f"- {output}")

if selected_phase == "1. Business Analyst (BA)":
    display_phase(
        "Phase 1: Business Analyst (BA)",
        """Start with a Business Analyst AI using advanced thinking modes from LLMs. Here, we refine your idea through back-and-forth dialogue—no coding yet! The BA elicits all necessary details to flesh out your concept, setting a solid foundation.""",
        [
            "Refined project idea",
            "Detailed requirements list",
            "Initial scope document"
        ]
    )

elif selected_phase == "2. Project Manager (PM)":
    display_phase(
        "Phase 2: Project Manager (PM)",
        """The PM AI takes the BA's distilled idea and conducts deep research using tools like OpenAI or Gemini. It analyzes similar applications, technologies, and styles, producing a Product Requirements Document (PRD) with a clear roadmap to your MVP.""",
        [
            "Product Requirements Document (PRD)",
            "Market and tech analysis report",
            "Clarified project roadmap"
        ]
    )

elif selected_phase == "3. Architect":
    display_phase(
        "Phase 3: Architect",
        """The Architect AI combines outputs from the BA and PM to create a comprehensive architecture document. It specifies languages, libraries, pages, transitions, security, infrastructure, deployment, and database schemas—everything needed for a technical roadmap.""",
        [
            "Detailed architecture document",
            "Technology stack recommendations",
            "Database schema and data models"
        ]
    )

elif selected_phase == "4. Product Owner (PO)":
    display_phase(
        "Phase 4: Product Owner (PO)",
        """The PO AI uses advanced thinking to craft a granular, sequenced task list based on the architect and PM outputs. This list is designed for junior developers to implement step-by-step, ensuring no details are missed.""",
        [
            "Granular task list",
            "Sequenced implementation plan",
            "Manual setup instructions (if needed)"
        ]
    )

elif selected_phase == "5. Scrum Master":
    display_phase(
        "Phase 5: Scrum Master",
        """The Scrum Master AI takes the PRD, architecture, and task list to create epics and stories. Epics group related tasks, while stories are detailed, standalone units of work with all context needed for an AI agent to execute.""",
        [
            "Epics and user stories",
            "Story-specific context (data models, file locations, etc.)",
            "Agile workflow artifacts"
        ]
    )

elif selected_phase == "6. Developer Agent":
    display_phase(
        "Phase 6: Developer Agent",
        """Finally, the Developer Agent picks up stories one-by-one in a new chat thread within a tool like Cursor. It builds, tests (aiming for 80-90% coverage), and pushes updates incrementally, ensuring stability as functionality grows.""",
        [
            "Implemented code per story",
            "Test suites with high coverage",
            "Continuous deployment updates"
        ]
    )

# Example Workflow Simulation
st.header("See It In Action")
if st.button("Simulate Workflow"):
    st.write("### Simulated Workflow Output")
    st.markdown("""
    1. **BA**: Refined idea - "A budget tracking app for freelancers"
    2. **PM**: PRD - "Web app with user auth, expense tracking, and reports; tech: Python, Flask, PostgreSQL"
    3. **Architect**: Architecture - "Flask backend, React frontend, PostgreSQL DB, AWS hosting"
    4. **PO**: Task List - "1. Setup AWS account, 2. Configure PostgreSQL, 3. Build login page..."
    5. **Scrum Master**: Story - "As a user, I want to log in securely, so I can access my dashboard"
    6. **Developer**: Code pushed - "Login endpoint tested and deployed"
    """)

# Footer
st.markdown("""
---
**Why This Works**: By front-loading planning with AI, you avoid costly pivots later. It’s affordable (most steps are outside expensive coding tools), fun, and accessible—even without deep industry experience. Start building your app today!
""")

# Run instructions
st.sidebar.markdown("""
To run this app:
1. Save as `app.py`
2. Install Streamlit: `pip install streamlit`
3. Run: `streamlit run app.py`
""")
