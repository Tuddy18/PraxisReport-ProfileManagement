from flask_jwt_extended import jwt_required, get_jwt_identity

from app import app, auto
from flask import request, render_template, flash, redirect, url_for, session, jsonify
from passlib.hash import sha256_crypt
from sqlalchemy.orm import with_polymorphic

from app.domain import *

@app.route('/doc')
@auto.doc()
def documentation():
    '''
    return API documentation page
    '''
    return auto.html()

@app.route('/profile/create', methods=['POST'])
@auto.doc(args=['user identity (JWT_token)', 'profile (json)'])
@jwt_required
def create():
    '''
    Creates a new profile based on a json
    '''
    profile_json = request.get_json()

    if profile_json["type"] == "profifle":
        profile = Profile()
    elif profile_json["type"] == "studentprofile":
        profile = StudentProfile()
    elif profile_json["type"] == "professorprofile":
        profile = ProfessorProfile()
    elif profile_json["type"] == "mentorprofile":
        profile = MentorProfile()
    elif profile_json["type"] == "secretaryprofile":
        profile = SecretaryProfile()
    else:
        raise RuntimeError("unknown profile type")

    profile.update_from_dict(profile_json)

    db.session().add(profile)
    db.session().commit()

    entities = with_polymorphic(Profile, '*')
    profile = db.session().query(entities).filter_by(id=profile.id).first()

    resp = jsonify(profile.json_dict())
    return resp


@app.route('/profile/get-by-id', methods=['GET'])
@jwt_required
def get_by_id():
    id = request.args.get('id', type=int)

    entities = with_polymorphic(Profile, '*')
    profile = db.session().query(entities).filter_by(id=id).first()

    # use this for non polymorphic query
    # profile = Profile.query.filter_by(id=id).first()

    resp = jsonify(profile.json_dict())
    return resp

@app.route('/profile/get-all', methods=['GET'])
@auto.doc(args=['user identity (JWT_token)'])
@jwt_required
def get_all():
    '''
    Get all profiles
    '''
    entities = with_polymorphic(Profile, '*')
    profiles = db.session().query(entities).all()

    # use this for non polymorphic query
    # profile = Profile.query.all()

    resp = jsonify([profile.json_dict() for profile in profiles])
    return resp

@app.route('/profile/get-by-email', methods=['GET'])
@auto.doc(args=['user identity (JWT_token)'])
@jwt_required
def get_by_email():
    '''
    Returns the user profile based on the user identity
    '''
    # Get Form Fields
    # email = request.get_json()['email']
    email = get_jwt_identity()

    entities = with_polymorphic(Profile, '*')
    profile = db.session().query(entities).filter_by(email=email).first()

    # use this for non polymorphic query
    # profile = Profile.query.filter_by(email=email).first()

    if profile:
        resp = jsonify(profile.json_dict())
        return resp
    else:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

@app.route('/profile/get-by-email', methods=['POST'])
@auto.doc(args=['user identity (JWT_token)', 'profile email'])
@jwt_required
def post_by_email():
    '''
    Returns the user profile based on the user identity
    '''
    # Get Form Fields
    email = request.get_json()['email']
    # email = get_jwt_identity()

    entities = with_polymorphic(Profile, '*')
    profile = db.session().query(entities).filter_by(email=email).first()

    # use this for non polymorphic query
    # profile = Profile.query.filter_by(email=email).first()

    if profile:
        resp = jsonify(profile.json_dict())
        return resp
    else:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

@app.route('/profile/update', methods=['PUT'])
@auto.doc(args=['user identity (JWT_token)', 'profile (json)'])
@jwt_required
def update():
    '''
    Updates the profile
    '''
    profile_json = request.get_json()

    entities = with_polymorphic(Profile, '*')
    profile = db.session().query(entities).filter_by(id=profile_json['id']).first()

    profile.update_from_dict(profile_json)
    db.session().commit()
    profile = db.session().query(entities).filter_by(id=profile.id).first()

    resp = jsonify(profile.json_dict())
    return resp

@app.route('/profile/delete', methods=['DELETE'])
@auto.doc(args=['user identity (JWT_token)', 'id'])
@jwt_required
def delete():
    '''
    Deletes the profile
    '''
    id = request.args.get('id', type=int)

    entities = with_polymorphic(Profile, '*')
    profile = db.session().query(entities).filter_by(id=id).first()

    db.session().delete(profile)
    db.session().commit()

    resp = jsonify(profile.json_dict())
    return resp