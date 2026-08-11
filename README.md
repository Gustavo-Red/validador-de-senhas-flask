# Validador de Senhas — Flask API

API REST desenvolvida em **Python** utilizando **Flask** para validar senhas de acordo com um conjunto de regras predefinidas.

Este projeto foi desenvolvido como parte de um **desafio técnico**, com o objetivo de praticar conceitos básicos de desenvolvimento de APIs, requisições HTTP, JSON e lógica de programação.

## Sobre o desafio

O objetivo é desenvolver uma API capaz de receber uma senha através de uma requisição HTTP e informar se ela atende aos critérios estabelecidos.

A API possui o endpoint:

```text
POST /validate
```

A senha é enviada no corpo da requisição em formato JSON e a API retorna um objeto indicando se ela é válida.

## Tecnologias utilizadas

* Python 3.10+
* Flask
* JSON
* HTTP / REST API
* Postman para testes

## Regras de validação

Uma senha é considerada válida quando atende a todas as seguintes condições:

* Possuir pelo menos 8 caracteres;
* Possuir pelo menos 1 letra maiúscula;
* Possuir pelo menos 1 letra minúscula;
* Possuir pelo menos 1 número;
* Não possuir espaços.

Essas são as regras definidas no desafio técnico.

## Estrutura do projeto

```text
validador-de-senhas-flask/
│
├── validador.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `validador.py`

Contém a aplicação Flask, a lógica de validação da senha e o endpoint `POST /validate`.

### `requirements.txt`

Contém as dependências necessárias para executar o projeto.

### `.gitignore`

Define arquivos e diretórios que não devem ser enviados para o repositório.

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/validador-de-senhas-flask.git
```

Entre na pasta:

```bash
cd validador-de-senhas-flask
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv .venv
```

### 3. Ative o ambiente virtual

No Linux/macOS:

```bash
source .venv/bin/activate
```

No Windows:

```powershell
.venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a API

```bash
python3 validador.py
```

A aplicação será iniciada localmente em:

```text
http://127.0.0.1:5000
```

## Endpoint

### `POST /validate`

O endpoint recebe uma senha através de um objeto JSON.

**URL:**

```text
http://127.0.0.1:5000/validate
```

**Método:**

```text
POST
```

### Body

No Postman, selecione:

```text
Body → raw → JSON
```

Envie:

```json
{
    "password": "Senha123"
}
```

O formato da requisição segue a especificação do desafio.

### Resposta — senha válida

```json
{
    "valid": true
}
```

### Resposta — senha inválida

```json
{
    "valid": false
}
```

Esses são os formatos de resposta definidos no desafio.

## Testando com Postman

Com a aplicação Flask em execução, abra o Postman e crie uma requisição:

```text
POST http://127.0.0.1:5000/validate
```

No **Body**, selecione:

```text
raw → JSON
```

### Teste 1 — Senha válida

```json
{
    "password": "Senha123"
}
```

Resposta esperada:

```json
{
    "valid": true
}
```

### Teste 2 — Sem letra maiúscula

```json
{
    "password": "senha123"
}
```

Resposta:

```json
{
    "valid": false
}
```

### Teste 3 — Sem letra minúscula

```json
{
    "password": "SENHA123"
}
```

Resposta:

```json
{
    "valid": false
}
```

### Teste 4 — Sem número

```json
{
    "password": "SenhaABC"
}
```

Resposta:

```json
{
    "valid": false
}
```

### Teste 5 — Contém espaço

```json
{
    "password": "Senha 123"
}
```

Resposta:

```json
{
    "valid": false
}
```

### Teste 6 — Menos de 8 caracteres

```json
{
    "password": "Sen1"
}
```

Resposta:

```json
{
    "valid": false
}
```

Os casos de teste acima correspondem aos casos apresentados no desafio técnico.

## Como funciona

A função responsável pela validação percorre cada caractere da senha e verifica:

* Se é uma letra maiúscula;
* Se é uma letra minúscula;
* Se é um número;
* Se é um espaço.

Depois, a senha é considerada válida somente quando todas as condições são atendidas e possui pelo menos 8 caracteres.

A API recebe o JSON através da requisição, extrai o campo `password` e envia o resultado da validação como resposta.

## Objetivos de aprendizado

Este projeto foi desenvolvido para praticar:

* Lógica de programação;
* Desenvolvimento de APIs com Flask;
* Requisições HTTP;
* Métodos HTTP;
* Manipulação de JSON;
* Validação de dados;
* Estruturação de pequenos projetos Python;
* Testes de APIs utilizando Postman.

## Critérios do desafio

O desafio avalia principalmente:

* Organização do código;
* Uso básico do Flask;
* Lógica de programação;
* Clareza e legibilidade da solução.

## Autor

**Gustavo Vieira dos Santos**

Projeto desenvolvido para fins de estudo e prática em **Python, Flask e desenvolvimento de APIs REST**.
