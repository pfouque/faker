from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    region_code = "LV"

    formats = (
        "+371 ########",
        "+(371) ########",
        "+371########",
    )
