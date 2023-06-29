#!/bin/bash

echo "Localizando conteúdos e trabalhando com as saídas"

echo "Filtrando o conteúdo"
mkdir labs/filtrando_conteudo
cd labs/filtrando_conteudo 
cp /etc/services . 
cat services
grep http services
grep https services
grep -i http services
cp /etc/passwd . 
cat passwd 
grep Vitor * 
grep -l Vitor * 
grep -L Vitor * 

echo "Utilizando a recursividade no Grep"
mkdir teste
cd teste/
cp ../services services2 
cd ..
grep HTTP services 
grep HTTP *
grep -r HTTP *
grep -rl HTTP *

echo "Formatando a saída na tela"
cat passwd
more passwd
cat services 
more services
less services
tail /etc/passwd 
head /etc/passwd
head -n 3 /etc/passwd

echo "Procurando arquivos no sistema"

echo "Procurando arquivos no sistema"
cd /etc
ls *.conf 
ls -l *.conf
cd / 
find / -name *.conf 
sudo find / -name *.conf 
sudo find /etc maxdepth 2 -name *.conf 

echo "Mais recursos do find - amin, atime, iname"
cd glob/
touch novo-teste 
ls -l
cd ..
find . -amin -5
find . -atime -2
sudo find / -size +100M
ls -l /swap.img
ls -lh /swap.img
sudo find / -size +3G
sudo find / -size 3G
sudo find /etc maxdepth 2  -iname *.conf 

echo "Redirecionamento e pipe"

echo "Redirecionando a saída padrão para um arquivo"
mkdir redirecionamento
cd redirecionamento
cp /etc/services . 
grep ssh services
grep ssh services > listagem.txt
cat listagem.txt 
grep 3389 ssh services > listagem.txt 
cat listagem.txt
grep 3389 ssh services > listagem.txt
grep 3389 ssh services >> listagem.txt 
cat /etc/passwd 
cat /etc/passwd | grep Vitor 
grep Vitor /etc/passwd 
cat /etc/passwd | grep Vitor > listagem_usuarios
cat listagem_usuarios

echo "Combinando comando com o pipe"
grep ssh services > listagem.txt
cat listagem.txt
grep ssh 3389 services >> listagem.txt 
cat listagem.txt
cat listagem.txt | sort 
cat listagem.txt | sort > listagem.txt
cat listagem.txt 
cat listagem.txt | sort > listagem2.txt 
cat listagem2.txt 
cd /var/log/ 
tail syslog
tail -n 5 syslog 
tail -n 5 syslog | grep systemd
tail -n 5 syslog | grep systemd > log5.txt
tail -n 5 syslog | grep systemd > ~/labs/redirecionamento/log5.txt  
more syslog 
tail -n 5 syslog | grep systemd | sort > ~/labs/redirecionamento/log5.txt 

echo "Filtrando as informações com o cut"
mkdir ~/labs/extraindo_conteudos
more syslogcat syslog | grep systemd
cat syslog | grep systemd | less
cat syslog | grep systemd | wc
cat syslog | grep systemd | wc -l
cat syslog | grep systemd > ~/labs/extraindo_conteudos/logs
cd ~/labs/extraindo_conteudos/
cat logs
cat logs | cut -d " " -f1
cat logs | cut -d " " -f7
cat logs | cut -d " " -f7-
cat logs | cut -d " " -f7- > logs1
cat logs1
cat logs | cut -d " " -f1-3,7-
cat logs | cut -d " " -f1-3,7- > log-completo.txt
cat log-completo.txt

echo "Utilizando as Regex"

echo "Regex com o Grep #1"
sudo apt update
sudo apt install wamerican
find /usr -name *american*
mkdir expressoes-regulares
cd expressoes-regulares/
cp /usr/share/dict/american-english .
more american-english
wc american-english
cat american-english | grep computer
cat american-english | grep -E "^computer"
cat american-english | grep -E "^computer$"

echo "Regex com o Grep #2"
grep -i computer american-english
echo "Computer" >> american-english
grep -i computer american-english
cat american-english | grep -E "^computer$"
cat american-english | grep -Ei "^computer$"
echo "COMPUTER" >> american-english
cat american-english | grep -Ei "^computer$"
egrep "^computer$" american-english
egrep -i  "^computer$" american-english
cat american-english | grep smartphone
cat american-english | grep -E "smartphone|computer"
cat american-english | grep -E "^smartphone$|^computer$"

echo "Regex com o Grep #3"
egrep "^.oot" american-english
egrep "^.oot$" american-english
egrep "^.oot..$" american-english
egrep "[aeiou]oot..$" american-english
egrep "[flmr]oot..$" american-english
egrep "^[flmr]oot..$" american-english
egrep "^[l-m]oot..$" american-english

echo "Editores de texto"


echo "Editores de texto nano e vi"
mkdir editores
cd editores/
head -n 50 /etc/services > edit1.txt
cat edit1.txt
nano edit1.txt
nano
vi
vi edit1.txt  

echo "Avançando no vi"

echo "Conclusão"
