from whatsapp_business_api.query_params import QueryParams


class OauthToken(QueryParams):
    """Query parameters for getting partner token"""

    client_id = 'client_id', 'Facebook app id'
    client_secret = 'client_secret', 'Facebook app secret'
    redirect_uri = 'redirect_uri', 'oAuth redirect ID'
    code = 'code', 'oAuth code'
    grant_type = 'grant_type', 'authorization_code'
    fb_exchange_token = 'fb_exchange_token', 'A valid system user access token'
    set_token_expires_in_60_days = \
        'set_token_expires_in_60_days', \
            'set to true to refresh an expiring system user access token'
