from whatsapp_business_api.query_params import QueryParams


class AccountIdMsgIdInURL(QueryParams):
    """URL Parameters for account_id in url"""

    account_id = 'account_id', 'Facebook account ID'


class AccountFields(QueryParams):
    """URL Parameters for account_id in url"""

    account_id = 'account_id', 'Facebook account ID'
    fields = 'fields', 'Response fields'


class AccessToken(QueryParams):
    """URL Parameters for access_token in url"""

    account_id = 'account_id', 'Facebook account ID'
    access_token = 'access_token', 'System user access token'


class PhoneNumberId(QueryParams):
    """URL Parameters for access_token in url"""

    phone_number_id = 'phone_number_id', 'Phone number ID'


class ActivatePhoneNumber(QueryParams):
    """URL Parameters for access_token in url"""

    messaging_product = 'messaging_product', \
                        'Messaging service used. Set this to "whatsapp"'
    pin = 'pin', '2FA one time code'
    data_localization_region = 'Data_localization_region', \
                               'indicating the country where you ' \
                               'want data-at-rest to be stored. ' \
                               'Set this to "DE".'

class SMBInitDataSync(QueryParams):
    """URL Parameters for initializing SMB data sync"""

    messaging_product = 'messaging_product', 'WhatsApp'
    sync_type = 'sync_type', 'Type of sync to perform'