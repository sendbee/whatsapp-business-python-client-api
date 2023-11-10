from whatsapp_business_api import constants
from whatsapp_business_api.bind import bind_request
from whatsapp_business_api.auth import query_params
from whatsapp_business_api.auth.models import OauthToken


class Auth:
    """Partner Api client for authentication"""

    oauth_token = bind_request(
        method=constants.RequestConst.GET,
        api_path='/v18.0/oauth/access_token',
        query_parameters=query_params.OauthToken,
        model=OauthToken,
        description='Get partner API token',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )
