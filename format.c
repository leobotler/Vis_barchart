#include <stdio.h>
#include <stdlib.h>

int main (int argv, char *argc[]){

	FILE *fp = fopen (argc[1],"r");
	FILE *s = fopen (argc[2],"w");
	
	//int ip_1,ip_2,ip_3,ip_4;
	int num_pct;
	int cont_barra_n = 0;
	char c;
	char tipo_pct[30];
	while (!feof(fp)){
		c=fgetc (fp);
		if (c=='\n') cont_barra_n++;
		if (cont_barra_n == 3){
		//	cont_barra_n = 0;
			fscanf (fp,"<section>");
			while (c!='<'){
				c=fgetc(fp);
				if (c=='<') fscanf(fp,"/section>");
				else{ 
					fprintf (s,"%c",c);
					//printf ("%c",c);
				//else printf ("%c",c);
				//fflush (stdin);
				//getchar();
				}
			}
		}
		else if (cont_barra_n == 5 ) {
			
			fscanf (fp,"<section>");
			fprintf (s,", ");		
			//printf (", ");		
			while (c!='<'){
				c=fgetc(fp);
				if (c=='<') fscanf(fp,"/section>");
				else{
					if (c >= 65 && c <= 90)
					 fprintf (s,"%c",(c + 32));
					 else fprintf (s,"%c",c);
				 }
			}
			c=fgetc(fp);
			//printf ("%c",c);
			//puts (tipo_pct);
		//else if (cont_barra_n == 6) {
			fscanf (fp,"<section>%d</section>",&num_pct);
			fprintf (s,", %d\n",num_pct);
			//printf (",%d\n",num_pct);
			cont_barra_n = 0;
			while (cont_barra_n < 4){
				c = fgetc(fp);
				if (c=='\n') cont_barra_n++;
			}
			cont_barra_n = 0;			
		}
	}
	
	fclose(fp);
	fclose(s);
	
	return 0;
}
