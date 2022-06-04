"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint, redirect
from api.models import db, Coordinator
from api.models import db, Event
from api.models import db, Guest
from api.models import db, GuestPermission
from api.models import db, Event_Coordinator
from api.models import db, Permission
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, decode_token
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

api = Blueprint('api', __name__)


@api.route('/coordinator', methods=['POST'])
def create_coordinator():
    coordinator = request.get_json()
    if request.json is None:
        return jsonify({"msg": "Missing the payload"}), 400
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    coordinator = Coordinator(email=email, password=password)
    db.session.add(coordinator)
    db.session.commit()
    return jsonify(coordinator.serialize())


@api.route('/coordinator', methods=['GET'])
@jwt_required()
def coordinator():
    current_coordinator_id = get_jwt_identity()
    coordinator = Coordinator.query.get(current_coordinator_id)

    return jsonify({"id": coordinator.id, "email": coordinator.email}), 200


# QR Code Redirect for dynamic QR code generator. redirect for guest and for coordinator
@api.route('/redirect', methods=['GET'])
@jwt_required()
def redirect_qr_scan():

    user_id = get_jwt_identity()
    coordinator = Coordinator.query.filter_by(id=user_id).first()
    guest = Guest.query.filter_by(id=user_id).first()
    if guest is not None:
        return redirect(os.getenv("FRONTEND_URL", "") + f"/guest_scan?token={request.args.get('token')}", code=302)
    if coordinator is not None:
        return redirect(os.getenv("FRONTEND_URL", "") + f"/coordinator_scan?token={request.args.get('token')}", code=302)

    return (f"I have no idea who you are {user_id}")


# guest registration
# send email after guest registration
@api.route('/guest', methods=['POST'])
def create_guest():
    guests = request.get_json()
    if request.json is None:
        return jsonify({"msg": "Missing the payload"}), 400
    email = request.json.get('email', None)
    name = request.json.get('name', None)
    image = request.json.get('image', None)
    event_id = request.json.get('event_id', None)
    guest = Guest(name=name, email=email, event_id=event_id, image=image)
    db.session.add(guest)
    db.session.commit()
    access_token = create_access_token(identity=guest.id)
    guest.guest_hash = access_token
    db.session.add(guest)
    db.session.commit()
    message = Mail(
        from_email='from_email@example.com',
        to_emails=email,
        subject='Welcome to Safety.Net',
        html_content=os.getenv("FRONT_URL", "") + f"/IDcard/{access_token}")
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
    return jsonify(guest.serialize())


@api.route('/guest', methods=['GET'])
def guest():
    guests = Guest.query.all()
    all_guests = list(map(lambda x: x.serialize(), guests))
    return jsonify(all_guests), 200


@api.route('/guest/<int:guest_id>', methods=['GET'])
def getGuest(guest_id):
    guests = Guest.query.get(guest_id)
    if guests is None:
        raise APIException('Guest not found', status_code=404)
    return jsonify(guests.serialize()), 200


@api.route('/guest/token/<string:token>', methods=['GET'])
def get_user_from_token(token):
    identity = decode_token(token)
    print("identity", identity)

    guests = Guest.query.get(identity["sub"])
    if guests is None:
        raise APIException('Guest not found', status_code=404)
    return jsonify(guests.serialize()), 200


@api.route('/guest/<int:guest_id>', methods=['PUT'])
def edit_guest(guest_id):
    ind_guest = Guest.query.get(guest_id)
    body = request.get_json()
    if ind_guest is None:
        raise APIException('Guest not found', status_code=404)
    if "name" in body:
        ind_guest.name = body["name"]
    if "email" in body:
        ind_guest.email = body["email"]
    db.session.commit()
    return jsonify(ind_guest.serialize())


@api.route('/guest/<int:guest_id>', methods=['DELETE'])
def delete_guest(guest_id):
    ind_guest = Guest.query.get(guest_id)
    if ind_guest is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(ind_guest)
    db.session.commit()
    return jsonify(ind_guest)


@api.route('/event', methods=['POST'])
def create_event():
    body = request.get_json()
    event = Event()
    event.event_name = body['Event_Name']
    db.session.add(event)
    db.session.commit()
    return jsonify(event.serialize())


@api.route('/event', methods=['GET'])
def event():
    event_name = request.json.get('event_name', None)
    event_id = request.json.get('event_Id', None)
    return jsonify(event)


@api.route('/permission', methods=['POST'])
def create_permission():
    permission = Permission(event_id=event_id, guest=guest,
                            vip=vip, valet=valet, dinner=dinner)
    db.session.add(permission)
    db.session.commit()
    return jsonify(permission.serialize())


@api.route('/permission', methods=['GET'])
def permission():
    event_id = request.json.get('event_Id', None)
    vip = request.json.get('vip', None)
    valet = request.json.get('valet', None)
    dinner = request.json.get('dinner', None)
    guest = request.json.get('guest', None)
    return jsonify(permission)


# @api.route('/permission', methods=['DELETE'])
# def delete_permission():
#     permission = Permission.query.get(permission.id)
#     if permission is None:
#         raise APIException('Permission not found', status_code=404)
# db.session.delete(permission)
# db.session.commit()


@api.route('/token', methods=['POST'])
def create_token():
    if request.json is None:
        raise APIException("Missing the payload")
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    coordinator = Coordinator.query.filter_by(
        email=email, password=password).first()
    if coordinator is None:
        raise APIException("Wrong email and password", 401)
    access_token = create_access_token(identity=coordinator.id)
    return jsonify({"token": access_token, "coordinator_id": coordinator.id})


@api.route('/contactUs', methods=['POST'])
def contact_message():
    contactUs = request.get_json()
    if request.json is None:
        return jsonify({"msg": "Missing the payload"}), 400
    email = request.json.get('email', None)
    name = request.json.get('name', None)
    message = request.json.get('message', None)
    contactUs = ContactUs(name=name, email=email, message=message)
    db.session.add(contactUs)
    db.session.commit()
    message = Mail(
        from_email='from_email@example.com',
        to_emails=email,
        subject='Welcome to Safety.Net',
        html_content=os.getenv("FRONT_URL", ""))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
    return jsonify(guest.serialize())
