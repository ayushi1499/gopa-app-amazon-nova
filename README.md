# gopa-app-amazon-nova
✨ GOPA: Little Krishna’s Adventures
A Multimodal AI Bedrock Engine for Value-Based Childhood Mythology
GOPA is an AI-powered storytelling platform designed for immigrant parents who want to introduce their children (ages 3-5) to Indian mythology and universal values through personalized, high-quality video content.

Built using the Amazon Nova suite, GOPA transforms simple value selections into animated bedtime stories where the child can actually "enter" the story as Krishna's friend.

🚀 The Vision
To bridge the cultural gap for the next generation using state-of-the-art Generative AI. We focus on "Bal Leela" (Childhood stories) to ensure content is age-appropriate, focusing on kindness, friendship, and fun—removing complex adult themes to suit a toddler's world.

🛠️ Tech Stack: The "Nova" Triple-Threat
This project utilizes a multi-agent architecture powered by Amazon Bedrock:

The Chronicler (Amazon Nova Pro): Orchestrates the reasoning. It filters mythological texts for age-appropriate content and generates structured scripts focused on core values like Friendship and Honesty.

The Visionary (Amazon Nova Canvas): Handles the image-to-image personalization. It takes an uploaded photo of a child and stylizes it into a 3D-animated character that exists alongside Little Krishna.

The Animator (Amazon Nova Reel): Converts static scenes into 60-second high-fidelity videos with consistent character motion and cinematic camera paths.

✨ Key Features
Value-Based Selection: Parents choose a lesson (e.g., "Sharing" with Krishna & Sudama).

Persona Personalization: Upload a photo to see your child animated into the story.

Safety First: Strict system prompts ensure no "Mahabharata-style" violence; only peaceful, colorful Vrindavan-era stories.

Multilingual Support: Ready for English, Hindi, and regional languages to help kids stay connected to their roots.

📂 Project Structure
/app.py: Streamlit-based interactive UI.

/agents: Logic for Nova Pro (Script), Canvas (Image), and Reel (Video).

/assets: Character design sheets and style guidelines for consistent AI generation.

🏗️ How to Run (MVP)
Clone the repo: git clone https://github.com/your-username/gopa-app.git

Install dependencies: pip install -r requirements.txt

Set up AWS Credentials for Amazon Bedrock.

Run the app: streamlit run app.py
