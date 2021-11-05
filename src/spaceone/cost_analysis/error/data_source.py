from spaceone.core.error import *


class ERROR_INVALID_PLUGIN_VERSION(ERROR_INVALID_ARGUMENT):
    _message = 'Plugin version is invalid. (plugin_id = {plugin_id}, version = {version})'


class ERROR_NOT_ALLOW_PLUGIN_SETTINGS(ERROR_INVALID_ARGUMENT):
    _message = 'Local type dose not allow plugin settings. (data_source_id = {data_source_id})'