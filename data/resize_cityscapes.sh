#!/bin/bash
# Author: Grace Han
# In place resampling to 512 x 1024 px
# Requires imagemagick on a *nix system
# Modify according to your directory structure

# for f in ./**/*.png; do
# for f in ~/datasets/leftImg8bit/val/**/*.png; do
for f in ~/datasets/leftImg8bit_small/val/**/*.png; do
    convert $f -resize 256x128 $f
done
