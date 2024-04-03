from whatsapp_business_api.query_params import QueryParams


class GetMessageTemplate(QueryParams):
    """Query parameters for getting message templates"""

    account_id = 'account_id', 'Account ID'
    name = 'name', 'Optional. Template name.'
    status = 'status', 'Optional. Template status. ' \
                       'Valid values are: "APPROVED", "IN_REVIEW", "REJECTED".'
    language = 'language', 'Optional. Template language.'
    category = 'category', 'Optional. Template category.'
    content = 'content', 'Optional. Template content.'
    name_or_content = 'name_or_content', 'Optional. Template name or content.'
    quality_score = 'quality_score', 'Optional. Template quality score.'
    fields = 'fields', 'Optional. List of template fields you want returned.'
    limit = 'limit', 'Optional. The maximum number of templates ' \
                     'you want returned in each page of results.'
    after = 'after', 'Optional. The cursor for the next page of data.'


class GetMessageTemplateById(QueryParams):
    """Query parameters for getting message template by id"""

    access_token = 'access_token', 'oAuth access token'
    template_id = 'template_id', 'Template ID'
    fields = 'fields', 'Optional. List of template fields you want returned.'


class AccountIdInURL(QueryParams):
    """Url parameters for account id"""

    account_id = 'account_id', 'Account ID'


class CreateMessageTemplate(QueryParams):
    """Query parameters for creating message templates"""

    allow_category_change = 'allow_category_change', \
                            'Set to true to allow us to assign a category based ' \
                            'on our template guidelines and the template\'s ' \
                            'contents. This can prevent the template status ' \
                            'from immediately being set to REJECTED upon ' \
                            'creation due to miscategorization. If omitted, ' \
                            'template will not be auto-assigned a category and ' \
                            'its status may be set to REJECTED if determined ' \
                            'to be miscategorized.'
    name = 'name', 'Required. Template name'
    language = 'language', 'Required. Template language'
    category = 'category', 'Required. Template category'
    sub_category = 'sub_category', 'Optional. Template sub-category'
    components = 'components', 'Array of components that make up the template. ' \
                               'See Template Components. ' \
                               'For types HEADER, BODY, FOOTER, text is required.'


class DeleteMessageTemplate(QueryParams):
    """Query parameters for deleting message templates"""

    id = 'hsm_id', 'ID of template to be deleted. Required if deleting a template by ID.'
    name = 'name', 'Required. Name of template to be deleted.'
