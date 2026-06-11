"""
CocoIndex quickstart — convert PDFs to Markdown.

Walk a folder of PDFs, convert each to Markdown with Docling, and write the
result to ./out. Re-runs only reprocess the files that actually changed.

Tutorial: https://cocoindex.io/docs/getting_started/quickstart/
"""

import pathlib

import cocoindex as coco
from cocoindex.connectors import localfs
from cocoindex.resources.file import PatternFilePathMatcher
from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

_pipeline_options = PdfPipelineOptions(
    accelerator_options=AcceleratorOptions(device=AcceleratorDevice.CPU)
)
_converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=_pipeline_options)
    }
)


@coco.fn(memo=True)
def process_file(file: localfs.File, outdir: pathlib.Path) -> None:
    markdown = _converter.convert(
        file.file_path.resolve()
    ).document.export_to_markdown()
    outname = file.file_path.path.stem + ".md"
    localfs.declare_file(outdir / outname, markdown, create_parent_dirs=True)


@coco.fn
async def app_main(sourcedir: pathlib.Path, outdir: pathlib.Path) -> None:
    files = localfs.walk_dir(
        sourcedir,
        recursive=True,
        path_matcher=PatternFilePathMatcher(included_patterns=["**/*.pdf"]),
    )
    await coco.mount_each(process_file, files.items(), outdir)


app = coco.App(
    "PdfToMarkdown",
    app_main,
    sourcedir=pathlib.Path("./pdf_files"),
    outdir=pathlib.Path("./out"),
)
