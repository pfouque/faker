from .. import Provider as PhoneNumberProvider

# phone number from https://en.wikipedia.org/wiki/Telephone_numbers_in_Taiwan


class Provider(PhoneNumberProvider):
    region_code = "TW"

    formats = (
        "(0#) %#######",
        "0#-%#######",
        "0## %#######",
        "09########",
        "09##-######",
        "0#-%######",
        "0# %######",
    )
