from flask import Flask, request, jsonify
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ambiente_hi_feriados.settings')
django.setup()

from datas.models import CustomUser, Feriados

app = Flask(__name__)

@app.route('/api/check_feriado', methods=['POST'])
def check_feriado():
    try:
        token = request.json.get('token')
        data_atual = request.json.get('data_atual')

        if token is None or data_atual is None:
            response = {
                'erro': 'Os campos Token e data_atual são obrigatórios.'
            }
            return jsonify(response), 400

        try:
            user = CustomUser.objects.get(token=token)
        except ObjectDoesNotExist:
            response = {
                'erro': 'Token inválido!'
            }
            return jsonify(response), 400

        try:
            data_atual = datetime.strptime(data_atual, '%d/%m/%Y').date()
        except ValueError:
            try:
                data_atual = datetime.strptime(data_atual, '%Y-%m-%d').date()
            except ValueError:
                response = {
                    'erro': 'Esta data está num formato inválido!'
                }
                return jsonify(response), 400

        feriado = Feriados.objects.filter(usuario=user, data=data_atual).first()

        if feriado:
            response = {
                'feriado': True,
                'description': feriado.description
            }
            return jsonify(response)
        else:
            response = {
                'feriado': False
            }
            return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()