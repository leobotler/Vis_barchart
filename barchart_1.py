from mayavi import mlab
import sys
import numpy as np
from traits.api import HasTraits,Int,Float,Str,Property

# Retorna um handle para a imagem atual
f = mlab.gcf()

# Limpa a imagem atual
mlab.clf();

# Retorna um handle para a camera
camera = f.scene.camera

# Desabilita renderizacao para podermos ver a imagem sendo construida
f.scene.disable_render = True

# criacao do mapa a partir do arquivo world.dar

# Arquivos a serem lidos
fread1 = open('world.dat','r')
fread2 = open('new_table_10000.txt','r')


# Define vetores com latitudes e longitudes
xvet = [];
yvet = [];
zerovet = [];
onevet = [];

x0 = []
for line in fread1:
	line_list = [float(x) for x in line.split()]
	x0.append(line_list)
	
	
for i in x0:
	if i != []:
		xvet.append(i[0]);
		yvet.append(i[1]);
		zerovet.append(0)

#mapa = mlab.points3d(xvet,yvet,zerovet, xvet, color = (0,1,0))
mapa = mlab.barchart(xvet,yvet, zerovet, color = (0,1,0))

# gira camera
camera.yaw(220)

x = 0; y = 0;

# Vetores que contem os ips de origem e destino dos pacotes
ip_src = [];
ip_dst = [];

# Vetor que contem o tamanho do pacote
z = [];

# Marca a posicao da linha atual
contline = 0;

# Faz a leitura do arquivo e adiciona as leituras aos vetores
for line in fread2:
	
	contline += 1;
	
	if contline%4 == 1:
		ip_src.append( line.strip() );
	if contline%4 == 2:
		ip_dst.append( line.strip() );			
	if contline%4 == 3:
		z.append( line.strip() );

# Aplica uma funcao de mapeamento a z utilizando inteiros		
z = map(int, z)

# Lista de blocos e lista auxiliar de blocos
blocos = [];
blocosaux = [];

# Lista de ips que ja estao presentes no grafico
ip_used = [];

vetzaux = [];

ang = 0.1;
vetx = [0]; vety = [0]; vetz= [0];
vetxaux = [0]; vetyaux = [0]; vetzaux= [0];

cont = 0;
cont1 = 0;

# le arquivo com coordenadas e manda os ip's com as coordenadas para o vetor coordenadas
file_cordenadas = open('Ip_lat_lon_10000.txt','r')
coordenadas = [];
lines = file_cordenadas.readlines();
for i in lines:
	coordenadas.append( i.split(" ") );
for j in coordenadas:
	j[2]=j[2][0:-1]


for ind_ip in ip_src: 
	
	cont += 1;
	x = coordenadas[cont-1][2];
	y = coordenadas[cont-1][1];
	fator_de_escala = 80
	zpad = ( (z[cont - 1])/fator_de_escala );
	
	# Se o ip estiver presente na lista de ips usados...
	if ind_ip in ip_used:

		# ...procure o bloco correspondente a ele...
		for p in blocos:	
			if ind_ip == p[3]:

				# ... e crie um novo bloco igual ao anterior, com a posicao z atualizada.
				new_bloco = [p[0], p[1], p[2] + zpad, ind_ip, ip_dst[ip_src.index(ind_ip)]]; 
				
	# Se o ip nao estiver presente na lista de ips usados...
	else:

		# ...adicione-o na lista de ips usados...
		ip_used.append(ind_ip);

		# ...crie um bloco correspondente...
		#new_bloco = [x, y, zpad, ind_ip, ip_dst[ip_src.index(ind_ip)]];
		new_bloco = [float(x), float(y), zpad, ind_ip, ip_dst[ip_src.index(ind_ip)]];
		
		# ...e coloque o bloco na lista de blocos.
		blocos.append(new_bloco);
	
	# Coloque o bloco recem criado na lista auxiliar
	blocosaux.append(new_bloco)

	vetx.append(new_bloco[0]);
	vety.append(new_bloco[1]);
	vetz.append(new_bloco[2]);
	
f.scene.disable_render = False

for cont1 in range(len(vetx)): 
		
	if cont1 < 100:
        
		mlab.barchart(vetx[(cont1-1):cont1], vety[(cont1-1):cont1], vetz[(cont1-1):cont1], resolution = 20)
		camera.yaw(ang)

	else:
		if cont1 < 1000:
			limite = 10
			if cont1%limite == 0:
				camera.yaw(ang*2)
				mlab.barchart(vetx[(cont1-limite):cont1], vety[(cont1-limite):cont1], vetz[(cont1-limite):cont1], resolution = 20)
				#print cont1
				
		else:
			limite = 100
			if cont1%limite == 0:
				camera.yaw(-ang)
				mlab.barchart(vetx[(cont1-limite):cont1], vety[(cont1-limite):cont1], vetz[(cont1-limite):cont1], resolution = 20)
				#print cont1	

# Isso aqui ta removendo o terreno que foi criado anteriormente
mlab.clf();

mapa = mlab.barchart(xvet,yvet,zerovet, color = (0,1,0))
s = mlab.barchart(vetx, vety, vetz, resolution = 20);

# define outline e x1
x1, y1, z1 = np.random.random((3, 10))

outline = mlab.outline(line_width=3, color=(1,1,1))
outline.outline_mode = 'cornered'
outline.bounds = (x1[0]-0.1, x1[0]+0.1,
                  y1[0]-0.1, y1[0]+0.1,
                  z1[0]-0.1, z1[0]+0.1)

nova_lista_de_ips = []
novo_numero_de_pacotes = 0;

def imprime_clicou(picker):
	if picker.actor in s.actor.actors:
		point_id = picker.point_id
		#print "clicou";
		if (point_id != -1):
			n_bloco = (point_id - 7)/24 + 1;
			#print n_bloco
			#print "Numero total de pacotes : ", vetz[n_bloco]*fator_de_escala
			ip_dst_aux = [];
			novo_numero_de_pacotes = vetz[n_bloco]*fator_de_escala
			#print "Mandou pacotes para os seguintes ip's:"
			nova_lista_de_ips = []
			for ind_ip_1 in range(len(ip_src)):
				if ip_src[ind_ip_1] == blocosaux[n_bloco-1][3]:
					if ip_dst[ind_ip_1] not in ip_dst_aux:
						ip_dst_aux.append(ip_dst[ind_ip_1])
						#print ip_dst[ind_ip_1]
						nova_lista_de_ips.append(ip_dst[ind_ip_1])
						
			outline.bounds = (blocosaux[n_bloco-1][0]-0.6, blocosaux[n_bloco-1][0]+0.6,blocosaux[n_bloco-1][1]-0.6,blocosaux[n_bloco-1][1]+0.6, 0, blocosaux[n_bloco-1][2] )
			p = ips_de_destino(Numero_de_pacotes_enviados = novo_numero_de_pacotes, Mandou_pacotes_para=nova_lista_de_ips)
			p.configure_traits()
			
picker = f.on_mouse_pick(imprime_clicou)
picker.tolerance = 0.014

# gui

class ips_de_destino(HasTraits):
	Numero_de_pacotes_enviados = Int
	Mandou_pacotes_para = []
	
p = ips_de_destino(Numero_de_pacotes_enviados = novo_numero_de_pacotes, Mandou_pacotes_para=nova_lista_de_ips)

# Permite que a imagem possa ser manipulada pelo usuario
if __name__ == '__main__':
	p.configure_traits()
	mlab.show()
