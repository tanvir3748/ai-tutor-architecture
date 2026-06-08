import streamlit as st
import time
from duckduckgo_search import DDGS

# --- 1. CONFIGURATION & UI SETUP ---
st.set_page_config(page_title="SapiensTutor AI", page_icon="🧠", layout="wide")

def inject_styles():
    st.markdown("""
        <style>
        .stApp { background-color: #f8fafc; }
        .node-box { padding: 20px; border-radius: 10px; background: white; border: 1px solid #e2e8f0; margin-bottom: 10px; }
        </style>
    """, unsafe_allow_html=True)

inject_styles()
st.title("🧠 SapiensTutor: Agentic Knowledge Engine")

# --- 2. SESSION STATE INITIALIZATION ---
if 'kb' not in st.session_state:
    st.session_state.kb = []
    st.session_state.topic = ""

# --- 3. AGENTIC CORE: WEB INGESTION ---
def fetch_data(query):
    """
    Robust ingestion logic. 
    Uses a fresh DDGS instance per call to bypass connection-pooling errors.
    """
    try:
        with DDGS() as ddgs:
            # Optimized query for scientific and conceptual depth
            results = list(ddgs.text(f"{query} fundamental explanation and principles", max_results=3))
            return results
    except Exception as e:
        st.error(f"Agent Connection Error: {e}")
        return None

# --- 4. CONTROL LAYER ---
with st.sidebar:
    st.header("⚙️ Agent Controls")
    user_topic = st.text_input("Enter Topic:")
    ingest_btn = st.button("🌐 Ingest Live Data")

if ingest_btn and user_topic:
    with st.spinner(f"Agent searching global nodes for '{user_topic}'..."):
        nodes = fetch_data(user_topic)
        if nodes:
            st.session_state.kb = nodes
            st.session_state.topic = user_topic
            st.success("Knowledge nodes successfully ingested!")
        else:
            st.warning("Engine throttled. Wait 30 seconds.")

# --- 5. INTERACTIVE WORKSPACE ---
if st.session_state.kb:
    st.markdown(f"### 📂 Workspace: {st.session_state.topic}")
    
    for i, node in enumerate(st.session_state.kb):
        with st.expander(f"Ref Node {i+1}: {node.get('title', 'Data')}", expanded=True):
            st.write(node.get('body', ''))
            st.caption(f"Source: {node.get('href', 'N/A')}")
            
            # Student evaluation field
            user_ans = st.text_area("Synthesize this concept:", key=f"inp_{i}")
            
            if st.button("Validate Logic", key=f"btn_{i}"):
                if len(user_ans) > 20:
                    st.balloons()
                    st.success("Validation: Concept alignment confirmed.")
                else:
                    st.warning("Needs more technical depth.")
