from flask_restful import Resource

lista_habilidades= ['Python','Java','Django']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades