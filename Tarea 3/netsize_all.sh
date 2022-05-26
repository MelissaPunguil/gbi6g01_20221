#! /bin/bash 
echo "Escriba un script que imprima los números de las filas y las columnas para cada red" >netsize_all.txt
echo "Melissa Punguil. Análisis de datos con bucle FOR" >> netsize_all.txt
for f in $(ls *.txt)
do 
	wc -l $f >> netsize_all.txt ; head -n1 $f | grep -o " " | wc -l >> netsize_all.txt ; 
done
