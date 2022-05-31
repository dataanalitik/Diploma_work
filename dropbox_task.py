import requests
import json


class Similar:
    auth = 'Bearer sl.BIc64MDebHFvlaWjYc15EKjtRfT0E4xcyIiYug_7kQM5fg3Kl0OOqOGVJWCd_tFUhmdhbXtqa47W7zfpLRTj0HrGwPdFwBqlrhlGnredu8-wN4_B5C4AFAlfcfxHgYyj9Z4XEzWs'
    method = "POST"


class UploadRequest(Similar):

    def __init__(self) -> None:
        self.id = None
        self.response = None
        self.params = {
            'url': "https://content.dropboxapi.com/2/files/upload",
            'headers': {
                'Dropbox-API-Arg': '{"path": "/file.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
                'Content-Type': 'application/octet-stream',
                'Authorization': self.auth
            }
        }

    def get_response(self):
        self.response = requests.request(
            method=self.method,
            url=self.params['url'],
            headers=self.params['headers'],
            data='This is test message for a new file'
        )
        self.id = json.loads(self.response.text)['id']


class GetFileMetadataRequest(Similar):

    def __init__(self) -> None:
        self.file_path = None
        self.response = None
        self.params = {
            'url': "https://api.dropboxapi.com/2/sharing/get_file_metadata",
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': self.auth
            }
        }

    def get_response(self, id):
        self.response = requests.request(
            method=self.method,
            url=self.params['url'],
            headers=self.params['headers'],
            data=json.dumps(
                {
                    "file": f"{id}",
                    "actions": []
                }
            )
        )
        self.file_path = json.loads(self.response.text)['path_display']


class DeleteRequest(Similar):
    def __init__(self) -> None:
        self.response = None
        self.params = {
            'url': "https://api.dropboxapi.com/2/files/delete_v2",
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': self.auth
            }
        }

    def get_response(self, file_path):
        self.response = requests.request(
            method=self.method,
            url=self.params['url'],
            headers=self.params['headers'],
            data=json.dumps(
                {
                    "path": f"{file_path}"
                }
            )
        )