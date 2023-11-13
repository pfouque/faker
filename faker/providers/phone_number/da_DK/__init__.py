from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):

    region_code = "DK"

    formats = (
        "+45 ########",
        "+45 #### ####",
        "+45 ## ## ## ##",
        "########",
        "#### ####",
        "## ## ## ##",
    )
