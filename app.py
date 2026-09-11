import streamlit as st

st.set_page_config(page_title="Punjab CTI Merit Calculator", layout="centered")

st.title("Punjab CTI Induction Merit Calculator")
st.caption("Based on HED Punjab e-Portal Rules (Proportional Flat Calculation)")

st.divider()

# ---------------------------------------------------------
# 1. COLLEGE & DEGREE TRACK SELECTION
# ---------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
    college_type = st.selectbox(
        "Target College Category:",
        ["Associate College", "Graduate College"]
    )

with col2:
    degree_track = st.selectbox(
        "Base Degree Pathway (16-Year):",
        ["BS (4-Year)", "MA / MSc (2-Year)"]
    )

st.divider()

# ---------------------------------------------------------
# 2. BASIC ACADEMIC MARKS INPUT (Matric & Intermediate)
# ---------------------------------------------------------
st.subheader("1. Basic Academic Qualification")

c1, c2 = st.columns(2)
with c1:
    st.markdown("**Matriculation**")
    matric_obt = st.number_input("Matric Obtained Marks:", min_value=0.0, value=900.0, step=1.0)
    matric_tot = st.number_input("Matric Total Marks:", min_value=1.0, value=1100.0, step=1.0)
    matric_pct = (matric_obt / matric_tot) * 100
    st.caption(f"Calculated Percentage: **{matric_pct:.2f}%**")

with c2:
    st.markdown("**Intermediate**")
    inter_obt = st.number_input("Inter Obtained Marks:", min_value=0.0, value=900.0, step=1.0)
    inter_tot = st.number_input("Inter Total Marks:", min_value=1.0, value=1100.0, step=1.0)
    inter_pct = (inter_obt / inter_tot) * 100
    st.caption(f"Calculated Percentage: **{inter_pct:.2f}%**")

st.divider()

# ---------------------------------------------------------
# 3. BASE DEGREE MARKS INPUT (BS vs MA/MSc)
# ---------------------------------------------------------
st.subheader("2. Base Graduation Degree (16 Years)")

if degree_track == "BS (4-Year)":
    bs_grading_type = st.radio(
        "BS Grading System:",
        ["Marks System (Obtained/Total)", "CGPA System"]
    )
    
    if bs_grading_type == "Marks System (Obtained/Total)":
        bs_obt = st.number_input("BS Obtained Marks:", min_value=0.0, value=3200.0, step=1.0)
        bs_tot = st.number_input("BS Total Marks:", min_value=1.0, value=4000.0, step=1.0)
        bs_pct = (bs_obt / bs_tot) * 100
    else:
        has_bs_dmc_pct = st.radio(
            "Is Percentage explicitly mentioned on your BS DMC?",
            ["Yes", "No (Auto-convert CGPA via HEC Formula)"]
        )
        if has_bs_dmc_pct == "Yes":
            bs_pct = st.number_input("Enter exact Percentage as printed on DMC (%):", min_value=0.0, max_value=100.0, value=80.0)
        else:
            bs_cgpa = st.number_input("Enter Obtained CGPA:", min_value=0.0, max_value=4.0, value=3.4, step=0.01)
            bs_max_cgpa = st.number_input("Max CGPA:", min_value=1.0, max_value=4.0, value=4.0, step=0.1)
            bs_pct = (bs_cgpa / bs_max_cgpa) * 100
            st.info(f"Converted Percentage: **{bs_pct:.2f}%**")

else:
    # MA / MSc Track
    st.markdown("**BA / BSc (2-Year)**")
    ba_obt = st.number_input("BA/BSc Obtained Marks:", min_value=0.0, value=550.0, step=1.0)
    ba_tot = st.number_input("BA/BSc Total Marks:", min_value=1.0, value=800.0, step=1.0)
    ba_pct = (ba_obt / ba_tot) * 100
    
    st.markdown("**MA / MSc (2-Year)**")
    ma_obt = st.number_input("MA/MSc Obtained Marks:", min_value=0.0, value=850.0, step=1.0)
    ma_tot = st.number_input("MA/MSc Total Marks:", min_value=1.0, value=1200.0, step=1.0)
    ma_pct = (ma_obt / ma_tot) * 100

st.divider()

# ---------------------------------------------------------
# 4. HIGHER QUALIFICATIONS & INTERVIEW
# ---------------------------------------------------------
st.subheader("3. Higher Qualification & Performance")

higher_qual = st.selectbox(
    "Higher Qualification in Relevant Subject:",
    ["None", "M.Phil / MS", "Ph.D."]
)

mphil_pct = 0.0

