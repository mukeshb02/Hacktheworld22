from werkzeug.security import generate_password_hash
from app import db, app
from flask import jsonify, request
from ..models.users import Users, user_schema, users_schema


def post_user():
    # get the post data
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    # instantiate the user model
    hashed_password = generate_password_hash(password)
    user = Users(username, hashed_password, name, email)

    try:
        # insert the user in the database
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'New user created!', 'data': result}), 201

    except Exception as e:
        app.logger.error(e)
        return jsonify({'message': 'Something went wrong'}), 500


def get_users():
    users = Users.query.all()
    if users:
        return jsonify({'message': 'Sucessfully fetched', 'data': users_schema.dump(users)}), 200

    app.logger.debug(users)
    return jsonify({'message': 'Not found'}), 404


def update_user(id):
    user = Users.query.get(id)
    if not user:
        app.logger.debug('User not found')
        return jsonify({'message': 'User not found'}), 404

    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']
    hashed_password = generate_password_hash(password)

    try:
        user.username = username
        user.password = hashed_password
        user.name = name
        user.email = email

        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'Sucessfully updated', 'data': result}), 200

    except Exception as e:
        app.logger.error(e)
        return jsonify({'message': 'Something went wrong'}), 500


def get_user(id):
    user = Users.query.get(id)
    if not user:
        app.logger.debug('User not found')
        return jsonify({'message': 'User not found'}), 404

    return jsonify({'message': 'Sucessfully fetched', 'data': user_schema.dump(user)}), 200


def delete_user(id):
    user = Users.query.get(id)
    if not user:
        app.logger.debug('User not found')
        return jsonify({'message': 'User not found'}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Sucessfully deleted'}), 200
    except Exception as e:
        app.logger.error(e)
        return jsonify({'message': 'Something went wrong'}), 500


def user_by_username(username):
    try:
        return Users.query.filter_by(username=username).first()
    except:
        return None
