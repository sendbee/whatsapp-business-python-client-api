import click

from whatsapp_business_api.auth.client import Auth
from whatsapp_business_api.messaging.client import Messaging


class Client(Auth, Messaging):
    """Main API class. Sets all API calls."""

    base_url = 'graph.facebook.com'
    protocol = 'https'

    def __init__(self, token=None, authorization=None, debug=False,
                 fake_response_path=None):

        self.debug = debug
        self.request = None
        self.api_key = None
        self.api_token = token
        self.api_authorization = authorization
        self.fake_response_path = fake_response_path

    @classmethod
    def print_params_for(cls, fn_name) -> None:
        """Prints parameters for certain API call function."""

        try:
            getattr(cls, fn_name)(None, print_params=True)
        except AttributeError:
            click.secho('Unknown API method: {}'.format(fn_name), fg='red')
