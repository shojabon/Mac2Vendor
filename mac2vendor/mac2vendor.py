import pickle

class __MacStringNotMacException(Exception):
    pass

class __mac_address:

    def __init__(self, mac_address, vendor, vendor_location, dic):
        self.__mac = mac_address
        self.__vendor = vendor
        self.__dic = dic
        self.__vendor_location = vendor_location

    def get_clean_oui(self):
        if self.__mac == 'None' or self.__mac is None:
            return None
        return str(self.__mac).replace(':', '')

    def get_oui(self):
        if self.__mac == 'None' or self.__mac is None:
            return None
        return str(self.__mac)[0:2] + ':' + str(self.__mac)[2:4] + ':' + str(self.__mac)[4:6]

    def get_vendor(self):
        return self.__vendor

    def get_vendor_address(self):
        return self.__vendor_location

    def get_dictionary(self):
        return self.__dic

    def __str__(self):
        return str(self.__dic)


def get_information(mac_address):
    formatted = str(mac_address).replace('-', ':').replace(':', '')
    if len(formatted) is not 6 and len(formatted) is not 12:
        raise __MacStringNotMacException('input mac address was not in the right form')
    file = open('mac_dict.p', 'rb')
    dic = pickle.load(file)
    file.close()
    formatted = str(formatted).upper()
    if formatted[0:6] not in dic:
        return __mac_address(None, None, None, None)
    info = dic[formatted[0:6]]
    return __mac_address(str(formatted)[0:6], str(info['organization_name']), str(info['organization_address']),info)