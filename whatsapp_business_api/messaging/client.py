from whatsapp_business_api import constants
from whatsapp_business_api.bind import bind_request
from whatsapp_business_api.messaging import query_params
from whatsapp_business_api.messaging.models import SendMessageResponse, \
    ChangeMessageStatus


class Messaging:
    """Api client for messaging"""

    send_message = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<app_id>/messages',
        model=SendMessageResponse,
        force_single_model_response=True,
        url_parameters=query_params.AppIdMsgIdInURL,
        query_parameters=query_params.SendMessage,
        default_parameters={
            'messaging_product': 'whatsapp'
        },
        description='Send a WhatsApp message'
    )

    send_template_message = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<app_id>/messages',
        model=SendMessageResponse,
        force_single_model_response=True,
        url_parameters=query_params.AppIdMsgIdInURL,
        query_parameters=query_params.SendTemplateMessage,
        default_parameters={
            'messaging_product': 'whatsapp', 'type': 'template'
        },
        description='Send a WhatsApp message template'
    )

    message_status = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<phone_number_id>/messages',
        model=ChangeMessageStatus,
        force_single_model_response=True,
        url_parameters=query_params.PhoneNumberIdInURL,
        query_parameters=query_params.MessageStatus,
        default_parameters={
            'messaging_product': 'whatsapp'
        },
        description='Change WhatsApp message status'
    )
