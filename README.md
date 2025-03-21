# 📘 API de Livros com Flask e Swagger

Este projeto é uma API simples para gerenciar livros, construída com **Flask**, utilizando **SQLite** como banco de dados e documentada com Swagger. 

## 🔥 Introdução
### 🎯 Funcionalidades
- **Cadastrar livros**: Cadastra livros na API.
- **Listar livros**: Retorna lista de livros cadastrados na API.
- **Atualizar livros**: Atualizar informaçãos de livros cadastrados na API de acordo com id do livro.
- **Deletar livros**: Remove livros cadastrados na API de acordo com id do livro.
- **Documentação**: Remove livros cadastrados na API de acordo com id do livro.


## ⚙️ Pré-requisitos
- Python instalado
- Pip (gerenciador de pacotes do Python)

## 🚀 Tecnologias Utilizadas
- **Linguagens**
  - Python
  - HTML

- **Bibliotecas e Frameworks**
  - Flask
  - SQLite3

- **Ferramentas**
  - Git
  - GitHub

## 📌 Instalação


### 1. Clone o repositório:
```sh
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Crie um ambiente virtual e ative-o:
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências:
```sh
pip install -r requirements.txt
```

## 📚 Endpoints da API

### 1️⃣ Listar Livros
```http
GET /livros
```
**Resposta:**
```json
{
  "mensagem": "Lista de livros"
}
```

### 2️⃣ Cadastrar Livro
```http
POST /livros
```
**Requisição:**
```json
{
  "title": "Livro Exemplo",
  "category": "Ficção",
  "author": "Autor X",
  "image_url": "http://exemplo.com/capa.jpg"
}
```
**Resposta:**
```json
{
  "mensagem": "Livro cadastrado com sucesso"
}
```

### 3️⃣ Atualizar Livro
```http
PUT /livros/{id}
```
**Requisição:**
```json
{
  "title": "Novo Título",
  "category": "Aventura",
  "author": "Novo Autor",
  "image_url": "http://exemplo.com/nova-capa.jpg"
}
```
**Resposta:**
```json
{
  "mensagem": "Livro atualizado com sucesso"
}
```

### 4️⃣ Deletar Livro
```http
DELETE /livros/{id}
```
**Resposta:**
```json
{
  "mensagem": "Livro removido com sucesso"
}
```


## ▶️ Executando o Projeto
Após instalar as dependências, inicie a API com:
```sh
python app.py
```
A API estará disponível em: `http://127.0.0.1:5000`

## 📌 Autor
**Tatyane Gonçalves** - [LinkedIn](https://www.linkedin.com/in/tatyanegoncalves/) - [GitHub](https://github.com/tatyanepgoncalves)

