from whatsapp_business_api.models import Model
from whatsapp_business_api.fields import TextField


class OauthToken(Model):
    """Data model for oauth token response"""

    _token = TextField(index='access_token', desc='oAuth access token')
    _token_type = TextField(index='token_type', desc='bearer')
    _expires_in = TextField(index='expires_in',
                            desc='Time left in seconds until the token expires')
