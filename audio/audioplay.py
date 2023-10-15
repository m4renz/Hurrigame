import pygame

# find the path of the current file and add the relative path files/TheFatRat_Time_Lapse.mp3 as the default path
import os
_CURRENT_FILE_PATH = os.path.dirname(os.path.realpath(__file__))

_DEFAULT_AUDIO_PATH = 'audio/files/TheFatRat-Time-Lapse.wav'



class AudioPlayer():

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()

    def play_audio(self, path: str) -> None:
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Sound.play(sound)
        while pygame.mixer.get_busy():
            pass

    

if __name__ == '__main__':

    player = AudioPlayer()
# ask user to input path to audio file. If empty, use default path use play_audio function to play audio file
    path = input("Enter path to audio file: ")
    if path == "":
        path = _DEFAULT_AUDIO_PATH
    player.play_audio(path)

