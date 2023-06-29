echo "Criando e configurando scripts"

echo "Variáveis e Scripts"
cd ~/labs/
mkdir scripts
cd scripts/
env
echo $HOME
echo $PWD
teste=xpto
echo $teste
vi backup.sh
----

echo "Digite o diretório de backup:"
read diretorio_bkp

cp -rv $diretorio_bkp ~/backup
echo ""
echo "Backup concluído!"
----

echo "Configurando e executando scripts"
mkdir backup
mv backup ~/
chmod +x backup.sh
./backup.sh
echo $PATH
cd backup/
cd bin/
cd ../..
more .profile
mkdir bin
cd bin/
cp ~/labs/scripts/backup.sh .
exit
echo $PATH
backup.sh

echo "Informações do sistema - hardware"

echo "Obtendo informações da rede"
cat backup.sh
cd backup/
cd ~/labs/scripts/
ifconfig
ip a
ping localhost
hostname -I
cat /etc/resolv.conf
cat /etc/hosts

echo "Informações de memória e CPU"
sudo vi /etc/hosts
sudo lshw
sudo lshw 
sudo lshw | grep sata
cd /proc
cat meminfo
free
cat cpuinfo | more
cat cpuinfo | grep processor
cat cpuinfo | grep processor | wc
cat cpuinfo | grep processor | wc -l

echo "Dispositivos de bloco (Discos)"
cd /dev
ls -l | grep sda
df -h
cd /var
cd log

echo "Informações do sistema - logs"

echo "Principais arquivos de log do sistema"
cd /var/log
dmesg
sudo dmesg
sudo dmesg | grep sda
more syslog
cat syslog | grep -i cron

echo "Visualizando os logs em tempo real"
cat auth.log
cat auth.log | grep -i ssh
tail -f auth.log
cat /etc/logrotate.conf

echo "Visualizando e gerenciando processos"

echo "Listando processos com o PS e o top"
ps -e
ps -ef
ps -aux
ps -aux | grep -i ssh
top
echo "Monitorando processos em tempo real"
cd /proc
ps aux | grep apache2
ps -ef | grep apache
while:; do curl -i http://192.168.15.6; done

echo "Gerenciando processos com o Kill"
ps aux | grep ping
kill -l
ps aux | grep ping
kill -9 15015
ps aux -ef
ps -ef
kill -15 14998
ps -ef
pstree

echo "Tipos de usuários e os seus papéis"

echo "Escalando privilégios com o Sudo"
sudo apt update
cat /etc/sudoers
sudo cat /etc/sudoers
sudo visudo                                                                                                         groups
cat /etc/group
cat /etc/group | grep sudo
su
sudo su

echo "Diferenças entre o root e os demais usuários"
passwd
sudo su
cat /etc/passwd
cat /etc/passwd | grep root
cat /etc/passwd | grep Vitor
sudo cat /etc/shadow
sudo cat /etc/shadow | grep Vitor

echo "Usuários do sistema"
ps aux | grep apache
sudo service apache2 stop
sudo service apache2 start
ps aux | grep apache
cat /etc/passwd | grep www
cat /etc/passwd | grep Vitor

echo "Conclusão"
