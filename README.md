<p align="center">
    <img src="https://cocoindex.io/images/github.svg" alt="CocoIndex">
</p>

<h1 align="center">CocoIndex Quickstart 🥥</h1>

<p align="center">
    <b>Build your first CocoIndex pipeline in 5 minutes.</b><br/>
    Convert a folder of PDFs into Markdown — and watch it only reprocess what actually changed.
</p>

<p align="center">
    <a href="https://github.com/cocoindex-io/cocoindex"><img src="https://img.shields.io/github/stars/cocoindex-io/cocoindex?color=5B5BD6&label=%E2%AD%90%20Star%20CocoIndex" alt="GitHub stars"></a>
    <a href="https://cocoindex.io/docs/getting_started/quickstart/"><img src="https://img.shields.io/badge/docs-quickstart-5B5BD6" alt="Docs"></a>
    <a href="https://discord.com/invite/zpA9S2DR7s"><img src="https://img.shields.io/badge/Discord-join-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
    <img src="https://img.shields.io/badge/python-3.11%2B-blue" alt="Python 3.11+">
</p>

---

This is the companion repo for the [**CocoIndex Quickstart**](https://cocoindex.io/docs/getting_started/quickstart/). Clone it, run two commands, and you have a working incremental data pipeline.

## What you'll build

```
pdf_files/*.pdf  ──▶  Docling (PDF → Markdown)  ──▶  out/*.md
```

1. **Read** PDF files from a local directory
2. **Convert** each one to Markdown with [Docling](https://github.com/DS4SD/docling)
3. **Write** the Markdown to an output directory as a **target state**

You declare the transformation in plain Python — `target_state = transformation(source_state)`. When a source file or your logic changes, CocoIndex figures out the minimum work needed and keeps the output in sync. No external services, runs entirely on your CPU.

## Prerequisites

- **Python 3.11+**
- That's it — no Postgres, no Docker, no API keys.

## Quickstart

**1. Install dependencies** (a sample PDF — *Attention Is All You Need* — is already in `pdf_files/`):

```bash
pip install -e .
```

**2. Run the pipeline:**

```bash
cocoindex update main.py
```

Your Markdown appears in `./out/`, one file per PDF:

```bash
ls out/
# 1706.03762v7.md
```

That's the whole thing. 🎉

## The magic: incremental processing

Re-running never redoes work that's already done. Try it:

```bash
# Add another PDF, then:
cocoindex update main.py     # ⚡ only the new file is converted

# Edit or replace a PDF, then:
cocoindex update main.py     # ⚡ only the changed file is reprocessed

# Remove a PDF, then:
rm pdf_files/some.pdf
cocoindex update main.py     # 🧹 its Markdown is deleted automatically
```

Every other file is skipped — CocoIndex memoizes by content and code, so re-runs are effectively free. This is what makes it practical to run real pipelines over thousands of files.

## How it works

The whole pipeline is [`main.py`](./main.py) — about 40 lines:

```python
@coco.fn(memo=True)                       # memoized: unchanged files are skipped
def process_file(file, outdir):
    markdown = _converter.convert(file.file_path.resolve()) \
                         .document.export_to_markdown()
    localfs.declare_file(outdir / (file.file_path.path.stem + ".md"), markdown,
                         create_parent_dirs=True)   # declare the output you want to exist

@coco.fn
async def app_main(sourcedir, outdir):
    files = localfs.walk_dir(sourcedir, recursive=True,
                             path_matcher=PatternFilePathMatcher(["**/*.pdf"]))
    await coco.mount_each(process_file, files.items(), outdir)  # one component per file
```

You describe the **output state** you want; the engine handles inserts, updates, and deletes for you.

## Next steps

- 📖 Read the full [Quickstart](https://cocoindex.io/docs/getting_started/quickstart/) and [Core Concepts](https://cocoindex.io/docs/programming_guide/core_concepts)
- 🔎 Build something bigger — [text embeddings & RAG](https://github.com/cocoindex-io/cocoindex/tree/main/examples/text_embedding), [codebase indexing](https://github.com/cocoindex-io/cocoindex/tree/main/examples/code_embedding), [knowledge graphs](https://github.com/cocoindex-io/cocoindex/tree/main/examples/meeting_notes_graph_neo4j)
- 🗂️ Browse all [examples](https://github.com/cocoindex-io/cocoindex/tree/main/examples)

## Support us ❤️

If this helped you get started, the easiest way to support CocoIndex is to [give it a ⭐ on GitHub](https://github.com/cocoindex-io/cocoindex) — it's how other developers find the project. Questions or ideas? Come say hi on [Discord](https://discord.com/invite/zpA9S2DR7s).
