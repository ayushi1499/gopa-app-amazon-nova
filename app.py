import streamlit as st
from PIL import Image
import time

# UI Header
st.set_page_config(page_title="GOPA: Krishna Stories", page_icon="✨")
st.title("GOPA ✨")
st.subheader("Personalized Mythology for Little Ones")

# Step 1: Selection
col1, col2 = st.columns(2)
with col1:
    value = st.selectbox("Choose a Value", ["Friendship (Sudama)", "Kindness (Cows)", "Fun (Butter)"])
with col2:
    duration = st.radio("Story Length", ["1 Min", "3 Mins"])

# Step 2: Personalization (The "Magic" Step)
st.write("---")
st.write("### 📸 Meet Your Friend!")
uploaded_file = st.file_uploader("Upload a photo to join Krishna in the story", type=['jpg', 'png'])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Nova is ready to stylize this face!", width=200)

# Step 3: Generate
if st.button("✨ CREATE MY STORY", use_container_width=True):
    with st.status("Nova is painting your story...", expanded=True) as status:
        st.write("1. Chronicler is writing the script...")
        time.sleep(2)
        st.write("2. Visionary is creating 3D characters...")
        time.sleep(2)
        st.write("3. Animator is bringing it to life...")
        time.sleep(3)
        status.update(label="Story Ready!", state="complete", expanded=False)
    
    # Placeholder for Video Output
    st.video("https://www.w3schools.com/html/mov_bbb.mp4") # Replace with Nova Reel URL
    st.success("Your story is ready for bedtime!")
