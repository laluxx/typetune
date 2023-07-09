#!/bin/bash

# This project use the same sructure as osu skins,
# so any osu skin can be converted to a typetune theme,
# this is meant to be used on linux, 
# osu installed trough lutris,

# this is a builtin command inside xos

destination_directory_base="$HOME/xos/typetune/switches"
file_types=("ogg" "wav")

ls $HOME/.local/share/osu-stable/Skins | fzf -m | while IFS= read -r theme_name; do
    if [ -z "$theme_name" ]
    then
        echo "No themes chosen"
        exit 1
    fi

    destination_directory="$destination_directory_base/$theme_name"
    mkdir -p "$destination_directory"

    for file_type in "${file_types[@]}"; do
        cp -iv "$HOME/.local/share/osu-stable/Skins/$theme_name/key-delete.${file_type}" \
               "$HOME/.local/share/osu-stable/Skins/$theme_name/key-press-1.${file_type}" \
               "$HOME/.local/share/osu-stable/Skins/$theme_name/key-press-2.${file_type}" \
               "$HOME/.local/share/osu-stable/Skins/$theme_name/key-press-3.${file_type}" \
               "$HOME/.local/share/osu-stable/Skins/$theme_name/key-press-4.${file_type}" \
               "$HOME/.local/share/osu-stable/Skins/$theme_name/key-press.${file_type}" \
               "$destination_directory" 2>/dev/null
    done
done
