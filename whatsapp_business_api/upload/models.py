from whatsapp_business_api.models import Model
from whatsapp_business_api.fields import TextField, ModelField, JsonField


class UploadSession(Model):
    """Data model for application upload session"""

    _id = TextField(index='id', desc='Upload session ID')


class UploadFile(Model):
    """Data model for application upload file"""

    _file_handle = TextField(index='h', desc='File handle')
