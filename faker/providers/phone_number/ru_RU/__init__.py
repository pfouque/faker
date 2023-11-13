from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    region_code = "RU"
    
    formats = (
        "+7 ### ### ####",
        "+7 ### ### ## ##",
        "+7 (###) ###-##-##",
        "+7 (###) ###-####",
        "+7##########",
        "8 ### ### ####",
        "8 ### ### ## ##",
        "8 (###) ###-##-##",
        "8 (###) ###-####",
        "8##########",
    )
