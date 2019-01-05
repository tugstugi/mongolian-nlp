#!/usr/bin/env bash

if [ ! -d Tacotron-2 ]; then
    echo "Tacotron-2 doesn't exist, cloning it...!"
    git clone https://github.com/tugstugi/Tacotron-2.git
    echo "installing its dependencies..."
    pip install -r Tacotron-2/requirements.txt
fi

if [ ! -d Tacotron-2/logs-Tacotron/taco_pretrained ]; then
    echo "Tacotron-2 pretrained model doesn't exist, downloading it...!"
    fileid="1fgx0kpf0Oe2Idz3lUZM6-p343nc-24Hq"
    filename="taco_pretrained.tar.gz"
    curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
    curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
    mkdir Tacotron-2/logs-Tacotron/
    tar xvfz $filename --directory Tacotron-2/logs-Tacotron/
fi
