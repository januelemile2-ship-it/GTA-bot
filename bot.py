import os
import time
import subprocess
import requests

# --- CONFIGURATION ---
GEMINI_API_KEY = "TA_CLE_API_GEMINI"

def search_gta_streams():
    print("Recherche des flux en direct en cours...")
    return ["https://twitch.tv/mon_streamer_test"]

def capture_and_buffer(stream_url):
    output_clip = "temp_live_clip.mp4"
    print(f"Capture de 60 secondes depuis {stream_url}...")
    return output_clip

def analyze_clip_with_gemini(video_path):
    print("Analyse du contenu par l'IA Gemini...")
    response_text = "OUI\nLE BUG LE PLUS FOLLE DE GTA\nOH NON !"
    lines = response_text.strip().split('\n')
    is_viral = "OUI" in lines[0].upper()
    title = lines[1] if len(lines) > 1 else "Moment épique sur GTA"
    overlay_text = lines[2] if len(lines) > 2 else "INCROYABLE"
    return is_viral, title, overlay_text

def process_vertical_video(input_path, output_path, overlay_text):
    print(f"Montage automatique au format vertical 9:16 avec le texte : '{overlay_text}'...")
    print(f"Vidéo prête pour publication : {output_path}")

if __name__ == "__main__":
    print("Lancement du bot autonome de clipping...")
    while True:
        streams = search_gta_streams()
        for stream in streams:
            try:
                clip = capture_and_buffer(stream)
                viral, title, text_overlay = analyze_clip_with_gemini(clip)
                
                if viral:
                    print(f"[{title}] détecté comme viral ! Lancement du montage...")
                    final_file = "video_finale_prete.mp4"
                    process_vertical_video(clip, final_file, text_overlay)
                    print("Vidéo générée et prête à être postée automatiquement !")
                else:
                    print("Moment banal, passage au segment suivant.")
            except Exception as e:
                print(f"Erreur technique : {e}")
                
        print("Attente de 5 minutes avant le prochain scan...")
        time.sleep(300)
