from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    region_code = "HU"

    formats = (
        "+36 ## ###-####",
        "(06)##/###-####",
        "(##)/###-####",
        "##/###-####",
        "##/### ####",
        "06-#/### ####",
        "06-##/### ####",
    )
