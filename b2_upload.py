import os
from dotenv import  load_dotenv 
from b2sdk.v2 import *

load_dotenv()

info = InMemoryAccountInfo()
b2_api = B2Api(info)

application_key_id = os.environ.get('B2_key_id')
application_key = os.environ.get('B2_app_key')
b2_api.authorize_account("production", application_key_id, application_key)

ig_planificateur= b2_api.get_bucket_by_name("planificateur-Instagram")

local_file_path = 'C:/Users/houss/Desktop/instagram_Saas/logo.png'
b2_file_name = 'logo.png'
file_info = {'how': 'good-file'}

ig_planificateur.upload_local_file(
        local_file=local_file_path,
        file_name=b2_file_name,
        file_infos=file_info,
    )

