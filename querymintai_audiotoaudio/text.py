import streamlit as st

# Replace with the path to your audio file
audio_file = "Temp.mp3"

# Text content for the containers
text1 = "What is Oncology?"
answer_text = "Oncology is the branch of medicine that deals with the prevention, diagnosis, and treatment of cancer. It encompasses various medical disciplines, including medical oncology (treatment using chemotherapy, targeted therapy, immunotherapy), surgical oncology (surgery to remove tumors), and radiation oncology (treatment using radiation therapy). Oncologists, who specialize in oncology, work closely with other healthcare professionals to provide comprehensive care to cancer patients, including managing symptoms, providing supportive care, and coordinating treatments across different specialties."

st.title("QueryMintAI: Text to Audio")

# Container for text 1 with border
st.markdown(f"""
<div style="border: 1px solid #ddd; padding: 10px; margin-bottom: 10px;">
<h3>Question</h3>
{text1}
</div>
""", unsafe_allow_html=True)

# Container for audio player
st.audio(audio_file, format="audio/mp3")

# Container for answer text
st.markdown(f"""
<div style="border: 1px solid #ddd; padding: 10px; margin-bottom: 10px;">
<h3>Answer</h3>
{answer_text}
</div>
""", unsafe_allow_html=True)

