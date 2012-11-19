#!/usr/bin/perl 

use LWP::Simple; 




$ip = "";
$n_ip = "";
$vir = 0;
open (ips,"<$ARGV[0]");
open FILEHANDLE, ">$ARGV[1]"; 
while (<ips>){
	$ip = $_;
	#print $ip;
	for ($i = 0; substr ($ip,$i,1) ne ','; $i++){
		$vir++;
		#print $vir;
	}
	$n_ip = substr ($ip,0,$vir);
	#print $n_ip,"\n";
	$vir=0;
	$website_content = get("http://api.ipinfodb.com/v3/ip-city/?key=3e8f84b5fb47fe9ee984b540b0aa7ecab2ea387ee7426c88adb096006bd2c82a&ip=$n_ip&format=json"); 
	
	print FILEHANDLE $website_content; 
	print FILEHANDLE"\n";
	
}
close FILEHANDLE;
close (ips);

#	while (($c = getc(ips)) ne ""){
#			
#			if ($c ne ','){
#				if ($vir == 0){
#					push(@ip,$c);
#					print $c;
#				}
#			}
#			elsif ( $c eq ',' || $c eq '\n') {
#				 $vir++;
#				 #print $vir;
#			 }
#			
#			if ($vir >= 3) {
#				$vir = 0;
#				print "blz";
#				print $c;
#				shift @ip;
#				shift @ip;
#			}
#	
#	}
#
#
#close (ips);

#!/usr/bin/perl
 
#@Vogais = ("a","e","i","o","u");
#@Frequencia = (0,0,0,0,0);
# 
#open(DADOS, "<$ARGV[0]") || die "$_[1] não encontrado\n";
#while(($CaracterAtual = getc(DADOS)) ne "") {
#   for($i=0;$i<=4;++$i) {
#      if($CaracterAtual eq $Vogais[$i]) {
#         $Frequencia[$i]++;
#      }
#   }
#}
# 
#close(DADOS);
#for($i=0;$i<=4;++$i) {
#   print "$Vogais[$i] aparece $Frequencia[$i] vezes em $ARGV[0]\n";
#}

#$HTML = "new_table.txt";
#open (HTML) or die "Can't open the file!";
#print <HTML>;
#close (HTML);

#open FILEHANDLE, "<new_table.txt";
#print FILEHANDLE;
#close FILEHANDLE;
