from whatsapp_business_api.query_params import QueryParams


class OauthToken(QueryParams):
    """Query parameters for getting partner token"""

    client_id = 'client_id', 'Facebook app id'
    client_secret = 'client_secret', 'Facebook app secret'
    redirect_uri = 'redirect_uri', 'oAuth redirect ID'
    code = 'code', 'oAuth code'
