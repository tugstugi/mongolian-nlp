This repo will contain a list of useful resources for Mongolian NLP and also my own experiments mostly with PyTorch.


## Datasets
* LJSpeech like male voice TTS [dataset](https://www.dropbox.com/s/dafueq0w278lbz6/mbspeech-csv.zip?dl=1) created from the Mongolian Bible
  * used in [pytorch-dc-tts](https://github.com/tugstugi/pytorch-dc-tts)
  * use [dl_and_preprop_dataset.py](https://github.com/tugstugi/pytorch-dc-tts/blob/master/dl_and_preprop_dataset.py) to download the audio files
* [Eduge news classification dataset](https://www.dropbox.com/s/h5bindkdhn1e6ud/news.csv.gz?dl=0)
  * used to train the [Eduge.mn](http://eduge.mn/) production news classifier
  * 75K news with 9 categories: `урлаг соёл`, `эдийн засаг`, `эрүүл мэнд`, `хууль`, `улс төр`,
`спорт`, `технологи`, `боловсрол` and `байгал орчин`
* [11-11.mn government agency complaint dataset](https://www.kaggle.com/enqush/mongolian-government-agency-1111mn-dataset/home)
  * 80K with 5 categories: `санал хүсэлт`, `гомдол`, `шүүмжлэл`, `талархал` and `өргөдөл`

## Mongolian TTS
* [TTS online demo of the Mongolian National University](http://172.104.34.197/nlp-web-demo/)
  * **only demo** no open source
  * 1x male and 2x female voices
  * HMM
* [pytorch-dc-tts](https://github.com/tugstugi/pytorch-dc-tts)
  * [Colab online demo](https://colab.research.google.com/github/tugstugi/pytorch-dc-tts/blob/master/notebooks/MongolianTTS.ipynb)
  * PyTorch
  * LJSpeech like male voice [dataset](https://www.dropbox.com/s/dafueq0w278lbz6/mbspeech-csv.zip?dl=1) created from the Mongolian Bible
  
## Mongolian Speech Recognition
* [Letter-Based Speech Recognition with Gated ConvNets](https://github.com/tugstugi/mongolian-speech-recognition)
  * single voice demo
  * PyTorch
  
## Mongolian Script
* [Cyrillic to Mongolian script converter demo](http://trans.mglip.com/EnglishC2T.aspx) of the Inner Mongolian university
  * **only demo** no open source
* [Mongolian script to (and back) cyrillic converter](bichig2cyrillic/)
  * PyTorch
* Mongolian script OCR
  * PyTorch, to be released
