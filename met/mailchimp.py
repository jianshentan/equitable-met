import requests
from mailchimp3 import MailChimp
from urllib3.exceptions import HTTPError

class MailchimpException(Exception):
    pass

class MailchimpClient():
    client = None
    list_id = None

    def set_credentials(self, username: str, key: str):
        self.client = MailChimp(key, username)

    def set_list_id(self, list_id: str):
        self.list_id = list_id

    def add_or_update_user(self, 
            email: str, 
            status: str = 'subscribed',
            first_name: str = '', 
            last_name: str = ''):
        '''
        add a new subscriber to mailchimp
        if subscriber already exists, do not throw error.
        '''

        try:
            self.client.lists.members.create_or_update(self.list_id, email, {
                'email_address': email,
                'status_if_new': 'subscribed',
                'status': status,
                'merge_fields': {
                    'FNAME': first_name,
                    'LNAME': last_name
                },
            })

        except KeyError as e:
            raise e

        except Exception as e:
            if e.response.status_code == 400:
                json = e.response.json()
                raise MailchimpException( \
                        json.get('errors') \
                        or json.get('title') \
                        or json.get('detail') \
                        or json)
            else:
                raise     


mc = MailchimpClient()