Given an audio file containing speech, and the corresponding transcript, computing a forced alignment is
the process of determining, for each fragment of the transcript, the time interval (in the audio file)
containing the spoken text of the fragment.

Typical applications of forced alignment include closed captioning and automating the creation of training data
for **automated speech recognition** and **text-to-speech** systems.

For more information about forced alignment tools,
see [pettarin/forced-alignment-tools](https://github.com/pettarin/forced-alignment-tools)

Currently, there is no Mongolian forced aligner tool. This is the first attempt to implement a forced aligner
for the Mongolian language using [Rayhane-mamah/Tacotron-2](https://github.com/Rayhane-mamah/Tacotron-2)
and [readbeyond/aeneas](https://github.com/readbeyond/aeneas).

For a Colab live demo, visit
[Forced_Aligner.ipynb](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/forced_aligner/Forced_Aligner.ipynb)


## Setup

```sh
# install aeneas
sudo apt-get install libespeak-dev
pip install https://codeload.github.com/readbeyond/aeneas/zip/devel

# install Tacotron2 text-to-speech with a pretrained model
./prepare-tts.sh
```

## Forced Alignment
To make a forced alignment for the given audio file [battulga.mp3](battulga.mp3) and
the transcription file [battulga.txt](battulga.txt), execute the following command:
```sh
# change to the forced aligner folder
cd mongolian-nlp/forced_aligner
# do forced alignment
python -m aeneas.tools.execute_task -r="tts=custom|tts_path=./aeneas-helper.py" \
    battulga.mp3 battulga.txt \
    "task_language=mon|os_task_file_format=json|is_text_type=plain" \
    result.json
```

The result will be written into the file **result.json**. To interpret the result,
either visit [readbeyond/aeneas](https://github.com/readbeyond/aeneas) or
try out the [Colab live demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/forced_aligner/Forced_Aligner.ipynb).
