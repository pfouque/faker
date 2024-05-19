from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    region_code = "FI"

    formats = (
        "+358 ## #######",
        "+358 #########",
        "+358#########",
        "(+358) #########",
        "0#########",
        "0## ### ####",
    )
