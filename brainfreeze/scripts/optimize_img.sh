#!/bin/sh
gm convert $1 -resize "600x" -unsharp 2x0.5+0.7+0 -quality 98 $2

