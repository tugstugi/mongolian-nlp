The traditional Mongolian script uses an old pronunciation which differs
from the modern Mongolian spoken language. This experiment tries to convert
between the Mongolian script (old pronunciation) and the cyrillic script (modern pronunciation)
using deep learning.


## Dependencies
Facebook's [fairseq](https://github.com/pytorch/fairseq) project is used to train the converter
which is added as a submodule. To install it, execute:
```bash
git clone --recursive https://github.com/tugstugi/mongolian-nlp.git
cd mongolian-nlp/bichig2cyrillic/fairseq
pip install -r requirements.txt
python setup.py build develop
```

80K lines modern Mongolian song lyrics are converted with
the Inner Mongolian University's [online translator tool](http://trans.mglip.com/EnglishC2T.aspx)
to the Mongolian script and used as the training [dataset](lyrics.txt.gz).
To prepare binarized datasets to use with `fairseq`, execute:
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

## Cyrillic to Mongolian Script
For an online Colab demo, visit: [Cyrillic2Bichig.ipynb](https://colab.research.google.com/github/tugstugi/mongolian-nlp/blob/master/bichig2cyrillic/notebooks/Cyrillic2Bichig.ipynb)

To train a [transformer](https://arxiv.org/abs/1706.03762) character model for 30 epochs, execute:
```bash
python fairseq/train.py  --optimizer adam --lr 5e-5 --min-lr 5e-10 --lr-shrink 0.5 \
  --max-tokens 1000 --arch transformer --clip-norm 0.5 \
  --max-epoch 30 \
  --save-dir checkpoints/cyrillic2bichig cyrillic2bichig-bin
```
After training, the training loss should be under 0.01.

Now convert some cyrillic [texts](http://dovchoo_93.blog.gogo.mn/read/entry47697) into the traditional Mongolian script:
```bash
echo "Хэн хүнтэй үг ярина гэдэг\nХэрэг дээрээ тулалдаан юм\nХалуун хүйтэн ямар ч зэвсгээс\nХатуу зөөлөн үг хүчтэй" | \
  python cyrillic2bichig.py --path checkpoints/cyrillic2bichig/checkpoint_best.pt cyrillic2bichig-bin
```
The above model outputs:
```
ᠬᠡᠨ ᠬᠦᠮᠦᠨ ᠲᠡᠢ ᠦᠭᠡ ᠶᠠᠷᠢᠨ᠎ᠠ ᠭᠡᠳᠡᠭ
ᠬᠡᠷᠡᠭ ᠳᠡᠭᠡᠷ᠎ᠡ ᠪᠡᠨ ᠲᠤᠯᠤᠯᠳᠤᠭᠠᠨ ᠶᠤᠮ
ᠬᠠᠯᠠᠭᠤᠨ ᠬᠦᠢᠲᠡᠨ ᠶᠠᠮᠠᠷ ᠴᠤ ᠵᠡᠪᠰᠡᠭ ᠡᠴᠡ
ᠬᠠᠲᠠᠭᠤ ᠵᠥᠭᠡᠯᠡᠨ ᠦᠭᠡ ᠬᠦᠴᠦᠲᠡᠢ
```

## Mongolian Script to Cyrillic Script

Similar to above. Here some conversion example from the Mongolian president's [website](http://president.mn/mng/?p=2206):
```bash
echo "ᠮᠣᠩ᠋ᠭᠣᠯ ᠤᠯᠤᠰ ᠤᠨ ᠶᠡᠷᠦᠩᠬᠡᠢᠢᠯᠡᠭᠴᠢ ᠬ ∙ ᠪᠠᠲᠤᠲᠤᠯᠭ᠎ᠠ ᠥᠨᠥᠳᠥᠷ ᠧᠦ᠋ᠷᠣᠫᠠ ᠢᠢᠨ ᠬᠣᠯᠪᠣᠭ᠎ᠠ\nᠲᠡᠭᠦᠨ ᠦ ᠭᠡᠰᠢᠭᠦᠨ ᠣᠷᠣᠨ ᠨᠤᠭᠤᠳ ᠠᠴᠠ ᠮᠣᠩ᠋ᠭᠣᠯ ᠤᠯᠤᠰ ᠲᠤ ᠰᠠᠭᠤᠷᠢᠨ ᠪᠣᠯᠤᠨ ᠬᠠᠪᠰᠤᠷᠤᠨ \nᠰᠠᠭᠤᠭ᠎ᠠ ᠣᠨᠴᠠ ᠪᠥᠭᠡᠳ ᠪᠦᠷᠢᠨ ᠡᠷᠬᠡᠲᠦ ᠡᠯᠴᠢᠨ ᠰᠠᠢᠢᠳ ᠨᠠᠷ ᠢ ᠬᠦᠯᠢᠶᠡᠨ ᠠᠪᠴᠤ ᠠᠭᠤᠯᠵᠠᠪᠠ" | \
  python bichig2cyrillic.py --path checkpoints/bichig2cyrillic/checkpoint_best.pt bichig2cyrillic-bin 
```
The output should look:
```
монгол улсын ерөнхийлөгч х баттулга өнөөдөр европийн холбоо
түүний гишүүн орнуудаас монгол улсад суурин болон хавсран
суугаа онц бүгээд бүрэн эрхэт элчин сайд нарыг хүлээн авч уулзав
```
If you try this network on the Mongolian script texts found on internet, it will **fail**! Because the majority of the Mongolian script texts are misspelled. See for more information: [Coping with Problems of Unicoded Traditional
Mongolian](http://www.cips-cl.org/static/anthology/CCL-2016/CCL-16-075.pdf)
