from io import BytesIO
import streamlit as st
from PIL import Image
from streamlit_webrtc import webrtc_streamer

st.info("NOTE: To use this apk please give webcam access.")

# Main function
def main():
    # Title and instructions
    st.title("Webcam Image Capture")
    st.write("Capture an Image from Webcam")

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

# Execute the main function
if __name__ == "__main__":
    main()
