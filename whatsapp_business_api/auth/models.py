from whatsapp_business_api.models import Model
from whatsapp_business_api.fields import TextField


class OauthToken(Model):
    """Data model for oauth token response"""

    _token = TextField(index='access_token', desc='oAuth access token')
