from whatsapp_business_api.models import Model
from whatsapp_business_api.fields import TextField, ModelField


class Number(Model):
    """Model for phone number"""

    _id = TextField(index='id', desc='Phone number ID')
    _verified_name = TextField(index='verified_name', desc='Verified name')
    _code_verification_status = TextField(
        index='code_verification_status', desc='Code verification status')
    _display_phone_number = TextField(
        index='display_phone_number', desc='Display phone number')
    _quality_rating = TextField(
        index='quality_rating', desc='Quality rating')
    _platform_type = TextField(
        index='platform_type', desc='Platform type')
    _throughput = TextField(
        index='throughput', desc='Throughput')
    _last_onboarded_time = TextField(
        index='last_onboarded_time', desc='Last onboarded time')


class NumberData(Model):
    """Data model for phone number"""

    _data = ModelField(Number, index='data', desc='WhatsApp ID')


class BusinessAccount(Model):
    """Data model for Facebook business account"""

    _id = TextField(index='id', desc='Account ID')
    _name = TextField(index='name', desc='Account name')
    _phone_numbers = ModelField(
        NumberData, index='phone_numbers', desc='Phone numbers')


class RegisterAccount(Model):
    """Data model for register account"""

    _success = TextField(index='success', desc='Success')
