import streamlit as st
from PIL import Image
import numpy as np

def rgb_to_monochrome(image):
    # Convert image to grayscale
    grayscale = image.convert("L")
    return grayscale

# Streamlit app
st.title("RGB to Monochrome Converter")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    # Open image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)

    # Convert to monochrome
    monochrome_image = rgb_to_monochrome(image)
    st.image(monochrome_image, caption="Monochrome Image", use_container_width=True)

    # Download button
    monochrome_array = np.array(monochrome_image)
    monochrome_image.save("monochrome_image.png")
    with open("monochrome_image.png", "rb") as file:
        st.download_button(
            label="Download Monochrome Image",
            data=file,
            file_name="monochrome_image.png",
            mime="image/png",
        )
