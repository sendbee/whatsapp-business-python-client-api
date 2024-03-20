from whatsapp_business_api.query_params import QueryParams


class AssignUserRequest(QueryParams):
    """Query parameters for assigned users request"""

    user_id = 'user', 'System user ID'
    tasks = 'tasks', 'Tasks to assign to the user. MANAGE or DEVELOP'
    access_token = 'access_token', 'System user access token'


class WabaIDInUrl(QueryParams):
    """URL parameters for WABA ID in url"""

    waba_id = 'waba_id', 'WhatsApp Business Account ID'
