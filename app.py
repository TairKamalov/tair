from PIL import Image
import requests 
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = "https://lottie.host/b0a33975-197e-4e27-8918-c134527e372b/SfOxUleAFK.json"
img_contact_from = Image.open("images/profilo.png")
img_lottie_animation = Image.open("images/tair.png")


with st.container():
    lefts_column, rights_column = st.columns(2)
    with lefts_column:
        st.title("Hi, I am Tair :wave:")
        st.header("19.08.2008")
with rights_column:
    st.image(img_contact_from, width=200)

with st.container():
    st.title('Образование')
    st.header('Я учусь в школе TAMOS Education')
    st.write("""  """)
    st.write("")

                   

with st.container():
    st.title("Хобби")
    st.header("Я играю в баскетбол, это мой любимый вид спорта")
    st.header('Я также хожу в зал')
    
    

with st.container():
        st.write("---")
        st.header("Отзывы")
        st.write("##")
        
        
        
        contact_from = """
        <form action="https://formsubmit.co/tairkamalov08@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form> 
        """ 
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_from, unsafe_allow_html=True)
        with right_column:
            st.empty()




def local_css(file_name):
    with open(file_name) as f:        
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")