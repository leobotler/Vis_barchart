#include <stdio.h>
#include <stdlib.h>

int main (int argv, char *argc[]) {
	FILE *fp = fopen (argc[1],"r");
	FILE *w = fopen (argc[2],"w");
	
	int i = 1;
	int max = atoi(argc[3]);
	char c;
	
	do{
		c =fgetc (fp);
		
		if (i >=13)fprintf (w,"%c",c);
		if (c == '\n') i++;
		}while (i<max);
		
	
	fclose (fp);
	return 0;
}
