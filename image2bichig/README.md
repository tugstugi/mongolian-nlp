## Mongolian Script OCR

### Synthetic Dataset
For generating a synthetic data set from Mongolian song lyrics and dictionary, first install
all fonts from [fonts](fonts). After that, execute the following commands:
```
mkdir images
./generate_from_dictionary.py > synthetic.csv
./generate_from_lyrics.py >> synthetic.csv
```

You can also download an already generated synthetic data set from
[here](https://drive.google.com/file/d/1s9t22tRI22uolUv1bv023xj-x68gu1dp).


### Train

To be released.

### Eval

Download a pre trained model from
[here](https://drive.google.com/uc?export=download&id=1FBnyrgBLVAxWXgmPGvRFMQX__nk32iND).
To make OCR on an image, execute:
```
python ocr.py --checkpoint image2bichig-epoch-0157.pth test.jpg
ᠮᠢᠨᠦ ᠨᠤᠲᠠᠭ
ᠬᠡᠨᠲᠡᠢ ᠂ ᠬᠠᠩᠭᠠᠢ᠂ ᠱᠣᠶᠣᠨ ᠤ ᠥᠨᠳᠥᠷ ᠰᠠᠶ᠋ᠢᠬᠠᠨ ᠨᠢᠷᠤᠭᠤᠨ ᠤᠳᠨ
ᠬᠣᠶᠢᠲᠤ ᠵᠦᠭ ᠦᠨ ᠴᠢᠮᠡᠭ ᠪᠣᠯᠤᠭᠰᠠᠨ ᠣᠢ ᠬᠥᠪᠴᠢ ᠶᠢᠨ ᠠᠭᠤᠯᠠᠨ ᠤᠳ
ᠮᠠᠨᠠᠨ  ᠮᠠᠷᠭ᠎ᠠ᠂ ᠨᠣᠮᠢᠨ ᠤ ᠥᠷᠭᠡᠨ ᠶᠡᠬᠡ ᠭᠣᠪᠢ ᠤᠳᠨ
ᠡᠮᠦᠨ᠎ᠡ ᠵᠦᠭ ᠦᠨ ᠮᠠᠩᠯᠠᠢ ᠪᠣᠯᠤᠭᠰᠠᠨ ᠡᠯᠡᠯᠡᠳ ᠮᠠᠩᠬᠠᠨ ᠳᠠᠯᠠᠢ ᠤᠳ
 ᠡᠨᠡ ᠪᠣᠯ ᠮᠢᠨᠦ ᠲᠦᠷᠦᠭᠰᠡᠨ ᠨᠤᠲᠤᠭ ᠮᠣᠩᠭᠣᠯ ᠤᠨ ᠰᠠᠶ᠋ᠢᠬᠠᠨ ᠣᠷᠣᠨ
```

You can try it also online on Colab [here](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/misc/MongolianScriptOCR.ipynb).