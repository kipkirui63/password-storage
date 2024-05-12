from flask_restx import Resource, Namespace
from marshmallow import schema , fields
from server import app, server


ns = Namespace('password_manager')

server.add_namespace(ns)





#*************************************servermodels*************************************#
users_schema = server.model('users', {
    'id' : fields.Integer(readOnly=True, description = 'id of user'),
    'username': fields.String(required=True, description = 'username of user'),
    'email' : fields.String(required=True)
})

users_input_schema = server.model('users_input', {
    'username': fields.String,
    'email': fields.String,

})

signup_input_schema = server.model('signup_input',{
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
    'repeatpassword':fields.String(required=True),
})


login_input_schema = server.model('login_input',{
    'username': fields.String(required=True),
    'password': fields.String(required=True),
})