if higher_qual == "M.Phil / MS":
    mphil_grading = st.radio(
        "M.Phil Grading System / DMC Status:",
        ["Percentage explicitly printed on DMC", "CGPA only (No Percentage on DMC)", "Marks System (Obtained/Total)"]
    )
    
    if mphil_grading == "Percentage explicitly printed on DMC":
        mphil_pct = st.number_input("Enter M.Phil Percentage printed on DMC (%):", min_value=0.0, max_value=100.0, value=82.0)
    elif mphil_grading == "CGPA only (No Percentage on DMC)":
        m_cgpa = st.number_input("Enter M.Phil CGPA:", min_value=0.0, max_value=4.0, value=3.5, step=0.01)
        mphil_pct = (m_cgpa / 4.0) * 100
        st.info(f"Converted M.Phil Percentage: **{mphil_pct:.2f}%**")
    else:
        m_obt = st.number_input("M.Phil Obtained Marks:", min_value=0.0, value=800.0, step=1.0)
        m_tot = st.number_input("M.Phil Total Marks:", min_value=1.0, value=1000.0, step=1.0)
        mphil_pct = (m_obt / m_tot) * 100

st.markdown("**Prior Performance & Interview**")
c3, c4 = st.columns(2)
with c3:
    prior_perf = st.number_input("Prior Performance Score (0 to 10):", min_value=0.0, max_value=10.0, value=0.0, step=0.5)
with c4:
    interview = st.number_input("Expected Interview Score (0 to 5):", min_value=0.0, max_value=5.0, value=3.5, step=0.5)

st.divider()

# ---------------------------------------------------------
# 5. CALCULATION LOGIC & OUTPUT
# ---------------------------------------------------------
if st.button("Calculate Final Merit Score", type="primary", use_container_width=True):
    
    # Associate College Logic
    if college_type == "Associate College":
        matric_score = (matric_pct / 100.0) * 15.0
        inter_score = (inter_pct / 100.0) * 15.0
        
        if degree_track == "BS (4-Year)":
            base_score = (bs_pct / 100.0) * 50.0
            acad_total = matric_score + inter_score + base_score
        else:
            ba_score = (ba_pct / 100.0) * 15.0
            ma_score = (ma_pct / 100.0) * 35.0
            acad_total = matric_score + inter_score + ba_score + ma_score

        # Flat points for higher qualification in Associate colleges
        if higher_qual == "Ph.D.":
            hq_score = 5.0
        elif higher_qual == "M.Phil / MS":
            hq_score = 3.0
        else:
            hq_score = 0.0

    # Graduate College Logic
    else:
        matric_score = (matric_pct / 100.0) * 15.0
        inter_score = (inter_pct / 100.0) * 15.0
        
        if degree_track == "BS (4-Year)":
            base_score = (bs_pct / 100.0) * 40.0
            acad_total = matric_score + inter_score + base_score
        else:
            ba_score = (ba_pct / 100.0) * 10.0
            ma_score = (ma_pct / 100.0) * 30.0
            acad_total = matric_score + inter_score + ba_score + ma_score

        # Proportional M.Phil points vs. Flat Ph.D. points in Graduate colleges
        if higher_qual == "Ph.D.":
            hq_score = 5.0
        elif higher_qual == "M.Phil / MS":
            hq_score = (mphil_pct / 100.0) * 10.0
        else:
            hq_score = 0.0

    total_merit = acad_total + hq_score + prior_perf + interview

    # Display Breakdown
    st.subheader("Merit Score Breakdown")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write(f"• **Matric Score:** {matric_score:.3f} / 15")
        st.write(f"• **Inter Score:** {inter_score:.3f} / 15")
        if degree_track == "BS (4-Year)":
            max_bs = 50.0 if college_type == "Associate College" else 40.0
            st.write(f"• **BS (4-Yr) Score:** {base_score:.3f} / {max_bs:.0f}")
        else:
            max_ba = 15.0 if college_type == "Associate College" else 10.0
            max_ma = 35.0 if college_type == "Associate College" else 30.0
            st.write(f"• **BA/BSc Score:** {ba_score:.3f} / {max_ba:.0f}")
            st.write(f"• **MA/MSc Score:** {ma_score:.3f} / {max_ma:.0f}")
            
    with col_b:
        st.write(f"• **Higher Qual. Score:** {hq_score:.3f} / 5.0 (or 10 for Graduate M.Phil)")
        st.write(f"• **Prior Performance:** {prior_perf:.3f} / 10")
        st.write(f"• **Interview Score:** {interview:.3f} / 5")

    st.success(f"### Final Merit Score: {total_merit:.3f} / 100")
