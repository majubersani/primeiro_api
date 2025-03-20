from flask import Flask

app = Flask(__name__)


# @app.route('/<informacao_texto>')
# def hello_name(informacao_texto):
#     return f'Hello, {informacao_texto}!'

@app.route('/soma/<int:numero1>+<float:numero2>')
def soma(numero1, numero2):
    return f'{numero1} + {numero2} = {numero1 + numero2}'

@app.route('/subtracao/<int:numero1>-<float:numero2>')
def subtracao(numero1, numero2):
    return f'{numero1}  {numero2} = {numero1 - numero2}'

@app.route('/multiplicacao/<int:numero1>*<float:numero2>')
def multiplicacao (numero1, numero2):
    return f'{numero1} * {numero2} = {numero1 * numero2}'

@app.route('/divisao/<int:numero1>/<float:numero2>')
def divisao(numero1, numero2):
    return f'{numero1} / {numero2} = {numero1 / numero2}'

@app.route('/verificar_par_impar/<int:numero1>')
def verificar_par_impar(numero1):
    if numero1 % 2 == 0:
        return f'O número {numero1} é par'
    elif numero1 % 2 != 1:
        return f'O numero {numero1}, é impar'
    else:
        print("algo deu errado")




# @app.route('/')
# def soma(numero1, numero2):
#     adicao = numero1 + numero2
#     return print("O resultado da edição é", adicao)
#
# @app.route('/')
# def subtracao(numero1, numero2):
#     subtracao = numero1 - numero2
#     return print("O resultado da subtração é", subtracao)
#
# @app.route('/')
# def multiplicacao(numero1, numero2):
#     multiplicacao = numero1 * numero2
#     return print("O resultado da multiplicacao é", multiplicacao)
#
# @app.route('/')
# def divisao(numero1, numero2):
#     divisao = numero1 * numero2
#     return print("O resultado da divisão é", divisao)


if __name__ == '__main__':
    app.run(debug=True)