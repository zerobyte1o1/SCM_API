from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class UnitConversion(GetTokenHeader):

    def create_scm_unit_conversion_api(self,variables):

        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_scm_unit_conversion(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_scm_unit_conversion
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res