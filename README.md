# ollama-python-example
Ollama Python example

## Setup

### CPU only

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

```bash
docker exec -it ollama /bin/bash
```

```bash
ollama pull llama3.1
```

## Run

```bash
python run.py
```

```bash
$ python run.py
地球の大気中には、光を放つ元素が含まれており、その色が青です。
```

```bash
$ python run.py
地球と太陽の間には、空気よりも軽いガスが存在します。このガスの色を見ると、空は青いことがわかります。
青い空というのは、人間のみが見ることになります。人以外の生物は青を見ることができません。
```

```bash
$ python run.py
「空の色がどうなるか」というのは、気象学者の間でも意見が一致しない問題でした。しかし、2006年の3月にNASAが発表した研究に よって、空の青い様子の理由がようやく明らかになりました。

空の青い色は、天文学者の中島昭夫博士が「空が青いのは、光の波長によるもの」という論文を2002年10月に、世界最大の科学雑誌『Nature』に発表しました。空の青い色に関するこの論文が注目を集めると、NASAも、この研究を2006年の3月、「NASA Tech Briefs」 で紹介しました。

これから先、この論文と同じ考え方が多くの気象学者によって採用されることが期待されています。
```
