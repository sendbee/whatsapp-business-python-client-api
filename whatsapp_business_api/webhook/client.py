from whatsapp_business_api import constants
from whatsapp_business_api.bind import bind_request
from whatsapp_business_api.webhook import query_params
from whatsapp_business_api.webhook.models import Apps, Success


class Webhook:
    """Partner Api client for WABA subscribed apps"""

    subscribe_app = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<account_id>/subscribed_apps',
        query_parameters=query_params.AccountIdInURL,
        url_parameters=query_params.AccountIdInURL,
        model=Success,
        description='Subscribe app',
        force_single_model_response=True,
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    list_subscribed_apps = bind_request(
        method=constants.RequestConst.GET,
        api_path='/v18.0/<account_id>/subscribed_apps',
        query_parameters=query_params.AccountIdInURL,
        model=Apps,
        force_single_model_response=True,
        description='List subscribed apps',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )
