import streamlit as st

st.title("Punjab CTI Induction Merit Calculator")

college_type = st.radio("Select College Type:", ["Associate College", "Graduate College"])
degree_track = st.radio("Select Degree Track:", ["BS 4-Year Program", "MA/MSc (2-Year) Program"])

# Academic Inputs
st.subheader("Academic Percentages")
matric_pct = st.number_input("Matric Percentage (%):", min_value=0.0, max_value=100.0, value=75.0)
inter_pct = st.number_input("Intermediate Percentage (%):", min_value=0.0, max_value=100.0, value=75.0)

if degree_track == "BS 4-Year Program":
    bs_pct = st.number_input("BS Percentage / Converted Percentage (%):", min_value=0.0, max_value=100.0, value=80.0)
else:
    ba_pct = st.number_input("BA/BSc Percentage (%):", min_value=0.0, max_value=100.0, value=65.0)
    ma_pct = st.number_input("MA/MSc Percentage (%):", min_value=0.0, max_value=100.0, value=75.0)

# Higher Qualification & Interview
higher_qual = st.selectbox("Higher Qualification in Relevant Subject:", ["None", "M.Phil", "Ph.D"])
mphil_pct = 0.0
if college_type == "Graduate College" and higher_qual == "M.Phil":
    mphil_pct = st.number_input("M.Phil Percentage (%):", min_value=0.0, max_value=100.0, value=80.0)

prior_perf = st.slider("Prior Performance Score (Principal Evaluation):", 0.0, 10.0, 0.0)
interview = st.slider("Interview Score:", 0.0, 5.0, 3.0)

# Calculate Button
if st.button("Calculate Merit Score"):
    if college_type == "Associate College":
        matric_score = (matric_pct / 100) * 15
        inter_score = (inter_pct / 100) * 15
        if degree_track == "BS 4-Year Program":
            bs_score = (bs_pct / 100) * 50
            acad_total = matric_score + inter_score + bs_score
        else:
            acad_total = (matric_pct/100)*15 + (inter_pct/100)*15 + (ba_pct/100)*15 + (ma_pct/100)*35
        
        hq_score = 5.0 if higher_qual == "Ph.D" else (3.0 if higher_qual == "M.Phil" else 0.0)
    else:
        matric_score = (matric_pct / 100) * 15
        inter_score = (inter_pct / 100) * 15
        if degree_track == "BS 4-Year Program":
            bs_score = (bs_pct / 100) * 40
            acad_total = matric_score + inter_score + bs_score
        else:
            acad_total = (matric_pct/100)*15 + (inter_pct/100)*15 + (ba_pct/100)*10 + (ma_pct/100)*30
        
        hq_score = 5.0 if higher_qual == "Ph.D" else ((mphil_pct / 100) * 10 if higher_qual == "M.Phil" else 0.0)

    total_merit = acad_total + hq_score + prior_perf + interview
    st.success(f"### Final Merit Score: {total_merit:.3f} / 100")