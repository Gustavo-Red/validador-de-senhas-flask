from flask import Flask, request

def input_senha(password):
    maiusculas = 0
    minusculas = 0
    numeros = 0
    espacos = 0
    for i in password:
        if i.isupper():
            maiusculas += 1
        if i.islower():
            minusculas += 1
        if i.isdigit():
            numeros += 1
        if i == ' ':
            espacos += 1
    if (maiusculas > 0) and (minusculas > 0) and (numeros > 0) and (espacos == 0) and (len(password) >= 8):
        return True
    else:
        return False
        
app = Flask(__name__)

@app.route("/validate", methods=["POST"])
def validador():
    try:
        dados = request.get_json(silent=True)
        password = dados["password"]
        return {"valid": input_senha(password)}
    except (TypeError, KeyError):
        return {"error": "Invalid input. Please provide a JSON object with a 'password' field."}, 400
if __name__ == "__main__":
    app.run(debug=True)
