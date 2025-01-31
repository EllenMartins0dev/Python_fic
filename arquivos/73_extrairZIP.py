from zipfile import ZipFile
import os

arquivo_zip = "escola/dados_para_download"
diretorio_extrair = "escola/arquivos_extraidos"
os.mkdir(diretorio_extrair)

with ZipFile(arquivo_zip, "r") as arq_zip:
    arq_zip.extractall(diretorio_extrair)
