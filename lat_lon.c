#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char *argv[]){

	FILE *fp = fopen (argv[1],"r");
	FILE *s = fopen (argv[2], "w");
	
	char c;
	int vir = 3;
	float lat,lon;
	
	while (!feof(fp)){
		
		c = fgetc(fp);
		
		if (c == '\n') vir++;
		if (vir >= 12){
			
			while (c!=':') c=fgetc(fp);
			c=fgetc(fp);
			c=fgetc(fp);
			fscanf (fp,"%f",&lat);
			while (c!=':') c=fgetc(fp);
			c=fgetc(fp);
			c=fgetc(fp);
			fscanf (fp,"%f",&lon);
			
			//fscanf (fp, "latidude: \"%f\",longitude: \"%f\",", &lat,&lon);
			printf ("lat: %f\nlon: %f\n",lat,lon);
			fprintf (s,"lat: %f - lon: %f\n",lat,lon);
			vir = 0;
		}
	}
	
	fclose (fp);
	fclose (s);
	
	return 0;
}
