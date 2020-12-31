#!/bin/bash
for host in $(cat /content/b3.txt);do
echo "Realizando Analise do Ativo:"$host
python3 script.py $host | tee final.txt
done
sort final.txt >> resultado.txt
echo "Processo Concluido! Arquivo salvo como resultado.txt"
rm final.txt
