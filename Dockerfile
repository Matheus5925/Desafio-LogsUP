# Usando imagem oficial do Python
FROM python:3.11

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do projeto
COPY . .

# Expor a porta do Django
EXPOSE 8000

# Garantir que as migrações sejam feitas apenas quando o container for iniciado
# O comando a seguir será executado quando o container for iniciado
CMD python manage.py makemigrations core && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
