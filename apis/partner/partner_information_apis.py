from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class PartnerInformation(GetTokenHeader):

    def create_partner_api(self, variables):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_partner(input=variables)
        op.create_partner()
        # start 和 end 的时间戳类型有sgqlc的缺陷，利用字符串替换手动更替
        op1 = str(op).replace('"start"', 'start')
        op2 = str(op1).replace('"end"', 'end')
        data = endpoint(op2)
        try:
            res = (op + data).create_partner
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res
