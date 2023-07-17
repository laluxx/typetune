# FIX  super shift enter now dont play super enter sound
import os
import time
import random
import pygame
from pynput import keyboard, mouse

# Get the directory of this script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Path to the theme directory.
theme_dir = os.path.join(script_dir, "switches", "- # LALO ⌞Red⌝")

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer
pygame.mixer.init()

# Dynamically load all sounds into separate dictionaries
super_sounds = {}
normal_sounds = {}
mouse_sounds = {}
for sound_file in os.listdir(theme_dir):
    sound_path = os.path.join(theme_dir, sound_file)
    if sound_file.startswith('super'):  # super sounds
        super_sounds[sound_file] = pygame.mixer.Sound(sound_path)
    elif sound_file.startswith('mouse'):  # mouse sounds
        mouse_sounds[sound_file] = pygame.mixer.Sound(sound_path)
    else:  # normal sounds
        normal_sounds[sound_file] = pygame.mixer.Sound(sound_path)

# Define a mapping from key combinations to sounds
key_to_sound = {
    (keyboard.Key.cmd, keyboard.KeyCode(char='1')): 'super-1.ogg',
    (keyboard.Key.cmd, keyboard.KeyCode(char='2')): 'super-2.ogg',
    (keyboard.Key.cmd, keyboard.KeyCode(char='3')): 'super-3.ogg',
    (keyboard.Key.cmd, keyboard.KeyCode(char='4')): 'super-4.ogg',
    (keyboard.Key.cmd, keyboard.KeyCode(char='5')): 'super-5.ogg',
    (keyboard.Key.cmd, keyboard.KeyCode(char='6')): 'super-6.ogg',
    (keyboard.Key.cmd, keyboard.KeyCode(char='7')): 'super-7.ogg',
    (keyboard.Key.cmd, keyboard.KeyCode(char='8')): 'super-8.ogg',
    (keyboard.Key.cmd, keyboard.KeyCode(char='9')): 'super-9.ogg',
    (keyboard.Key.cmd, keyboard.Key.shift, keyboard.KeyCode(char='c')): 'click-close.ogg',
    (keyboard.Key.cmd, keyboard.Key.shift, keyboard.Key.enter): 'silent.wav',  # silent.wav is an empty sound file
    (keyboard.Key.cmd, keyboard.Key.enter): 'super-enter.wav',
}

mouse_to_sound = {
    mouse.Button.left: 'mouse-left.wav',
    mouse.Button.right: 'mouse-right.wav',
    mouse.Button.middle: 'mouse-middle.wav',
}

key_states = {}

# For double click detection
last_click_time = 0
double_click_threshold = 0.3  # seconds

def on_press(key):
    key_states[key] = True
    check_for_combo()

def on_release(key):
    key_states[key] = False

def on_click(x, y, button, pressed):
    global last_click_time
    if pressed and button in mouse_to_sound and mouse_to_sound[button] in mouse_sounds:
        current_time = time.time()
        if button == mouse.Button.left and (current_time - last_click_time) < double_click_threshold:
            # This is a double click, play a different sound
            mouse_sounds['mouse-left-double.ogg'].play()
        else:
            # This is a single click
            mouse_sounds[mouse_to_sound[button]].play()
        last_click_time = current_time

def check_for_combo():
    excluded_keys = [keyboard.KeyCode(char=i) for i in "hjkl123456"]
    excluded_keys.extend([keyboard.Key.up, keyboard.Key.right, keyboard.Key.left, keyboard.Key.down, keyboard.Key.backspace,
                          keyboard.Key.enter, keyboard.Key.shift, keyboard.Key.ctrl, keyboard.Key.cmd, keyboard.Key.alt, keyboard.Key.tab])

    excluded_combinations = [(keyboard.Key.shift, keyboard.Key.cmd, keyboard.KeyCode(char='j')),
                             (keyboard.Key.shift, keyboard.Key.cmd, keyboard.KeyCode(char='h'))]

    for comb in excluded_combinations:
        if all((key in key_states and key_states[key] for key in comb)):
            return

    for comb, sound_name in key_to_sound.items():
        if all((key in key_states and key_states[key] for key in comb)) and sound_name in super_sounds:
            # Check if 'shift' key is pressed when triggering 'super + enter'
            if comb == (keyboard.Key.cmd, keyboard.Key.enter) and key_states.get(keyboard.Key.shift, False):
                continue
            super_sounds[sound_name].play()
            return

    if not any((key in key_states and key_states[key] for key in excluded_keys)):
        sound = random.choice(list(normal_sounds.values()))
        sound.play()

key_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
mouse_listener = mouse.Listener(on_click=on_click)

key_listener.start()
mouse_listener.start()

key_listener.join()
mouse_listener.join()










