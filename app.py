from flask import Flask, jsonify, request
import json

app= Flask(__name__)

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
@app.route('/dev/<int:id>', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    metodo= request.method
    if metodo=='GET': 
        try:
            response= desenvolvedores[id]
        except IndexError:
            mensagem= 'Desenvolvedor de id {} não encontrado'.format(id)
            response={'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem= 'Erro desconhecido, contate o administrador'
            response={'status':'erro','mensagem':mensagem}
        return jsonify(response)

    elif metodo=='PUT':
        dados= json.loads(request.data)
        desenvolvedores[id]= dados
        return jsonify(dados)

    elif metodo=='DELETE':
        desenvolvedores.pop(id)
        mensagem= 'Registro {} deletado'.format(id)
        return jsonify({'status':'sucesso','mensagem':mensagem})

# Retorna todos os desenvolvedores ou cria novos
@app.route('/dev', methods=['POST', 'GET'])
def lista_desenvolvedor():
    metodo= request.method
    if metodo=='POST':
        dados= json.loads(request.data)
        desenvolvedores.append(dados)
        posicao= len(desenvolvedores)
        dados['id']=int(posicao)-1
        mensagem= 'Registro adicionado no id {}'.format(dados['id'])
        return jsonify({'status':'sucesso','mensagem':mensagem})
    elif metodo=='GET':
        return jsonify(desenvolvedores)

if __name__=='__main__':
    app.run(debug=True)

