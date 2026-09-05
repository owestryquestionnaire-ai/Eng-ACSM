import streamlit as st

# ---------- 1. Initialization & Config ----------
st.set_page_config(page_title="Risk Stratification of Cardiopulmonary Fitness Training", layout="wide")


def inject_custom_css():
    st.markdown(
        """
        <style>
        /* =========================================================
           🖥️ DESKTOP & iPAD VIEW (Senior Friendly & Refined Typography)
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

        /* Headers - BOLD */
        h1 { font-size: 30px !important; font-weight: bold !important; line-height: 1.45 !important; margin-bottom: 12px !important;}
        h2 { font-size: 28px !important; font-weight: bold !important; border-bottom: 2px solid var(--text-color); padding-bottom: 8px !important; line-height: 1.45 !important; margin-top: 12px !important; margin-bottom: 15px !important;}
        h3 { font-size: 26px !important; font-weight: bold !important; line-height: 1.45 !important; margin-bottom: 12px !important;}
        h4 { font-size: 24px !important; font-weight: bold !important; line-height: 1.45 !important; margin-bottom: 12px !important; opacity: 0.8;}

        /* Radio Buttons & Checkbox Labels */
        div[data-testid="stRadio"] label p, div[data-testid="stCheckbox"] label p {
            font-size: 26px !important; 
            font-weight: 400 !important; 
            line-height: 1.45 !important; 
        }
        .stRadio > div { gap: 0rem !important; } 
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

        /* Combined Result Box Styling */
        .final-result-box { border: 3px solid var(--text-color); border-radius: 10px; overflow: hidden; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 15px !important; }
        .final-thr-part { font-size: 36px !important; font-weight: bold !important; line-height: 1.45 !important; padding: 15px 20px !important; background-color: var(--background-color); }
        .final-rec-part { background-color: var(--secondary-background-color); padding: 15px 20px !important; border-top: 3px dashed var(--text-color); }
        .final-rec-part p { margin-bottom: 6px !important; line-height: 1.45 !important; }

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

        /* --- Top Status Box (Desktop/iPad Default) --- */
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

            .final-thr-part { font-size: 28px !important; padding: 12px 15px !important; }
            .final-rec-part { padding: 12px 15px !important; }

            /* Mobile exclusive: auto-shrink top status box */
            .risk-strat-box {
                padding: 8px !important;
            }
            .risk-strat-text {
                font-size: 20px !important;
            }
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

    if "force_show_all" not in st.session_state:
        st.session_state["force_show_all"] = False
    if "current_tab" not in st.session_state:
        st.session_state["current_tab"] = "1. Form B (Major signs or symptoms)"
    if "show_b_errors" not in st.session_state:
        st.session_state["show_b_errors"] = False
    if "show_a_errors" not in st.session_state:
        st.session_state["show_a_errors"] = False


def update_val(key):
    st.session_state.data[key] = st.session_state[key]


init_session_states()

# ---------- 2. Logic Functions ----------
b_key_names = {
    "s_1": "Symptom 1 (Pain/discomfort in chest etc.)", "s_2": "Symptom 2 (Shortness of breath)",
    "s_3": "Symptom 3 (Dizziness/syncope)",
    "s_4": "Symptom 4 (Orthopnea)", "s_5": "Symptom 5 (Ankle edema)", "s_6": "Symptom 6 (Palpitations)",
    "s_7": "Symptom 7 (Intermittent claudication)", "s_8": "Symptom 8 (Known heart murmur)",
    "s_9": "Symptom 9 (Unusual fatigue)",
    "d_cardio": "Known CV disease", "d_metabolic": "Known metabolic disease", "d_renal": "Known renal disease",
    "is_active": "Participates in Regular Exercise"
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
    if rhr >= mhr: return None, "Abnormal Resting Heart Rate (>= Maximum HR)"
    hrr = mhr - rhr

    details_html = f'<div style="font-size: 20px; font-weight: normal; margin-top: 5px; opacity: 0.8;">Maximum HR: {mhr} | Standing HR at rest: {rhr} | HR Reserve: {hrr}</div>'

    if risk_level == "Class III":
        limit = int((hrr * 0.40) + rhr)
        thr_main = f"Training HR: &lt; {limit} bpm"
        return thr_main + details_html, None
    elif risk_level == "Class II":
        limit = int((hrr * 0.60) + rhr)
        thr_main = f"Training HR: &lt; {limit} bpm"
        return thr_main + details_html, None
    else:
        upper = int((hrr * 0.84) + rhr)
        thr_main = f"Training HR: ≤ {upper} bpm"
        return thr_main + details_html, None


# ---------- 3. Callbacks & Helpers ----------
def go_to_tab(tab_name):
    st.session_state["current_tab"] = tab_name
    st.session_state["show_b_errors"] = False
    st.session_state["show_a_errors"] = False


def enable_all_tabs_and_go():
    st.session_state["force_show_all"] = True
    go_to_tab("2. Form A (PAR-Q)")


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

    col1, col2 = st.columns([7, 3])
    with col1:
        if is_missing:
            # Keep red styling for errors
            st.markdown(
                f'<div class="question-text" style="color: #c62828 !important; font-weight: bold; background-color: #ffebee !important; border-left: 5px solid #c62828; padding-left: 10px;">{label}</div>',
                unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="question-text">{label}</div>', unsafe_allow_html=True)
    with col2:
        saved_val = st.session_state.data.get(key)
        idx = options.index(saved_val) if saved_val in options else None
        st.radio("", options, key=key, index=idx, horizontal=True, label_visibility="collapsed", on_change=update_val,
                 args=(key,))


# ---------- 4. Tab Functions ----------
def tab_b_acsm(b_class, show_all_tabs):
    check_err = st.session_state.get("show_b_errors", False)

    st.header("Form B: Major signs or symptoms")
    st.write("Please tick Yes or No as appropriate:")

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

    st.info(
        "*Note: Patients with the above symptoms may not be fit to perform moderate to vigorous intensity cardiopulmonary fitness training. For details, please refer to your doctor or physiotherapist")

    st.markdown("---")
    st.subheader("Known Diseases")
    render_inline_question("Known Cardiovascular (CV) Disease", "d_cardio", check_error=check_err)
    render_inline_question("Known Metabolic Disease", "d_metabolic", check_error=check_err)
    render_inline_question("Known Renal Disease", "d_renal", check_error=check_err)

    st.markdown("---")
    st.subheader("Current Exercise Habits")
    activity_question = "Participates in Regular Exercise?<br><span style='font-size: 20px; opacity: 0.8;'>(participated in planned, structured physical activity for at least 30 mins at moderate intensity on at least 3 days per week for at least the last 3 months)</span>"

    render_inline_question(activity_question, "is_active", options=("No", "Yes"), check_error=check_err)

    st.markdown("---")

    if check_err:
        missing = get_missing_b()
        if missing:
            st.error(
                f"⚠️ There are still **{len(missing)}** unanswered questions. Please check the items highlighted in red above.")

    if b_class == "Pending":
        st.button("➡️ Save and proceed to next step", type="primary", use_container_width=True, on_click=try_complete_b,
                  args=("3. Target HR & Clinical Guidelines",))
    elif b_class in ["Class II", "Class III"]:
        if not show_all_tabs:
            st.warning(
                f"🚨 According to Form B, the risk stratification is **{b_class}**. Form A has been hidden automatically.")
            c1, c2 = st.columns(2)
            with c1:
                st.button("✅ Complete Risk Stratification (Please return to staff)", type="primary",
                          use_container_width=True, on_click=try_complete_b,
                          args=("3. Target HR & Clinical Guidelines",))
            with c2:
                st.button("📝 Show hidden form (Proceed to Form A)", use_container_width=True,
                          on_click=enable_all_tabs_and_go)
        else:
            st.warning(
                f"🚨 According to Form B, the risk stratification is **{b_class}**. You chose to continue filling out Form A.")
            st.button("➡️ Save and proceed to 'Form A (PAR-Q)'", type="primary", use_container_width=True,
                      on_click=try_complete_b, args=("2. Form A (PAR-Q)",))
    else:
        st.button("➡️ Save and proceed to 'Form A (PAR-Q)'", type="primary", use_container_width=True,
                  on_click=try_complete_b, args=("2. Form A (PAR-Q)",))


def tab_a_parq():
    check_err = st.session_state.get("show_a_errors", False)

    st.header("Form A: Physical Activity Readiness Questionnaire (PAR-Q)")
    st.write("Please tick Yes or No as appropriate:")

    render_inline_question("1. Has your doctor ever said that you have a heart condition or high blood pressure?",
                           "parq_1", check_error=check_err)
    render_inline_question(
        "2. Do you feel pain in your chest at rest, during your daily activities of living or when you do physical activity?",
        "parq_2", check_error=check_err)
    render_inline_question(
        "3. Do you lose your balance because of dizziness or have you ever lost consciousness in the last 12 months?",
        "parq_3", check_error=check_err)

    render_inline_question(
        "4. Have you ever been diagnosed with another medical chronic condition (other than heart disease or high blood pressure)?",
        "parq_4", check_error=check_err)
    if st.session_state.data.get("parq_4") == "Yes":
        st.text_input("Please list here:", value=st.session_state.data.get("parq_4_text", ""), key="parq_4_text",
                      on_change=update_val, args=("parq_4_text",))

    render_inline_question("5. Are you currently taking prescribed medications for a chronic medical condition?",
                           "parq_5", check_error=check_err)
    if st.session_state.data.get("parq_5") == "Yes":
        st.text_input("Please list here:", value=st.session_state.data.get("parq_5_text", ""), key="parq_5_text",
                      on_change=update_val, args=("parq_5_text",))

    render_inline_question(
        "6. Do you currently have (or have had within the past 12 months) a bone or joint, or soft tissue (muscle, ligament, or tendon) problem that could be made worse by becoming more physically active?",
        "parq_6", check_error=check_err)
    render_inline_question(
        "7. Has your doctor ever said that you should only do medically supervised physical activity?", "parq_7",
        check_error=check_err)

    st.markdown("---")

    if check_err:
        missing = get_missing_a()
        if missing:
            st.error(
                f"⚠️ There are still **{len(missing)}** unanswered questions. Please check the items highlighted in red above.")

    st.button("✅ Complete Risk Stratification (Please return to staff)", type="primary", use_container_width=True,
              on_click=try_complete_a, args=("3. Target HR & Clinical Guidelines",))


def tab_d_thr(current_class):
    st.header("Target Heart Rate & Clinical Recommendations")

    st.subheader("⚙️ Select Risk Class")

    if current_class == "Pending":
        st.markdown("💡 The system evaluation is currently **Incomplete**. Please manually select the Risk Class below:")
    else:
        st.markdown(f"💡 The system evaluates the patient as **{current_class}**. You can manually override this below:")

    options = ["Class I", "Class II", "Class III"]
    default_idx = options.index(current_class) if current_class in options else None
    selected_class = st.radio("Manual Override", options, index=default_idx, horizontal=True,
                              label_visibility="collapsed")

    result_container = st.container()

    st.markdown("---")
    st.subheader("🎯 Input Data")

    c1, c2 = st.columns(2)
    age = c1.number_input("Age", min_value=10, max_value=120, value=None, step=1, key="thr_age")
    rhr = c2.number_input("Standing Resting HR", min_value=30, max_value=220, value=None, step=1, key="thr_rhr")

    if st.button("Calculate", type="primary", use_container_width=True):
        if selected_class is None:
            result_container.warning("⚠️ Please select a Risk Class before calculating.")
        elif age is not None and rhr is not None:
            thr_string, err = calculate_thr(int(age), int(rhr), selected_class)

            if not err:
                recs = {
                    "Class I": {
                        "intensity": "Moderate: ✔️ Vigorous: ✔️",
                        "hrr": "≤ 84% HRR",
                        "rpe": "&lt; 17",
                        "medical": "Not necessary",
                        "supervision": "Not required",
                        "monitor": "Monitor HR in First session (optional)"
                    },
                    "Class II": {
                        "intensity": "Moderate: ✔️ Vigorous: ❌",
                        "hrr": "&lt; 60% HRR",
                        "rpe": "&lt; 14",
                        "medical": "Recommended for vigorous intensity exercise",
                        "supervision": "Not required: light to moderate intensity<br>Required: vigorous intensity",
                        "monitor": "Continuous HR or RPE monitoring"
                    },
                    "Class III": {
                        "intensity": "Moderate: ❌ Vigorous: ❌",
                        "hrr": "&lt; 40% HRR",
                        "rpe": "&lt; 12",
                        "medical": "Recommended",
                        "supervision": "Required",
                        "monitor": "Continuous HR and RPE monitoring together with close supervision"
                    }
                }
                rec = recs[selected_class]

                result_container.markdown(f"""
                <div class="final-result-box">
                    <div class="final-thr-part">
                        {thr_string}
                    </div>
                    <div class="final-rec-part">
                        <h3 style="margin-top: 0; border-bottom: 2px solid var(--text-color); padding-bottom: 10px;">📋 {selected_class} Clinical Guidelines</h3>
                        <p><b>Recommended Exercise Intensity:</b><br>{rec['intensity']}</p>
                        <p><b>Safe exercise zone:</b> {rec['hrr']}</p>
                        <p><b>RPE during Exercise:</b> {rec['rpe']}</p>
                        <p><b>Medical Clearance:</b><br>{rec['medical']}</p>
                        <p><b>Supervision:</b><br>{rec['supervision']}</p>
                        <p><b>Monitoring:</b><br>{rec['monitor']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                result_container.error(err)
        else:
            result_container.warning("⚠️ Please input valid Age and Standing Resting HR values before calculating.")
    else:
        result_container.info(
            "💡 Please input the patient's **Age** and **Standing Resting HR** above, then click 'Calculate' to generate the report.")


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

    st.title("🏃‍♂️ Risk Stratification of Cardiopulmonary Fitness Training")

    st.markdown(f"""
    <div class="risk-strat-box" style="background-color: {theme['bg']}; border: 2px solid {theme['border']};">
        <span class="risk-strat-text" style="color: {theme['text']};">Risk Stratification: {display_text}</span>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    show_all_tabs = st.session_state.get("force_show_all", False)
    should_hide_a = (b_class_only in ["Class II", "Class III"]) and not show_all_tabs

    if should_hide_a:
        available_tabs = ["1. Form B (Major signs or symptoms)", "3. Target HR & Clinical Guidelines"]
    else:
        available_tabs = ["1. Form B (Major signs or symptoms)", "2. Form A (PAR-Q)",
                          "3. Target HR & Clinical Guidelines"]

    if st.session_state["current_tab"] not in available_tabs:
        st.session_state["current_tab"] = available_tabs[0]

    cols = st.columns(len(available_tabs))
    for i, tab_name in enumerate(available_tabs):
        btn_type = "primary" if st.session_state["current_tab"] == tab_name else "secondary"
        if cols[i].button(tab_name, type=btn_type, key=f"nav_{i}", use_container_width=True):
            go_to_tab(tab_name)
            st.rerun()

    st.markdown("---")

    if st.session_state["current_tab"] == "1. Form B (Major signs or symptoms)":
        tab_b_acsm(b_class_only, show_all_tabs)
    elif st.session_state["current_tab"] == "2. Form A (PAR-Q)":
        tab_a_parq()
    elif st.session_state["current_tab"] == "3. Target HR & Clinical Guidelines":
        tab_d_thr(current_class)

    st.markdown("---")
    st.caption(
        "#Adjustment to target HR zone should be made on individual basis (keep increment of progress ≤ 5%HRR per week)")


if __name__ == "__main__":
    main()