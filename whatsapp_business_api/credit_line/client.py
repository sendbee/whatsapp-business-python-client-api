from whatsapp_business_api import constants
from whatsapp_business_api.bind import bind_request
from whatsapp_business_api.credit_line import query_params
from whatsapp_business_api.credit_line.models import ExtendedCredit


class CreditLine:
    """Partner Api client for Facebook payment credit line"""

    extended_credits = bind_request(
        method=constants.RequestConst.GET,
        api_path='/v18.0/<business_id>/extendedcredits',
        query_parameters=query_params.ExtendedCredits,
        model=ExtendedCredit,
        force_single_model_response=True,
        description='Get extended credits',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    add_credit_line = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<extended_credit_id>/whatsapp_credit_sharing_and_attach',
        url_parameters=query_params.ExtendedCreditId,
        query_parameters=query_params.ExtendedCredits,
        model=ExtendedCredit,
        force_single_model_response=True,
        description='Get extended credits',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )
