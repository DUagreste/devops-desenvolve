#!/bin/bash

echo "Administrando usuários e grupos"

echo "Apresentação"

echo "Criando usuários com useradd e adduser"
sudo useradd Vitor2
sudo adduser Vitor3
cd /home
cd Vitor3
cat /etc/passwd | grep Vitor
cat /etc/group | grep Vitor

echo "Adicionando grupos aos usuários"
cd
groups
groups Vitor3
su - Vitor3
sudo groupadd scripts
cat /etc/group
cat /etc/group | grep scripts
sudo usermod -aG scripts Vitor3
groups Vitor3
sudo groupadd desenvolvedores
sudo vi /etc/group
sudo userdel Vitor2
sudo groupdel desenvolvedores
cat /etc/passwd

echo "Por dentro dos permissionamentos"

echo "Entendendo o permissionamento dos arquivos e diretórios"
ls
touch novoteste
ls -l
ls -l /var

echo "Alterando as permissões, donos e grupos"
sudo mkdir /scripts
ls -l /
sudo chmod 770 /scripts
sudo chmod 774 /scripts
sudo usermod -aG scripts Vitor3
sudo adduser Vitor4
groups Vitor4
cd /scripts/
sudo chown Vitorf /scripts
sudo chown Vitor:scripts /scripts
echo "projeto da NASA" > proj1
cat proj1

echo "Permissionamentos restritivos e especiais"
su - Vitor3
sudo chmod 660 proj1
sudo chmod o-r proj1
su - Vitor3
su - Vitor4
sudo chmod o-r /scripts
touch projeto2
cd ..
sudo chmod g+s /scripts
ls -l /
cd /scripts/
touch projeto3
ls -l

echo "Links simbólicos e suas utilidades"
cd
ln -s /scripts/ scripts
ls -l
pwd
cd scripts
pwd
cd
rm -rf scripts
ls -l /

echo "Gerenciamento de pacotes"

echo "Gerenciamento de pacotes com o apt"
sudo apt install apache2
sudo apt update
sudo apt-get install apache2
apt search apache2
apt search openssh-server
apt show apache2
apt search mysql
sudo apt install mysql-server   

echo "Informações e upgrade dos pacotes instalados"
sudo apt remove apache2
sudo apt autoremove
sudo apt update
sudo apt install apache2
apt list --upgradable
sudo apt upgrade 

echo "Consultando a base instalada com a apt list"
apt list --upgradable
apt list
apt list | grep installed > lista-pacotes.txt
cat lista-pacotes.txt
sudo apt list --installed 

echo "Gerenciamentos de discos"

echo "Instalando e particionando um novo disco"
sudo poweroff
sudo lshw
sudo lshw -c disk
sudo fdisk -l
sudo fdisk -l | grep sd
sudo fdisk -l
sudo fdisk /dev/sdb

echo "Instalando o File System ext4"
sudo fdisk -l
sudo mkfs -t ext4 /dev/sdb1
mount | grep sd
sudo mkfs.ext4 /dev/sdb1
mount

echo "Montando o disco de forma automática"
cd /media
sudo mkdir disk2
sudo mount /dev/sdb1 /media/disk2/
cd disk2/
mount | grep sd
cat /etc/fstab
sudo blkid
ls -l /dev/sdb
sudo /etc/
cd  /etc/
sudo cp fstab fstab.bkp
sudo vi /etc/fstab

echo "Testando a inicialização e o acesso ao dispositivo"
mount
sudo umount /media/disk2
sudo mount -a
cd /media/
ls -l
sudo su
cd disk2/
sudo reboot

echo "Systemd - Gerenciando os serviços"

echo "Gerenciando serviços"
sudo systemctl
sudo systemctl status apache2
sudo systemctl stop apache2
sudo systemctl status apache2
sudo systemctl start apache2
sudo service apache2 stop
sudo service apache2 status
systemctl disable apache2
sudo systemctl disable apache2
sudo systemctl enable apache2

echo "Conclusão"


