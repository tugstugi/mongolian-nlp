This repo will contain a list of useful resources for Mongolian NLP. Feel free to contribute.


## Datasets
* ****`DATASET`**** LJSpeech like male voice TTS [dataset](datasets/MBSpeech-1.0-csv.zip) created from the Mongolian Bible
  * used in [tugstugi/pytorch-dc-tts](https://github.com/tugstugi/pytorch-dc-tts)
  * use [dl_and_preprop_dataset.py](https://github.com/tugstugi/pytorch-dc-tts/blob/master/dl_and_preprop_dataset.py) to download the audio files
* ****`DATASET`**** [Eduge news classification dataset](datasets/eduge.csv.gz)
  * used to train the [Eduge.mn](http://eduge.mn/) production news classifier
  * 75K news with 9 categories: `урлаг соёл`, `эдийн засаг`, `эрүүл мэнд`, `хууль`, `улс төр`,
`спорт`, `технологи`, `боловсрол` and `байгал орчин`
* ****`DATASET`**** [11-11.mn government agency complaint dataset](https://www.kaggle.com/enqush/mongolian-government-agency-1111mn-dataset/home)
  * 80K with 5 categories: `санал хүсэлт`, `гомдол`, `шүүмжлэл`, `талархал` and `өргөдөл`
* ****`DATASET`**** [online news corpus](https://yadi.sk/d/z5e3MVnKvFvF6w?fbclid=IwAR2wRJ4fRRMSDI8rhbNLdU2n_RiK08hU2rKwXwI7rc6JN2YNTeTna8xOOlg)
  * 700 million words
* [opendata.burtgel.gov.mn](http://opendata.burtgel.gov.mn)
  * ****`DATASET`**** [220K Mongolian personal names](datasets/mongolian_personal_names.csv.gz)
  * ****`DATASET`**** [90K Mongolian clan/family names](datasets/mongolian_clan_names.csv.gz)
  * ****`DATASET`**** [180K Mongolian company names](datasets/mongolian_company_names.csv.gz)

## Mongolian TTS
* ****`PYTORCH`**** [tugstugi/pytorch-dc-tts](https://github.com/tugstugi/pytorch-dc-tts)
  * ****`DEMO`**** [Colab online demo](https://colab.research.google.com/github/tugstugi/pytorch-dc-tts/blob/master/notebooks/MongolianTTS.ipynb)
  * ****`DATASET`**** LJSpeech like male voice [dataset](datasets/MBSpeech-1.0-csv.zip) created from the Mongolian Bible
* ****`TF`**** [tugstugi/Tacotron-2](https://github.com/tugstugi/Tacotron-2) fork of [Rayhane-mamah/Tacotron-2](https://github.com/Rayhane-mamah/Tacotron-2) adapted for
the Mongolian Bible dataset
  * ****`DEMO`**** [Colab online demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/misc/Tacotron_MongolianTTS.ipynb)
  * ****`DEMO`**** [speaker adaptation Colab online demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/misc/Tacotron_MongolianTTS_Elbegdorj.ipynb) for the former Mongolian president Elbegdorj. The Tacotron model trained with the 5 hours Mongolian Bible dataset was fine tuned with a 10 minutes dataset created from a Elbegdorj's speech.
* ****`DEMO`**** HMM [TTS online demo of the Mongolian National University](http://172.104.34.197/nlp-web-demo/)
  * 1x male and 2x female voices
* ****`DEMO`**** Yet another HMM? [TTS online demo](http://178.128.108.243/tts/) from “Мон Спийч Ай Ти” ХХК
  * 1x male and 1x female
* ****`DEMO`**** [Tacotron2? based TTS online demo](http://mtts.mglip.com/) of the Inner Mongolian university
  * 1x female
* ****`PRODUCT`**** [NVDA/HTS screen reader](https://www.idc-mn.info/english.php) developed by Innovation Development Center for the blind
  * 1x female (Mongolian National University voice?)

## Mongolian Speech Recognition
* ****`PYTORCH`**** [tugstugi/mongolian-speech-recognition](https://github.com/tugstugi/mongolian-speech-recognition)
  * single voice demo
  
## Mongolian Script
* ****`DEMO`**** [Cyrillic to Mongolian script converter demo](http://trans.mglip.com/EnglishC2T.aspx) of the Inner Mongolian university
* ****`DEMO`**** [Mongolian script OCR demo](http://ocr.mglip.com/OcrDemo) of the Inner Mongolian university
* ****`PYTORCH`**** [tugstugi/bichig2cyrillic](bichig2cyrillic/) Mongolian script to (and back) cyrillic converter
  * ****`DEMO`**** [Cyrillic to Mongolian Colab online demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/bichig2cyrillic/notebooks/Cyrillic2Bichig.ipynb)
* ****`PYTORCH`**** Mongolian script OCR to be released

## Mongolian Text Classification
* ****`TF`**** [sharavsambuu/mongolian-text-classification](https://github.com/sharavsambuu/mongolian-text-classification)

## Misc
* ****`PYTORCH`**** [tugstugi/forced_aligner](forced_aligner/) Mongolian forced alignment tool using [Rayhane-mamah/Tacotron-2](https://github.com/Rayhane-mamah/Tacotron-2)
and [readbeyond/aeneas](https://github.com/readbeyond/aeneas) 
  * ****`DEMO`**** [Colab online demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/forced_aligner/Forced_Aligner.ipynb)
