from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    region_code = "IN"
    formats = (
        "+91##########",
        "0##########",
        "##########",
    )