# double click DONE
# super + enter DONE
# super + super-shift-c NOT DONE
# TODO  super + shift + c custom stound for windows when closing, also super + enter custom sound, will probably write this in xmonad to keep this script small

# import os
# import time
# import random
# import pygame
# from pynput import keyboard, mouse
#
# # Get the directory of this script
# script_dir = os.path.dirname(os.path.realpath(__file__))
#
# # Path to the theme directory.
# theme_dir = os.path.join(script_dir, "switches", "- # LALO ⌞Red⌝")
#
# # Initialize Pygame
# pygame.init()
#
# # Initialize Pygame mixer
# pygame.mixer.init()
#
# # Dynamically load all sounds into separate dictionaries
# super_sounds = {}
# normal_sounds = {}
# mouse_sounds = {}
# for sound_file in os.listdir(theme_dir):
#     sound_path = os.path.join(theme_dir, sound_file)
#     if sound_file.startswith('super'):  # super sounds
#         super_sounds[sound_file] = pygame.mixer.Sound(sound_path)
#     elif sound_file.startswith('mouse'):  # mouse sounds
#         mouse_sounds[sound_file] = pygame.mixer.Sound(sound_path)
#     else:  # normal sounds
#         normal_sounds[sound_file] = pygame.mixer.Sound(sound_path)
#
# # Define a mapping from key combinations to sounds
# key_to_sound = {
#     (keyboard.Key.cmd, keyboard.KeyCode(char='1')): 'super-1.ogg',
#     (keyboard.Key.cmd, keyboard.KeyCode(char='2')): 'super-2.ogg',
#     (keyboard.Key.cmd, keyboard.KeyCode(char='3')): 'super-3.ogg',
#     (keyboard.Key.cmd, keyboard.KeyCode(char='4')): 'super-4.ogg',
#     (keyboard.Key.cmd, keyboard.KeyCode(char='5')): 'super-5.ogg',
#     (keyboard.Key.cmd, keyboard.KeyCode(char='6')): 'super-6.ogg',
#     (keyboard.Key.cmd, keyboard.KeyCode(char='7')): 'super-7.ogg',
#     (keyboard.Key.cmd, keyboard.KeyCode(char='8')): 'super-8.ogg',
#     (keyboard.Key.cmd, keyboard.KeyCode(char='9')): 'super-9.ogg',
#     (keyboard.Key.cmd, keyboard.Key.shift, keyboard.KeyCode(char='c')): 'click-close.ogg',
#     (keyboard.Key.cmd, keyboard.Key.enter): 'super-enter.wav',
# }
#
# mouse_to_sound = {
#     mouse.Button.left: 'mouse-left.wav',
#     mouse.Button.right: 'mouse-right.wav',
#     mouse.Button.middle: 'mouse-middle.wav',
# }
#
# key_states = {}
#
# # For double click detection
# last_click_time = 0
# double_click_threshold = 0.3  # seconds
#
# def on_press(key):
#     key_states[key] = True
#     check_for_combo()
#
# def on_release(key):
#     key_states[key] = False
#
# def on_click(x, y, button, pressed):
#     global last_click_time
#     if pressed and button in mouse_to_sound and mouse_to_sound[button] in mouse_sounds:
#         current_time = time.time()
#         if button == mouse.Button.left and (current_time - last_click_time) < double_click_threshold:
#             # This is a double click, play a different sound
#             mouse_sounds['mouse-left-double.ogg'].play()
#         else:
#             # This is a single click
#             mouse_sounds[mouse_to_sound[button]].play()
#         last_click_time = current_time
#
# def check_for_combo():
#     excluded_keys = [keyboard.KeyCode(char=i) for i in "hjkl123456"]
#     excluded_keys.extend([keyboard.Key.up, keyboard.Key.right, keyboard.Key.left, keyboard.Key.down, keyboard.Key.backspace,
#                           keyboard.Key.enter, keyboard.Key.shift, keyboard.Key.ctrl, keyboard.Key.cmd, keyboard.Key.alt, keyboard.Key.tab])
#
#     excluded_combinations = [(keyboard.Key.shift, keyboard.Key.cmd, keyboard.KeyCode(char='j')),
#                              (keyboard.Key.shift, keyboard.Key.cmd, keyboard.KeyCode(char='h'))]
#
#     for comb in excluded_combinations:
#         if all((key in key_states and key_states[key] for key in comb)):
#             return
#
#     for comb, sound_name in key_to_sound.items():
#         if all((key in key_states and key_states[key] for key in comb)) and sound_name in super_sounds:
#             super_sounds[sound_name].play()
#             return
#
#     if not any((key in key_states and key_states[key] for key in excluded_keys)):
#         sound = random.choice(list(normal_sounds.values()))
#         sound.play()
#
# key_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# mouse_listener = mouse.Listener(on_click=on_click)
#
# key_listener.start()
# mouse_listener.start()
#
# key_listener.join()
# mouse_listener.join()


