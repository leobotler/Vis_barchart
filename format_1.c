#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[]){

	FILE *fp = fopen (argv[1],"r");
	FILE *s = fopen (argv[2],"w");
	
	//int ip_1,ip_2,ip_3,ip_4;
	int num_pct;
	int cont_barra_n = 0;
	char c;
	while (!feof(fp)){
		c=fgetc (fp);
		if (c=='\n') cont_barra_n++;
		if (cont_barra_n == 3){
		//	cont_barra_n = 0;
			fscanf (fp,"<section>");
			while (c!='<'){
				c=fgetc(fp);
				if (c=='<') fscanf(fp,"/section>");
				else fprintf (s,"%c",c);
				//else printf ("%c",c);
				//fflush (stdin);
				//getchar();
			}
		}
		if (cont_barra_n == 4){
			fprintf (s,"\n");
		//	cont_barra_n = 0;
			fscanf (fp,"<section>");
			while (c!='<'){
				c=fgetc(fp);
				if (c=='<') fscanf(fp,"/section>");
				else fprintf (s,"%c",c);
				//else printf ("%c",c);
				//fflush (stdin);
				//getchar();
			}
		}
		else if (cont_barra_n == 6) {
			fscanf (fp,"<section>%d</section>",&num_pct);
			fprintf (s,"\n%d\n\n",num_pct);
			//printf ("\n%d\n\n",num_pct);
			cont_barra_n = 0;
			while (cont_barra_n < 4){
				c = fgetc(fp);
				if (c=='\n') cont_barra_n++;
			}
			cont_barra_n = 0;			
		}
	}
	return 0;
}
