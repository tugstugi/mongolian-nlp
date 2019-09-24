This repo will contain a list of useful resources for Mongolian NLP. Feel free to contribute.


## Datasets
* ****`DATASET`**** LJSpeech like male voice TTS [dataset](datasets/MBSpeech-1.0-csv.zip) created from the Mongolian Bible
  * used in [tugstugi/pytorch-dc-tts](https://github.com/tugstugi/pytorch-dc-tts)
  * use [dl_and_preprop_dataset.py](https://github.com/tugstugi/pytorch-dc-tts/blob/master/dl_and_preprop_dataset.py) to download the audio files
* ****`DATASET`**** [Eduge news classification dataset](datasets/eduge.csv.gz) provided by [Bolorsoft LLC](https://bolorsoft.com/)
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
  * ****`DATASET`**** [192K Mongolian company names](datasets/mongolian_company_names.csv.gz)
* ****`DATASET`**** [250 Mongolian most frequent words](datasets/most_frequent_words.csv) from Mongolian news, books and Wikipedia articles. (total 670M words / 2M unique words).
  * These words could be used also as the stop words.
* ****`DATASET`**** [500 Mongolian abbreviations](datasets/mongolian_abbreviations.csv)
* ****`DATASET`**** [Mongolian NER dataset](datasets/NER_v1.0.json.gz) created from Mongolian politics and sport news
  * 10K sentences annotated by [tugstugi](https://github.com/tugstugi) and [enod](https://github.com/enod) using [doccano](https://github.com/chakki-works/doccano)
  * 4 categories `LOCATION` (6453/1753), `PERSON` (2839/1698), `ORGANIZATION` (4453/1970) and `MISC` (3716/2617)
* ****`DATASET`**** [Mongolian POS dataset](http://www.panl10n.net/center-for-research-on-language-processing-crlp-national-university-of-mongolia-mongolia/) of the Mongolian National University
  * 100k words
* ****`DATASET`**** [Traditional Mongolian synthetic OCR dataset](https://drive.google.com/file/d/1s9t22tRI22uolUv1bv023xj-x68gu1dp) created from Mongolian song lyrics and dictionary
  * 80K images
  * without any data augmentation, for augmenting data use external libraries like [albumentations](https://github.com/albu/albumentations).
* ****`DATASET`**** [Handwritten Mongolian Cyrillic Characters Database](https://www.kaggle.com/vimpigro/handwritten-mongolian-cyrillic-characters-database/version/1) of the Mongolian University of Science and Technology
  * 28x28 gray scale, 350k images
  * [dataset description](https://www.studocu.com/en/document/mongolian-university-of-science-and-technology/information-technology/other/hmcc-with-erdenechimeg/5451932/view)

## Mongolian Text-to-Speech
* ****`PYTORCH`**** [tugstugi/pytorch-dc-tts](https://github.com/tugstugi/pytorch-dc-tts)
  * ****`DEMO`**** [Colab online demo](https://colab.research.google.com/github/tugstugi/pytorch-dc-tts/blob/master/notebooks/MongolianTTS.ipynb)
  * ****`DATASET`**** LJSpeech like male voice [dataset](datasets/MBSpeech-1.0-csv.zip) created from the Mongolian Bible
* ****`TF`**** [tugstugi/Tacotron-2](https://github.com/tugstugi/Tacotron-2) fork of [Rayhane-mamah/Tacotron-2](https://github.com/Rayhane-mamah/Tacotron-2) adapted for
the Mongolian Bible dataset
  * ****`DEMO`**** [Colab online demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/misc/Tacotron_MongolianTTS.ipynb)
  * ****`DEMO`**** [speaker adaptation Colab online demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/misc/Tacotron_MongolianTTS_Elbegdorj.ipynb) for the former Mongolian president Elbegdorj. The Tacotron model trained with the 5 hours Mongolian Bible dataset was fine tuned with a 10 minutes dataset created from a Elbegdorj's speech.
* ****`PYTORCH`**** [Chimege TTS demo](https://chimege.mn/tts)
  * 1x female
  * [NVIDIA/tacotron2](https://github.com/NVIDIA/tacotron2/) + [NVIDIA/waveglow](https://github.com/NVIDIA/waveglow)
* ****`DEMO`**** HMM [TTS online demo of the Mongolian National University](http://172.104.34.197/nlp-web-demo/)
  * 1x male and 2x female voices
* ****`DEMO`**** ~~Yet another HMM? [TTS online demo](http://178.128.108.243/tts/) from “Мон Спийч Ай Ти” ХХК~~
  * demo server is currently down
  * 1x male and 1x female
* ****`SAMPLES`**** Tacotron2 [TTS demo samples](https://ikon.mn/n/1j9a) of Ikon.MN
  * 1x female (35h)
* ****`DEMO`**** [HMM based TTS online demo](http://mtts.mglip.com/) of the Inner Mongolian university
  * 1x female
* ****`PRODUCT`**** [NVDA/HTS screen reader](https://www.idc-mn.info/english.php) developed by Innovation Development Center for the blind
  * 1x female (Mongolian National University voice)

## Mongolian Language Model
* ***`MODEL`*** [5-gram binary LM](https://drive.google.com/open?id=1XsNNdLDpJ75GBpw1FAUqZXyqwsb4919x) generated by KenLM on a 670M word ***dirty*** corpus.
  * it can be used either with [mozilla/DeepSpeech](https://github.com/mozilla/DeepSpeech): `./generate_trie alphabet.txt mn_5gram.binary trie`
  * or in [tugstugi/mongolian-speech-recognition](https://github.com/tugstugi/mongolian-speech-recognition)
* ***`TF`*** / ***`PYTORCH`*** [tugstugi/mongolian-bert](https://github.com/tugstugi/mongolian-bert) pretrained Mongolian [BERT](https://arxiv.org/abs/1810.04805) models
  * trained by [tugstugi](https://github.com/tugstugi), [enod](https://github.com/enod) and [sharavsambuu](https://github.com/sharavsambuu)
  * [nabar](https://github.com/nabar) sponsored 5x TPUs.

## Mongolian Speech Recognition
* ****`PYTORCH`**** [tugstugi/mongolian-speech-recognition](https://github.com/tugstugi/mongolian-speech-recognition)
  * ****`DEMO`**** [Chimege Speech Recognition](https://chimege.mn/stt)
  * a proprietary dataset is used
* ****`PRODUCT`**** Chinese and [traditional Mongolian voice input](https://www.aicloud.com/home/product/subpage?key=znsr) from [aicloud.com](https://www.aicloud.com)
  * direct [link](https://hci-app.oss-cn-beijing.aliyuncs.com/aicloud_input/HciCloudInputAndroid.apk) to the APK file
  * seems to be working only for simple cases (or it works only for Southern Mongolian dialects...)
  * same system but for [windows](http://index.mzywfy.org.cn:48080/fanyiju/download.jsp) (according to someone, you have to register with a Chinese identity card to use it)
* ****`DEMO`**** ~~[Speech recognition](http://asr.mglip.com) of the Inner Mongolian university~~
  * seems to be non functional

## Mongolian Script
* ****`DEMO`**** [Cyrillic to Mongolian script converter demo](http://trans.mglip.com/EnglishC2T.aspx) of the Inner Mongolian university
* ****`DEMO`**** [Mongolian script OCR demo](http://ocr.mglip.com/OcrDemo) of the Inner Mongolian university
* ****`PYTORCH`**** [tugstugi/bichig2cyrillic](bichig2cyrillic/) Mongolian script to (and back) cyrillic converter
  * ****`DEMO`**** [Cyrillic to Mongolian Colab online demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/bichig2cyrillic/notebooks/Cyrillic2Bichig.ipynb)
* ****`PYTORCH`**** [tugstugi/image2bichig](image2bichig/) Traditional Mongolian OCR using CRNN
  * ****`DEMO`**** [OCR Colab online demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/misc/MongolianScriptOCR.ipynb)
  * ****`DATASET`**** [Traditional Mongolian synthetic OCR dataset](https://drive.google.com/file/d/1s9t22tRI22uolUv1bv023xj-x68gu1dp)

## Mongolian Text Classification
* ****`TF2`**** [sharavsambuu/mongolian-text-classification](https://github.com/sharavsambuu/mongolian-text-classification)
* ****`SKLEARN`**** / ****`DEMO`**** simple [SVM Colab notebook](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/misc/Eduge_SVM.ipynb) classifying the Eduge dataset with around 91% accuracy.
  * SentencePiece model from [tugstugi/mongolian-bert](https://github.com/tugstugi/mongolian-bert) is used as the text tokenizer.


## Mongolian Named Entity Recognition
* ****`DATASET`**** [Mongolian NER dataset](datasets/NER_v1.0.json.gz) created from Mongolian politics and sport news
  * for more info see [datasets](https://github.com/tugstugi/mongolian-nlp#datasets)
* ****`PYTORCH`**** [enod/mongolian-bert-ner](https://github.com/enod/mongolian-bert-ner) BERT based Mongolian NER
  * uses [tugstugi/mongolian-bert](https://github.com/tugstugi/mongolian-bert) Mongolian pre-trained BERT models
* ****`DEMO`**** [NER demo of the Mongolian National University](http://172.104.34.197/nlp-web-demo/)

## Misc
* ****`PYTORCH`**** [tugstugi/forced_aligner](forced_aligner/) Mongolian forced alignment tool using [Rayhane-mamah/Tacotron-2](https://github.com/Rayhane-mamah/Tacotron-2)
and [readbeyond/aeneas](https://github.com/readbeyond/aeneas)
  * ****`DEMO`**** [Colab online demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/forced_aligner/Forced_Aligner.ipynb)
* ****`TF2`**** cyrillic transliteration Colab notebook [sharavsambuu/cyrillic-mongolian-transliteration](https://colab.research.google.com/drive/10Eq_VvR84oEOBUK5EflvAB35ZcrlQwGm)
