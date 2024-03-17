import streamlit as st
from PIL import Image
import google.generativeai as genai

st.info("NOTE: In order to use this mode, you need to give webcam access.")

genai.configure(api_key= st.secrets["genainp"])
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text
    
def main():
    st.sidebar.header("Navigation")

    # Sidebar navigation links with bullets
    st.sidebar.markdown("- [GitHub Repo](https://github.com/nabdeep-patel/image-qa/)")
    st.sidebar.write("---")
    
    # Connect with me section
    st.sidebar.markdown("Connect with me:")
    github_link = "[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat-square&logo=github)](https://github.com/nabdeep-patel)"
    linkedin_link = "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/nabdeeppatel)"
    website_link = "[![Website](https://img.shields.io/badge/Personal-Website-blue?style=flat-square&logo=chrome)](https://linktr.ee/nabdeeppatel/store)"
    email_link = "[![Email](https://img.shields.io/badge/Google-Mail-blue?style=flat-square&logo=gmail)](mailto:nabdeeppatel@gmail.com)"
    
    st.sidebar.markdown(github_link + " " + linkedin_link + " " + website_link + " " + email_link)
    st.sidebar.markdown("Created by Nabdeep Patel")

    
    st.title("Image QA_Bot")
    st.write("Capture an Image from Webcam or Upload an Image")

    # Radio button to choose capture mode
    capture_mode = st.radio("Choose Capture Mode", ("Webcam", "Upload"))

    # If webcam capture mode is selected
    if capture_mode == "Webcam":
        # Webcam capture mode
        img_file_buffer = st.camera_input(
            label="",
            key="webcam",
            help="Make sure you have given webcam permission to the site"
        )

        # If image is captured
        if img_file_buffer is not None:
            # Convert image buffer to PIL Image
            image = Image.open(img_file_buffer)
            
            # Display the captured image
            st.image(image, caption='Captured Image', use_column_width=True)

    # If upload mode is selected
    else:
        # File uploader to upload an image
        uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

        # If image is uploaded
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
    
    input=st.text_input("Input Prompt: ",key="input")
    submit=st.button("Get Response")

    if submit:
        response=get_gemini_response(input,image)
        st.subheader("The Response is")
        st.write(response)

    
if __name__ == "__main__":
    main()
