from whatsapp_business_api.models import Model
from whatsapp_business_api.fields import JsonField, ModelField, TextField, \
    BooleanField


class BusinessProfileData(Model):
    """Data model for WABA business profile"""

    _about = TextField(
        index='about', desc='The business\'s About text. This text appears '
                          'in the business\'s profile, beneath its profile '
                          'image, phone number, and contact buttons.')
    _address = TextField(
        index='address', desc='Address of the business. '
                              'Character limit 256.')
    _description = TextField(
        index='description', desc='Description of the business. '
                                  'Character limit 512.')
    _email = TextField(
        index='email', desc='The contact email address (in valid email format) '
                            'of the business. Character limit 128.')
    _messaging_product = TextField(
        index='messaging_product', desc='The messaging service used for '
                                        'the request. This value will '
                                        'always be whatsapp.')
    _profile_picture_url = TextField(
        index='profile_picture_url', desc='URL of the profile picture that '
                                          'was uploaded to Meta. Use the '
                                          'profile_picture_handle parameter '
                                          'to update this value.')
    _vertical = TextField(
        index='vertical', desc='Optional. Industry of the business. This can '
                               'be either an empty string or one of the '
                               'accepted values. Supported Values: UNDEFINED, '
                               'OTHER, AUTO, BEAUTY, APPAREL, EDU, ENTERTAIN, '
                               'EVENT_PLAN, FINANCE, GROCERY, GOVT, HOTEL, '
                               'HEALTH, NONPROFIT, PROF_SERVICES, RETAIL, '
                               'TRAVEL, RESTAURANT, NOT_A_BIZ')
    websites = JsonField(
        index='websites', desc='Optional. The URLs associated with the '
                               'business. For instance, a website, Facebook '
                               'Page, or Instagram. You must include the '
                               'http:// or https:// portion of the URL. '
                               'There is a maximum of 2 websites with '
                               'a maximum of 256 characters each.')


class BusinessProfile(Model):
    """Data model for WABA business profile"""

    _data = ModelField(BusinessProfileData,
                       index='data', desc='WABA business profile data')


class UpdateBusinessProfileResponse(Model):
    """Data model for WABA business profile update response"""

    _success = BooleanField(index='success', desc='Indicates whether the '
                                                  'request was successful.')
