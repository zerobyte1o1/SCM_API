from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Reason(GetTokenHeader):

    def create_reason_api(self, variables):
        """
        创建原因
        :param variables:
        :return:
        """
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

    def update_reason_api(self, input_data):
        """
        更新原因
        :param input_data:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_reason(input=input_data)
        data = endpoint(op)
        try:
            res = (op + data).update_reason
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_reason_api(self, ids: list):
        """
        删除原因
        :param ids: list
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_reason(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).delete_reason
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def reason_list_api(self):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.reason_list()
        data = endpoint(op)
        res = (op + data).reason_list
        return res
