This repo will contain a list of useful resources for Mongolian NLP. Feel free to contribute.


## Datasets
* ****`DATASET`**** LJSpeech like male voice TTS [dataset](datasets/MBSpeech-1.0-csv.zip) created from the Mongolian Bible
  * used in [tugstugi/pytorch-dc-tts](https://github.com/tugstugi/pytorch-dc-tts)
  * use [dl_and_preprop_dataset.py](https://github.com/tugstugi/pytorch-dc-tts/blob/master/dl_and_preprop_dataset.py) to download the audio files
* ****`DATASET`**** LJSpeech like Kalmyk (West Mongolian) female voice TTS [dataset](https://drive.google.com/uc?id=12JbPAwNeH-qRD1Lz1JfY6Rc2jetPddbG) created from the Kalmyk Bible (2 hours)
* ****`DATASET`**** 300 hours [Kalmyk synthetic STT dataset](https://www.dropbox.com/s/thog6q63w53ub99/kalmyk_synthetic_stt_dataset_v2.tar.gz) created by a voice conversion model
  * each WAV has a different text created from Kalmyk books
  * source voice is the Kalmyk Bible female TTS
  * target voices are from the VCTK dataset
  * an example WAV: https://twitter.com/tugstugi/status/1409111296897912835
* ****`DATASET`**** [Eduge news classification dataset](datasets/eduge.csv.gz) provided by [Bolorsoft LLC](https://bolorsoft.com/)
  * used to train the [Eduge.mn](http://eduge.mn/) production news classifier
  * 75K news with 9 categories: `урлаг соёл`, `эдийн засаг`, `эрүүл мэнд`, `хууль`, `улс төр`,
`спорт`, `технологи`, `боловсрол` and `байгал орчин`
* ****`DATASET`**** [11-11.mn government agency complaint dataset](https://www.kaggle.com/enqush/mongolian-government-agency-1111mn-dataset/home)
  * 80K with 5 categories: `санал хүсэлт`, `гомдол`, `шүүмжлэл`, `талархал` and `өргөдөл`
* ****`DATASET`**** [online news corpus](https://yadi.sk/d/z5e3MVnKvFvF6w?fbclid=IwAR2wRJ4fRRMSDI8rhbNLdU2n_RiK08hU2rKwXwI7rc6JN2YNTeTna8xOOlg)
  * 700 million words
* ****`DATASET`**** [Digital Archive of Mongolian Newspapers 1990-1995](https://eap.bl.uk/collection/EAP010-1?f%5B0%5D=ss_simplified_type%3AFile) of the British Library
* [Common Crawl Mongolian dataset](http://data.statmt.org/cc-100/)
* [opendata.burtgel.gov.mn](http://opendata.burtgel.gov.mn)
  * ****`DATASET`**** [220K Mongolian personal names](datasets/mongolian_personal_names.csv.gz)
  * ****`DATASET`**** [90K Mongolian clan/family names](datasets/mongolian_clan_names.csv.gz)
  * ****`DATASET`**** [192K Mongolian company names](datasets/mongolian_company_names.csv.gz)
* ****`DATASET`**** [Mongolian provinces (aimags and sums) names](datasets/districts.csv)
* ****`DATASET`**** [195 country (with capital cities) names in Mongolian](datasets/countries.csv)
* ****`DATASET`**** [250 Mongolian most frequent words](datasets/most_frequent_words.csv) from Mongolian news, books and Wikipedia articles. (total 670M words / 2M unique words).
  * These words could be used also as the stop words.
* ****`DATASET`**** [500 Mongolian abbreviations](datasets/mongolian_abbreviations.csv)
* ****`DATASET`**** [Mongolian NER dataset](datasets/NER_v1.0.json.gz) created from Mongolian politics and sport news
  * 10K sentences annotated by [tugstugi](https://github.com/tugstugi) and [enod](https://github.com/enod) using [doccano](https://github.com/chakki-works/doccano)
  * 4 categories `LOCATION` (6453/1753), `PERSON` (2839/1698), `ORGANIZATION` (4453/1970) and `MISC` (3716/2617)
* ****`DATASET`**** [Mongolian POS dataset](http://www.panl10n.net/center-for-research-on-language-processing-crlp-national-university-of-mongolia-mongolia/) of the Mongolian National University
  * 100k words
  * used [POS tagsets](https://www.aclweb.org/anthology/W09-3415)
* ****`DATASET`**** [Traditional Mongolian synthetic OCR dataset](https://drive.google.com/file/d/1s9t22tRI22uolUv1bv023xj-x68gu1dp) created from Mongolian song lyrics and dictionary
  * 80K images
  * without any data augmentation, for augmenting data use external libraries like [albumentations](https://github.com/albu/albumentations).
* ****`DATASET`**** [Handwritten Mongolian Cyrillic Characters Database](https://www.kaggle.com/vimpigro/handwritten-mongolian-cyrillic-characters-database/version/1) of the Mongolian University of Science and Technology
  * 28x28 gray scale, 350k images
  * [dataset description](https://www.studocu.com/en/document/mongolian-university-of-science-and-technology/information-technology/other/hmcc-with-erdenechimeg/5451932/view)
* ****`DATASET`**** [Mongolian Wordnet](https://github.com/kbatsuren/monwn) of the Mongolian National University
  * 26875 words, 2979 glosses, 23665 synsets, 213 examples
* ****`DATASET`**** [Multilingual Spoken Words](https://mlcommons.org/en/multilingual-spoken-words/) multilingual keyword spotting dataset
  * 2200 Mongolian keywords, 44000 audio files
  * example keywords: `аав`, `байна`, `бэлдэж`, `дүрслэх`, `ламын`, `олов`, `сонирхож`, `түүний`, `хаанаас`, `хуулиар`, `чиглэсэн`

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
  * [female voice samples](http://nhrcm.gov.mn/%D0%BC%D1%8D%D0%B4%D1%8D%D1%8D/%D0%BD%D2%AF%D0%B1-%D1%8B%D0%BD-%D1%85%D2%AF%D0%BD%D0%B8%D0%B9-%D1%8D%D1%80%D1%85%D0%B8%D0%B9%D0%BD-%D0%BE%D0%BB%D0%BE%D0%BD-%D1%83%D0%BB%D1%81%D1%8B%D0%BD-%D1%81%D1%83%D1%83%D1%80%D1%8C-%D0%B3%D1%8D%D1%80%D1%8D%D1%8D/)
* ****`SAMPLES`**** Tacotron2 [TTS demo samples](https://ikon.mn/n/1j9a) of Ikon.MN
  * 1x female (35h)
  * [NVIDIA/tacotron2](https://github.com/NVIDIA/tacotron2/) + [NVIDIA/waveglow](https://github.com/NVIDIA/waveglow)
* ****`DEMO`**** [HMM based TTS online demo](http://mtts.mglip.com/) of the Inner Mongolian university
  * 1x female
* ****`DEMO`**** MTL-Tacotron [TTS demo samples](https://ttslr.github.io/SPL2020/) of the Inner Mongolian university & National University of Singapore
  * 1x female
* ****`TF`**** [ttslr/MonTTS](https://github.com/ttslr/MonTTS) Inner Mongolian TTS training code
  * ****`SAMPLES`**** [Speech samples](https://github.com/ttslr/MonTTS/tree/main/prediction/mon_inference_fastspeech2)
  * ****`DATASET SAMPLES`**** [MonSpeech](https://github.com/ttslr/MonTTS/tree/main/MonSpeech-samples) of the Inner Mongolia University
  * dataset and pretrained models are not available
* ****`PRODUCT`**** [NVDA/HTS screen reader](https://www.idc-mn.info/english.php) developed by Innovation Development Center for the blind
  * 1x female (Mongolian National University voice)
* ****`PYTORCH/DEMO`**** [Kalmyk TTS demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/misc/Kalmyk_NVidia_Tacotron2_Waveglow.ipynb) Kalmyk is a Mongolic language spoken in Russia
  * [dataset](https://drive.google.com/uc?id=12JbPAwNeH-qRD1Lz1JfY6Rc2jetPddbG) created from the Kalmyk Bible (2 hours)
  * [NVIDIA/tacotron2](https://github.com/NVIDIA/tacotron2/) + [NVIDIA/waveglow](https://github.com/NVIDIA/waveglow)
* ****`PYTORCH/DEMO`**** [Kalmyk TTS demo from Silero](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/misc/SileroKalmykTTS.ipynb) Kalmyk is a Mongolic language spoken in Russia
  * [snakers4/silero-models](https://github.com/snakers4/silero-models)

## Mongolian Language Model
* ***`MODEL`*** [5-gram binary LM](https://drive.google.com/open?id=1XsNNdLDpJ75GBpw1FAUqZXyqwsb4919x) generated by KenLM on a 670M word ***dirty*** corpus.
  * it can be used either with [mozilla/DeepSpeech](https://github.com/mozilla/DeepSpeech): `./generate_trie alphabet.txt mn_5gram.binary trie`
  * or in [tugstugi/mongolian-speech-recognition](https://github.com/tugstugi/mongolian-speech-recognition)
* ***`TF`*** / ***`PYTORCH`*** [tugstugi/mongolian-bert](https://github.com/tugstugi/mongolian-bert) pretrained Mongolian [BERT](https://arxiv.org/abs/1810.04805) models
  * trained by [tugstugi](https://github.com/tugstugi), [enod](https://github.com/enod) and [sharavsambuu](https://github.com/sharavsambuu)
  * [nabar](https://github.com/nabar) sponsored 5x TPUs.
* ***`PYTORCH`*** [bayartsogt-ya/albert-mongolian](https://github.com/bayartsogt-ya/albert-mongolian) pretrained Mongolian [ALBERT](https://arxiv.org/abs/1909.11942)
* ***`PYTORCH`*** [robertritz/NLP](https://github.com/robertritz/NLP) ULMFiT experiments
* ***`PYTORCH`*** [huggingface.co/bayartsogt/mongolian-gpt2](https://huggingface.co/bayartsogt/mongolian-gpt2) Mongolian GPT-2 model
* ***`PYTORCH`*** [huggingface.co/bayartsogt/mongolian-roberta-base](https://huggingface.co/bayartsogt/mongolian-roberta-base) Mongolian Roberta base model

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
* ****`PRODUCT`**** [Huawei cloud ASR](https://www.huaweicloud.com/en-us/product/rasr.html) supports minority languages such as Mongolian, Tibetan, and Uyghur.
* ****`PRODUCT`**** [Google Cloud Speech-to-text](https://cloud.google.com/speech-to-text/docs/languages)
  * 20% WER on a 3000 audio private test dataset
* ****`PYTORCH`**** [Wav2Vec2 XLSR](https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/) finetuned on Mongolian Common Voice
  * ****`DEMO`**** [Colab online demo](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/misc/Wav2Vec2_XLSR_Mongolian.ipynb)
  * 50% WER
* ****`PYTORCH`**** [Wav2Vec2 XLSR](https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/) trained on Kalmyk dataset
  * pretrained on 500 hours Kalmyk TV recordings and 1000 hours Mongolian speech recognition dataset
  * finetuned on 300 hours synthetic Kalmyk STT dataset created by voice conversion
  * 50% WER on a private test set created from Kalmyk TV recordnings, on clean voice recordings, it should have much lower WER
  * ****`DEMO`**** [https://huggingface.co/tugstugi/wav2vec2-large-xlsr-53-kalmyk](https://huggingface.co/tugstugi/wav2vec2-large-xlsr-53-kalmyk)
* ****`TF`**** [coqui.ai mongolian speech recognition](https://coqui.ai/mongolian/itml/v0.1.1) trained on Mongolian CommonVoice
  * 90.08% WER

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
* ****`DATASET`**** 1M back-translated MN->EN sentence dataset [download link](https://drive.google.com/file/d/14AtTVgibirSdHYTBFM9G1XPS7DvM5SdE/view)
  * [sharavsambuu/english-mongolian-nmt-dataset-augmentation](https://github.com/sharavsambuu/english-mongolian-nmt-dataset-augmentation)
* ****`DICTIONARY`**** [Mongolian digitalized dictionaries](http://hkuri.cneas.tohoku.ac.jp/project1/ftsdata/list?groupId=14) from Center for Northeast Asian of the Tohoku University in Japan
  * for usage see [Digitizing the Mongolian Language: An Introduction to the Polyglot “Online Dictionaries and Full-text Search of Mongolian Languages and Written Manchu”](https://digitalorientalist.com/2020/10/02/digitizing-the-mongolian-language-an-introduction-to-the-polyglot-online-dictionaries-and-full-text-search-of-mongolian-languages-and-written-manchu/)
  * it includes also IPA pronuncations for Mongolian words
