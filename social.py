import streamlit as st
import qrcode
import qrcode.image.svg
import io

def show_info():
    st.title("You just scanned a new friend!")
    st.header("Basic info")
    query_params = st.experimental_get_query_params()
    st.text(query_params['name'][0])
    st.text(query_params['phone'][0])
    st.text(query_params['email'][0])

    st.header("Socials")
    st.subheader("Add any if possible")
    st.text(query_params['insta'][0])
    st.text(query_params['snap'][0])
    st.text(query_params['fb'][0])

    st.header("Professional")
    st.text(query_params['linked'][0])
    st.text(query_params['github'][0])
    st.text(query_params['web'][0])


def create_code():
    st.title("Make your own QR code!")
    st.header("Fill in whichever fields you would like to share")
    st.subheader("Basic info")
    left1, middle1, right1 = st.beta_columns(3)
    name = left1.text_input("Name")
    if name == "":
        name = "null"
    phone = middle1.text_input('Number')
    if phone == "":
        phone = "null"
    email = right1.text_input('Email')
    if email == "":
        email = "null"

    st.subheader("Socials")
    left2, middle2, right2 = st.beta_columns(3)
    insta = left2.text_input("Instagram")
    if insta == "":
        insta = "null"
    snap = middle2.text_input("Snapchat")
    if snap == "":
        snap = "null"
    fb = right2.text_input("Facebook")
    if fb == "":
        fb = "null"



    st.subheader("Professional")
    left3, middle3, right3 = st.beta_columns(3)
    linkedin = left3.text_input("LinkedIn")
    if linkedin == "":
        linkedin = "null"
    github = middle3.text_input("Github")
    if github == "":
        github = "null"
    website = right3.text_input("Personal Website")
    if website == "":
        website = "null"
    #make a ton of fields
    #use the info in those fields to make the link,
    #then make the qr code from the link
    link = ("https://share.streamlit.io/rivera-fernando/streamlit-social/main/social.py/" +
                                    "?name=" + name +
                                    "&phone=" + phone +
                                    "&email=" + email +
                                    "&insta=" + insta +
                                    "&snap=" + snap +
                                    "&fb=" + fb +
                                    "&linked=" + linkedin +
                                    "&github=" + github +
                                    "&web=" + website)
    link = link.replace(" ", "%20")
    if st.button("Make my QR Code!"):
        img = qrcode.make(link)
        bytes = io.BytesIO()
        img.save(bytes, format='PNG')
        bytes = bytes.getvalue()
        st.image(bytes, "personal code", 200)

query_params = st.experimental_get_query_params()
if query_params == {}:
    create_code()
else:
    show_info()
