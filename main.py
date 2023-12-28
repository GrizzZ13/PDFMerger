# -*- coding:utf-8*-

from PyPDF2 import PdfMerger
import os
import time
import glob
import argparse


def get_pdf_filelist(filepath):
    file_list = glob.glob("{}/*.pdf".format(filepath))
    file_list.sort()
    return file_list


def merge_pdf(input_path, output_file):
    merger = PdfMerger()
    pdf_filelist = get_pdf_filelist(input_path)
    num = len(pdf_filelist)
    for i, pdf_filename in enumerate(pdf_filelist):
        print(f"[{i+1}/{num}] adding {pdf_filename}")
        pdf_file = open(pdf_filename, "rb")
        pdf_file_basename = os.path.basename(pdf_filename)[:-4]
        merger.append(pdf_file, outline_item=pdf_file_basename)
        pdf_file.close()
    merger.write(open(output_file, "wb"))


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="""PDF merger. Merger multiple pdf file into one while keeping their structures"""
    )
    arg_parser.add_argument(
        "-i",
        "--input",
        help="Directory to the input pdf files",
        required=True,
    )
    arg_parser.add_argument(
        "-o",
        "--output",
        help="Pathname of the merged pdf file",
        required=True,
    )

    args = arg_parser.parse_args()
    input = args.input
    output = args.output

    if not output.endswith(".pdf"):
        print("Output file name should end with .pdf")
        exit(1)

    time1 = time.time()
    merge_pdf(input, output)
    time2 = time.time()
    print("Finished. It takes %.4f s" % (time2 - time1))
