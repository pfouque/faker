from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    region_code = "JP"

    formats = (
        "070-####-####",
        "080-####-####",
        "090-####-####",
        "##-####-####",
    )
