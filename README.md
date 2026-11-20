# Validador de Senhas — API em Flask

API REST em **Python** com **Flask** que recebe uma senha em JSON e informa se ela atende a um conjunto de regras de segurança. Requisições malformadas recebem um erro **400** com mensagem clara, sem derrubar o servidor.

Projeto desenvolvido como **desafio técnico**, para praticar desenvolvimento de APIs, requisições HTTP, JSON, validação de dados e tratamento de erros.

## Regras de validação

Uma senha é válida quando atende a **todas** as condições:

- ter pelo menos 8 caracteres;
- ter pelo menos 1 letra maiúscula;
- ter pelo menos 1 letra minúscula;
- ter pelo menos 1 número;
- não ter espaços.

## Endpoint

### `POST /validate`

**Requisição** (corpo em JSON):

```json
{
    "password": "Senha123"
}
```

**Respostas:**

| Situação | Status HTTP | Corpo da resposta |
|---|---|---|
| Senha atende às regras | `200` | `{"valid": true}` |
| Senha não atende às regras | `200` | `{"valid": false}` |
| Requisição inválida | `400` | `{"error": "Invalid input. Please provide a JSON object with a 'password' field."}` |

São consideradas **requisições inválidas**:

- corpo que não é JSON ou JSON malformado;
- JSON sem o campo `password`;
- campo `password` que não é texto (por exemplo, um número);
- JSON que não é um objeto (por exemplo, uma lista).

## Tratamento de erros

A rota usa `try/except` para capturar apenas os erros causados por uma requisição mal formada:

- `request.get_json(silent=True)` devolve `None` quando o corpo não é um JSON válido, em vez de interromper a requisição;
- acessar `dados["password"]` gera `TypeError` quando não há um objeto JSON e `KeyError` quando o campo não existe;
- percorrer uma senha que não é texto também gera `TypeError`.

Esses dois erros são tratados e viram uma resposta **400** (erro de quem fez a requisição). Os demais erros não são capturados de propósito, para que falhas no próprio código não fiquem escondidas.

## Como executar

Requisito: Python 3.10 ou superior.

```bash
git clone https://github.com/Gustavo-Red/validador-de-senhas-flask.git
cd validador-de-senhas-flask

python3 -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate

pip install -r requirements.txt
python3 validador.py
```

A API fica disponível em `http://127.0.0.1:5000`.

## Testando

### Pelo terminal, com `curl`

```bash
# Senha válida → 200 {"valid": true}
curl -X POST http://127.0.0.1:5000/validate \
     -H "Content-Type: application/json" \
     -d '{"password": "Senha123"}'

# Senha sem número → 200 {"valid": false}
curl -X POST http://127.0.0.1:5000/validate \
     -H "Content-Type: application/json" \
     -d '{"password": "SenhaABC"}'

# JSON sem o campo password → 400
curl -X POST http://127.0.0.1:5000/validate \
     -H "Content-Type: application/json" \
     -d '{}'

# Corpo que não é JSON → 400
curl -X POST http://127.0.0.1:5000/validate -d 'qualquer coisa'
```

### Pelo Postman

Com a API em execução:

1. Crie uma nova requisição e escolha o método **POST**.
2. Use a URL `http://127.0.0.1:5000/validate`.
3. Na aba **Body**, selecione **raw** e, no menu ao lado, **JSON**.
4. Escreva o corpo, por exemplo `{"password": "Senha123"}`, e clique em **Send**.

Casos de teste:

| Caso | Senha enviada | Resultado |
|---|---|---|
| Válida | `Senha123` | `{"valid": true}` |
| Sem letra maiúscula | `senha123` | `{"valid": false}` |
| Sem letra minúscula | `SENHA123` | `{"valid": false}` |
| Sem número | `SenhaABC` | `{"valid": false}` |
| Com espaço | `Senha 123` | `{"valid": false}` |
| Menos de 8 caracteres | `Sen1` | `{"valid": false}` |

Para ver o tratamento de erros no Postman, envie o corpo `{}` (sem o campo `password`) ou troque **JSON** por **Text** e envie um texto qualquer: a resposta deve ter status **400 BAD REQUEST** e a mensagem de erro.

## Como funciona

A função `input_senha` percorre cada caractere da senha contando letras maiúsculas, minúsculas, números e espaços. A senha só é válida se todas as contagens atenderem às regras e o tamanho for de pelo menos 8 caracteres.

A rota `/validate` lê o JSON da requisição, extrai o campo `password`, chama `input_senha` e devolve o resultado em JSON.

## Estrutura do projeto

```text
validador-de-senhas-flask/
├── validador.py       # aplicação Flask, regras de validação e endpoint
├── requirements.txt   # dependências (Flask)
├── .gitignore
└── README.md
```

## Tecnologias

- Python 3
- Flask
- HTTP / REST e JSON
- Postman e curl para testes

## Autor

**Gustavo Vieira dos Santos** — estudante de Ciência da Computação na UFMT.
