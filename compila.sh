num_entradas=$(($2/10))

echo "Num_entradas: $num_entradas"
echo "Inicio: $(date +%T)"

gcc -o format format.c
gcc -o format_1 format_1.c
gcc -o le_tabela le_tabela.c
gcc -o lat_lon lat_lon.c

nome_arquivo_padrao="opa_$num_entradas"
ips="ips_$num_entradas"
id_ip="id_ip_$num_entradas"
lat_lon="lat_lon_$num_entradas.txt"
new_table="new_table_$num_entradas.txt"

./le_tabela $1 $nome_arquivo_padrao $2
echo "passo 1 - feito"
./format $nome_arquivo_padrao $ips
echo "passo 2 - feito"
./format_1 $nome_arquivo_padrao $new_table
echo "new_table -feito"
perl hello.pl $ips $id_ip
echo "passo 3 - feito"
./lat_lon $id_ip $lat_lon
echo "passo 4 - feito"

echo "Fim:    $(date +%T)"
