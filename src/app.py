"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")


new_member = jackson_family.add_member (  {
             'name': 'John',
            
             'age': 33,
             'lucky_numbers':'7, 13, 22'
             })
newer_member = jackson_family.add_member (  {
             'name': 'Jane',
            
             'age': 35,
             'lucky_numbers':'10, 14, 3'
             })
newest_member = jackson_family.add_member (  {
             'name': 'Jimmy',
            
             'age': 5,
             'lucky_numbers':'1'
             })


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "members": members
    }


    return jsonify(response_body), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def handle_get_member_by_id(member_id):
    member = jackson_family.get_member(member_id)

    if member is None:
        return {"error": "Member not found"}, 404

    response_body = {
        'name': member['name'],
        'last_name': member['last_name'],
        'age': member['age'],
        'lucky_numbers': member['lucky_numbers']
    }
    return jsonify(response_body), 200

@app.route('/members', methods=['POST'])
def handle_add_member():
        member = request.get_json()

        if member is None:
            return 'Error body not found', 400
        if member ['name'] is None:
            return 'Error name is not found', 400
        if member ['age'] is None:
            return 'Error age is not found', 400
        if member ['lucky_numbers'] is None:
            return 'Error lucky numbers is not found', 400
        
        new_member = jackson_family.add_member(member)    
        return new_member

@app.route('/members/<int:member_id>', methods=['DELETE'])
def handle_delete_member(member_id):
    deleted_member = jackson_family.delete_member(member_id)
    
    if deleted_member is not None:
        return {
            "message": "Family member deleted successfully",
            "deleted_member": deleted_member
        }, 200
    else:
        return {"error": "Invalid member ID"}, 400

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
