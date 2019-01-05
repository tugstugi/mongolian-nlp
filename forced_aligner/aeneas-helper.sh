#!/usr/bin/env bash

# read single line from stdin
read -r line
echo "synthesizing into '$1': $line"

# change to the Tacotron2 folder
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
pushd $dir/Tacotron-2

# synthesize
python3 ./simple-synthesize.py --text_list "$line"

# move the WAV to the wanted path
cp tacotron_output/logs-eval/wavs/wav-batch_0_sentence_0-linear.wav 1.wav
popd
mv $dir/Tacotron-2/tacotron_output/logs-eval/wavs/wav-batch_0_sentence_0-linear.wav $1
