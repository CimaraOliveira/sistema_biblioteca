# sistema_biblioteca
CRUD simples utilizando CBV Python com Django cadastro de livros de uma biblioteca


Heroku:  https://sistem-biblioteca.herokuapp.com/

Api Heroku: https://sistem-biblioteca.herokuapp.com/api/

Api local: http://127.0.0.1:8000/api/ 


Orientações para execução do projeto em uma máquina local.

1 - Clone esse repositório.

2 - Crie um virtualenv com Python 3.

3 - Ative o virtualenv.

4 - Rode as migrações.

5 - Rode o projeto

Windows:

git clone https://github.com/CimaraOliveira/sistema_biblioteca.git

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

Linux:

git clone https://github.com/CimaraOliveira/sistema_biblioteca.git

sudo apt install python3-venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
