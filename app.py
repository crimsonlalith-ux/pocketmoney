import streamlit as st

st.title("Pocket Money Tracker")

money = st.number_input("Monthly pocket money (₹)", min_value=0, value=6000, step=100)

st.subheader("Split your money (%)")
food = st.slider("Food", 0, 100, 40)
clothes = st.slider("Clothes", 0, 100, 15)
travel = st.slider("Travel", 0, 100, 15)
savings = st.slider("Savings / Investing", 0, 100, 20)
others = st.slider("Others", 0, 100, 10)

total = food + clothes + travel + savings + others

if total != 100:
    st.warning(f"Your total is {total}%. It should be exactly 100%.")
else:
    st.success("Perfect split!")
    st.subheader("Your budget this month")
    st.write(f"Food: ₹{money * food / 100:.0f}")
    st.write(f"Clothes: ₹{money * clothes / 100:.0f}")
    st.write(f"Travel: ₹{money * travel / 100:.0f}")
    st.write(f"Savings / Investing: ₹{money * savings / 100:.0f}")
    st.write(f"Others: ₹{money * others / 100:.0f}")