from whatsapp_business_api.models import Model
from whatsapp_business_api.fields import TextField, ModelField, JsonField


class Contact(Model):
    """Data model for message contact"""

    _input = TextField(
        index='input', desc='The customer phone number that the message '
                            'was sent to. This may not match wa_id.'
    )
    _id = TextField(
        index='wa_id', desc='WhatsApp ID of the customer who the message '
                            'was sent to. This may not match input.'
    )
    _user_id = TextField(
        index='user_id', desc='Business-scoped user ID of the customer. '
                              'Present when the message was sent to a BSUID; '
                              'wa_id is omitted in that case.'
    )


class Message(Model):
    """Data model for message"""

    _id = TextField(
        index='id', desc='WhatsApp message ID. You can use the ID listed '
                         'after "wamid." to track your message status'
    )


class SendMessageResponse(Model):
    """Data model for sent message"""

    _messaging_product = TextField(
        index='messaging_product', desc='Messaging product'
    )
    _contacts = ModelField(Contact, index='contacts', desc='Contacts models')
    _messages = ModelField(Message, index='messages', desc='Messages models')
    _error = JsonField(index='error', desc='Error model')


class ChangeMessageStatus(Model):
    """Data model for change message status"""

    _success = TextField(index='success', desc='Success')
