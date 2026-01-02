import streamlit as st

st.set_page_config(page_title="Legal Policies - SVP Web", layout="centered")

st.title("Business Terms & Policies")
st.write("Last Updated: January 2026")

tab1, tab2 = st.tabs(["English Version", "සිංහල අනුවාදය"])

with tab1:
    # --- Terms & Conditions ---
    st.header("1. Business Terms & Conditions")
    st.write("""
    * By using our services, you agree to provide accurate information.
    * Payments must be made in full before service delivery.
    * We reserve the right to modify our service fees with prior notice.
    """)

    # --- Return Policy ---
    st.header("2. Return & Refund Policy")
    st.write("""
    * Refunds are processed for undelivered services or technical errors.
    * Requests must be made within 7 days.
    """)
    
    # --- Privacy Policy ---
    st.header("3. Privacy Policy")
    st.write("""
    * We do not store your credit/debit card details. 
    * All payments are securely handled by PayHere (Pvt) Ltd.
    """)

with tab2:
    # --- Terms & Conditions (Sinhala) ---
    st.header("1. ව්‍යාපාරික කොන්දේසි (Terms & Conditions)")
    st.write("""
    * අපගේ සේවාවන් ලබාගැනීමේදී ඔබ නිවැරදි තොරතුරු ලබාදිය යුතුය.
    * සේවාව ලබාදීමට පෙර සම්පූර්ණ ගෙවීම් සිදුකළ යුතුය.
    * සේවා ගාස්තු සංශෝධනය කිරීමේ අයිතිය අප සතු වේ.
    """)

    # --- Return Policy (Sinhala) ---
    st.header("2. මුදල් ආපසු ගෙවීමේ ප්‍රතිපත්තිය")
    st.write("""
    * සේවාව ලබා නොදුන් අවස්ථාවලදී හෝ තාක්ෂණික දෝෂවලදී මුදල් ආපසු ගෙවනු ලැබේ.
    * දින 7ක් ඇතුළත දැනුම් දිය යුතුය.
    """)

    # --- Privacy Policy (Sinhala) ---
    st.header("3. පෞද්ගලිකත්ව ප්‍රතිපත්තිය")
    st.write("""
    * ඔබගේ බැංකු කාඩ්පත් විස්තර අප ගබඩා කර නොගන්නා අතර ඒවා PayHere ආයතනය මගින් ඉතා ආරක්ෂිතව හසුරුවනු ලැබේ.
    """)

st.divider()
st.write("**Contact:** isurukihanduwage1988lk@gmail.com | 076 677 0856")
