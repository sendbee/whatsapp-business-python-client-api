from whatsapp_business_api.query_params import QueryParams


class BusinessProfileFields(QueryParams):
    """URL Parameters for phone_number_id in url"""

    phone_number_id = 'phone_number_id', 'WABA phone number ID'
    fields = 'fields', 'Response fields'


class UpdateBusinessProfileFields(QueryParams):
    """URL Parameters for updating WABA business profile"""

    about = 'about', 'Optional. The business\'s About text. This text appears ' \
                     'in the business\'s profile, beneath its profile image, ' \
                     'phone number, and contact buttons. String cannot be ' \
                     'empty. Strings must be between 1 and 139 characters. ' \
                     'Rendered emojis are supported however their unicode ' \
                     'values are not. Emoji unicode values must be Java- or ' \
                     'JavaScript-escape encoded. Hyperlinks can be included ' \
                     'but will not render as clickable links. ' \
                     'Markdown is not supported.'
    address = 'address', 'Optional. ' \
                         'Address of the business. Character limit 256.'
    description = 'description', 'Optional. ' \
                                 'Description of the business. ' \
                                 'Character limit 512.'
    email = 'email', 'Optional. ' \
                     'The contact email address (in valid email format) ' \
                     'of the business. Character limit 128.'
    messaging_product = 'messaging_product', 'Required. The messaging service ' \
                                             'used for the request. Always ' \
                                             'set it to "whatsapp" if you ' \
                                             'are using the WhatsApp ' \
                                             'Business API.'
    profile_picture_handle = 'profile_picture_handle', 'Optional. Handle of the profile ' \
                                                       'picture. This handle is generated ' \
                                                       'when you upload the binary file ' \
                                                       'for the profile picture to Meta ' \
                                                       'using the Resumable Upload API.'
    vertical = 'vertical', 'Optional. Industry of the business. This can ' \
                           'be either an empty string or one of the ' \
                           'accepted values. Supported Values: UNDEFINED, ' \
                           'OTHER, AUTO, BEAUTY, APPAREL, EDU, ENTERTAIN, ' \
                           'EVENT_PLAN, FINANCE, GROCERY, GOVT, HOTEL, ' \
                           'HEALTH, NONPROFIT, PROF_SERVICES, RETAIL, ' \
                           'TRAVEL, RESTAURANT, NOT_A_BIZ'
    websites = 'websites', 'Optional. The URLs associated with the ' \
                           'business. For instance, a website, Facebook ' \
                           'Page, or Instagram. You must include the ' \
                           'http:// or https:// portion of the URL. ' \
                           'There is a maximum of 2 websites with ' \
                           'a maximum of 256 characters each.'
