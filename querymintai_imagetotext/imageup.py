import streamlit as st

# Replace these placeholders with your desired image path and text content
image_path = "imageup.png"  # Replace with actual image path
text1 = "Describe the image."
text2 = "The image is a still life of a basket of fresh fruits, including apples and grapes. The fruits are stored in a storage basket, and the image represents natural foods and healthy eating."

st.title("QueryMintAI: Image Chatbot")

def add_border(text):
  """Adds a CSS border style to the provided text."""
  return f"<div style='border: 1px solid #ddd; padding: 10px; margin-bottom: 10px;'>{text}</div>"



# Display the image in a container
col1, col2 = st.columns(2)
with col1:
  st.image(image_path, width=250)

# Display each text paragraph in separate containers with borders
with col2:
  st.subheader("Question")
  st.write(add_border(text1), unsafe_allow_html=True)
  st.subheader("Answer")
  st.write(add_border(text2), unsafe_allow_html=True)