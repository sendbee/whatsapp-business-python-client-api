from whatsapp_business_api.models import Model
from whatsapp_business_api.fields import \
    TextField, ModelField, JsonField, DictField, ListField


class Cursors(Model):
    """Data model for paging cursor"""

    _before = TextField(index='before', desc='Before cursor')
    _after = TextField(index='after', desc='After cursor')


class Paging(Model):
    """Data model for paging"""

    _cursors = ModelField(Cursors, index='cursors', desc='oAuth access token')
    _next = TextField(index='next', desc='Next page url')


class Component(Model):
    """Data model for template component"""

    _type = TextField(index='type', desc='Component type')
    _format = TextField(index='format', desc='Component format')
    _text = TextField(index='text', desc='Component text')
    _example = DictField(index='example', desc='Component example')
    _buttons = ListField(index='buttons', desc='Component buttons')


class MessageTemplate(Model):
    """Data model for message template object"""

    _name = TextField(index='name', desc='Template name')
    _language = TextField(index='language', desc='Template language')
    _category = TextField(index='category', desc='Template category')
    _sub_category = TextField(
        index='sub_category', desc='Template sub category')
    _status = TextField(index='status', desc='Template status')
    _id = TextField(index='id', desc='Template id')
    _quality_score = DictField(
        index='quality_score', desc='Template quality score')
    _rejected_reason = TextField(
        index='rejected_reason', desc='Template rejected reason')
    _components = ModelField(
        Component, index='components', desc='Template components')


class MessageTemplateList(Model):
    """Data model for message template list"""

    _data = ModelField(
        MessageTemplate, index='data', desc='List of message templates')
    _paging = ModelField(Paging, index='paging', desc='Paging information')


class CreatedMessageTemplate(Model):
    """Data model for created message template object"""

    _category = TextField(index='category', desc='Template category')
    _status = TextField(index='status', desc='Template status')
    _id = TextField(index='id', desc='Template id')
    _error = JsonField(index='error', desc='Error message')


class DeletedMessageTemplate(Model):
    """Data model for deleted message template object"""

    _success = TextField(index='success', desc='Request success')
