echo "Instalando pacotes"
python3 pip install -r requirements.txt

echo "Criando banco de dados"
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Coletando arquivos estáticos"
python3 manage.py collectstatic --noinput