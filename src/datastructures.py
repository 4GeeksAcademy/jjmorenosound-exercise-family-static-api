
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
        #   {
        #     'name': 'John',
        #     'last_name': last_name,
        #     'age': 33,
        #     'lucky_numbers': [7, 13, 22]
        #   },
        #   {
        #     'name': 'Jane',
        #     'last_name': last_name,
        #     'age': 35,
        #     'lucky_numbers': [10, 14, 3]
        #   },
        #   {
        #     'name': 'Jimmy',
        #     'last_name': last_name,
        #     'age': 5,
        #     'lucky_numbers': [1]
        #   }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
      member ['id']= self._generateId();
      member ['last_name'] = self.last_name;
      self._members.append(member)
      return member

    def delete_member(self, id):
       for i, member in enumerate(self._members):
        if member["id"] == id:
            return self._members.pop(i)
        return id
    
    def get_member(self, id):
        for member in self._members:
         if member["id"] == id:
            return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    
    def __repr__(self):
        return "family lastname: {self.lastname}"

    def serialize(self):
        return {
            'last_name': self.last_name,
            'members': self._members
        }