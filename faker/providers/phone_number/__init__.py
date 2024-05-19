from itertools import chain

import phonenumbers

from .. import BaseProvider, ElementsType

# Data source
#
# The country codes in this provider comes from the following source:
# List of country calling codes
# https://en.wikipedia.org/wiki/List_of_country_calling_codes
#
# Data was collected from the alphabetical listing by country or region

localized = True


class Provider(BaseProvider):
    country_calling_codes: ElementsType[str] = (
        "+93",
        "+358 18",
        "+355",
        "+213",
        "+1 684",
        "+376",
        "+244",
        "+1 264",
        "+1 268",
        "+54",
        "+374",
        "+297",
        "+247",
        "+61",
        "+672 1",
        "+672",
        "+43",
        "+994",
        "+1 242",
        "+973",
        "+880",
        "+1 246",
        "+1 268",
        "+375",
        "+32",
        "+501",
        "+229",
        "+1 441",
        "+975",
        "+591",
        "+599 7",
        "+387",
        "+267",
        "+55",
        "+246",
        "+1 284",
        "+673",
        "+359",
        "+226",
        "+257",
        "+855",
        "+237",
        "+1",
        "+238",
        "+599 3",
        "+599 4",
        "+599 7",
        "+1 345",
        "+236",
        "+235",
        "+64",
        "+56",
        "+86",
        "+61 89164",
        "+61 89162",
        "+57",
        "+269",
        "+242",
        "+243",
        "+682",
        "+506",
        "+385",
        "+53",
        "+599 9",
        "+357",
        "+420",
        "+45",
        "+246",
        "+253",
        "+1 767",
        "+1 809",
        "+1 829",
        "+1 849",
        "+670",
        "+56",
        "+593",
        "+20",
        "+503",
        "+881 2",
        "+881 3",
        "+882 13",
        "+240",
        "+291",
        "+372",
        "+268",
        "+251",
        "+500",
        "+298",
        "+679",
        "+358",
        "+33",
        "+596",
        "+594",
        "+689",
        "+241",
        "+220",
        "+995",
        "+49",
        "+233",
        "+350",
        "+881",
        "+881 8",
        "+881 9",
        "+30",
        "+299",
        "+1 473",
        "+590",
        "+1 671",
        "+502",
        "+44 1481",
        "+44 7781",
        "+44 7839",
        "+44 7911",
        "+224",
        "+245",
        "+592",
        "+509",
        "+504",
        "+852",
        "+36",
        "+354",
        "+881 0",
        "+881 1",
        "+91",
        "+62",
        "+870",
        "+800",
        "+882",
        "+883",
        "+979",
        "+808",
        "+98",
        "+964",
        "+353",
        "+881 6",
        "+881 7",
        "+44 1624",
        "+44 7524",
        "+44 7624",
        "+44 7924",
        "+972",
        "+39",
        "+225",
        "+1 876",
        "+47 79",
        "+81",
        "+44 1534",
        "+962",
        "+7 6",
        "+7 7",
        "+254",
        "+686",
        "+850",
        "+82",
        "+383",
        "+965",
        "+996",
        "+856",
        "+371",
        "+961",
        "+266",
        "+231",
        "+218",
        "+423",
        "+370",
        "+352",
        "+853",
        "+261",
        "+265",
        "+60",
        "+960",
        "+223",
        "+356",
        "+692",
        "+596",
        "+222",
        "+230",
        "+262 269",
        "+262 639",
        "+52",
        "+691",
        "+1 808",
        "+373",
        "+377",
        "+976",
        "+382",
        "+1 664",
        "+212",
        "+258",
        "+95",
        "+374 47",
        "+374 97",
        "+264",
        "+674",
        "+977",
        "+31",
        "+1 869",
        "+687",
        "+64",
        "+505",
        "+227",
        "+234",
        "+683",
        "+672 3",
        "+389",
        "+90 392",
        "+44 28",
        "+1 670",
        "+47",
        "+968",
        "+92",
        "+680",
        "+970",
        "+507",
        "+675",
        "+595",
        "+51",
        "+63",
        "+64",
        "+48",
        "+351",
        "+1 787",
        "+1 939",
        "+974",
        "+262",
        "+40",
        "+7",
        "+250",
        "+599 4",
        "+590",
        "+290",
        "+1 869",
        "+1 758",
        "+590",
        "+508",
        "+1 784",
        "+685",
        "+378",
        "+239",
        "+966",
        "+221",
        "+381",
        "+248",
        "+232",
        "+65",
        "+599 3",
        "+1 721",
        "+421",
        "+386",
        "+677",
        "+252",
        "+27",
        "+500",
        "+995 34",
        "+211",
        "+34",
        "+94",
        "+249",
        "+597",
        "+47 79",
        "+46",
        "+41",
        "+963",
        "+886",
        "+992",
        "+255",
        "+888",
        "+66",
        "+882 16",
        "+228",
        "+690",
        "+676",
        "+373 2",
        "+373 5",
        "+1 868",
        "+290 8",
        "+216",
        "+90",
        "+993",
        "+1 649",
        "+688",
        "+256",
        "+380",
        "+971",
        "+44",
        "+1",
        "+878",
        "+598",
        "+1 340",
        "+998",
        "+678",
        "+39 06 698",
        "+379",
        "+58",
        "+84",
        "+1 808",
        "+681",
        "+967",
        "+260",
        "+255 24",
        "+263",
    )

    region_code: str | None = None

    formats: ElementsType[str] = ("###-###-###",)

    msisdn_formats: ElementsType[str] = ("#############",)

    """
    "safe_numbers" provided by https://fakenumber.org/

    The GB/United Kingdom "safe_numbers" are reported as invalid by the phonenumbers package.
    """
    safe_numbers = {
        "AU": [
            "+61491570156",
            "+61491570157",
            "+61491570158",
            "+61491570159",
            "+61491570110",
        ],
        "US": [
            "+12025550191",
            "+12025550188",
            "+12025550187",
            "+12025550137",
            "+12025550105",
            "+12025550124",
        ],
        "GB": [
            "+441632960600",
            "+441632960541",
            "+441632960702",
            "+441632960979",
            "+441632960570",
            "+441632960864",
        ],
        "CA": [
            "+16135550110",
            "+16135550120",
            "+16135550109",
            "+16135550151",
            "+16135550136",
            "+16135550119",
        ],
    }

    # e164_formats: ElementsType[str] = ("+#############",)
    _e164_numerify_pattern = "%######!!!!!!!!"  # https://en.wikipedia.org/wiki/E.164

    def phone_number(self) -> str:
        return self.numerify(self.random_element(self.formats))

    def country_calling_code(self) -> str:
        return self.random_element(self.country_calling_codes)

    def msisdn(self) -> str:
        """https://en.wikipedia.org/wiki/MSISDN"""
        return self.numerify(self.random_element(self.msisdn_formats))

    def _get_e164_numerify_pattern(self, region_code: str, is_possible: bool = True) -> str:
        if not is_possible:
            return "#!!!!!!"
        country_code = phonenumbers.country_code_for_region(region_code)
        return str(country_code) + self._e164_numerify_pattern[len(str(country_code)) :]

    def _e164(self, region_code: str, is_valid: bool = True, is_possible: bool = True) -> phonenumbers.PhoneNumber:
        """
        Generate an e164 phone number
        """
        assert not (is_valid and not is_possible), "is_valid must be False if is_possible is False"
        e164_numerify_pattern = self._get_e164_numerify_pattern(region_code, is_possible=is_possible)
        phone_number: str | phonenumbers.PhoneNumber = self.numerify(e164_numerify_pattern)
        while not isinstance(phone_number, phonenumbers.PhoneNumber):
            try:
                phone_number = phonenumbers.parse(phone_number, region_code)
            except phonenumbers.phonenumberutil.NumberParseException:
                phone_number = self.numerify(e164_numerify_pattern)
                continue

            if is_valid and not phonenumbers.is_valid_number(phone_number):
                phone_number = self.numerify(e164_numerify_pattern)
                continue
            elif not is_valid and phonenumbers.is_valid_number(phone_number):
                phone_number = self.numerify(e164_numerify_pattern)
                continue

            if is_possible and not phonenumbers.is_possible_number(phone_number):
                phone_number = self.numerify(e164_numerify_pattern)
                continue
            elif not is_possible and phonenumbers.is_possible_number(phone_number):
                phone_number = self.numerify(e164_numerify_pattern)
                continue

        return phone_number

    def e164(self, region_code: str = None, valid: bool = True, possible: bool = True) -> str:
        """Return a random e164 formatted phone number"""
        if region_code is None:
            region_code = self.region_code or self.random_element(phonenumbers.SUPPORTED_REGIONS)
        return phonenumbers.format_number(
            numobj=self._e164(region_code, is_valid=valid, is_possible=possible),
            num_format=phonenumbers.PhoneNumberFormat.E164,
        )

    def safe_e164(self, region_code: str | None = None) -> str:
        """Return a "safe" e164 phone number"""
        region_code = region_code or self.region_code

        if region_code not in self.safe_numbers.keys():
            raise ValueError(f"No safe numbers for region code {region_code}")

        if region_code is None:
            region_code = self.random_element(list(self.safe_numbers.keys()))

        phone_number = phonenumbers.parse(self.random_element(self.safe_numbers[region_code]))
        return phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
