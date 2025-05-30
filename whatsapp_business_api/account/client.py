from whatsapp_business_api import constants
from whatsapp_business_api.bind import bind_request
from whatsapp_business_api.account import query_params
from whatsapp_business_api.account.models import \
    BusinessAccount, RegisterAccount, Number, SMBInitDataSync, WabaAccount, \
    NumberData


class Account:
    """Partner Api client for Facebook business account"""

    business_account = bind_request(
        method=constants.RequestConst.GET,
        api_path='/v18.0/<account_id>',
        query_parameters=query_params.AccountFields,
        model=BusinessAccount,
        force_single_model_response=True,
        description='Get Facebook business account',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    waba_details = bind_request(
        method=constants.RequestConst.GET,
        api_path='/v18.0/<account_id>',
        query_parameters=query_params.AccountFields,
        model=WabaAccount,
        description='Get WABA account',
        force_single_model_response=True,
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    number_details = bind_request(
        method=constants.RequestConst.GET,
        api_path='/v18.0/<account_id>',
        query_parameters=query_params.AccountFields,
        model=Number,
        force_single_model_response=True,
        description='Get WABA number details',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    phone_numbers = bind_request(
        method=constants.RequestConst.GET,
        api_path='/v18.0/<account_id>/phone_numbers',
        query_parameters=query_params.AccountIdMsgIdInURL,
        model=NumberData,
        force_single_model_response=True,
        description='Get Facebook business account phone numbers',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    register_number = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<phone_number_id>/register',
        url_parameters=query_params.PhoneNumberId,
        query_parameters=query_params.ActivatePhoneNumber,
        model=RegisterAccount,
        force_single_model_response=True,
        description='Register WABA phone number',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )
    
    smb_init_data_sync = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<phone_number_id>/smb_app_data',
        url_parameters=query_params.PhoneNumberId,
        query_parameters=query_params.SMBInitDataSync,
        model=SMBInitDataSync,
        force_single_model_response=True,
        description='Initialize SMB data sync',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )
