import os
import sys
import pytest

from devtools_testutils import AzureTestCase
from azure_devtools.scenario_tests import RecordingProcessor
from azure.maps.search import SearchClient, LatLong



class HeaderReplacer(RecordingProcessor):
    def __init__(self):
        self.headers = []

    def register_header(self, header_name, old_val, new_val):
        self.headers.append((header_name, old_val, new_val))

    def process_request(self, request):
        for header_name, old_val, new_val in self.headers:
            for key, values in request.headers.items():
                if key.lower() == header_name.lower():
                    if isinstance(values, list):
                        request.headers[key] = [v.replace(old_val, new_val) for v in values]
                    else:
                        request.headers[key] = values.replace(old_val, new_val)
                    break
        return request


class AzureMapsSearchClientTest(AzureTestCase):
    def __init__(self, *args, **kwargs):
        self.replacer = HeaderReplacer()
        super(AzureMapsSearchClientTest, self).__init__(*args, recording_processors=[self.replacer], **kwargs)

    def setUp(self):
        super(AzureMapsSearchClientTest, self).setUp()
        self.replacer.register_header("subscription-key", self.get_settings_value("SUBSCRIPTION_KEY"), "<RealSubscriptionKey>")
        self.replacer.register_header("x-ms-client-id", self.get_settings_value("CLIENT_ID"), "<RealClientId>")

        self.client = self.create_client_from_credential(SearchClient,
            credential="NotUsed",
            client_id=self.get_settings_value("CLIENT_ID"),
            authentication_policy = self.get_credential(SearchClient))
        assert self.client is not None

        #self.all_countries = ["AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AN", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BM", "BN", "BO", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "EU", "FI", "FJ", "FK", "FM", "FO", "FR", "FX", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NT", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RS", "RO", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SU", "SV", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TM", "TN", "TO", "TP", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UK", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XK", "YE", "YT", "YU", "ZA", "ZM", "ZR", "ZW"]

    def test_fuzzy_search_poi_coordinates(self):
        #result = client.fuzzy_search("Taipei 101", coordinates=LatLong(latitude=25.0338053,longitude=121.5640089))
        result = self.client.fuzzy_search("Taipei 101", coordinates={"latitude":25.0338053,"longitude":121.5640089})
        assert len(result.results) > 0 and result.results[0].type == "POI"

    def test_fuzzy_search_poi_country_set(self):
        result = self.client.fuzzy_search("Taipei 101", country_filter=["TW"])
        assert len(result.results) > 0 and result.results[0].address.country_code_iso3 == "TWN"
        result = self.client.fuzzy_search("Taipei 101", country_filter=["US"])
        assert len(result.results) > 0 and result.results[0].address.country_code_iso3 == "USA"
        result = self.client.fuzzy_search("Taipei 101", country_filter=["AQ"])
        assert len(result.results) == 0

    def test_fuzzy_search_address(self):
        result = self.client.fuzzy_search("19F., No. 68, Sec. 5, Zhongxiao E. Rd., Xinyi Dist., Taipei City, Taiwan")
        assert len(result.results) > 0 and result.results[0].address.municipality == "Taipei City"






if __name__ == "__main__" :
    testArgs = [ "-v" , "-s" ] if len(sys.argv) == 1 else sys.argv[1:]
    #testArgs = [ "-s" , "-n" , "auto" , "--dist=loadscope" ] if len(sys.argv) == 1 else sys.argv[1:]
    #pytest-xdist: -n auto --dist=loadscope
    #pytest-parallel: --tests-per-worker auto
    #print( "testArgs={}".format(testArgs) )

    pytest.main(args=testArgs)

    print("main() Leave")