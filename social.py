import streamlit as st
import qrcode
import qrcode.image.svg
import io

def show_info():
    st.sidebar.title('Hey there!')
    st.sidebar.header('Quick webpage info')
    explanation = st.sidebar.beta_expander("What's the point?", True)
    explanation.write("In college, there are a lot of opportunities to meet a ridiculous amount of people. In this day and age, asking them for all their social media @'s is potentially very awkard. They might not want to give you their Snapchat, or maybe their username is too complicated to catch in a setting where you're surrounded by new people. This website creates standardized QR codes to easily get the information they're comfortable giving out!")
    how = st.sidebar.beta_expander("How does it work?", True)
    how.markdown("""There are two use-cases for this website.
    \nFirst, you just met someone and they have a QR code generated with us. In this case, you would scan the code using your phones camera, and then have access to whatever information they decided to add to their code. You will be able to easily follow them on their social medias!
    \nSecond, you want to generate a QR code with us. In this case, you simply go to the [homepage](https://share.streamlit.io/rivera-fernando/streamlit-social/main/social.py), fill out the fields and generate your code, which you can download easily.""")
    st.title("You just scanned a new friend!")
    st.header("Basic info")
    query_params = st.experimental_get_query_params()
    st.text(query_params['name'][0])
    st.text(query_params['phone'][0])
    st.text(query_params['email'][0])

    st.header("Socials")
    st.subheader("Add any if possible")
    insta = query_params['insta'][0]
    if insta == "null":
        st.markdown("Instagram: **not provided**")
    else:
        st.markdown("Instagram: ["+insta+"](" + "https://www.instagram.com/" + insta +")")
    snap = query_params['snap'][0]
    if snap == "null":
        st.markdown("Snapchat: **not provided**")
    else:
        st.markdown("Snapchat: ["+snap+"](" + "https://www.snapchat.com/add/" + snap +")")
    fb = query_params['fb'][0]
    if fb == "null":
        st.markdown("Facebook: **not provided**")
    else:
        st.markdown("Facebook: ["+fb+"](" + "https://www.facebook.com/profile.php?id=" + fb +")")


    st.header("Professional")
    linked = query_params['linked'][0]
    if linked == "null":
        st.markdown("LinkedIn: **not provided**")
    else:
        st.markdown("LinkedIn: ["+linked+"](" + "https://www.linkedin.com/in/" + linked +")")
    git = query_params['github'][0]
    if git == "null":
        st.markdown("GitHub: **not provided**")
    else:
        st.markdown("GitHub: ["+git+"](" + "https://www.github.com/" + git +")")
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
    insta = left2.text_input("Instagram Username")
    if insta == "":
        insta = "null"
    snap = middle2.text_input("Snapchat Username")
    if snap == "":
        snap = "null"
    fb = right2.text_input("Facebook Personal ID")
    if fb == "":
        fb = "null"



    st.subheader("Professional")
    left3, middle3, right3 = st.beta_columns(3)
    linkedin = left3.text_input("LinkedIn URL Ending")
    if linkedin == "":
        linkedin = "null"
    github = middle3.text_input("Github Username")
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
        st.write(link)
        img = qrcode.make(link)
        bytes = io.BytesIO()
        img.save(bytes, format='PNG')
        bytes = bytes.getvalue()
        st.image(bytes, "personal code", 300)

query_params = st.experimental_get_query_params()
if query_params == {}:
    create_code()
else:
    show_info()
