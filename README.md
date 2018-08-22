#Mac2Vendor
Mac2Vendor is a simple project made to convert mac addresses to vendor information
vendor source: https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries
not very ram-friendly...

##Requirements
・pickle

##Usage

```
>>> import mac2vendor
>>>
>>>
>>> info = mac2vendor.get_information('00:00:00:12:34:56')
>>> print(info.get_oui())
>>> 00:00:00
>>> print(info.get_clean_oui())
>>> 000000
>>> print(info.get_vendor())
>>> XEROX CORPORATION
>>> print(info.get_vendor_location())
>>> M/S 105-50C WEBSTER NY US 14580
>>> print(info.get_dictionary())
>>> {'mac': '000000', 'organization_name': 'XEROX CORPORATION', 'organization_address': 'M/S 105-50C WEBSTER NY US 14580 '}
```