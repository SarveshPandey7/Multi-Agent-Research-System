import streamlit as st
from pipeline import run_research_pipeline


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Research AI | Multi-Agent System",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0E1117;
}

/* Main container */
.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1150px;
}

/* Header */
.main-title {
    font-size: 38px;
    font-weight: 750;
    color: #F0F2F6;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    color: #9CA3AF;
    text-align: center;
    font-size: 15px;
    margin-bottom: 35px;
}

/* Section headings */
.section-title {
    font-size: 21px;
    font-weight: 650;
    color: #E5E7EB;
    margin-top: 20px;
    margin-bottom: 12px;
}

/* Cards */
.info-card {
    background-color: #171B24;
    border: 1px solid #292F3B;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 12px;
}

/* Agent status */
.agent-box {
    background-color: #171B24;
    border: 1px solid #292F3B;
    border-radius: 10px;
    padding: 14px;
    text-align: center;
    color: #D1D5DB;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 8px;
    height: 45px;
    font-weight: 600;
    background-color: #6366F1;
    color: white;
    border: none;
}

.stButton > button:hover {
    background-color: #4F46E5;
    color: white;
}

/* Input */
.stTextInput input {
    background-color: #171B24;
    border: 1px solid #343B49;
    border-radius: 8px;
    color: white;
}

/* Expanders */
.streamlit-expanderHeader {
    background-color: #171B24;
    border-radius: 8px;
}

/* Divider */
hr {
    border-color: #292F3B;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🔬 Research AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'An intelligent multi-agent research system powered by AI'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- HELPER FUNCTION ----------------

def extract_text(value):

    if hasattr(value, "content"):
        return value.content

    if isinstance(value, dict):
        return str(value)

    return str(value)


# ---------------- TOPIC INPUT ----------------

st.markdown('<div class="section-title">What do you want to research?</div>',
            unsafe_allow_html=True)

with st.form("research_form"):

    topic = st.text_input(
        "Research Topic",
        placeholder="e.g. Latest advancements in Generative AI...",
        label_visibility="collapsed"
    )

    submitted = st.form_submit_button("🚀 Generate Research")


# ---------------- PIPELINE EXECUTION ----------------

if submitted:

    if not topic.strip():

        st.warning("Please enter a research topic.")

    else:

        st.session_state.pop("research_data", None)

        progress_placeholder = st.empty()

        try:

            with st.spinner("AI agents are working on your research..."):

                progress_placeholder.info(
                    "🔍 Search Agent → 🌐 Reader Agent → ✍️ Writer Agent → 🧐 Critic Agent"
                )

                result = run_research_pipeline(topic.strip())

                st.session_state["research_data"] = result
                st.session_state["research_topic"] = topic.strip()

            progress_placeholder.empty()

            st.success("Research completed successfully!")

        except Exception as e:

            progress_placeholder.empty()

            st.error(f"Something went wrong: {str(e)}")


# ---------------- DISPLAY RESULTS ----------------

if "research_data" in st.session_state:

    data = st.session_state["research_data"]

    st.markdown("---")

    st.markdown(
        f"### 📚 Research Results: {st.session_state['research_topic']}"
    )

    # Agent workflow
    st.markdown("#### Agent Workflow")

    col1, col2, col3, col4 = st.columns(4)

    agents = [
        ("🔍", "Search Agent"),
        ("🌐", "Reader Agent"),
        ("✍️", "Writer Agent"),
        ("🧐", "Critic Agent")
    ]

    for col, (icon, name) in zip(
        [col1, col2, col3, col4], agents
    ):

        with col:

            st.markdown(
                f"""
                <div class="agent-box">
                    <div style="font-size:25px">{icon}</div>
                    <b>{name}</b>
                    <div style="color:#22C55E;font-size:12px">
                        ● Completed
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- SEARCH RESULTS ----------------

    with st.expander("🔍 Search Results", expanded=False):

        st.write(
            extract_text(data.get("search_result", "No search results found."))
        )

    # ---------------- SCRAPED CONTENT ----------------

    with st.expander("🌐 Scraped Content", expanded=False):

        st.write(
            extract_text(data.get("scrapped_result", "No scraped content found."))
        )

    # ---------------- FINAL REPORT ----------------

    st.markdown("### 📄 Final Research Report")

    report = extract_text(data.get("report", "No report generated."))

    st.markdown(
        """
        <div style="
            background-color:#171B24;
            border:1px solid #292F3B;
            border-radius:12px;
            padding:25px;
        ">
        """,
        unsafe_allow_html=True
    )

    st.markdown(report)

    st.markdown("</div>", unsafe_allow_html=True)

    st.download_button(
        label="⬇️ Download Research Report",
        data=report,
        file_name="research_report.txt",
        mime="text/plain"
    )

    # ---------------- CRITIC REVIEW ----------------

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("🧐 Critic Review", expanded=True):

        critic_report = extract_text(
            data.get("critic_report", "No critic review available.")
        )

        st.markdown(critic_report)

    st.markdown("---")

    st.caption(
        "Research AI | Multi-Agent Research System | Built with LangChain & Streamlit"
    )

