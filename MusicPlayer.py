import random

class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_track_index = -1
        self.playing = False
        self.volume = 50  # Default volume is set to 50%

    def add_track(self, track):
        self.playlist.append(track)

    def remove_track(self, track):
        if track in self.playlist:
            self.playlist.remove(track)
            if self.current_track_index >= len(self.playlist):
                self.current_track_index = -1

    def play(self):
        if not self.playlist:
            return "Playlist is empty. Add tracks to play."
        if not self.playing:
            self.playing = True
            if self.current_track_index == -1:
                self.current_track_index = 0
            return f"Playing {self.playlist[self.current_track_index]}"
        return "Player is already playing."

    def pause(self):
        if self.playing:
            self.playing = False
            return f"Paused {self.playlist[self.current_track_index]}"
        return "Player is already paused."

    def next_track(self):
        if not self.playlist:
            return "Playlist is empty. Add tracks to play."
        if self.playing:
            self.pause()
        self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        return f"Playing {self.playlist[self.current_track_index]}"

    def previous_track(self):
        if not self.playlist:
            return "Playlist is empty. Add tracks to play."
        if self.playing:
            self.pause()
        self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        return f"Playing {self.playlist[self.current_track_index]}"

    def shuffle_playlist(self):
        if len(self.playlist) > 1:
            random.shuffle(self.playlist)
            if self.playing:
                self.pause()
            self.current_track_index = 0
            return "Playlist shuffled."
        return "Shuffling requires at least 2 tracks in the playlist."

    def adjust_volume(self, new_volume):
        if 0 <= new_volume <= 100:
            self.volume = new_volume
            return f"Volume adjusted to {self.volume}%"
        else:
            return "Volume should be between 0% and 100%."

    def current_track_info(self):
        if self.current_track_index != -1:
            return f"Current track: {self.playlist[self.current_track_index]}"
        return "No track is currently playing."

    def playlist_info(self):
        if not self.playlist:
            return "Playlist is empty."
        return "\n".join(self.playlist)

    def clear_playlist(self):
        if self.playing:
            self.pause()
        self.playlist.clear()
        self.current_track_index = -1
        return "Playlist cleared."

    def repeat_track(self):
        if not self.playlist:
            return "Playlist is empty. Add tracks to play."
        if self.playing:
            self.pause()
        return f"Repeating {self.playlist[self.current_track_index]}"

    def get_current_volume(self):
        return f"Current volume: {self.volume}%"

    def set_track(self, track_index):
        if 0 <= track_index < len(self.playlist):
            if self.playing:
                self.pause()
            self.current_track_index = track_index
            return f"Set to track {self.playlist[self.current_track_index]}"
        return "Invalid track index."

    def get_playlist_length(self):
        return f"Playlist length: {len(self.playlist)} tracks"

    def add_album(self, album_name, tracks):
        for track in tracks:
            self.add_track(f"{album_name} - {track}")

    def remove_album(self, album_name):
        tracks_to_remove = [track for track in self.playlist if album_name in track]
        for track in tracks_to_remove:
            self.remove_track(track)

    def play_album(self, album_name):
        album_tracks = [track for track in self.playlist if album_name in track]
        if not album_tracks:
            return f"No tracks found for album: {album_name}"
        if self.playing:
            self.pause()
        self.playlist = album_tracks
        self.current_track_index = 0
        return f"Playing album: {album_name}"

    def get_current_track_index(self):
        if self.current_track_index != -1:
            return f"Current track index: {self.current_track_index}"
        return "No track is currently playing."

    def get_current_track_duration(self):
        if self.current_track_index != -1:
            return f"Track duration: {random.randint(180, 300)} seconds"  # Simulated duration
        return "No track is currently playing."
