from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class TaxRate(GetTokenHeader):

    def create_tax_rate_api(self, rate):
        """
        :param rate:税率
        :return:
        """
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

    def delete_tax_rate_api(self, id):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_tax_rate(id=id)
        data = endpoint(op)
        try:
            res = (op + data).delete_tax_rate
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def effective_tax_rate_api(self, id):
        """
        生效税率
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.effective_tax_rate(id=id)
        data = endpoint(op)
        try:
            res = (op + data).effective_tax_rate
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def expired_tax_rate_api(self, id):
        """
        失效税率
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.expired_tax_rate(id=id)
        data = endpoint(op)
        try:
            res = (op + data).expired_tax_rate
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def tax_rate_list_api(self, search=None):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        filter = {}
        if search is not None:
            filter["search"] = str(search)
        op.tax_rate_list(filter=filter)
        data = endpoint(op)
        try:
            res = (op + data).tax_rate_list
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    t = TaxRate()
    for i in range(99):
        res = t.create_tax_rate_api(i)
        print(res)
