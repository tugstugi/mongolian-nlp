The traditional Mongolian script uses an old pronunciation which differs
from the modern Mongolian spoken language. This experiment tries to convert
between the Mongolian script (old pronunciation) to the cyrillic script (modern pronunciation)
using deep learning.


## Dependencies
Facebook's [fairseq](https://github.com/pytorch/fairseq) project is used to train the converter
which is added as submodule. To install it, execute:
```bash
git clone --recursive https://github.com/tugstugi/mongolian-nlp.git
cd mongolian-nlp/bichig2cyrillic/fairseq
pip install -r requirements.txt
python setup.py build develop
```

Modern Mongolian song lyrics (80K lines) are converted with
the Inner Mongolian University's [online translator tool](http://trans.mglip.com/EnglishC2T.aspx)
to the Mongolian script and used as the training [dataset](lyrics.txt.gz).
To prepare the dataset to use with `fairseq`, execute:
```bash
python create_dataset.py
# binarized dataset for Mongolian script to cyrillic
python fairseq/preprocess.py \
  --trainpref dataset/train --validpref dataset/valid --testpref dataset/test \
  --source-lang bichig --target-lang cyrillic \
  --destdir bichig2cyrillic-bin
# binarized dataset for cyrillic to Mongolian script
python fairseq/preprocess.py \
  --trainpref dataset/train --validpref dataset/valid --testpref dataset/test \
  --source-lang cyrillic --target-lang bichig \
  --destdir cyrillic2bichig-bin
```


## Mongolian Script to Cyrillic Script

To train a [fully convolutional seq2seq](https://arxiv.org/abs/1705.03122) model for 20 epochs, execute:
```bash
mkdir -p checkpoints/bichig2cyrillic
python fairseq/train.py  --optimizer adam --lr 5e-5 --min-lr 5e-10 --lr-shrink 0.5 \
  --max-tokens 1000 --arch fconv --clip-norm 0.1 \
  --max-epoch 20 \
  --save-dir checkpoints/bichig2cyrillic bichig2cyrillic-bin
```
After training, the training loss should be under 0.02.

Now convert some Mongolian scripts to cyrillic:
```bash
echo "ᠬᠡᠨ ᠬᠦᠮᠦᠨ ᠲᠡᠢ ᠦᠭᠡ ᠶᠠᠷᠢᠨ᠎ᠠ ᠭᠡᠳᠡᠭ\nᠬᠡᠷᠡᠭ ᠳᠡᠭᠡᠷ᠎ᠡ ᠪᠡᠨ ᠲᠤᠯᠤᠯᠳᠤᠭᠠᠨ ᠶᠤᠮ\nᠬᠠᠯᠠᠭᠤᠨ ᠬᠦᠢᠲᠡᠨ ᠶᠠᠮᠠᠷ ᠴᠤ ᠵᠡᠪᠰᠡᠭ ᠡᠴᠡ\nᠬᠠᠲᠠᠭᠤ ᠵᠦᠭᠡᠯᠡᠨ ᠦᠭᠡ ᠬᠦᠴᠦᠲᠡᠢ" | \
  python convert.py --path checkpoints/bichig2cyrillic/checkpoint_best.pt bichig2cyrillic-bin 
```
The output should look:
```
хэн хүн тэй үг ярина гэдэг
хэрэг дээр бэн тулалдаан юм
халуун хүйтэн ямар ч зэвсгээс
хатуу зүглэн үгээ хүчтэй
```

## Cyrillic to Mongolian Script

Looks similar to above. Replace `bichig2cyrillic` with `cyrillic2bichig`.
