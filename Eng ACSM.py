import streamlit as st

# ---------- 1. Initialization & Config ----------
st.set_page_config(page_title="Class stratification for cardiopulmonary fitness training", layout="wide", initial_sidebar_state="collapsed")

def inject_custom_css():
    st.markdown(
        """
        <style>
        /* =========================================================
           🖥️ WHITE BACKGROUND OVERRIDE
           ========================================================= */
        /* Forces the main app container and sidebar to be pure white */
        [data-testid="stAppViewContainer"], .stApp, [data-testid="stSidebar"] {
            background-color: #ffffff !important;
        }

        /* =========================================================
           🖥️ HEADER & SPACING FIX
           ========================================================= */
        /* Increased padding-top to 3.5rem to clear the header without hiding the title */
        .block-container {
            padding-top: 3.5rem !important; 
            padding-bottom: 1.5rem !important;
        }
        
        /* Make the native Streamlit menu button highly visible but let the header auto-hide normally */
        [data-testid="collapsedControl"] {
            background-color: #2c3e50 !important;
            border-radius: 8px !important;
            padding: 5px !important;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2) !important;
        }
        [data-testid="collapsedControl"] svg {
            fill: #ffffff !important;
            width: 30px !important;
            height: 30px !important;
        }

        /* =========================================================
           🖥️ DESKTOP & iPAD VIEW (Elderly Friendly + Clean UI)
           ========================================================= */
        html, body, [data-testid="stMarkdownContainer"] {
            font-size: 24px !important; 
            font-weight: 400 !important;
            line-height: 1.45 !important; 
        }

        /* --- SAFE SPACING --- */
        div[data-testid="stVerticalBlock"] { gap: 0.6rem !important; }
        .element-container { margin-bottom: 0px !important; }
        hr { margin-top: 0.6rem !important; margin-bottom: 0.6rem !important; padding: 0px !important; }

        /* Headers - BOLD (Removed top margin to keep it tight under the header) */
        h1 { font-size: 30px !important; font-weight: bold !important; line-height: 1.45 !important; margin-top: 0px !important; padding-top: 0px !important; margin-bottom: 12px !important;}
        h2 { font-size: 28px !important; font-weight: bold !important; border-bottom: 2px solid var(--text-color); padding-bottom: 8px !important; line-height: 1.45 !important; margin-top: 12px !important; margin-bottom: 15px !important;}
        h3 { font-size: 26px !important; font-weight: bold !important; line-height: 1.45 !important; margin-bottom: 12px !important;}
        h4 { font-size: 24px !important; font-weight: bold !important; line-height: 1.45 !important; margin-bottom: 12px !important; opacity: 0.8;}

        /* Radio Buttons & Checkbox Labels */
        div[data-testid="stRadio"] label p, div[data-testid="stCheckbox"] label p {
            font-size: 26px !important; 
            font-weight: 400 !important; 
            line-height: 1.45 !important; 
        }
        
        /* Force single line for radio buttons */
        .stRadio > div { 
            gap: 0rem !important; 
            flex-wrap: nowrap !important;
        } 
        
        .stCheckbox > div { margin-bottom: 0rem !important; }

        /* Standard Text */
        .stMarkdown p {
            font-size: 24px !important; 
            line-height: 1.45 !important; 
            margin-bottom: 12px !important; 
        }

        /* Input Box Labels */
        label[data-testid="stWidgetLabel"] p {
            font-size: 26px !important; 
            font-weight: bold !important; 
            margin-bottom: 6px !important;
        }

        .question-text { margin-top: 0px !important; font-size: 26px !important; line-height: 1.45 !important; }

        /* ----- CUSTOM RED BUTTON STYLING ----- */
        button[kind="primary"], [data-testid="baseButton-primary"], button[kind="secondary"], [data-testid="baseButton-secondary"] {
            font-size: 24px !important; 
            padding: 10px 20px !important; 
            font-weight: bold !important; 
            line-height: 1.45 !important;
        }
        button[kind="primary"], [data-testid="baseButton-primary"] { background-color: #ef5350 !important; color: white !important; border-color: #ef5350 !important; }
        button[kind="primary"]:hover, [data-testid="baseButton-primary"]:hover { background-color: #e53935 !important; border-color: #e53935 !important; color: white !important;}

        /* =========================================================
           🖥️ SIDEBAR NAVIGATION PANEL
           ========================================================= */
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] div, [data-testid="stSidebar"] span {
            font-size: 18px !important; 
        }
        [data-testid="stSidebar"] h2 {
            font-size: 22px !important;
            margin-bottom: 10px !important;
        }
        [data-testid="stSidebar"] button[kind="primary"], 
        [data-testid="stSidebar"] [data-testid="baseButton-primary"], 
        [data-testid="stSidebar"] button[kind="secondary"], 
        [data-testid="stSidebar"] [data-testid="baseButton-secondary"] {
            font-size: 18px !important; 
            padding: 12px 12px !important; 
            font-weight: bold !important; 
            height: auto !important; 
            text-align: left !important;
        }
        
        [data-testid="stSidebar"] button div {
            justify-content: flex-start !important; 
            width: 100%;
        }
        [data-testid="stSidebar"] button p {
            white-space: pre-wrap !important; 
            text-align: left !important;
            line-height: 1.3 !important;
        }

        /* --- Status Banner --- */
        .risk-strat-box {
            border-radius: 8px; 
            padding: 12px; 
            text-align: center; 
            margin-bottom: 20px;
        }
        .risk-strat-text {
            font-size: 28px; 
            font-weight: bold;
        }

        /* =========================================================
           🎯 TARGET HR RESULT BOX & GUIDELINES TABLE
           ========================================================= */
        .thr-calc-banner {
            background-color: #f0f2f6 !important;
            padding: 15px 10px !important;
            border-radius: 8px 8px 0 0 !important;
            text-align: center !important;
            border: 1px solid #ddd !important;
            border-bottom: none !important;
            margin-bottom: 0px !important;
        }
        .thr-calc-banner h2 {
            color: #333333 !important;
            font-size: 42px !important;  
            font-weight: 900 !important;
            line-height: 1.1 !important;
            margin: 0 !important;
            padding: 0 !important;
            border-bottom: none !important;
            white-space: nowrap !important; /* FORCES TEXT ONTO ONE SINGLE LINE */
        }
        .thr-calc-banner p {
            color: #555555 !important;
            font-size: 14px !important; 
            line-height: 1.2 !important;
            margin: 0 !important;
            padding: 0 !important;
            padding-bottom: 5px !important;
        }
        .thr-calc-banner hr {
            border: 0 !important;
            border-top: 1px solid rgba(0,0,0,0.1) !important;
            margin: 10px auto !important;
            width: 95% !important;
        }

        /* Invisible Table to prevent Streamlit columns from breaking on mobile */
        .guidelines-table {
            width: 100% !important;
            border-collapse: collapse !important;
            border: none !important;
        }
        .guidelines-table tr { border: none !important; }
        .guidelines-table td {
            border: none !important;
            padding: 6px 0px !important;
            vertical-align: top !important;
            font-size: 24px !important;
            line-height: 1.45 !important;
            color: var(--text-color) !important;
        }
        .guidelines-label {
            width: 42% !important;
            font-weight: bold !important;
        }

        /* =========================================================
           📱 MOBILE RESPONSIVE PATCH
           ========================================================= */
        @media (max-width: 767px) {
            html, body, [data-testid="stMarkdownContainer"] { font-size: 20px !important; }
            h1 { font-size: 24px !important; }
            h2 { font-size: 22px !important; }
            h3 { font-size: 20px !important; }
            h4 { font-size: 18px !important; }
            
            .stMarkdown p { font-size: 20px !important; margin-bottom: 8px !important;}
            .question-text { font-size: 22px !important; margin-bottom: 8px !important; }
            
            [data-testid="column"] { margin-bottom: 12px !important; }
            .element-container { margin-bottom: 12px !important; }
            
            div[data-testid="stRadio"] label p, div[data-testid="stCheckbox"] label p {
                font-size: 22px !important; 
            }
            .stRadio > div { 
                gap: 1.5rem !important; 
                padding-bottom: 15px !important;
            } 
            
            button[kind="primary"], [data-testid="baseButton-primary"], button[kind="secondary"], [data-testid="baseButton-secondary"] {
                font-size: 22px !important;
                padding: 14px 12px !important; 
                white-space: normal !important; 
                height: auto !important;
            }

            .risk-strat-box { padding: 8px !important; }
            .risk-strat-text { font-size: 20px !important; }
            
            .thr-calc-banner h2 { 
                font-size: 26px !important; 
                white-space: nowrap !important;
            }
            .thr-calc-banner p { font-size: 10px !important; }

            .guidelines-table td { font-size: 18px !important; }
            .guidelines-label { width: 50% !important; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def init_session_states():
    if "data" not in st.session_state:
        st.session_state.data = {}
        for i in range(1, 10): st.session_state.data[f"s_{i}"] = None
        for k in ["d_cardio", "d_metabolic", "d_renal", "is_active"]: st.session_state.data[k] = None
        for i in range(1, 8): st.session_state.data[f"parq_{i}"] = None
        st.session_state.data["parq_4_text"] = ""
        st.session_state.data["parq_5_text"] = ""

    if "current_tab" not in st.session_state:
        st.session_state["current_tab"] = "1. Exercise Risk Assessment\n(Form B)"
    if "show_b_errors" not in st.session_state:
        st.session_state["show_b_errors"] = False
    if "show_a_errors" not in st.session_state:
        st.session_state["show_a_errors"] = False

def update_val(key):
    st.session_state.data[key] = st.session_state[key]

init_session_states()


# ---------- 2. Logic Functions ----------
b_key_names = {
    "s_1": "Pain/discomfort from ischemia", "s_2": "Shortness of breath", "s_3": "Dizziness or syncope",
    "s_4": "Orthopnea/paroxysmal nocturnal dyspnea", "s_5": "Ankle edema", "s_6": "Palpitations or tachycardia",
    "s_7": "Intermittent claudication", "s_8": "Known heart murmur", "s_9": "Unusual fatigue or shortness of breath",
    "d_cardio": "Known CV disease", "d_metabolic": "Known metabolic disease", "d_renal": "Known renal disease",
    "is_active": "Current Exercise Habits"
}

a_key_names = {
    f"parq_{i}": f"Question {i}" for i in range(1, 8)
}

def get_missing_b():
    missing = []
    for k, name in b_key_names.items():
        if st.session_state.data.get(k) is None:
            missing.append(name)
    return missing

def get_missing_a():
    missing = []
    for k, name in a_key_names.items():
        if st.session_state.data.get(k) is None:
            missing.append(name)
    return missing

def evaluate_b_only():
    missing_b = get_missing_b()
    if missing_b:
        return "Pending"

    symptoms = sum(1 for i in range(1, 10) if st.session_state.data.get(f"s_{i}") == "Yes")
    has_disease = any([
        st.session_state.data.get("d_cardio") == "Yes", 
        st.session_state.data.get("d_metabolic") == "Yes", 
        st.session_state.data.get("d_renal") == "Yes"
    ])
    is_active = st.session_state.data.get("is_active") == "Yes"
    
    if (has_disease and not is_active) or (symptoms >= 1):
        return "Class III"
    if has_disease and is_active and symptoms == 0:
        return "Class II"
        
    return "Pending Form A"

def calculate_current_class():
    b_class = evaluate_b_only()
    
    if b_class in ["Class III", "Class II", "Pending"]:
        return b_class
        
    missing_a = get_missing_a()
    if missing_a:
        return "Pending"

    parq_score = sum(1 for i in range(1, 8) if st.session_state.data.get(f"parq_{i}") == "Yes")
    
    symptoms = sum(1 for i in range(1, 10) if st.session_state.data.get(f"s_{i}") == "Yes")
    has_disease = any([
        st.session_state.data.get("d_cardio") == "Yes", 
        st.session_state.data.get("d_metabolic") == "Yes", 
        st.session_state.data.get("d_renal") == "Yes"
    ])

    if not has_disease and parq_score == 0 and symptoms == 0:
        return "Class I"
    elif parq_score > 0:
        return "Class II"
        
    return "Class I"

def calculate_thr(age, rhr, risk_level):
    mhr = 220 - age
    if rhr >= mhr: return None, None, "Abnormal Resting Heart Rate (>= Maximum HR)"
    hrr = mhr - rhr

    details_str = f"Maximum HR: {mhr} bpm &nbsp;|&nbsp; Standing HR at rest: {rhr} bpm &nbsp;|&nbsp; HR Reserve: {hrr} bpm"

    if risk_level == "Class III":
        limit = int((hrr * 0.40) + rhr)
        thr_main = f"Training HR: &lt; {limit} bpm"
        return thr_main, details_str, None
    elif risk_level == "Class II":
        limit = int((hrr * 0.60) + rhr)
        thr_main = f"Training HR: &lt; {limit} bpm"
        return thr_main, details_str, None
    else:
        upper = int((hrr * 0.84) + rhr)
        thr_main = f"Training HR: &le; {upper} bpm"
        return thr_main, details_str, None


# ---------- 3. Callbacks & Helpers ----------
def go_to_tab(tab_name):
    st.session_state["current_tab"] = tab_name
    st.session_state["show_b_errors"] = False
    st.session_state["show_a_errors"] = False

def try_complete_b(target_tab):
    missing = get_missing_b()
    if missing:
        st.session_state["show_b_errors"] = True
    else:
        st.session_state["show_b_errors"] = False
        go_to_tab(target_tab)

def try_complete_a(target_tab):
    missing = get_missing_a()
    if missing:
        st.session_state["show_a_errors"] = True
    else:
        st.session_state["show_a_errors"] = False
        go_to_tab(target_tab)

def render_inline_question(label, key, options=("No", "Yes"), check_error=False):
    is_missing = check_error and st.session_state.data.get(key) is None
    
    col1, col2 = st.columns([8.2, 1.8]) 
    with col1:
        if is_missing:
            st.markdown(f'<div class="question-text" style="color: #c62828 !important; font-weight: bold; background-color: #ffebee !important; border-left: 5px solid #c62828; padding-left: 10px;">{label}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="question-text">{label}</div>', unsafe_allow_html=True)
    with col2:
        saved_val = st.session_state.data.get(key)
        idx = options.index(saved_val) if saved_val in options else None
        st.radio("", options, key=key, index=idx, horizontal=True, label_visibility="collapsed", on_change=update_val, args=(key,))


# ---------- 4. Tab Functions ----------
def tab_b_acsm(b_class):
    check_err = st.session_state.get("show_b_errors", False)
    
    st.header("Form B: Major signs or symptoms")
    st.write("Please select \"Yes\" or \"No\":")
    
    s_items = [
        "1. Pain, discomfort (or other anginal equivalent) in the chest, neck, jaw, arms, or other areas that may result from ischemia",
        "2. Shortness of breath at rest or with mild exertion",
        "3. Dizziness or syncope",
        "4. Orthopnea or paroxysmal nocturnal dyspnea",
        "5. Ankle edema",
        "6. Palpitations or tachycardia",
        "7. Intermittent claudication",
        "8. Known heart murmur",
        "9. Unusual fatigue or shortness of breath with usual activities"
    ]
    for i, q in enumerate(s_items, 1):
        render_inline_question(q, f"s_{i}", check_error=check_err)
        if i == 1:
            st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        
    st.info("*Note: Patients with the above symptoms may not be fit to perform moderate to vigorous intensity cardiopulmonary fitness training. For details, please refer to your doctor or physiotherapist")
    
    st.markdown("---")
    st.subheader("Known Medical Conditions")
    render_inline_question("Known CV disease", "d_cardio", check_error=check_err)
    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    
    render_inline_question("Known metabolic disease", "d_metabolic", check_error=check_err)
    render_inline_question("Known renal disease", "d_renal", check_error=check_err)

    st.markdown("---")
    st.subheader("Current Exercise Habits")
    activity_question = "Do you currently engage in regular physical activity?<br><span style='font-size: 20px; opacity: 0.8;'>(participated in planned, structured physical activity for at least 30 mins at moderate intensity on at least 3 days per week for at least the last 3 months)</span>"
    render_inline_question(activity_question, "is_active", options=("No", "Yes"), check_error=check_err)

    st.markdown("---")
    
    if check_err:
        missing = get_missing_b()
        if missing:
            st.error(f"⚠️ There are still **{len(missing)}** unanswered questions. Please check the items marked in red above.")

    if b_class == "Pending":
        st.button("➡️ Save and Proceed to Next Step", type="primary", use_container_width=True, on_click=try_complete_b, args=("2. Physical Activity Readiness Questionnaire\n(Form A)",))
    elif b_class in ["Class II", "Class III"]:
        st.warning(f"🚨 Based on Form B, the risk category is **{b_class}**. Form A has been automatically skipped.")
        c1, c2 = st.columns(2)
        with c1:
            st.button("✅ Complete Risk Stratification (Proceed to Calculate Guidelines)", type="primary", use_container_width=True, on_click=try_complete_b, args=("3. Target HR &\nClinical Guidelines",))
        with c2:
            st.button("📝 Show Skipped Form (Go to Form A)", use_container_width=True, on_click=try_complete_b, args=("2. Physical Activity Readiness Questionnaire\n(Form A)",))
    else:
        st.button("➡️ Save and Proceed to \"Form A (PAR-Q)\"", type="primary", use_container_width=True, on_click=try_complete_b, args=("2. Physical Activity Readiness Questionnaire\n(Form A)",))


def tab_a_parq():
    check_err = st.session_state.get("show_a_errors", False)
    
    st.header("Form A: Physical Activity Readiness Questionnaire (PAR-Q)")
    st.write("Please select \"Yes\" or \"No\":")
    
    render_inline_question("1. Has your doctor ever said that you have a heart condition or high blood pressure?", "parq_1", check_error=check_err)
    render_inline_question("2. Do you feel pain in your chest at rest, during your daily activities of living or when you do physical activity?", "parq_2", check_error=check_err)
    render_inline_question("3. Do you lose your balance because of dizziness or have you ever lost consciousness in the last 12 months?", "parq_3", check_error=check_err)
    
    render_inline_question("4. Have you ever been diagnosed with another medical chronic condition (other than heart disease or high blood pressure)?", "parq_4", check_error=check_err)
    if st.session_state.data.get("parq_4") == "Yes":
        st.text_input("Please list here:", value=st.session_state.data.get("parq_4_text", ""), key="parq_4_text", on_change=update_val, args=("parq_4_text",))
        
    render_inline_question("5. Are you currently taking prescribed medications for a chronic medical condition?", "parq_5", check_error=check_err)
    if st.session_state.data.get("parq_5") == "Yes":
        st.text_input("Please list here:", value=st.session_state.data.get("parq_5_text", ""), key="parq_5_text", on_change=update_val, args=("parq_5_text",))
        
    render_inline_question("6. Do you currently have (or have had within the past 12 months) a bone or joint, or soft tissue (muscle, ligament, or tendon) problem that could be made worse by becoming more physically active?", "parq_6", check_error=check_err)
    render_inline_question("7. Has your doctor ever said that you should only do medically supervised physical activity?", "parq_7", check_error=check_err)

    st.markdown("---")
    
    if check_err:
        missing = get_missing_a()
        if missing:
            st.error(f"⚠️ There are still **{len(missing)}** unanswered questions. Please check the items marked in red above.")

    st.button("✅ Complete Risk Stratification (Proceed to Calculate Guidelines)", type="primary", use_container_width=True, on_click=try_complete_a, args=("3. Target HR &\nClinical Guidelines",))


def tab_d_thr(current_class):
    st.header("Target Heart Rate Calculator")
    
    st.markdown("<div style='font-size: 22px; font-weight: normal; margin-bottom: 8px;'>1. Select Risk Class</div>", unsafe_allow_html=True)
    
    if current_class == "Pending":
        st.markdown("💡 The system evaluation is currently **Incomplete**. Please manually select the Risk Class below:")
    else:
        st.markdown(f"💡 The system evaluates the patient as **{current_class}**. You can manually override this below:")
        
    options = ["Class I", "Class II", "Class III"]
    default_idx = options.index(current_class) if current_class in options else None
    selected_class = st.radio("Manual Override", options, index=default_idx, horizontal=True, label_visibility="collapsed")
    
    if current_class in ["Class I", "Class II", "Class III"]:
        reasons = []
        symptoms = sum(1 for i in range(1, 10) if st.session_state.data.get(f"s_{i}") == "Yes")
        has_disease = any([
            st.session_state.data.get("d_cardio") == "Yes", 
            st.session_state.data.get("d_metabolic") == "Yes", 
            st.session_state.data.get("d_renal") == "Yes"
        ])
        is_active = st.session_state.data.get("is_active") == "Yes"
        parq_score = sum(1 for i in range(1, 8) if st.session_state.data.get(f"parq_{i}") == "Yes")

        if current_class == "Class III":
            if symptoms >= 1:
                reasons.append("Form B ≥ 1")
            if has_disease and not is_active:
                reasons.append("Known CV, metabolic or renal disease without regular exercise")
        elif current_class == "Class II":
            if has_disease and is_active and symptoms == 0:
                reasons.append("Known CV, metabolic or renal disease with regular exercise & Form B = 0")
            if parq_score > 0:
                reasons.append("Form A (PAR-Q) ≥ 1")
        elif current_class == "Class I":
            reasons.append("No Known CV, metabolic or renal disease & Form A & Form B = 0")
            
        if reasons:
            if current_class == "Class III":
                reason_str = " AND ".join(reasons)
            elif current_class == "Class II":
                reason_str = " AND/OR ".join(reasons)
            else:
                reason_str = reasons[0]
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            if current_class == "Class I":
                st.success(f"✅ **Reason for {current_class}:** {reason_str}")
            elif current_class == "Class II":
                st.warning(f"⚠️ **Reason for {current_class}:** {reason_str}")
            elif current_class == "Class III":
                st.error(f"🚨 **Reason for {current_class}:** {reason_str}")

    st.markdown("---")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div style='font-size: 22px; font-weight: normal; margin-bottom: 5px;'>2. Patient Age</div>", unsafe_allow_html=True)
        age = st.number_input("Age", min_value=10, max_value=120, value=None, step=1, key="thr_age", label_visibility="collapsed")
    
    with c2:
        st.markdown("<div style='font-size: 22px; font-weight: normal; margin-bottom: 5px;'>3. Standing Resting Heart Rate (bpm)</div>", unsafe_allow_html=True)
        rhr = st.number_input("Standing Resting HR", min_value=30, max_value=220, value=None, step=1, key="thr_rhr", label_visibility="collapsed")

    result_container = st.container()

    if st.button("Calculate Guidelines", type="primary", use_container_width=True):
        if selected_class is None:
            result_container.warning("⚠️ Please select a Risk Class before calculating.")
        elif age is not None and rhr is not None:
            thr_main, thr_details, err = calculate_thr(int(age), int(rhr), selected_class)
            
            if not err:
                recs = {
                    "Class I": {
                        "intensity": "Moderate: ✔️ Vigorous: ✔️",
                        "hrr": "&lt;/= 84%HRR",
                        "rpe": "&lt;17",
                        "medical": "Not necessary",
                        "supervision": "Not required",
                        "monitor": "Monitor HR in First session (optional)"
                    },
                    "Class II": {
                        "intensity": "Moderate: ✔️ Vigorous: ❌",
                        "hrr": "&lt; 60 %HRR",
                        "rpe": "&lt; 14",
                        "medical": "Recommended for vigorous intensity exercise",
                        "supervision": "Not required: light to moderate intensity<br>Required: vigorous intensity",
                        "monitor": "Continuous HR <br>or <br>RPE monitoring"
                    },
                    "Class III": {
                        "intensity": "Moderate: ❌ Vigorous: ❌",
                        "hrr": "&lt; 40%HRR",
                        "rpe": "&lt;12",
                        "medical": "Recommended",
                        "supervision": "Required",
                        "monitor": "Continuous HR <br>and <br>RPE monitoring together with close supervision"
                    }
                }
                rec = recs[selected_class]
                
                with result_container:
                    st.markdown(f"""
                    <div class="thr-calc-banner">
                        <h2>{thr_main}</h2>
                        <hr>
                        <p>{thr_details}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    with st.container(border=True):
                        st.markdown(f"""
                        <div style="font-size: 26px !important; font-weight: bold !important; color: var(--text-color) !important; margin-bottom: 5px !important;">📋 {selected_class} Clinical Guidelines</div>
                        <hr style="margin: 0px 0px 15px 0px !important; border: 0; border-top: 2px solid #eee;" />
                        """, unsafe_allow_html=True)
                        
                        # INVISIBLE TABLE TO FIX MOBILE STACKING
                        guidelines_table = f"""
                        <table class="guidelines-table">
                            <tr>
                                <td class="guidelines-label">Recommended Intensity:</td>
                                <td>{rec['intensity']}</td>
                            </tr>
                            <tr>
                                <td class="guidelines-label">Safe exercise zone:</td>
                                <td>{rec['hrr']}</td>
                            </tr>
                            <tr>
                                <td class="guidelines-label">RPE during Exercise:</td>
                                <td>{rec['rpe']}</td>
                            </tr>
                            <tr>
                                <td class="guidelines-label">Medical clearance:</td>
                                <td>{rec['medical']}</td>
                            </tr>
                            <tr>
                                <td class="guidelines-label">Supervision:</td>
                                <td>{rec['supervision']}</td>
                            </tr>
                            <tr>
                                <td class="guidelines-label">Monitoring:</td>
                                <td>{rec['monitor']}</td>
                            </tr>
                        </table>
                        """
                        st.markdown(guidelines_table, unsafe_allow_html=True)
                        
            else:
                result_container.error(err)
        else:
            result_container.warning("⚠️ Please input valid Age and Standing Resting HR values before calculating.")


def main():
    inject_custom_css()
    
    current_class = calculate_current_class()
    b_class_only = evaluate_b_only()
    
    class_colors = {
        "Pending": {"bg": "#f8f9fa", "border": "#6c757d", "text": "#495057"},
        "Pending Form A": {"bg": "#f8f9fa", "border": "#6c757d", "text": "#495057"},
        "Class I": {"bg": "#e8f5e9", "border": "#2e7d32", "text": "#1b5e20"},
        "Class II": {"bg": "#fff3e0", "border": "#ef6c00", "text": "#e65100"},
        "Class III": {"bg": "#ffebee", "border": "#c62828", "text": "#b71c1c"}
    }
    
    theme = class_colors[current_class] if current_class in class_colors else class_colors["Pending"]
    display_text = "Incomplete" if "Pending" in current_class else current_class
    
    st.title("Class stratification for cardiopulmonary fitness training")
    
    st.markdown(f"""
    <div class="risk-strat-box" style="background-color: {theme['bg']}; border: 2px solid {theme['border']}; margin-bottom: 20px;">
        <span class="risk-strat-text" style="color: {theme['text']};">Risk Stratification: {display_text}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Form A is ALWAYS available in the navigation
    available_tabs = ["1. Exercise Risk Assessment\n(Form B)", "2. Physical Activity Readiness Questionnaire\n(Form A)", "3. Target HR &\nClinical Guidelines"]
        
    if st.session_state["current_tab"] not in available_tabs:
        st.session_state["current_tab"] = available_tabs[0]
        
    # --- Navigation Sidebar ---
    with st.sidebar:
        st.header("Form Selection")
        st.markdown("Please select a form below:")
        for i, tab_name in enumerate(available_tabs):
            btn_type = "primary" if st.session_state["current_tab"] == tab_name else "secondary"
            if st.button(tab_name, type=btn_type, key=f"nav_{i}", use_container_width=True):
                go_to_tab(tab_name)
                st.rerun()

    if st.session_state["current_tab"] == "1. Exercise Risk Assessment\n(Form B)":
        tab_b_acsm(b_class_only)
    elif st.session_state["current_tab"] == "2. Physical Activity Readiness Questionnaire\n(Form A)":
        tab_a_parq()
    elif st.session_state["current_tab"] == "3. Target HR &\nClinical Guidelines":
        tab_d_thr(current_class)
        
    st.markdown("---")
    st.caption("#Adjustment to target HR zone should be made on individual basis (keep increment of progress ≤ 5%HRR per week)")

if __name__ == "__main__":
    main()
