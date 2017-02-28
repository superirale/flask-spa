from app import api, db, models, Resource, reqparse, marshal, marshal_with, fields, abort
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('email', type=str)
parser.add_argument('phone', type=str)

contact_fields = {
    'id': fields.String,
    'name': fields.String,
    'email': fields.String,
    'phone': fields.String
}

class ContactResource(Resource):
    "Contact Controller class"
    def get(self, contact_id):
        "get contact method"
        contact = models.Contact.query.get(contact_id)
        if not contact:
            abort(404, message="Contact {} doesn't exist".format(contact_id))
        return marshal(contact, contact_fields), 201

    def put(self, contact_id):
        "update contact"
        args = parser.parse_args()
        contact = models.Contact.query.get(contact_id)
        if not contact:
            abort(404, message="Contact {} doesn't exist".format(contact_id))
        contact.name = args.name
        contact.email = args.email
        contact.phone = args.phone
        db.session.commit()
        return marshal(contact, contact_fields), 201

    def delete(self, contact_id):
        "delete contact"
        contact = models.Contact.query.get(contact_id)
        if not contact:
            abort(404, message="Contact {} doesn't exist".format(contact_id))
        db.session.delete(contact)
        db.session.commit()
        return "", 204

class ContactListResource(Resource):
    @marshal_with(contact_fields)
    def get(self):
        "get all contact method"
        contacts = models.Contact.query.all()
        return [marshal(contact, contact_fields) for contact in contacts]

    def post(self):
        "create new contact"
        args = parser.parse_args()
        contact = models.Contact(args.name, args.phone, args.email)
        db.session.add(contact)
        db.session.commit()
        return marshal(contact, contact_fields), 201
                
api.add_resource(ContactListResource, '/contacts')
api.add_resource(ContactResource, '/contacts/<int:contact_id>')
