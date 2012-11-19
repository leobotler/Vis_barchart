#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[]){
	
	FILE *ips = fopen (argv[1],"r");
	FILE *lat_lon = fopen (argv[2],"r");
	FILE *s = fopen (argv[3],"w");
	
	int ip;
	int linha = 1;
	float lat, lon;
	char c = '1';
	
	while (!feof(ips)){
		
		fscanf (ips,"%d.",&ip);
		fprintf (s,"%d.",ip);
		
		fscanf (ips,"%d.",&ip);
		fprintf (s,"%d.",ip);
		
		fscanf (ips,"%d.",&ip);
		fprintf (s,"%d.",ip);
		
		fscanf (ips,"%d,",&ip);
		fprintf (s,"%d ",ip);
		
		fscanf (lat_lon,"lat: %f - lon: %f\n",&lat,&lon);
		//c = fgetc(lat_lon);
		fprintf (s,"%f %f\n",lat,lon);
		
		c = fgetc(ips);
		while (c != '\n' && c!= EOF) c = fgetc(ips);
		printf ("linha %d %d\n", linha++,c);
		
	}
	
	fclose (ips);
	fclose (lat_lon);
	fclose (s);
	return 0;
	
}
