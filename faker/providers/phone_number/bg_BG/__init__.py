from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    region_code = "BG"

    formats = (
        "+359(0)#########",
        "+359(0)### ######",
        "+359(0)### ### ###",
        "+359#########",
        "0#########",
        "0### ######",
        "0### ### ###",
        "0### ###-###",
        "(0###) ######",
        "(0###) ### ###",
        "(0###) ###-###",
    )
