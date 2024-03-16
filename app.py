import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration

class VideoTransformer(VideoProcessorBase):
    def transform(self, frame):
        return frame

def main():
    st.title("Capture Image from Camera")

    # Front camera configuration
    front_camera_config = RTCConfiguration({"video": True, "audio": False})
    front_camera = webrtc_streamer(
        key="front-camera",
        video_transformer_factory=VideoTransformer,
        rtc_configuration=front_camera_config,
        mode="video",
        async_transform=True,
    )

    # Back camera configuration
    back_camera_config = RTCConfiguration({"video": {"facingMode": "environment"}, "audio": False})
    back_camera = webrtc_streamer(
        key="back-camera",
        video_transformer_factory=VideoTransformer,
        rtc_configuration=back_camera_config,
        mode="video",
        async_transform=True,
    )

    # Display captured image
    if front_camera and back_camera:
        st.image(front_camera, channels="BGR", use_column_width=True, caption="Front Camera")
        st.image(back_camera, channels="BGR", use_column_width=True, caption="Back Camera")
    elif front_camera:
        st.image(front_camera, channels="BGR", use_column_width=True, caption="Front Camera")
    elif back_camera:
        st.image(back_camera, channels="BGR", use_column_width=True, caption="Back Camera")

if __name__ == "__main__":
    main()
