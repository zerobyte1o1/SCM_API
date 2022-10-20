from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class UnitConversion(GetTokenHeader):

    def create_scm_unit_conversion_api(self,variables):
        """
        创建单位换算
        :param variables:
        :return:
        """
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

    def scm_unit_conversion_list_api(self, args=None):
        """
        单位换算列表
        :param args:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        scm_unit_conversion_list = op.scm_unit_conversion_list()
        if args is not None:
            scm_unit_conversion_list.__fields__(*args)
        data = endpoint(op)
        res = (op + data).scm_unit_conversion_list
        return res

    def update_scm_unit_conversion_api(self,variables):
        """
        更新单位换算
        :param variables:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_scm_unit_conversion(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_scm_unit_conversion
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_scm_unit_conversion_api(self,ids):
        """
        删除单位换算
        :param ids: list
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_scm_unit_conversion(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).delete_scm_unit_conversion
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res