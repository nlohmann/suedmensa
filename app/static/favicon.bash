#!/bin/bash
# Favicon and Apple Touch Icon Generator.
# Copyright 2012 @emarref
# Copyright 2012 Tom Vincent <http://tlvince.com/contact>	
# From: https://gist.github.com/3374193
#
# This bash script takes an image as a parameter, and uses ImageMagick to
# convert it to several other formats used on modern websites. The following
# copies are generated:
# 
# * apple-touch-icon-114x114-precomposed.png
# * apple-touch-icon-57x57-precomposed.png
# * apple-touch-icon-72x72-precomposed.png
# * apple-touch-icon-precomposed.png
# * apple-touch-icon.png
# * favicon.ico
#
# Concept from
# http://bergamini.org/computers/creating-favicon.ico-icon-files-with-imagemagick-convert.html

info() { echo "$0: $1"; }
error() { info "$1" >&2 && exit 1; }
have() { which "$1" >/dev/null 2>&1; }
usage() { echo "usage: $0 src_image [dest_dir]"; exit 1; }

[ $1 ] || usage
have convert || error "ImageMagick not found"

tmp="$(mktemp -d favicon.XXX)"

info "Generating square base image"
convert "$1" -flatten -resize 256x256! -transparent white "$tmp/favicon-256.png"
[ -f "$tmp/favicon-256.png" ] || error "Generating square base image failed"

info "Generating ico"
convert "$tmp/favicon-256.png" -resize 16x16 "$tmp/favicon-16.png"
convert "$tmp/favicon-16.png" -colors 256 "$tmp/favicon.ico"

info "Generating touch icons"
convert "$tmp/favicon-256.png" -resize 57x57 "$tmp/apple-touch-icon.png"
cp "$tmp/apple-touch-icon.png" "$tmp/apple-touch-icon-precomposed.png"
cp "$tmp/apple-touch-icon.png" "$tmp/apple-touch-icon-57x57-precomposed.png"
convert "$tmp/favicon-256.png" -resize 72x72 "$tmp/apple-touch-icon-72x72-precomposed.png"
convert "$tmp/favicon-256.png" -resize 114x114 "$tmp/apple-touch-icon-114x114-precomposed.png"
convert "$tmp/favicon-256.png" -resize 120x120 "$tmp/apple-touch-icon-120x120-precomposed.png"
convert "$tmp/favicon-256.png" -resize 144x144 "$tmp/apple-touch-icon-144x144-precomposed.png"

info "Removing temp files"
rm "$tmp/favicon-16.png"

[ "$2" ] && { mkdir -p "$2"; mv $tmp/* "$2"; rm -rf "$tmp"; } || info "$tmp"
