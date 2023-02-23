from random import randint

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class MaterialSignal(GetTokenHeader):

    def create_scm_material_signal_api(self,variables):
        """
        创建物料信号
        :param variables:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_scm_material_signal(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_scm_material_signal
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def scm_material_signal_list_api(self, args=None):
        """
        物料分类列表
        :param args:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        scm_material_signal_list = op.scm_material_signal_list()
        if args is not None:
            scm_material_signal_list.__fields__(*args)
        data = endpoint(op)
        res = (op + data).scm_material_signal_list
        return res

    def random_material_signal_id(self):
        """
        随机取一个物料分类的id
        :return:
        """
        signal_list = self.scm_material_signal_list_api()
        a = randint(0, signal_list.total_count - 1)
        res = signal_list.data[a].id
        return res

    def update_scm_material_signal_api(self,variables):
        """
        更新物料信号
        :param variables:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_scm_material_signal(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_scm_material_signal
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_scm_material_signal_api(self,ids):
        """
        删除物料信号
        :param ids:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_scm_material_signal(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).delete_scm_material_signal
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res