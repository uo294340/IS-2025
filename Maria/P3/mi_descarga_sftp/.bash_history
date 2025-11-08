ip a
sudo  apt install  nombre_paquete_instalar~
sudo  apt install  nombre_paquete_instalar
sudo apt update
sudo apt upgrade
sudo apt install openssh-server
sudo apt install git
sudo apt install vim
sudo apt install python
sudo apt install python3
sudo apt install Docker
sudo addgroup --system docker
sudo adduser $USER docker
sudo snap install docker
sudo poweroff
docker version
git config --global user.name "uo294340"
git config --global user.email "uo294340@uniovi.es"
git init
git init \Users\UO294340\Desktop\IS-2025\prueba
git branch -m main
git -ls
ls
./
git clone https://github.com/uo294340/IS-2025.git
ls
cd IS-2025
ls
git status
git log
git pull
ls
git log
git status
_WinPython_\App\python.exe
python.exe
python3.exe
sudo poweroff
ip a
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_servidor1.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_cliente1.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_servidor1.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_cliente1.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_servidor1.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_cliente1.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_servidor1.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_cliente1.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_servidor1.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_servidor1.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_cliente1.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_servidor2_simula_perdidas,py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_cliente2_numera_mensajes.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_servidor2_simula_perdidas,py
git config pull.rebase false
git config pull.rebase true
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_servidor4_reintenta.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_servidor3_con_ok.py
/bin/python3 /home/uo294340/IS-2025/IS-2025/Maria/P1/UDP/udp_cliente4_reintenta.py
git pull
cd P1
mkdir P1
cd P1
cd ./
cd .
cd ..
mkdir diego maria
cd maria
mkdir p1
mkdir UDP
mkdir TCP
cd UCP
cd p1
cd UDP
mv UCP UDP
rmdir UDP TCP
cd ..
rmdir UDP TCP
cd p1
mkdir UDP TCP
git add
git add .
git ls
git status
cd ..
git add .
cd IS-2025/
git add .
git commit -m "practica 1 directorios"
git push
git status
git pull
cd Maria
mkdir UDP
mkdir TCP
git add UDP
git add TCP
cd UDP
git commit -m "carpetas p1"
git push
sudopoweroff
ipconfig
ip a
sudo poweroff
ipconfig a
ifconfig
ip a
ip a
sudo poweroff
ip a
cd IS-2025/P2
cd IS-2025/
cd P2
ls
cd Maria
ls
cd ..
cd IS-2025/
cd Maria
cd P2
ls
git pull
ls
mkdir P2
docker ls
docker ps
cd P2
mkdir html
mkdir sitios_nginx
mkdir html2
mkdir hola_flask
ls
sudo netstat -4tln
sudo apt install net-tools
sudo netstat -4tln
sudo apt install nginx
nginx -V
systemctl status nginx
ip a
cd /usr/share/nginx/html/
ls
nano index.html
sudo nano index.html
cd ..
cd /var/www/html/
sudo nano index.html
ls
sudo nano index.nginx-debian.html 
cd ..
cd /var/log/nginx/
ls
nano access.log
sudo systemctl stop nginx
sudo apt remove nginx
sudo apt autoremove
cd ..
sudo netstat -4tln
docker pull nginx
docker images
docker run -d --rm --network pruebas --name nginx nginx
docker pull python:3.7
docker run python:3.7
cd IS-2025
ls
cd home/uo294340/
ls
cd IS-2025
ls
cd IS-2025/
cd Maria
cd P1
cd UDP
./udp_docker_lanzar_servidores.sh
./udp_docker_lanzar_cliente.sh
cd ..
cd P2
docker network create pruebas
docker run -d --rm --network pruebas --name nginx nginx
docker ps
sudo netstat -4tpl
docker inspect nginx
wget 172.18.0.2
wget 172.18.0.2/50x.html
docker exec -it nginx bash
docker stop
docker ps
docker stop nginx
cd html
cd ..
ls
cp 50x.html index.html ./html
ls
cd html
git commit -m "nginx"
git add .
git commit -m "nginx"
git push
docker run -d --rm --network pruebas --name nginx nginx -p 80:80 -v $(pwd):/usr/share/nginx/html
docker run -d --network pruebas --name nginx nginx -p 80:80 -v $(pwd):/usr/share/nginx/html
ip a
docker ps -a
docker run --rm -d --network pruebas --name nginx nginx -p 80:80 -v $(pwd):/usr/share/nginx/html
docker container prune
docker run --rm -d --network pruebas --name nginx nginx -p 80:80 -v $(pwd):/usr/share/nginx/html
docker ps
docker ps -a
docker run --rm -d --network pruebas --name nginx nginx -p 80:80 -v $(pwd):/usr/share/nginx/html
docker ps -a
docker run --rm -d --network pruebas --name nginx -p 80:80 -v $(pwd):/usr/share/nginx/html nginx
sudo nano index.xhtml
ls
nano index.html
docker logs nginx
cd
cd /IS-2025/IS-2025/Maria/P2/
cd /home
cd /IS-2025/IS-2025/Maria/P2/
ls
cd /uo294340
cd uo294340
cd /IS-2025/IS-2025/Maria/P2/
ls
cd IS-2025/IS-2025/Maria/P2/
cd sitios_nginx
sudo nano default.conf
ls
sudo nano default.conf
docker nginx stop
docker stop nginx
cd ..
docker run --rm -d --network pruebas    --name nginx -p 80:80    -v $(pwd)/html:/usr/share/nginx/html    -v $(pwd)/sitios_nginx:/etc/nginx/conf.d nginx
docker ps -a
git push
docker run --rm -it --network pruebas   --name nginx -p 80:80   -v $(pwd)/html:/usr/share/nginx/html   -v $(pwd)/sitios_nginx:/etc/nginx/conf.d nginx
nano sitios_nginx/default.conf
git pull
git add .
git pull
git commit -m "actualizado nginx"
git pull
git push
git ls
git status
sudo poweroff
sudo nano /etc/inetd.conf
sudo systemctl restart inetd
ls
exit
source /home/uo294340/IS-2025/.venv/bin/activate
ps -ef
cd Maria/P3/
ps -ef
exit
ps -ef
nohup python3 udp_servidor3_con_ok.py &
exit
ps -ef
nohup python3 udp_servidor3_con_ok.py &
exit
cd IS-2025/Maria/P3
ps -ef
nohup python3 udp_servidor3_con_ok.py &
exit
cd IS-2025/Maria/P3
ps -ef | grep udp_servidor3_con_ok.py
exit
cd IS-2025/Maria/P3
ps -ef | grep udp_servidor3_con_ok.py
exit
/usr/bin/python3 /home/uo294340/IS-2025/Maria/P3/E1.py
/home/uo294340/IS-2025/.venv/bin/python /home/uo294340/IS-2025/Maria/P3/E1.py
/home/uo294340/IS-2025/.venv/bin/python /home/uo294340/IS-2025/Maria/P3/telnet1_ejemplo.py
cd Maria/P3/
source /home/uo294340/IS-2025/.venv/bin/activate
cd Maria/P3/
ps -ef
ps -ef | grep "udp"
source /home/uo294340/IS-2025/.venv/bin/activate
cd .
cd ..
sudo nano /etc/inetd.conf
sudo systemctl restart inetd
source /home/uo294340/IS-2025/.venv/bin/activate
/home/uo294340/IS-2025/.venv/bin/python /home/uo294340/IS-2025/Maria/P3/telnet2_lanza_servidor.py
ls
cd Maria/P3/
ls
cd .
cd ..
ls
/home/uo294340/IS-2025/.venv/bin/python /home/uo294340/IS-2025/Maria/P3/telnet2_lanza_servidor.py
source /home/uo294340/IS-2025/.venv/bin/activate
/home/uo294340/IS-2025/.venv/bin/python /home/uo294340/IS-2025/Maria/P3/telnet1_ejemplo.py
source /home/uo294340/IS-2025/.venv/bin/activate
/home/uo294340/IS-2025/.venv/bin/python /home/uo294340/IS-2025/Maria/P3/udp_servidor3_con_ok.py
sudo apt-get install telnetd
nano /etc/inetd.conf
sudo nano /etc/inetd.conf
sudo systemctl restart inetd
telnet localhost
ip a
sudo poweroff
ipconfig a
ip a
source /home/uo294340/IS-2025/.venv/bin/activate
/home/uo294340/IS-2025/.venv/bin/python /home/uo294340/IS-2025/Maria/P3/ssh_ejemplo_mal.py
source /home/uo294340/IS-2025/.venv/bin/activate
cd Maria/P3/
ls /etc/ssh
ls -l /etc/ssh
ps aux|grep sshd
ssh usuario@maquina
ssh uo294340@192.168.207.162
ssh-keygen -l -f /etc/ssh/ssh_host_ed25519_key.pb
''''bash
ls -l /etc/ssh/ssh_host_*ed25519*
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
ssh-keygen
ssh-keygen -t rsa -b 4096 -C "uo294340@192.168.207.162" -f ~/mi_clave_rsa
ssh-keygen -lf ~/mi_clave_rsa.pub -E sha256
ssh-copy-id -i ~/mi_clave_rsa.pub uo294340@192.168.207.162
ssh-copy-id -i ~/mi_clave_rsa.pub usuario@IP_o_hostname
ssh-copy-id -i ~/mi_clave_rsa.pub uo294340@192.168.207.162
puttygen ~/mi_clave_rsa -o ~/mi_clave_rsa.ppk
sh uo294340@192.168.207.162 'cat ~/.ssh/authorized_keys | grep -F "$(cat ~/mi_clave_rsa.pub)" && echo "ya está" || echo "no encontrada"'
ssh uo294340@192.168.207.162 'cat ~/.ssh/authorized_keys | grep -F "$(cat ~/mi_clave_rsa.pub)" && echo "ya está" || echo "no encontrada"'
ls -l ~/mi_clave_rsa* ~/.ssh /etc/ssh/ssh_host_*ed25519*
cat ~/.ssh/mi_clave_rsa.pub   
cat ~/home/mi_clave_rsa.pub   
cat ~ /mi_clave_rsa.pub   
cat ~/mi_clave_rsa.pub   
~/.ssh
cat ~/.ssh
cat ~/mis_claves/mi_clave_rsa.pu
cat ~/IS-2025/
~/IS-2025/
~/.ssh
cd ssh
cd ~/.ssh
ls
nano ~/.ssh/authorized_keys
cd ..
cd IS-2025/
cd IS-2025/Maria/P3
cd IS-2025/Maria/
cd P3
ls
cd ..
cd Maria/
cd P3
python3 -m venv ~/paramikoenv
sudo apt install python3.12-venv
python3 -m venv ~/paramikoenv
source ~/paramikoenv/bin/activate
pip install --upgrade pip
pip install paramiko
run ssh_ejemplo_mal.py 
source ~/paramikoenv/bin/activate
python -m pip show paramiko
python -c "import paramiko; print(paramiko.__file__, paramiko.__version__)"
                                                                        cd Maria/P3/
source ~/paramikoenv/bin/activate
pip install paramiko
code .
