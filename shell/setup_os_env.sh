#setup ubuntu env
apt-get update
apt-get install -y apt-transport-https
apt-get install -y ca-certificates
apt-get install -y curl
apt-get install -y apt-transport-https
apt-get install -y software-properties-common
apt-get install -y gcc
apt-get install -y g++
apt-get install -y make
apt-get install -y git

#setup python3.6 env
add-apt-repository ppa:deadsnakes/ppa
wget https://bootstrap.pypa.io/get-pip.py
apt-get update
apt-get install python3.6
mv /usr/bin/python /usr/bin/python.backup
ln -s /usr/bin/python3.6 /usr/bin/python
python get-pip.py 

#setup nodejs env
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
apt-get install -y nodejs
apt-get install -y build-essential
apt-get install -y sqlite3
#npm i -g npm #do not excute this upgrade, this will make "npm install sqlite3" failed, and current version is 5.6.0
npm install -y -g pm2