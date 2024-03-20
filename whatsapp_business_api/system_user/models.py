from whatsapp_business_api.models import Model
from whatsapp_business_api.fields import TextField


class Response(Model):
    """Data model for response"""

    _success = TextField(index='success', desc='Success')
