import os
import random
import pygame
from pynput import keyboard

# Get the directory of this script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Path to the theme directory. Change 'theme_name' to your desired theme.
theme_dir = os.path.join(script_dir, "switches", "「 ANZT10S 」")

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

# Define a function that plays the sound when a key is pressed
def on_press(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = key.name.lower()  # Convert to lowercase for case-insensitive comparison

    # Do not play sounds for the specified keys
    excluded_keys = ["h", "j", "k", "l", "up", "right", "left", "down", "1", "2", "3", "4", "5", "6", "backspace", "enter", "shift", "ctrl", "cmd", "alt", "tab"]
    excluded_combinations = [(keyboard.Key.shift, keyboard.Key.cmd, keyboard.KeyCode(char='j')),
                             (keyboard.Key.shift, keyboard.Key.cmd, keyboard.KeyCode(char='h'))]

    if key_name in excluded_keys:
        # Check for excluded combinations and return if present
        for comb in excluded_combinations:
            if key == comb:
                return
        else:
            return

    # Play a random sound for any key
    sound = random.choice(list(sounds.values()))
    sound.play()

# Set up the key listener
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
