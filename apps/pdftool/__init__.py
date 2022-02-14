from logging import Logger
from typing import List

from pikepdf import Pdf


class PdfTool():
    def __init__(self, logger: Logger) -> None:
        """
        PdfToolクラスをインスタンス化する

        Parameters
        ----------
        logger: Logger
            ロガー
        """

        self.logger = logger

    def merge(self, input_files: List[str], output_file: str) -> None:
        """
        PDFファイルを結合する

        Parameters
        ----------
        input_files: List[str]
            結合するPDFファイルのパスのリスト
        output_file: str
            結合後生成されるPDFファイルのパス
        """
        pdf = Pdf.new()
        version = pdf.pdf_version
        for file in input_files:
            src = Pdf.open(file)
            version = max(version, src.pdf_version)
            pdf.pages.extend(src.pages)
            self.logger.info(f'merged <= {file}')
        pdf.remove_unreferenced_resources()
        pdf.save(output_file, min_version=version)
        self.logger.info(f'done => {output_file}')

    def split(self, input_file: str, output_folder: str) -> None:
        """
        PDFファイルを分割する

        Parameters
        ----------
        input_file: str
            分割するPDFファイルのパス
        output_folder: str
            分割後生成されるPDFファイルを置くフォルダのパス
        """
        pdf = Pdf.open(input_file)
        self.logger.info(f'read <= {input_file}')
        for n, page in enumerate(pdf.pages):
            dst = Pdf.new()
            dst.pages.append(page)
            pdf_file = f'{output_folder}/{n:02}.pdf'
            dst.save(pdf_file)
            self.logger.info(f'splitted => {pdf_file}')
