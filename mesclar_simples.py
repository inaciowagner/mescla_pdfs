import PyPDF2
import os

arquivo_final = input("digite o nome do arquivo final resultante da mescla dos PDFs ")

merger = PyPDF2.PdfMerger(strict=False)

lista_arquivos = os.listdir()
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(arquivo)

merger.write(f"{arquivo_final}.pdf")
