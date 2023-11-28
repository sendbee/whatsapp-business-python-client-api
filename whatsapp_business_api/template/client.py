from whatsapp_business_api import constants
from whatsapp_business_api.bind import bind_request
from whatsapp_business_api.template import query_params
from whatsapp_business_api.template.models import \
    MessageTemplateList, CreatedMessageTemplate, DeletedMessageTemplate


class Template:
    """Partner Api client for message templates"""

    get_message_templates = bind_request(
        method=constants.RequestConst.GET,
        api_path='/v18.0/<account_id>/message_templates',
        query_parameters=query_params.GetMessageTemplate,
        model=MessageTemplateList,
        description='Get message templates',
        force_single_model_response=True,
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    create_message_templates = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<account_id>/message_templates',
        query_parameters=query_params.CreateMessageTemplate,
        url_parameters=query_params.AccountIdInURL,
        model=CreatedMessageTemplate,
        description='Get message templates',
        force_single_model_response=True,
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    delete_message_templates = bind_request(
        method=constants.RequestConst.DELETE,
        api_path='/v18.0/<account_id>/message_templates',
        query_parameters=query_params.DeleteMessageTemplate,
        url_parameters=query_params.AccountIdInURL,
        model=DeletedMessageTemplate,
        description='Get message templates',
        force_single_model_response=True,
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )
