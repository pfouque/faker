from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    region_code = "SE"

    formats = (
        "+46 (0)8 ### ### ##",
        "+46 (0)## ## ## ##",
        "+46 (0)### ### ##",
        "08-### ### ##",
        "08-### ## ##",
        "08-## ## ##",
        "0##-### ## ##",
        "0##-## ## ##",
        "0###-## ## ##",
        "0###-### ##",
    )
