from whatsapp_business_api.models import Model
from whatsapp_business_api.fields import TextField, ModelField, JsonField


class CreditLine(Model):
    """Model for credit line"""

    _id = TextField(index='id', desc='Credit line ID')
    _legal_entity_name = TextField(
        index='legal_entity_name', desc='Legal entity name')


class ExtendedCredit(Model):
    """Data model for extended credit line"""

    _data = ModelField(CreditLine, index='data', desc='WhatsApp ID')
