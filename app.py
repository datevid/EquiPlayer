from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from AppRoot.model.models import Player,db
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from AppRoot.model.database import create_database


app = Flask(__name__)
# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Cambia la URL de conexión según tu base de datos
#db = SQLAlchemy(app)
db.init_app(app)

@app.route('/players', methods=['POST'])
def create_player():
    data = request.json
    fullname = data['fullname']
    sizeplayer = data['sizeplayer']

    player = Player(fullname=fullname, sizeplayer=sizeplayer)
    db.session.add(player)
    db.session.commit()

    return jsonify({'message': 'Player created successfully'})


@app.route('/players', methods=['GET'])
def get_all_players():
    players = Player.query.all()
    result = []
    for player in players:
        player_data = {
            'id': player.id,
            'fullname': player.fullname,
            'sizeplayer': player.sizeplayer
        }
        result.append(player_data)
    return jsonify(result)


@app.route('/player/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = Player.query.get(player_id)
    if not player:
        return jsonify({'message': 'Player not found'})

    player_data = {
        'id': player.id,
        'fullname': player.fullname,
        'sizeplayer': player.sizeplayer
    }
    return jsonify(player_data)


@app.route('/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    player = Player.query.get(player_id)
    if not player:
        return jsonify({'message': 'Player not found'})

    data = request.json
    fullname = data['fullname']
    sizeplayer = data['sizeplayer']

    player.fullname = fullname
    player.sizeplayer = sizeplayer
    db.session.commit()

    return jsonify({'message': 'Player updated successfully'})


@app.route('/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    player = Player.query.get(player_id)
    if not player:
        return jsonify({'message': 'Player not found'})

    db.session.delete(player)
    db.session.commit()

    return jsonify({'message': 'Player deleted successfully'})


if __name__ == '__main__':
    app.run()
