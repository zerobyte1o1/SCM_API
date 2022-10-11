from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class TaxRate(GetTokenHeader):

    def create_tax_rate_api(self, rate):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_tax_rate(input={"rate": rate})
        data = endpoint(op)
        try:
            res = (op + data).create_tax_rate
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    t = TaxRate()
    for i in range(99):
        res = t.create_tax_rate_api(i)
        print(res)
