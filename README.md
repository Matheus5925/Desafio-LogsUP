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
- Docker

### Passos

1. Clone o repositório:

    ```bash
    git clone https://github.com/seuusuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Suba os containers com o comando:

    ```
    docker-compose up
    ```

3. Crie um superusuário:

    ```
    docker-compose  exec -it web bash # Comando para interagir com o bash do container
    python manage.py createsuperuser # Criar super usuário
    ```

4. Criar os grupos:
```
  É necessário a criação de 3 grupos: SUPERVISORS, ANALYSTS e CLIENTS. Esses grupos tem as permissões que citamos anteriormente que são os requisitos do desafio técnico.
```

5. O sistema estará rodando em `http://127.0.0.1:8000/` por padrão.

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
```

### 2. **Buscar Produto**

- **URL:** `/api/v1/products`
- **Header:** 
```json
{
    "Authorization": "Bearer <token>"
}
```
- **Método:** `GET`
- **Parâmetros:**
  - `name`: Nome do produto
**Exemplo de requisição:**
```query
http://127.0.0.1:8000/api/v1/products?name=Teclado

```
