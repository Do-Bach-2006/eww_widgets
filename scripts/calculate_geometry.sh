#!/bin/bash

# Get screen dimensions
screen_width=$(xrandr | grep '*' | awk '{print $1}' | awk -Fx '{print $1}')
screen_height=$(xrandr | grep '*' | awk '{print $1}' | awk -Fx '{print $2}')

# json type for the eww to read
echo {"x":"${screen_width}" , "y":"${screen_height}"}
