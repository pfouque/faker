from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # https://de.wikipedia.org/wiki/Rufnummer#Schreibweisen

    region_code = "DE"

    formats = (
        "+49(0)##########",
        "+49(0)#### ######",
        "+49 (0) #### ######",
        "+49(0) #########",
        "+49(0)#### #####",
        "0##########",
        "0#########",
        "0#### ######",
        "0#### #####",
        "(0####) ######",
        "(0####) #####",
    )
