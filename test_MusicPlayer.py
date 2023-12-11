from itertools import permutations
import unittest
from unittest.mock import patch
import random

# Import the MusicPlayer class
from MusicPlayer import MusicPlayer

class TestMusicPlayer(unittest.TestCase):
    def setUp(self):
        self.player = MusicPlayer()

    def test_add_track(self):
        self.player.add_track("Track 1")
        self.assertIn("Track 1", self.player.playlist)

    def test_remove_track(self):
        self.player.add_track("Track 1")
        self.player.remove_track("Track 1")
        self.assertNotIn("Track 1", self.player.playlist)

    def test_play(self):
        result = self.player.play()
        self.assertEqual(result, "Playlist is empty. Add tracks to play.")

        self.player.add_track("Track 1")
        result = self.player.play()
        self.assertTrue(result.startswith("Playing"))

    def test_pause(self):
        result = self.player.pause()
        self.assertEqual(result, "Player is already paused.")

        self.player.add_track("Track 1")
        self.player.play()
        result = self.player.pause()
        self.assertTrue(result.startswith("Paused"))

    def test_next_track(self):
        result = self.player.next_track()
        self.assertEqual(result, "Playlist is empty. Add tracks to play.")

        self.player.add_track("Track 1")
        self.player.add_track("Track 2")
        self.player.play()
        result = self.player.next_track()
        self.assertTrue(result.startswith("Playing Track 2"))

    def test_previous_track(self):
        self.player.add_track("Track 1")
        self.player.add_track("Track 2")
        self.player.play()
        result = self.player.previous_track()
        self.assertTrue(result.startswith("Playing Track 2"))

    def test_shuffle_playlist(self):
        self.player.add_track("Track 1")
        self.player.add_track("Track 2")
        self.player.play()
        original_playlist = self.player.playlist.copy()
        
        # Set a random seed to ensure consistent shuffling for the test
        random.seed(12345)
        result = self.player.shuffle_playlist()
        self.assertEqual(result.strip(), "Playlist shuffled.")

        # Shuffle the playlist manually
        shuffled_playlist = self.player.playlist.copy()
        random.shuffle(shuffled_playlist)

        # Check that the shuffled playlist is different from the original playlist
        self.assertNotEqual(shuffled_playlist, original_playlist)

        # Check that both playlists have the same elements
        self.assertTrue(set(shuffled_playlist) == set(original_playlist))    
        
    def test_adjust_volume(self):
        result = self.player.adjust_volume(75)
        self.assertEqual(result.strip(), "Volume adjusted to 75%")

        result = self.player.adjust_volume(110)
        self.assertEqual(result.strip(), "Volume should be between 0% and 100%.")


    def test_current_track_info(self):
        result = self.player.current_track_info()
        self.assertEqual(result, "No track is currently playing.")

        self.player.add_track("Track 1")
        self.player.play()
        result = self.player.current_track_info()
        self.assertTrue(result.startswith("Current track: Track 1"))

    def test_playlist_info(self):
        result = self.player.playlist_info()
        self.assertEqual(result, "Playlist is empty.")

        self.player.add_track("Track 1")
        self.player.add_track("Track 2")
        result = self.player.playlist_info()
        self.assertEqual(result, "Track 1\nTrack 2")

    def test_clear_playlist(self):
        result = self.player.clear_playlist()
        self.assertEqual(result, "Playlist cleared.")
        self.assertEqual(self.player.playlist, [])
        self.assertEqual(self.player.current_track_index, -1)

    def test_repeat_track(self):
        result = self.player.repeat_track()
        self.assertEqual(result, "Playlist is empty. Add tracks to play.")

        self.player.add_track("Track 1")
        self.player.play()
        result = self.player.repeat_track()
        self.assertTrue(result.startswith("Repeating Track 1"))

    def test_get_current_volume(self):
        result = self.player.get_current_volume()
        self.assertEqual(result, "Current volume: 50%")

    def test_set_track(self):
        self.player.add_track("Track 1")
        self.player.add_track("Track 2")
        result = self.player.set_track(1)
        self.assertTrue(result.startswith("Set to track Track 2"))

        result = self.player.set_track(2)
        self.assertEqual(result, "Invalid track index.")

    def test_get_playlist_length(self):
        result = self.player.get_playlist_length()
        self.assertEqual(result, "Playlist length: 0 tracks")

        self.player.add_track("Track 1")
        self.player.add_track("Track 2")
        result = self.player.get_playlist_length()
        self.assertEqual(result, "Playlist length: 2 tracks")

    def test_add_album(self):
        self.player.add_album("Album 1", ["Track A", "Track B"])
        self.assertIn("Album 1 - Track A", self.player.playlist)
        self.assertIn("Album 1 - Track B", self.player.playlist)

    def test_remove_album(self):
        self.player.add_album("Album 1", ["Track A", "Track B"])
        self.player.remove_album("Album 1")
        self.assertNotIn("Album 1 - Track A", self.player.playlist)
        self.assertNotIn("Album 1 - Track B", self.player.playlist)

    def test_play_album(self):
        result = self.player.play_album("Album 1")
        self.assertEqual(result, "No tracks found for album: Album 1")

        self.player.add_album("Album 1", ["Track A", "Track B"])
        result = self.player.play_album("Album 1")
        self.assertTrue(result.startswith("Playing album: Album 1"))

    def test_get_current_track_index(self):
        result = self.player.get_current_track_index()
        self.assertEqual(result, "No track is currently playing.")

        self.player.add_track("Track 1")
        self.player.play()
        result = self.player.get_current_track_index()
        self.assertTrue(result.startswith("Current track index:"))

    def test_get_current_track_duration(self):
        result = self.player.get_current_track_duration()
        self.assertEqual(result, "No track is currently playing.")

        self.player.add_track("Track 1")
        self.player.play()
        result = self.player.get_current_track_duration()
        self.assertTrue(result.startswith("Track duration:"))

if __name__ == '__main__':
    unittest.main()
