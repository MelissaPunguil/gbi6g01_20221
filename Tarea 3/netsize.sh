#! /bin/bash 

echo "Escriba un script que tome uno de estos archivos y determine el número de filas (polinizadores) y columnas (plantas). Tenga en cuenta que las columnas estan separadas por espacios y que hay un espacio al final de cada linea." > netsize.txt 
echo "." >> netsize.txt
echo "Melissa Punguil,Análisis de datos simples" >> netsize.txt ; echo "Archivo: n1.txt" >> netsize.txt ; echo "Número de filas:" >> netsize.txt ; wc -l n1.txt >> netsize.txt ; echo "Número de columnas:" >> netsize.txt ; head -n1 n1.txt | grep -o " " | wc -l >> netsize.txt
