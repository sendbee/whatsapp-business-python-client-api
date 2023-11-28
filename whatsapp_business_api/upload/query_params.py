from whatsapp_business_api.query_params import QueryParams


class AccountIdInURL(QueryParams):
    """Url parameters for account id"""

    account_id = 'account_id', 'Account ID'


class UploadSession(QueryParams):
    """Query parameters for starting an upload session"""

    file_length = 'file_length', 'Required. The length of the file in bytes.'
    file_type = 'file_type', 'Required. The type of file being uploaded.' \
                             'Valid values are: application/pdf, image/jpeg, ' \
                             'image/jpg, image/png, and video/mp4'
    access_token = 'access_token', 'Required. The access token for the upload session.'


class UploadFile(QueryParams):
    """Query parameters for uploading a file"""

    upload_session_id = 'upload_session_id', 'Required. The ID of the upload session.'


class UploadTemplateMediaFile(QueryParams):
    """Parameters for uploading template example media file"""

    file = 'file', 'File upload object'
