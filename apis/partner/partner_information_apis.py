from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class PartnerInformation(GetTokenHeader):

    def create_partner_api(self, variables):
        """
        创建业务伙伴
        :param variables:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_partner(input=variables)
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

    def update_partner_api(self, variables):
        """
        更新业务伙伴
        :param variables:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_partner(input=variables)
        # start 和 end 的时间戳类型有sgqlc的缺陷，利用字符串替换手动更替
        op1 = str(op).replace('"start"', 'start')
        op2 = str(op1).replace('"end"', 'end')
        data = endpoint(op2)
        try:
            res = (op + data).update_partner
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def active_partner_api(self, ids):
        """
        激活业务伙伴
        :param ids: list
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.active_partner(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).active_partner
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def frozen_partner_api(self, ids):
        """
        冻结业务伙伴
        :param ids: list
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.frozen_partner(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).frozen_partner
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def partner_list_api(self):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.partner_list()
        data = endpoint(op)
        try:
            res = (op + data).partner_list
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_partner_api(self,ids):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_partner(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).delete_partner
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res