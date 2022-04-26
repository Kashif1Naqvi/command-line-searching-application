import json

# General template for user guideline
template = """
Welcome to Zendesk Search
Type 'quit' to exit at any time, Press 'Enter' to continue

            Select search options:
              * Press 1 to search Zendesk
              * Press 2 to view a list of searchable fields
              * Type 'quit' to exit
"""

print(template)


class Search:
    def __init__(self, selection):
        self.selection = selection

    # display result according to user selection
    def options(self):
      
      # if user chose nothing just press enter then ask for accurate options
      if(self.selection == ''):
            self.selection = input("Please choose accurate options.")
      
      # if user press 1 then enter in search Zendesk
      if(self.selection == '1'):
        
        # open file organizations.json for reading
        organization_file = open('organizations.json', 'r')

        # open file users.json for reading
        user_file = open('users.json', 'r')
        
        # open file tickets.json for reading
        ticket_file = open('tickets.json', 'r')
        
        # convert from json to python dictionary
        users = json.loads(user_file.read())
        organizations = json.loads(organization_file.read())
        tickets = json.loads(ticket_file.read())

        template_str = """"
        Select 1) User or Select 2)  Tickets or 3) Organizations
        """

        #template for user information for search in Zendesk
        print(template_str)

        #Ask from user for searching in zendesk e.g seach tickets or users or organizations
        selection_search = input()
        
      
        # if user chose nothing just press enter then ask for accurate options
        if(selection_search == ''):
          
            selection_search = input("Please choose accurate options.")

        # if user press 1 then search for users  
        if(selection_search == '1'):
          
          # call function for users search
          self.search_users(users, tickets, organizations)

        # if user press 1 then search for tickets
        elif(selection_search == '2'):
          
          # call function for tickets search
          self.search_tickets(users, tickets, organizations)

        # if user press 1 then search for organizations
        elif(selection_search == '3'):
          
          # call function for organizations search
          self.search_organizations(users, tickets, organizations)

        # if user type quit then exit from Zendesk
        elif(selection_search == 'quit'):
          print("exit")
      
      # if user press 2 then see the searchable fields in Zendesk
      elif(self.selection == '2'):
        
        # call function for viewing searchable fields
        self.searchable_fields()
      
      # if user type quit then exit from Zendesk
      elif(self.selection == 'quit'):
        
        print("exit")
      

    def search_users(self, users, tickets, organizations):
      
      # term mean user key from users.json file object e.g _id
      term = input("Enter search term ")

      # value mean user value from users.json file object e.g 1
      value = input("Enter search value ")
        
      # flag for testing if False then search is not matched
      check = True

      # emptry dictionary for declaration 
      result = {}

      #loop through user
      for user in users:
        
        # check term in user
        if(term in user):

          # check user entered value matched with user term valye e.g user[term] = 5 value = 5
          if(str(user[term]) == value):
            
            # if match then return the filtered data
            result = user

            #if data is matched then we False the check flag
            check = False

          if(term == 'tags'):
            
            #check value exist in tags list or not
            if(value in str(user[term])):
            
              # if match then return the filtered data
              result = user

              #if data is matched then we False the check flag
              check = False

      # we check if data not matched then show message for user understanding
      if(check):
        
        # Searching users template for user guideline

        template_str = f"""Searching users for {term} with  a value of {value} \nNo results found"""
        print(template_str)
      
      # we add this for tickets counter
      index = 0

      #if result is not emptry dict
      if(result):

        #loop through organization
        for organization in organizations:
          
          # checking here organization id matched with result id
          if(organization['_id'] == result['organization_id']):

            #add new key add assign organization name value 
            result['organization_name'] =  organization['name']
        
        #loop through tickets
        for ticket in tickets:
          
          #if ticket key have no organization_id we add this check for preventing keyError 
          if('organization_id' in ticket):
            
            # checking here ticket organization id matched with result organization_id
            if(ticket['organization_id'] == result['organization_id']):
              
              # increment index at every iteration in this block
              index += 1

              # populate key with index in result dictionary 
              result[f'ticket_{index}'] = ticket['subject']

        # geting key from dict
        for key in result:
          # :<30 for indentation
          print(f"{key:<30} {result[key]}")

          
    def search_tickets(self, users, tickets, organizations):
      
       # term mean user key from users.json file object e.g _id
      term = input("Enter search term ")

      # value mean user value from users.json file object e.g 1
      value = input("Enter search value ")
      
      #emptry dictionary for declaration 
      result = {}

      # we check if data not matched then show message for user understanding
      check = True

      # loop through tickets
      for ticket in tickets:

        #check term exist in ticket list or not
        if(term in ticket):

          # check user entered value matched with user term valye e.g user[term] = 5 value = 5
          if(str(ticket[term]) == value):

            # if match then return the filtered data
            result = ticket

            #if data is matched then we False the check flag
            check = False

          if(term == 'tags'):
            
            #check value exist in tickets or not
            if(value in str(ticket[term])):

              # if match then return the filtered data
              result = ticket

              #if data is matched then we False the check flag
              check = False

      # we check if data not matched then show message for user understanding
      if(check):

        # Searching tickets template for user guideline
        template_str = f"""Searching tickets for {term} with  a value of {value} \nNo results found"""
        print(template_str)
      
      #if result is not emptry dict
      if(result):

        #loop through organization
        for organization in organizations:

          # checking here organization id matched with result id
          if(organization['_id'] == result['organization_id']):
            result['name'] = organization['name']
        
        #loop through users
        for user in users:

          #if user key have no organization_id we add this check for preventing keyError 
          if('organization_id' in user):

            # checking here user organization id matched with result organization_id
            if(user['organization_id'] == result['organization_id']):

              result['user_name'] =  user['name']
          
        # geting key from dict      
        for key in result:
          # :<30 for indentation
          print(f"{key:<30} {result[key]}")
      

    def search_organizations(self, users, tickets, organizations):
      
      # term mean user key from organizations.json file object e.g _id
      term = input("Enter search term ")

      # value mean organizations value from organizations.json file object e.g 1
      value = input("Enter search value ")

      # emptry dictionary for declaration 
      result = {}

      # we check if data not matched then show message for user understanding
      check = True

      #loop through organization
      for organization in organizations:
        
        #check term exist in organization list or not
        if(term in organization):

          # check user entered value matched with user term valye e.g user[term] = 5 value = 5
          if(str(organization[term]) == value):
            result = organization

            #if data is matched then we False the check flag
            check = False

          if(term == 'tags'):

            #check value exist in tags list or not
            if(value in str(organization[term])):

              # if match then return the filtered data
              result = organization
              #if data is matched then we False the check flag
              check = False

          if(term == "domain_names"):

            #check value exist in tags list or not
            if(value in str(organization[term])):
              
              result = organization
              
              #if data is matched then we False the check flag
              check = False

         
      # we check if data not matched then show message for user understanding
      if(check):

        # Searching organization template for user guideline

        template_str = f"""Searching organization for {term} with  a value of {value} \nNo results found"""
        print(template_str)

      # we add this for tickets counter
      index = 0

      #if result is not emptry dict
      if(result):
        for user in users:

          #if user key have no organization_id we add this check for preventing keyError 
          if('organization_id' in user):
            if(user['organization_id'] == result['_id']):
              result['user_name'] =  user['name']
        
        for ticket in tickets:
          
          if('organization_id' in ticket):
            
            if(ticket['organization_id'] == result['_id']):

              # increment index at every iteration in this block
              index += 1

              # populate key with index in result dictionary
              result[f'ticket_{index}'] = ticket['subject']
        
        # geting key from dict
        for key in result:
          # :<30 for indentation
          print(f"{key:<30} {result[key]}")
        

    def searchable_fields(self):
      # list for searchable fields
      template_str = """
        --------------------------------------------------
        Search  Users with
        _id
        url
        external_id
        name
        alias
        created_at
        active
        verified
        shared
        locale
        timezone
        last_login_at
        email
        phone
        signature
        organization_id
        tags
        suspended
        role
        --------------------------------------------------
        Search Tickets with 
        _id
        url
        external_id
        created_at
        type
        subject
        description
        priority
        status
        submitter_id
        assignee_id
        organization_id
        tags
        has_incidents
        due_at
        via
        --------------------------------------------------
        Search Organizations with
        _id
        url
        external_id
        name
        domain_names
        created_at
        details
        shared_tickets
        tags
        --------------------------------------------------
      """
      print(template_str)
      

    
"""
Get value from user selection based i explined above but explain again
 * Press 1 to search Zendesk
 * Press 2 to view a list of searchable fields
 * Type 'quit' to exit from Zendesk
"""
selection  = input()

#instantiate the class 
obj = Search(selection)

#call function based on options
obj.options()
