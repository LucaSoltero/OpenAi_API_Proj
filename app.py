import streamlit as st
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_idea(description, seed_words):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Product description: A home milkshake maker\n"
               "Seed words: fast, healthy, compact.\n"
               "Product names: HomeShaker, Fit Shaker, QuickShake, Shake Maker\n"

               f"Product description: {description}\n"
               f"Seed words:{seed_words}",
        temperature=0.8,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    r = response["choices"]
    smt = r[0]
    return smt["text"]


def get_salespitch(audience, product_description):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a creative ad for the following product to run on Facebook aimed at {audience}:\n"
               f"\nProduct: {product_description}",
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    r = response["choices"]
    smt = r[0]
    return smt["text"]


# CONFIGS
page_title = "Ok AI Business Ideas"
st.set_page_config(page_title=page_title, layout="centered")

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

st.header("Welcome to Ok AI Business Ideas :exclamation:")
st.subheader("Are you to lazy think of a name for your business :question:")
st.subheader("Let Ai do it for free :smile: (be careful how this ends up)")
st.markdown("#")

st.subheader("Generate a name for your Company :exclamation:")
with st.form("P_NAME", clear_on_submit=False):
    st.write("In order to generate names for your business you must give the AI : ")
    st.write(":one:  A Product description")
    st.write(":two:  A list of seed words that describe your business")
    st.write("For example:point_down:")
    st.write("Product description: A home milkshake maker")
    st.write("Seed words: fast, healthy, compact.")

    st.text_input("Product Description :eggplant:", "", key="DESCRIPTION")
    st.text_input("Seed Words :sweat_drops:", "", key="SEED")
    submitted = st.form_submit_button("Submit")

    if submitted:
        description = str(st.session_state["DESCRIPTION"]).strip()
        seed_word = str(st.session_state["SEED"]).strip()
        api_dec = get_idea(description, seed_word)
        st.write(api_dec)

st.markdown("#")

st.subheader("Generate a Sales Pitch :exclamation:")
with st.form("P_SALESPITCH"):
    st.write("To generate a Sales Pitch you must prompt the AI with :")
    st.write(":one:  A target audience")
    st.write(":two:  A Product description")
    st.write("For example:point_down:")
    st.write("Target Audience: Parents")
    st.write("Product Description: A watch that also doubles as a phone")

    st.text_input("Target Audience :family:", "", key="AUDIENCE")
    st.text_input("Prodcut Description :boom:", "", key="P_DESCRIP")

    submitted = st.form_submit_button("Submit")

    if submitted:
        audience = str(st.session_state["AUDIENCE"]).strip()
        desc = str(st.session_state["P_DESCRIP"]).strip()
        api_pitch = get_salespitch(audience, desc)
        st.write(api_pitch)