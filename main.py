import os
import pygame
from pynput import keyboard
import random

# Get the directory of this script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Path to the theme directory. Change 'theme_name' to your desired theme.
theme_dir = os.path.join(script_dir, "switches", "bloop")

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer
pygame.mixer.init()

# Dynamically load all sounds into a dictionary
sounds = {}
for sound_file in os.listdir(theme_dir):
    if sound_file.endswith(".ogg") or sound_file.endswith(".wav"):
        sound_path = os.path.join(theme_dir, sound_file)
        sounds[sound_file] = pygame.mixer.Sound(sound_path)

# Define a mapping from key combinations to sounds
key_to_sound = {
    (keyboard.Key.cmd, keyboard.KeyCode(char='1')): 'key-press-1.wav',
    (keyboard.Key.cmd, keyboard.KeyCode(char='2')): 'key-press-2.wav',
    # Add more key combinations as needed...
}

def on_press(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = key.name.lower()  # Convert to lowercase for case-insensitive comparison

    # Check for specific key combinations and play the corresponding sound
    for comb, sound_name in key_to_sound.items():
        if key == comb and sound_name in sounds:
            sounds[sound_name].play()
            return

    # Play a random sound for any other key
    sound = random.choice(list(sounds.values()))
    sound.play()

# Set up the key listener
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
