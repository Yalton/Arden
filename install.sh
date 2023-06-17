#!/bin/bash 
echo "###################################"
echo "Installing required system packages"
echo "###################################"

sudo apt install -y portaudio19-dev \
espeak \
mpg123 \
libasound2-dev \
flac \
at

echo "###################################"
echo "Installing required python packages"
echo "###################################"
python3 -m pip install -r requirements.txt
python3 -m spacy download en_core_web_sm