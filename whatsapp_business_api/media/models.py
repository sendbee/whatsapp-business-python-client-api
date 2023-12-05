from whatsapp_business_api.models import Model
from whatsapp_business_api.fields import TextField, ModelField, JsonField


class UploadSession(Model):
    """Data model for application upload session"""

    _id = TextField(index='id', desc='Upload session ID')


class UploadFile(Model):
    """Data model for application upload file"""

    _file_handle = TextField(index='h', desc='File handle')


class MediaFile(Model):
    """Data model for media file"""

    _messaging_product = TextField(
        index='messaging_product', desc='Messaging product')
    _url = TextField(index='url', desc='Media file url')
    _mime_type = TextField(index='mime_type', desc='Media file mime type')
    _sha256 = TextField(index='sha256', desc='Media file sha256')
    _file_size = TextField(index='file_size', desc='Media file size')
    _id = TextField(index='id', desc='Media file id')
