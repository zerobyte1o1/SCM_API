from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Reason(GetTokenHeader):

    def create_reason_api(self, variables):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_reason(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_reason
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res
