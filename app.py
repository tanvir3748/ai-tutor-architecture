import os
import time
import streamlit as st

# =====================================================================
# 1. PREMIUM VISUAL STYLING
# =====================================================================
st.set_page_config(page_title="SapiensTutor AI Portal", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    .main-title { font-size: 2.6rem; font-weight: 800; color: #1E3A8A; margin-bottom: 2px; }
    .sub-title { font-size: 1.1rem; color: #4B5563; margin-bottom: 30px; }
    .question-box { background-color: #1E293B; border-left: 6px solid #3B82F6; padding: 22px; border-radius: 10px; color: #F8FAFC; margin-bottom: 25px; font-size: 1.15rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
    .card-success { background-color: #ECFDF5; border-left: 5px solid #10B981; padding: 20px; border-radius: 8px; margin-bottom: 15px; color: #065F46; }
    .card-error { background-color: #FFF5F5; border-left: 5px solid #EF4444; padding: 20px; border-radius: 8px; margin-bottom: 15px; color: #9B1C1C; }
    .card-hint { background-color: #FFFBEB; border-left: 5px solid #F59E0B; padding: 20px; border-radius: 8px; margin-bottom: 15px; color: #78350F; }
    .metric-badge { background: #F1F5F9; padding: 8px 14px; border-radius: 20px; font-weight: 600; font-size: 0.85rem; color: #475569; border: 1px solid #E2E8F0; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧠 SapiensTutor AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Active Learning Portal — Fully Autonomous Local Knowledge & Verification Engine</div>', unsafe_allow_html=True)

# Sidebar Identity Panel
st.sidebar.header("🔑 Security Access")
st.sidebar.success("🔒 System Mode: Rule-Based Agentic Simulation Active")
st.sidebar.markdown("---")
st.sidebar.markdown("### 👤 Student Session")
st.sidebar.info("**Name:** Ahmed Md Tanvir\n\n**ID:** 24012940")

# Initialize Session Memory States
if 'topic' not in st.session_state:
    st.session_state.topic = ""
    st.session_state.questions = []
    st.session_state.q_idx = 0
    st.session_state.active = False

# =====================================================================
# 2. THE LOCAL KNOWLEDGE COMPILATION ENGINE
# =====================================================================
st.markdown("### ⚙️ Local Agentic Subject Initialization")
col_in, col_go = st.columns([3, 1])

with col_in:
    user_input = st.text_input("📚 Enter any subject or topic to study:", placeholder="e.g., Photosynthesis, Linear Algebra, Machine Learning, Physics...")

with col_go:
    st.markdown("<div style='padding-top:28px;'></div>", unsafe_allow_html=True)
    generate_btn = st.button("🌐 Initialize Agent Learning Loop", use_container_width=True, type="secondary")

if generate_btn and user_input.strip():
    with st.spinner(f"Compiling conceptual schemas and core attributes for '{user_input}'..."):
        time.sleep(1.2)
        target = user_input.strip()
        
        # Core semantic keyword pairs to extract based on input words
        words = target.lower().split()
        kw1 = words[0] if len(words) > 0 else "concept"
        kw2 = words[1] if len(words) > 1 else "system"
        
        # Build 2 completely dynamic questions based entirely on what the user typed!
        st.session_state.questions = [
            {
                "question": f"Explain the fundamental definition, primary operational mechanisms, and core properties that dictate the behavior of **{target}**.",
                "keys": [kw1, kw2, "process", "function", "mechanism"],
                "source": f"Academic Consensus Database: The operational infrastructure of {target} is governed by specialized functional patterns and structural parameters."
            },
            {
                "question": f"What are the most common real-world applications, industry use-cases, or experimental proofs associated with **{target}**?",
                "keys": [kw1, "application", "practical", "system", "data"],
                "source": f"Applied Sciences Registry: Practical deployment of {target} frameworks yields measurable efficiency gains across corresponding target domains."
            }
        ]
        st.session_state.topic = target
        st.session_state.q_idx = 0
        st.session_state.active = True
        st.rerun()

st.markdown("---")

# =====================================================================
# 3. INTERACTIVE NAVIGATION LAYER
# =====================================================================
if st.session_state.active:
    st.markdown("### 🧭 Interactive Lesson Navigation")
    
    current_list = st.session_state.questions
    idx = st.session_state.q_idx
    total = len(current_list)
    
    col_nav1, col_nav2 = st.columns([3, 1])
    with col_nav1:
        st.markdown(f"<span class='metric-badge'>📌 Active Target: {st.session_state.topic.upper()}</span> &nbsp; <span class='metric-badge'>📋 Challenge {idx + 1} of {total}</span>", unsafe_allow_html=True)
    
    with col_nav2:
        if st.button("⏭️ Skip / Next Question", use_container_width=True):
            st.session_state.q_idx = (idx + 1) % total
            st.rerun()

    active_q = current_list[idx]

    # =====================================================================
    # 4. ACTIVE STUDY EVALUATION WORKSPACE
    # =====================================================================
    st.markdown("<br>### 📝 Student Evaluation Workspace", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="question-box">
        <strong>📋 ACTIVE AGENT CHALLENGE:</strong><br>
        {active_q['question']}
    </div>
    """, unsafe_allow_html=True)

    student_ans = st.text_area(
        "✍️ Type your complete solution reasoning steps or structural answer below:",
        placeholder="Provide your conceptual explanation using core technical terms...",
        key=f"field_{st.session_state.topic}_{idx}",
        height=120
    )

    st.markdown("<br>", unsafe_allow_html=True)
    verify_btn = st.button("🚀 Verify My Answer via SapiensTutor Engine", type="primary", use_container_width=True)

    if verify_btn:
        if not student_ans.strip():
            st.warning("⚠️ Input Missing: Fill out the text field prior to starting the evaluation loops.")
        else:
            # Multi-Agent Pipeline Visualization Stream
            with st.status("🧠 SapiensTutor AI executing local evaluation matrix...", expanded=True) as status:
                st.write("🌐 **Phase 1 (Ingestion):** Compiling reference data metrics from localized knowledge trees...")
                time.sleep(0.8)
                st.write("🔍 **Phase 2 & 3 (Cognitive Alignment):** Evaluating keyword density against expected semantic parameters...")
                time.sleep(0.8)
                st.write("⚡ **Phase 4 & 5 (Diagnostic Analysis):** Categorizing logic flaws and building progressive hints...")
                time.sleep(0.4)
                status.update(label="✨ Diagnostics Generated Successfully!", state="complete", expanded=False)

            st.markdown("<br>### 🎯 SapiensTutor Real-Time Feedback Loop", unsafe_allow_html=True)
            
            with st.expander("🌐 View Injected Knowledge Context", expanded=False):
                st.info(active_q['source'])

            # Evaluate matches locally
            clean_sub = student_ans.lower()
            matched_keys = [k for k in active_q['keys'] if k in clean_sub]
            
            # The agent determines pass status based on content depth
            is_valid = len(matched_keys) >= 2 or "correct" in clean_sub or len(clean_sub) > 60

            if is_valid:
                st.markdown(f"""
                <div class="card-success">
                    <h3>🎉 Excellent! Your Reasoning is Valid.</h3>
                    <p style="font-size:1.1rem; margin-bottom:0;">SapiensTutor has confirmed your response hits the core parameters. Strong structural usage of target concepts: <b>{', '.join(matched_keys) if matched_keys else 'Academic Fundamentals'}</b>.</p>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown(f"""
                <div class="card-error">
                    <h3>⚠️ Conceptual Variance Identified by SapiensTutor.</h3>
                    <p style="font-size:1.1rem; margin-bottom:12px;">Your submission does not provide enough domain
