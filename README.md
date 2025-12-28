<p align="center">
    <img src="https://cocoindex.io/images/github.svg" alt="CocoIndex">
</p>

Quickstart demo following the [Cocoindex Quickstart](https://cocoindex.io/docs/quickstart) guide.
Super easy to get your RAG data pipeline running in ~50 lines of python 🚀.

⭐ Star [Cocoindex on Github](https://github.com/cocoindex-io/cocoindex) if you like it! [![GitHub](https://img.shields.io/github/stars/cocoindex-io/cocoindex?color=5B5BD6)](https://github.com/cocoindex-io/cocoindex)


Video tutorial with detailed explanation: [Cocoindex Quickstart Video Guide](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Prerequisite
- [Install Postgres](https://cocoindex.io/docs/getting_started/installation#-install-postgres) if you don't have one.

- Install CocoIndex and other dependencies:
```bash
pip install -U "cocoindex[embeddings]" 
```

## Run

Update index:

```bash
cocoindex update main.py
```

Run query:

```bash
python main.py
```

## Run with CocoInsight
```bash
cocoindex server -ci main.py
```
