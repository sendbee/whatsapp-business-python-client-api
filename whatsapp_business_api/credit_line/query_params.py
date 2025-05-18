from whatsapp_business_api.query_params import QueryParams


class ExtendedCredits(QueryParams):
    """URL Parameters for extended credit line"""

    waba_id = 'waba_id', 'WhatsApp Business Account ID'
    waba_currency = 'waba_currency', 'Currency of WhatsApp Business Account'
    access_token = 'access_token', 'System user access token'


class ExtendedCreditId(QueryParams):
    """URL Parameters for extended credit line"""

    extended_credit_id = 'extended_credit_id', 'Extended credit ID'

