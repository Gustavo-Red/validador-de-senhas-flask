# validador-de-senhas-flask
API REST simples desenvolvida em Python e Flask para validação de senhas.


# 🔐 Validador de Senhas — Flask

API REST desenvolvida em **Python** utilizando **Flask** para validar senhas de acordo com regras predefinidas.

## 📌 Sobre o projeto

Este projeto foi desenvolvido como solução para um desafio técnico de desenvolvimento de uma API utilizando Python e Flask.

A API recebe uma senha através de uma requisição HTTP `POST` e retorna `true` ou `false`, indicando se a senha atende aos critérios de validação.

## 🚀 Tecnologias utilizadas

* Python 3.10+
* Flask
* API REST
* JSON

## ✅ Regras de validação

Para ser considerada válida, a senha deve:

* Ter pelo menos **8 caracteres**;
* Conter pelo menos **1 letra maiúscula**;
* Conter pelo menos **1 letra minúscula**;
* Conter pelo menos **1 número**;
* **Não conter espaços**.

Essas são as regras definidas no desafio técnico.

## 📂 Estrutura do projeto

```text
validador-de-senhas-flask/
├── validador.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/validador-de-senhas-flask.git
cd validador-de-senhas-flask
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv .venv
```

### 3. Ative o ambiente virtual

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
python validador.py
```

A API estará disponível localmente em:

```text
http://127.0.0.1:5000
```

## 📡 Endpoint

### `POST /validate`

Recebe uma senha em formato JSON.

#### Requisição

```json
{
    "password": "Senha123"
}
```

#### Resposta para uma senha válida

```json
{
    "valid": true
}
```

#### Resposta para uma senha inválida

```json
{
    "valid": false
}
```

O endpoint e o formato das requisições e respostas seguem as especificações do desafio.

## 🧪 Exemplos de validação

| Senha       | Resultado               |
| ----------- | ----------------------- |
| `Senha123`  | ✅ Válida                |
| `senha123`  | ❌ Sem letra maiúscula   |
| `SENHA123`  | ❌ Sem letra minúscula   |
| `SenhaABC`  | ❌ Sem número            |
| `Senha 123` | ❌ Contém espaço         |
| `Sen1`      | ❌ Menos de 8 caracteres |

Os casos acima são os casos de teste definidos no desafio.

## 🎯 Objetivo

O projeto tem como objetivo praticar:

* Desenvolvimento de APIs com Flask;
* Requisições HTTP;
* Manipulação de JSON;
* Lógica de programação;
* Validação de dados;
* Organização e legibilidade de código.

## 👨‍💻 Autor

**Gustavo Vieira dos Santos**

Projeto desenvolvido para fins de estudo e prática em desenvolvimento backend com Python e Flask.

