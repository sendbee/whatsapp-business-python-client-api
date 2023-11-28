from whatsapp_business_api.models import Model
from whatsapp_business_api.fields import TextField, ModelField, JsonField


class MetaApp(Model):
    """Data model for Meta app"""

    _app = JsonField(index='whatsapp_business_api_data', desc='App data')


class Apps(Model):
    """Data model for Meta apps"""

    _data = ModelField(MetaApp, index='data', desc='List of apps')


class Success(Model):
    """Data model for subscribed app"""

    _success = TextField(index='success', desc='Success')
