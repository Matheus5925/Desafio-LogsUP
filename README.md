# Desafio Técnico LogsUp

## Descrição

Este desafio técnico tem como objetivo uma plataforma onde os usuários podem cadastrar e gerenciar produtos

Exemplo:
Este projeto é uma aplicação de **gerenciamento de produtos**, onde usuários podem visualizar, adicionar, editar e excluir produtos. 

---

## Funcionalidades

- **Cadastro de Usuário:** Permite que novos usuários se registrem no sistema.
- **Autenticação com JWT:** Utiliza tokens JWT para autenticar usuários e garantir a segurança nas requisições.
- **Gestão de Produtos:** Permite aos usuários visualizar, adicionar, editar e excluir produtos.
- **Filtragem de Produtos:** Opção para filtrar produtos por nome.
- **Logout:** Funcionalidade para o usuário desconectar-se da aplicação.
- **Permissões:** Há 3 permissões diferentes. ANALISTAS, SUPERVISORES e CLIENTS.

---

## Tecnologias Utilizadas

- **Backend:** Django, Django REST Framework, djangorestframework-simplejwt
- **Frontend:** HTML e Django
- **Banco de Dados:** PostgreSQL 
- **Autenticação:** JWT 

---

## Instalação

### Pré-requisitos

- Python 3.x
- Pip
- Docker

### Passos

1. Clone o repositório:

    ```bash
    git clone https://github.com/seuusuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie e ative o ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Realize as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário (opcional para acessar o painel de administração do Django):

    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

7. O sistema estará rodando em `http://127.0.0.1:8000/` por padrão.

---

## Endpoints da API

### 1. **Login (Obter Access Token)**

- **URL:** `/api/token/`
- **Método:** `POST`
- **Parâmetros:**
  - `username`: Nome de usuário
  - `password`: Senha do usuário
- **Resposta:**
  - `access`: Token de acesso (usado nas requisições autenticadas)
  - `refresh`: Token de atualização (usado para renovar o `access_token`)

**Exemplo de requisição:**
```json
{
  "username": "usuario",
  "password": "senha"
}
