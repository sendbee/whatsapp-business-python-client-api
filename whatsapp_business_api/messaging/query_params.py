from whatsapp_business_api.query_params import QueryParams


class SendMessage(QueryParams):
    """Parameters for sending a WhatsApp message"""

    destination = 'to', 'Destination phone number'
    recipient_type = 'recipient_type', 'Recipient type'
    type = 'type', 'Indicates message type'
    text = 'text', 'Text messages contents'
    reaction = 'reaction', 'Reaction message contents'
    image = 'image', 'Media message contents. The property name should match ' \
                     'the type of media message you are sending (image for an ' \
                     'image message, video for a video message, etc.)'
    document = 'document', 'Document message'
    video = 'video', 'Video message contents'
    audio = 'audio', 'Audio message contents'
    sticker = 'sticker', 'Sticker message contents'
    location = 'location', 'Location message contents'
    contacts = 'contacts', 'Contacts message contents'
    interactive = 'interactive', 'Interactive message contents'


class SendTemplateMessage(QueryParams):
    """Parameters for sending a WhatsApp message template"""

    destination = 'to', 'Destination phone number'
    template = 'template', 'Template data'


class AppIdMsgIdInURL(QueryParams):
    """URL Parameters for app_id and msg_id in url"""

    app_id = 'app_id', 'Phone number ID'
