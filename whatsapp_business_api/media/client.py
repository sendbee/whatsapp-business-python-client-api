from whatsapp_business_api import constants
from whatsapp_business_api.bind import bind_request
from whatsapp_business_api.media import query_params
from whatsapp_business_api.media.models import \
    UploadSession, UploadFile, MediaFile


class Upload:
    """Partner Api client for application uploads"""

    create_upload_session = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<account_id>/uploads',
        url_parameters=query_params.UploadSession,
        model=UploadSession,
        description='Start upload session',
        force_single_model_response=True,
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    upload_file = bind_request(
        method=constants.RequestConst.POST,
        api_path='/v18.0/<upload_session_id>',
        url_parameters=query_params.UploadFile,
        file_parameters=query_params.UploadTemplateMediaFile,
        file_to_data_parameter='file',
        header={'file_offset': '0',
                'Content-Type': 'application/octet-stream'},
        model=UploadFile,
        description='Start file upload',
        force_single_model_response=True,
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    get_media = bind_request(
        method=constants.RequestConst.GET,
        api_path='/v18.0/<media_id>',
        model=MediaFile,
        force_single_model_response=True,
        query_parameters=query_params.MediaIdInURL,
        description='Get media file'
    )
