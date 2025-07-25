<p align="center">
    <img src="https://cocoindex.io/images/github.svg" alt="CocoIndex">
</p>

Quickstart demo following the [Cocoindex Quickstart](https://cocoindex.io/docs/quickstart) guide.
Super easy to get your RAG data pipeline running in ~50 lines of python 🚀.

⭐ Please give [Cocoindex on Github](https://github.com/cocoindex-io/cocoindex) a star to support us if you like our work. Thank you so much with a warm coconut hug 🥥🤗. [![GitHub](https://img.shields.io/github/stars/cocoindex-io/cocoindex?color=5B5BD6)](https://github.com/cocoindex-io/cocoindex)


Video tutorial with detailed explanation: [Cocoindex Quickstart Video Guide](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Prerequisite
- [Install Postgres](https://cocoindex.io/docs/getting_started/installation#-install-postgres) if you don't have one.

- Install CocoIndex and other dependencies:
```bash
pip install -U "cocoindex[embeddings]" "psycopg[binary,pool]" pgvector
```

-  Make sure you have specify the database URL by environment variable:
```
export COCOINDEX_DATABASE_URL="postgresql://cocoindex:cocoindex@localhost:5432/cocoindex"
```

## Run

Update index:

```bash
cocoindex update --setup quickstart.py
```

Run query:

```bash
python quickstart.py
```