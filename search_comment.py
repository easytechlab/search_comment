import tkinter as tk
from tkinter import filedialog
from TikTokApi import TikTokApi
import asyncio
import os
import sys

# Fonction pour rechercher le mot-clé dans les commentaires
async def get_comments(video_id, search_term, output_text):
    async with TikTokApi() as api:
        await api.create_sessions(num_sessions=1, sleep_after=3)
        video = api.video(id=video_id)
        found = False
        async for comment in video.comments(count=100):
            if search_term.lower() in comment.text.lower():
                output_text.insert(tk.END, f"{comment.text}\n")
                output_text.insert(tk.END, f"https://www.tiktok.com/@scrowhacking/video/{video_id}\n\n")
                found = True
        return found

# Fonction pour parcourir un fichier texte et obtenir les IDs de vidéo
def read_video_ids(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Fonction pour rechercher le mot-clé dans les vidéos
def search_videos():
    search_term = search_entry.get()
    video_ids = read_video_ids(file_entry.get())
    
    for video_id in video_ids:
        found = asyncio.run(get_comments(video_id, search_term, output_text))
        if found:
            output_text.insert(tk.END, f"Mot-clé trouvé dans la vidéo {video_id}\n\n")
        else:
            output_text.insert(tk.END, f"Mot-clé non trouvé dans la vidéo {video_id}\n\n")

# Fonction pour parcourir et sélectionner un fichier texte
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Recherche de Mot-Clé dans les Vidéos TikTok")

# Créer des widgets pour l'interface utilisateur
search_label = tk.Label(root, text="Mot-clé à rechercher:")
search_label.pack()

search_entry = tk.Entry(root)
search_entry.pack()

file_label = tk.Label(root, text="Fichier contenant les IDs de vidéos:")
file_label.pack()

file_entry = tk.Entry(root)
file_entry.pack()

browse_button = tk.Button(root, text="Parcourir", command=browse_file)
browse_button.pack()

search_button = tk.Button(root, text="Rechercher", command=search_videos)
search_button.pack()

output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()
