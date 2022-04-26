You need the latest version of python for running Zendesk command line application.

Run this file using

cd coding-exercise/

python3 search.py


if you press "1"
    Then you can search in Zendesk
        Ask from you search for 
            1: users
            2: tickets
            3: organizations

                if you want to test user search then press "1"

                1: for users search
                        Enter search term _id
                        Enter search value 1
                            return search
                               _id                            1
                                url                            http://initech.aiworks.com/api/v2/users/1.json
                                external_id                    74341f74-9c79-49d5-9611-87ef9b6eb75f
                                name                           Francisca Rasmussen
                                alias                          Miss Coffey
                                created_at                     2016-04-15T05:19:46 -10:00
                                active                         True
                                verified                       True
                                shared                         False
                                locale                         en-AU
                                timezone                       Sri Lanka
                                last_login_at                  2013-08-04T01:03:27 -10:00
                                email                          coffeyrasmussen@flotonic.com
                                phone                          8335-422-718
                                signature                      Don't Worry Be Happy!
                                organization_id                119
                                tags                           ['Springville', 'Sutton', 'Hartsville/Hartley', 'Diaperville']
                                suspended                      True
                                role                           admin
                                organization_name              Multron
                                ticket_1                       A Nuisance in Bangladesh
                                ticket_2                       A Catastrophe in San Marino
                                ticket_3                       A Drama in Chad
                                ticket_4                       A Problem in Guatemala
                                ticket_5                       A Nuisance in Suriname
                                ticket_6                       A Catastrophe in Thailand
                                ticket_7                       A Drama in Nigeria

                        if search not matched then 
                        for example 
                        Enter search term _id
                        Enter search value 39992
                        Searching users for _id with  a value of 39992 
                        No results found
                
                        if you want to search tags then work same way
                        Enter search term tags
                        Enter search value Springville

                        then also return filtered data


                2: for tickets search
                        Enter search term _id
                        Enter search value 436bf9b0-1147-4c0a-8439-6f79833bff5b
                        return search
                            _id                            436bf9b0-1147-4c0a-8439-6f79833bff5b
                            url                            http://initech.aiworks.com/api/v2/tickets/436bf9b0-1147-4c0a-8439-6f79833bff5b.json
                            external_id                    9210cdc9-4bee-485f-a078-35396cd74063
                            created_at                     2016-04-28T11:19:34 -10:00
                            type                           incident
                            subject                        A Catastrophe in Korea (North)
                            description                    Nostrud ad sit velit cupidatat laboris ipsum nisi amet laboris ex exercitation amet et proident. Ipsum fugiat aute dolore tempor nostrud velit ipsum.
                            priority                       high
                            status                         pending
                            submitter_id                   38
                            assignee_id                    24
                            organization_id                116
                            tags                           ['Ohio', 'Pennsylvania', 'American Samoa', 'Northern Mariana Islands']
                            has_incidents                  False
                            due_at                         2016-07-31T02:37:50 -10:00
                            via                            web
                            name                           Zentry
                            user_name                      Nash Rivers

                        if search not matched then 
                        for example 
                        Enter search term _id
                        Enter search value 436bf9b0-1147-4c0a-8439-6f79833bff5b
                        Searching users for _id with  a value of 436bf9b0-1147-4c0a-8439-6f79833bff5b 
                        No results found
                
                        if you want to search tags then work same way
                        Enter search term tags
                        Enter search value Pennsylvania

                        then also return filtered data

                3: for organizations search
                    Enter search term _id
                    Enter search value 119
                    return search
                        _id                            119
                        url                            http://initech.aiworks.com/api/v2/organizations/119.json
                        external_id                    2386db7c-5056-49c9-8dc4-46775e464cb7
                        name                           Multron
                        domain_names                   ['bleeko.com', 'pulze.com', 'xoggle.com', 'sultraxin.com']
                        created_at                     2016-02-29T03:45:12 -11:00
                        details                        Non profit
                        shared_tickets                 False
                        tags                           ['Erickson', 'Mccoy', 'Wiggins', 'Brooks']
                        user_name                      Catalina Simpson
                        ticket_1                       A Nuisance in Bangladesh
                        ticket_2                       A Catastrophe in San Marino
                        ticket_3                       A Drama in Chad
                        ticket_4                       A Problem in Guatemala
                        ticket_5                       A Nuisance in Suriname
                        ticket_6                       A Catastrophe in Thailand
                        ticket_7                       A Drama in Nigeria

                    if you want to search tags then work same way
                    Enter search term tags
                    Enter search value Erickson
                    then also return filtered data

if you press "2"
    Then see the searchable fields list

if type "quit"
    Then exit




How we can run the test?

i create seprate file for testing with name of test.py

if you run for match term value data then run this way 

```python3 -m unittest test.SearchTest.search_tickets_term_value```

if you want to add all tests then pass all tests names

``` python3 -m unittest test.SearchTest.search_users_term_value  test.SearchTest.search_tickets_term_value test.SearchTest.search_organizations_term_value
 ```

it's working but if you change anything in id or anywhere on filtered data then test is failed
