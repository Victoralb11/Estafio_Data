#!/bin/bash

DATA=$(date '+%Y%m%d')

mkdir -p /home/victor/ecommerce/vendas
mkdir -p /home/victor/ecommerce/vendas/backup

cp /home/victor/ecommerce/dados_de_vendas.csv /home/victor/ecommerce/vendas
cp /home/victor/ecommerce/dados_de_vendas.csv "/home/victor/ecommerce/vendas/backup/backup-dados${DATA}.csv"

touch /home/victor/ecommerce/vendas/backup/relatorio.txt

date '+%Y/%m/%d %H:%M' >> /home/victor/ecommerce/vendas/backup/relatorio.txt
(awk -F, 'NR==2 {print $NF} END {print $NF}' /home/victor/ecommerce/dados_de_vendas.csv)  >> /home/victor/ecommerce/vendas/backup/relatorio.txt
head -n 10 /home/victor/ecommerce/dados_de_vendas.csv >> /home/victor/ecommerce/vendas/backup/relatorio.txt
echo  "total de vendas feitas: $(tail -n +2 /home/victor/ecommerce/dados_de_vendas.csv| wc -l)" >> /home/victor/ecommerce/vendas/backup/relatorio.txt

cd /home/victor/ecommerce/vendas/backup
zip "backup-dados${DATA}.zip" "backup-dados${DATA}.csv"

rm "/home/victor/ecommerce/vendas/dados_de_vendas.csv"
rm "/home/victor/ecommerce/vendas/backup/backup-dados${DATA}.csv"
