__author__ = 'Administrator'
import os


class GtConfig:
    def __init__(self):
        pass

    @staticmethod
    def isPushSingleBatchAsync():
        return os.getenv("gexin_pushSingleBatch_needAsync", False)

    @staticmethod
    def isPushListAsync():
        return os.getenv("gexin_pushList_needAsync", False)

    @staticmethod
    def isPushListNeedDetails():
        return GtConfig.getProperty("gexin_pushList_needDetails", "needDetails", False)

    @staticmethod
    def getHttpProxyIp():
        return os.getenv("gexin_http_proxy_ip", None)

    @staticmethod
    def getHttpProxyPort():
        return os.getenv("gexin_http_proxy_port", 80)

    @staticmethod
    def getSyncListLimit():
        return os.getenv("gexin_pushList_syncLimit", 1000)

    @staticmethod
    def getAsyncListLimit():
        return os.getenv("gexin_pushList_asyncLimit", 10000)

    @staticmethod
    def getHttpConnectionTimeOut():
        return os.getenv("gexin_http_connection_timeout", 60)

    @staticmethod
    def getHttpSoTimeOut():
        return os.getenv("gexin_http_so_timeout", 30)

    @staticmethod
    def getHttpTryCount():
        return os.getenv("gexin_http_tryCount", 3)

    @staticmethod
    def getHttpInspectInterval():
        return os.getenv("gexin_http_inspect_interval", 60)

    @staticmethod
    def getDefaultDomainUrl():
        hosts = list()
        host = os.getenv("gexin_default_domainurl", None)
        if host is None or "" == host.strip():
            hosts.append("http://sdk.open.api.igexin.com/serviceex")
            hosts.append("http://sdk.open.api.gepush.com/serviceex")
            hosts.append("http://sdk.open.api.igetui.net/serviceex")
            for i in range(0, 3):
                hosts.append('http://sdk' + str(i) + "open.api.igexin.com/serviceex")
        else:
            for h in host.split(','):
                hosts.append(h)

        return hosts

    @staticmethod
    def getSDKVersion():
        return "4.0.0.1"

    @staticmethod
    def getProperty(oldKey, newKey, defaultValue):
        newValue = os.getenv(newKey)
        oldValue = os.getenv(oldKey)

        if newValue is not None:
            return newValue
        elif oldValue is not None:
            return oldValue
        else:
            return defaultValue




