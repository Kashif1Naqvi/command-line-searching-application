import unittest
import json

class SearchTest(unittest.TestCase):
    # searching term value testing for tickets
    
    def get_files(self):
        ticket_file = open('tickets.json', 'r')
        tickets = json.loads(ticket_file.read())
        ticket_file.close()

        organization_file = open('organizations.json', 'r')
        organizations = json.loads(organization_file.read())
        organization_file.close()
        
        users_file = open('users.json', 'r')
        users = json.loads(users_file.read())
        users_file.close()

        return {
            "tickets": tickets,
            "organizations": organizations,
            "users": users
        }

    def search_tickets_term_value(self):
        term = "_id"
        value = "436bf9b0-1147-4c0a-8439-6f79833bff5b"
        
        get_data = self.get_files()
        tickets = get_data["tickets"]
        organizations = get_data["organizations"]


        expected_result = {'_id': '436bf9b0-1147-4c0a-8439-6f79833bff5b', 'url': 'http://initech.aiworks.com/api/v2/tickets/436bf9b0-1147-4c0a-8439-6f79833bff5b.json', 'external_id': '9210cdc9-4bee-485f-a078-35396cd74063', 'created_at': '2016-04-28T11:19:34 -10:00', 'type': 'incident', 'subject': 'A Catastrophe in Korea (North)', 'description': 'Nostrud ad sit velit cupidatat laboris ipsum nisi amet laboris ex exercitation amet et proident. Ipsum fugiat aute dolore tempor nostrud velit ipsum.', 'priority': 'high', 'status': 'pending', 'submitter_id': 38, 'assignee_id': 24, 'organization_id': 116, 'tags': ['Ohio', 'Pennsylvania', 'American Samoa', 'Northern Mariana Islands'], 'has_incidents': False, 'due_at': '2016-07-31T02:37:50 -10:00', 'via': 'web', 'organization_name': 'Zentry'}

        current_result = {}
        for ticket in tickets:
            if(term in ticket):
                if(ticket[term] == value):
                    current_result = ticket
                    for organization in organizations:
                        if(current_result['organization_id'] == organization["_id"]):
                            current_result['organization_name'] =  organization['name']
        
        self.assertDictEqual(current_result, expected_result)


    # searching term value testing for users
    def search_users_term_value(self):
        term = "_id"
        value = 1

        get_data = self.get_files()
        users = get_data["users"]
        organizations = get_data["organizations"]



        expected_result = {'_id': 1, 'url': 'http://initech.aiworks.com/api/v2/users/1.json', 'external_id': '74341f74-9c79-49d5-9611-87ef9b6eb75f', 'name': 'Francisca Rasmussen', 'alias': 'Miss Coffey', 'created_at': '2016-04-15T05:19:46 -10:00', 'active': True, 'verified': True, 'shared': False, 'locale': 'en-AU', 'timezone': 'Sri Lanka', 'last_login_at': '2013-08-04T01:03:27 -10:00', 'email': 'coffeyrasmussen@flotonic.com', 'phone': '8335-422-718', 'signature': "Don't Worry Be Happy!", 'organization_id': 119, 'tags': ['Springville', 'Sutton', 'Hartsville/Hartley', 'Diaperville'], 'suspended': True, 'role': 'admin', 'organization_name': 'Multron'}

        current_result = {}
        for user in users:
            if(term in user):
                if(user[term] == value):
                    current_result = user
                    for organization in organizations:
                        if(current_result['organization_id'] == organization["_id"]):
                            current_result['organization_name'] =  organization['name']
        
        self.assertDictEqual(current_result, expected_result)

    # searching term value testing for organizations
    def search_organizations_term_value(self):
        term = "_id"
        value = 119
        # open file tickets.json for reading
        get_data = self.get_files()
        organizations = get_data["organizations"]


        expected_result = {'_id': 119, 'url': 'http://initech.aiworks.com/api/v2/organizations/119.json', 'external_id': '2386db7c-5056-49c9-8dc4-46775e464cb7', 'name': 'Multron', 'domain_names': ['bleeko.com', 'pulze.com', 'xoggle.com', 'sultraxin.com'], 'created_at': '2016-02-29T03:45:12 -11:00', 'details': 'Non profit', 'shared_tickets': False, 'tags': ['Erickson', 'Mccoy', 'Wiggins', 'Brooks']}
        
        current_result = {}
        for organization in organizations:
            if(term in organization):
                if(organization[term] == value):
                    current_result = organization
        
        self.assertDictEqual(current_result, expected_result)





if __name__ == '__main__':
    unittest.main()

        