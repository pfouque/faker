from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    region_code = "NO"
    
    formats = (
        "+47########",
        "+47 ## ## ## ##",
        "## ## ## ##",
        "## ## ## ##",
        "########",
        "########",
        "9## ## ###",
        "4## ## ###",
        "9#######",
        "4#######",
    )
