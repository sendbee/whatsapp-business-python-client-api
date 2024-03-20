from whatsapp_business_api import constants
from whatsapp_business_api.bind import bind_request
from whatsapp_business_api.system_user import query_params
from whatsapp_business_api.system_user.models import Response


class SystemUsers:
    """Partner Api client for Facebook business account"""

    add_system_user = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<waba_id>/assigned_users',
        url_parameters=query_params.WabaIDInUrl,
        query_parameters=query_params.AssignUserRequest,
        model=Response,
        force_single_model_response=True,
        description='Get Facebook business account system users',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )
