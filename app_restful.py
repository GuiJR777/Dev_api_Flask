# imports do projeto
from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

# Linha construtora
app= Flask(__name__)
api= Api(app)

# Dados "D.B."
desenvolvedores= [
    {'nome':'Rafael',
     'habilidades':['Python','Flask'],
     'id':0
     },
    {'nome':'Guilherme',
     'habilidades':['Python','Django','Flask'],
     'id':1
     }
]

# Consulta, altera ou exclui desenvolvedores pelo id
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response= desenvolvedores[id]
        except IndexError:
            mensagem= 'Desenvolvedor de id {} não encontrado'.format(id)
            response={'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem= 'Erro desconhecido, contate o administrador'
            response={'status':'erro','mensagem':mensagem}
        return response

    def put(self, id):
        dados= json.loads(request.data)
        desenvolvedores[id]= dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        mensagem= 'Registro {} deletado'.format(id)
        return {'status':'sucesso','mensagem':mensagem}

# Retorna todos os desenvolvedores ou cria novos
class ListaDesenvolvedores(Resource):
    def post(self):
        dados= json.loads(request.data)
        desenvolvedores.append(dados)
        posicao= len(desenvolvedores)
        dados['id']=int(posicao)-1
        mensagem= 'Registro adicionado no id {}'.format(dados['id'])
        return {'status':'sucesso','mensagem':mensagem}

    def get(self):
        return desenvolvedores

# Registro de funções da API
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/hab/')

# Executor
if __name__=='__main__':
    app.run(debug=True)