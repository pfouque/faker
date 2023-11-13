from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    region_code = "LT"
    
    formats = (
        "+370 ########",
        "+(370) ########",
        "+370########",
    )
