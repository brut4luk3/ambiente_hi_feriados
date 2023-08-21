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

@app.route('/api/check_holiday', methods=['POST'])
def check_holiday():
    try:
        token = request.json.get('token')
        data_atual = request.json.get('data_atual')

        if token is None or data_atual is None:
            return jsonify({'error': 'Os campos Token e data_atual são obrigatórios.'}), 400

        try:
            user = CustomUser.objects.get(token=token)
        except ObjectDoesNotExist:
            return jsonify({'error': 'Token inválido!'}), 400

        try:
            data_atual = datetime.strptime(data_atual, '%d/%m/%Y').date()
        except ValueError:
            try:
                data_atual = datetime.strptime(data_atual, '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'error': 'Esta data está num formato inválido!'}), 400

        feriado = Feriados.objects.filter(usuario=user, data=data_atual).first()

        if feriado:
            return jsonify({'description': feriado.description})
        else:
            return jsonify({'message': 'Não há feriados nesta data!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()