import os
import pygame
import tkinter as tk
from tkinter import ttk, filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        # Set the background color to white
        self.root.configure(bg="white")

        self.playlist = []
        self.current_index = 0
        self.paused = False

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Set up the GUI with themed widgets
        self.setup_gui()

    def setup_gui(self):
        # Create the treeview for playlist display
        self.playlist_tree = ttk.Treeview(self.root, columns=('Track', 'Path', 'Duration'), show='headings', style="Treeview")
        self.playlist_tree.heading('Track', text='Track')
        self.playlist_tree.heading('Path', text='Path')
        self.playlist_tree.heading('Duration', text='Duration')
        self.playlist_tree.pack(padx=10, pady=10)

        # Buttons
        ttk.Button(self.root, text="Load Playlist", command=self.load_playlist, style="TButton").pack(pady=10)
        ttk.Button(self.root, text="Play", command=self.play_music, style="TButton").pack(pady=10)
        ttk.Button(self.root, text="Pause", command=self.pause_music, style="TButton").pack(pady=10)
        ttk.Button(self.root, text="Stop", command=self.stop_music, style="TButton").pack(pady=10)
        ttk.Button(self.root, text="Next", command=self.next_music, style="TButton").pack(pady=10)
        ttk.Button(self.root, text="Previous", command=self.prev_music, style="TButton").pack(pady=10)

        # Volume control
        self.volume_scale = ttk.Scale(self.root, from_=0, to=1, orient='horizontal', command=self.set_volume, length=200, style="Horizontal.TScale")
        self.volume_scale.set(0.5)
        self.volume_scale.pack(pady=10)

        # Progress bar
        self.progress_var = tk.DoubleVar()
        ttk.Style().configure("TProgressbar", thickness=20, troughcolor="white", background="green")
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, mode='determinate', style="TProgressbar")
        self.progress_bar.pack(pady=10)

        # Configure style for Treeview, TButton, and Horizontal.TScale
        self.root.style = ttk.Style()
        self.root.style.configure("Treeview", background="white", fieldbackground="white", foreground="black", highlightthickness=0)
        self.root.style.configure("TButton", background="white", foreground="black", highlightthickness=0)
        self.root.style.configure("Horizontal.TScale", troughcolor="white", slidercolor="black")

    def load_playlist(self):
        files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
        self.playlist = list(files)

        # Update the playlist display
        self.update_playlist()

    def update_playlist(self):
        self.playlist_tree.delete(*self.playlist_tree.get_children())

        for index, track_path in enumerate(self.playlist, start=1):
            track_name = os.path.basename(track_path)
            duration = self.get_duration_str(track_path)
            self.playlist_tree.insert('', 'end', values=(index, track_name, track_path, duration))

    def get_duration_str(self, file_path):
        # Get the duration of the song in minutes and seconds
        audio = pygame.mixer.Sound(file_path)
        duration_in_seconds = int(audio.get_length())
        minutes, seconds = divmod(duration_in_seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def play_music(self):
        if not self.playlist:
            return

        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

        self.root.after(100, self.update_progress)

    def pause_music(self):
        pygame.mixer.music.pause()
        self.paused = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.progress_var.set(0)

    def next_music(self):
        if not self.playlist:
            return

        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.stop_music()
        self.play_music()

    def prev_music(self):
        if not self.playlist:
            return

        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.stop_music()
        self.play_music()

    def set_volume(self, value):
        pygame.mixer.music.set_volume(float(value))

    def update_progress(self):
        if pygame.mixer.music.get_busy():
            # Calculate percentage completion and update progress bar
            pos = pygame.mixer.music.get_pos() / 1000  # Convert to seconds
            length = pygame.mixer.Sound(self.playlist[self.current_index]).get_length()
            progress_percentage = (pos / length) * 100
            self.progress_var.set(progress_percentage)

            # Update the song running time label
            running_time = self.get_running_time_str(pos)
            self.playlist_tree.item(self.current_index, values=(self.current_index, os.path.basename(self.playlist[self.current_index]), self.playlist[self.current_index], running_time))

            # Call the update_progress function after 100 milliseconds
            self.root.after(100, self.update_progress)
        else:
            # Reset the progress bar and running time label when the song ends
            self.progress_var.set(0)
            self.playlist_tree.item(self.current_index, values=(self.current_index, os.path.basename(self.playlist[self.current_index]), self.playlist[self.current_index], "00:00"))

    def get_running_time_str(self, elapsed_time):
        # Get the running time of the song in minutes and seconds
        minutes, seconds = divmod(elapsed_time, 60)
        return f"{int(minutes):02d}:{int(seconds):02d}"

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
