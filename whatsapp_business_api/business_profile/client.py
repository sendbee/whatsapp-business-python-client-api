from whatsapp_business_api import constants
from whatsapp_business_api.bind import bind_request
from whatsapp_business_api.business_profile import query_params
from whatsapp_business_api.business_profile.models import BusinessProfile, \
    UpdateBusinessProfileResponse


class BusinessProfiles:
    """Partner Api client for WABA business profile"""

    whatsapp_business_profile = bind_request(
        method=constants.RequestConst.GET,
        api_path='/v18.0/<phone_number_id>/whatsapp_business_profile',
        query_parameters=query_params.BusinessProfileFields,
        model=BusinessProfile,
        force_single_model_response=True,
        description='Get WABA profile data',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    update_whatsapp_business_profile = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<phone_number_id>/whatsapp_business_profile',
        url_parameters=query_params.BusinessProfileFields,
        query_parameters=query_params.UpdateBusinessProfileFields,
        model=UpdateBusinessProfileResponse,
        force_single_model_response=True,
        default_parameters={
            'messaging_product': 'whatsapp'
        },
        description='Update WABA business profile data',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )
