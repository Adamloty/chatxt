
import streamlit as st  # pip install streamlit
from PIL import Image  # pip install pillow
from pathlib import Path

# --- PATH SETTINGS ---
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"


# --- GENERAL SETTINGS ---
STRIPE_CHECKOUT = "https://megaminds-academy.com/"
CONTACT_EMAIL = "adamlotfy011@gmail.com"
PRODUCT_NAME = "chatxt"
PRODUCT_TAGLINE = "Ready to become an AI superhero? 🚀"
PRODUCT_DESCRIPTION = """
Chatxt AI provides an AI variety such as chatting with a website.
What are the reasons that make us buy this application: First, because there are no sites where all these tools are located, and with safety """


def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --- PAGE CONFIG ---
st.set_page_config(
    page_title=PRODUCT_NAME,
    page_icon=":star:",
    layout="centered",
    initial_sidebar_state="collapsed",
)
load_css_file(CSS_FILE)


# --- MAIN SECTION ---
st.header(PRODUCT_NAME)
st.subheader(PRODUCT_TAGLINE)
left_col, right_col = st.columns((2, 1))
with left_col:
    st.text("")
    st.write(PRODUCT_DESCRIPTION)
    st.markdown(
        f'<a href={STRIPE_CHECKOUT} class="button">👉 Subscribe and download</a>',
        unsafe_allow_html=True,
    )
with right_col:
    product_image = Image.open(ASSETS_DIR / "product.png")
    st.image(product_image, width=450)


# --- FEATURES ---
st.write("")
st.write("---")
st.subheader(":rocket: Features")
features = {
    "Feature_1.png": [
        "chat with website",
        "I mean the Internet is under a website link and you ask what is in reality Okay, what will we benefit? We will benefit if there is a lot of information on the site and we are searching for this every now and then, the issue will make it very easy for us.",
    ],
    "Feature_2.png": [
        "Chat PDF",
        "Talk to PDF and this means that you will stay with your PDF and if there is a lot of data you can ask for specific data.",
    ],
    "Feature_3.png": [
        "Summarizing PDF",
        "under PDF and summarized in less than 50 words or more according to the table.",
    ],
}
for image, description in features.items():
    image = Image.open(ASSETS_DIR / image)
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.image(image, use_column_width=True)
    right_col.write(f"**{description[0]}**")
    right_col.write(description[1])


st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ")
faq = {
    "Question 1 Are there any updates that will happen? ": "Yes, there will be continuous updates",
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)


st.write("")
st.write("---")
st.subheader(":mailbox: Have A Question? Ask Away!")
contact_form = f"""
<form action="https://formsubmit.co/{CONTACT_EMAIL}" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit" class="button">Send ✉</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)