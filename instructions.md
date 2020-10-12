docker run -it "ubuntu"
apt update
apt install -y gcc cmake libmariadb-dev nano git wget software-properties-common default-jre mysql-server python3-pip

8
27

apt-add-repository -y ppa:rael-gc/rvm
apt update
apt install -y rvm
source /usr/share/rvm/scripts/rvm
rvm install 2.0
rvm --default use 2.0
mkdir sql-to-graph
cd sql-to-graph
gem install mysql2
gem install minitest -v 5.12.0
gem install ffi -v 1.12.2
gem install neo4j-core -v 8.1.4
gem install neo4apis-activerecord -v 0.7.0
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | apt-key add -
echo 'deb https://debian.neo4j.com stable latest' | tee -a /etc/apt/sources.list.d/neo4j.list
apt update
apt install neo4j=1:4.1.3
/etc/init.d/mysql start
mkdir config
nano config/database.yml

development:
  adapter: mysql2
  encoding: utf8mb4
  reconnect: false
  database: movies
  pool: 5
  username: user
  password: correcthorsebatterystaple

git clone https://github.com/ThePythonist/DatabasesProject
cd DatabasesProject
pip3 install mysql-connector-python
mysql_secure_installation

Y
0
root
root
Y
N
N
N
Y

mysql

CREATE USER 'user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'correcthorsebatterystaple';
CREATE DATABASE movies CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'user'@'localhost' WITH GRANT OPTION;
exit

python3 ./query.py
cd ..
neo4apis activerecord all_tables --identify-model --import-all-associations

