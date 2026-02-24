# ============================================================
#  🎉 My First Streamlit App — Beginner Friendly!
#  Run it with:  streamlit run my_first_app.py
# ============================================================

import streamlit as st

# ----------------------------------------------------------
# PAGE CONFIG  (must be the very first Streamlit command)
# ----------------------------------------------------------
st.set_page_config(
    page_title="My First App",
    page_icon="🚀",
    layout="centered",
)

# ----------------------------------------------------------
# TITLE & INTRO
# ----------------------------------------------------------
st.title("🚀 My First Streamlit App")
st.write("Welcome! This app shows you the most useful Streamlit features.")

# A horizontal divider
st.divider()

# ----------------------------------------------------------
# SECTION 1 — Text Input
# ----------------------------------------------------------
st.header("1️⃣ Say Hello")

name = st.text_input("What's your name?", placeholder="Type your name here…")

if name:                          # only runs when the user has typed something
    st.success(f"Hello, {name}! 👋 Great to meet you!")
else:
    st.info("👆 Type your name above to get a greeting.")

st.divider()

# ----------------------------------------------------------
# SECTION 2 — Slider
# ----------------------------------------------------------
st.header("2️⃣ Number Slider")

age = st.slider("How old are you?", min_value=1, max_value=100, value=25)
st.write(f"You selected: **{age}** years old.")

# A little fun fact based on the age
if age < 18:
    st.write("🎒 You're still in school — enjoy it!")
elif age < 60:
    st.write("💼 Prime working years!")
else:
    st.write("🌴 Retirement mode — well deserved!")

st.divider()

# ----------------------------------------------------------
# SECTION 3 — Selectbox (Drop-down)
# ----------------------------------------------------------
st.header("3️⃣ Pick a Favourite")

fruit = st.selectbox(
    "What's your favourite fruit?",
    ["🍎 Apple", "🍌 Banana", "🍇 Grapes", "🥭 Mango", "🍓 Strawberry"],
)
st.write(f"Great choice — **{fruit}** is delicious!")

st.divider()

# ----------------------------------------------------------
# SECTION 4 — Checkbox
# ----------------------------------------------------------
st.header("4️⃣ Checkbox Toggle")

show_secret = st.checkbox("Show a fun fact 🤫")

if show_secret:
    st.balloons()                  # fun confetti animation!
    st.info("🧠 Fun Fact: Honey never spoils. Archaeologists found 3000-year-old honey in Egyptian tombs and it was still edible!")

st.divider()

# ----------------------------------------------------------
# SECTION 5 — Button
# ----------------------------------------------------------
st.header("5️⃣ Click a Button")

if st.button("Generate a motivational quote 💪"):
    import random
    quotes = [
        "The best time to start was yesterday. The next best time is NOW.",
        "Every expert was once a beginner.",
        "Small steps every day lead to big results.",
        "You don't have to be great to start, but you have to start to be great.",
        "Code. Break. Fix. Repeat. Grow. 🚀",
    ]
    st.success(random.choice(quotes))

st.divider()

# ----------------------------------------------------------
# SECTION 6 — Simple Chart
# ----------------------------------------------------------
st.header("6️⃣ A Simple Chart")

import pandas as pd
import random

# Create some fake data
data = pd.DataFrame({
    "Day":    ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Steps":  [random.randint(3000, 15000) for _ in range(7)],
})

st.bar_chart(data.set_index("Day"))
st.caption("📊 Random step counts for the week (refresh to regenerate!)")

st.divider()

# ----------------------------------------------------------
# FOOTER
# ----------------------------------------------------------
st.write("Built with ❤️ using [Streamlit](https://streamlit.io)")