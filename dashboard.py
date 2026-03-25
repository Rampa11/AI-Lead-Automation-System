import streamlit as st
import requests
import pandas as pd

st.title("📊 AI Lead Dashboard")

# =========================
# SUBMIT LEAD
# =========================
st.header("Submit New Lead")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Submit Lead"):
    res = requests.post(
        "https://ai-lead-automation-system.onrender.com/leads/",
        json={
            "name": name,
            "email": email,
            "message": message
        }
    )

    data = res.json()

    # 🔥 DEBUG (VERY IMPORTANT)
    st.write("API RESPONSE:", data)

    if "status" in data:
        st.success("Lead Processed Successfully")
        st.write(f"**Status:** {data['status']}")
        st.write(f"**Summary:** {data['summary']}")
        st.write(f"**Response:** {data['response']}")
    else:
        st.error("Unexpected API response")


# =========================
# ANALYTICS SECTION
# =========================
st.header("📈 Lead Analytics")

# 👇 You’ll add this endpoint next
try:
    res = requests.get("https://ai-lead-automation-system.onrender.com/leads/")
    leads = res.json()

    df = pd.DataFrame(leads)

    if not df.empty:
        st.write("### All Leads")
        st.dataframe(df)

        st.write("### Lead Status Breakdown")
        st.bar_chart(df["status"].value_counts())

except:
    st.warning("Run backend to see analytics")