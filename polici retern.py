import streamlit as st

# පිටුවේ සැකසුම්
st.set_page_config(page_title="Return Policy - SVP Web", layout="centered")

st.title("Return & Refund Policy")
st.write("Last Updated: January 2026")

# භාෂා දෙක තේරීමට tab දෙකක් පාවිච්චි කරමු
tab1, tab2 = st.tabs(["English", "සිංහල"])

with tab1:
    st.markdown("""
    ### 1. Refund Eligibility
    You are eligible for a refund if:
    * The service was not delivered as described.
    * A technical error caused a double payment.

    ### 2. Time Frame
    Refund requests must be made within **7 days** of the transaction date.

    ### 3. Processing Time
    Approved refunds will reflect in your original payment method within **5 to 10 working days**.

    ### 4. Contact Us
    * **Email:** isurukihanduwage1988lk@gmail.com
    * **Phone:** 076 677 0856
    """)

with tab2:
    st.markdown("""
    ### 1. මුදල් ආපසු ලබාගැනීමේ සුදුසුකම්
    පහත අවස්ථාවලදී ඔබට මුදල් ආපසු ලබාගත හැක:
    * පොරොන්දු වූ පරිදි සේවාව ලබා නොදුන්නේ නම්.
    * තාක්ෂණික දෝෂයක් නිසා එකම ගනුදෙනුව සඳහා දෙවරක් මුදල් කැපී ඇත්නම්.

    ### 2. කාල සීමාව
    ගනුදෙනුව සිදු කර **දින 7ක්** ඇතුළත අප වෙත දැනුම් දිය යුතුය.

    ### 3. මුදල් ලැබෙන කාලය
    අනුමත වූ මුදල් දින **5 සිට 10 දක්වා** කාලයක් ඇතුළත ඔබේ ගිණුමට බැර කරනු ලැබේ.

    ### 4. අප හා සම්බන්ධ වීමට
    * **ඊමේල්:** isurukihanduwage1988lk@gmail.com
    * **දුරකථන:** 076 677 0856
    """)

st.divider()
st.info("Securely processed by PayHere (Pvt) Ltd.")
