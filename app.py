import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import openai # Optionnel : pour l'IA

st.set_page_config(page_title="LexiClip", page_icon="✍️")

st.title("✍️ LexiClip : Vidéo -> Article")
st.write("Transformez n'importe quelle vidéo YouTube en article de blog en un clic.")

url = st.text_input("Collez l'URL de la vidéo YouTube :")

if url:
    try:
        video_id = url.split("v=")[1].split("&")[0]
        
        if st.button("Générer l'article"):
            with st.spinner('Extraction du texte...'):
                # Récupère la transcription
                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['fr', 'en'])
                full_text = " ".join([t['text'] for t in transcript])
                
                st.subheader("Transcription brute :")
                st.text_area("Texte extrait", full_text, height=300)
                
                # Note : Pour un vrai SaaS, ici tu connectes l'API OpenAI 
                # pour transformer ce texte en bel article structuré.
                st.success("Terminé ! Vous pouvez copier ce texte pour votre blog.")
                
    except Exception as e:
        st.error("Erreur : Assurez-vous que la vidéo possède des sous-titres.")
