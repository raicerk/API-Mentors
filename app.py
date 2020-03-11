from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Mentis(Resource):
    def get(self):
        return jsonify({
            'saludo': 'hola'
        })

    def post(self):
        last_name = request.json['nombre']
        first_name = request.json['apellido']
        return jsonify({
            'status': 'registro almacenado correctamente'
        })


class Mentores(Resource):
    def get(self):
        return jsonify({
            'data': 'otro',
            'masdata': 1
        })


class Registros(Resource):
    def get(self, registro_id):
        return jsonify({
            'data': True,
            'id_registro': registro_id
        })



api.add_resource(Mentis, '/mentis')  # Route_1
api.add_resource(Mentores, '/mentores')  # Route_2
api.add_resource(Registros, '/registro/<registro_id>')  # Route_3


if __name__ == '__main__':
    app.run(port='5000')
