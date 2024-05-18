from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    region_code = "NP"

    formats = (
        "+977 ##########",
        "+977 ### #######",
        "984#######",
        "985#######",
        "980#######",
    )
