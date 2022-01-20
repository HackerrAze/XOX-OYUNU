#!/bin/bash
clear
cd ..
rm -rf XOX-OYUNU
rm -rf GENELTOOLS
git clone https://github.com/HackerrAze/XOX-OYUNU
chmod +x XOXoyunu.py
rm -rf geneltools.sh
python XOXoyunu.py