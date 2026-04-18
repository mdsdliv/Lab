import pygame
import os

class MusicPlayer:
    def __init__(self, music_dir):
        pygame.mixer.init()
        self.music_dir = music_dir
        # Загружаем только музыкальные файлы
        self.playlist = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
        self.current_index = 0
        self.is_playing = False

    def load_track(self):
        track_path = os.path.join(self.music_dir, self.playlist[self.current_index])
        pygame.mixer.music.load(track_path)

    def play(self):
        if not self.is_playing:
            if not pygame.mixer.music.get_busy():
                self.load_track()
            pygame.mixer.music.play()
            self.is_playing = True
        else:
            pygame.mixer.music.pause()
            self.is_playing = False

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.load_track()
        if self.is_playing:
            pygame.mixer.music.play()

    def prev_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.load_track()
        if self.is_playing:
            pygame.mixer.music.play()

    def get_current_track_name(self):
        return self.playlist[self.current_index] if self.playlist else "No Music Found"