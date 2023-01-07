from PIL import Image
import requests
import streamlit as st 
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":fish:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_LbTpQe.json")
img_contact_form = Image.open("images/images07.png")
img_lottie_animation = Image.open("images/images13.png")


with st.container():
     st.subheader("Hi,I am MV :dolphin:")
     st.title("An Aquarist")
     st.write("I am passionate about aquariums and growing exotics fishes.")
     st.write("[learn more >](https://instagram.com/whale_drogon?igshid=ZDdkNTZiNTM=)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what i do")
        st.write("##")
        st.write(
            """
            I have alots of aquarium in my home:
            - An Oranda gold fish aquarium.
            - An Oscar aquarium.
            - An betta fish aquarium.
            - An community tank.
            - A  japanese koi fish pond.
            """
        )

        st.write("[instagram page >](https://www.instagram.com/reel/Ck3hxLLuMTQ/?igshid=YmMyMTA2M2Y=)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)

    with text_column:
        st.subheader("Video")
        st.write(
            """
            video!
            Its feeding time
            """
        )
        st.markdown("[Watch Video...](https://www.instagram.com/reel/Ch-L0jYsQ_y/?igshid=YmMyMTA2M2Y=)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Video")
        st.write(
            """
            Reels!
            Community tank
            """
        )         
        st.markdown("[Watch Video...](https://www.instagram.com/reel/CYwcim4JvnL/?igshid=YmMyMTA2M2Y=)")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/sankar.vb2000@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()