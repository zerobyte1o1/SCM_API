from random import randint

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Material(GetTokenHeader):

    def create_scm_material_api(self,variables):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_scm_material(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_scm_material
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def scm_material_list_api(self, args=None):
        """
        物料列表
        :param args:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        scm_material_list = op.scm_material_list()
        if args is not None:
            scm_material_list.__fields__(*args)
        data = endpoint(op)
        res = (op + data).scm_material_list
        return res

    def random_material_id(self):
        """
        随机取一个物料分类的id
        :return:
        """
        material_list = self.scm_material_list_api()
        a = randint(0, material_list.total_count - 1)
        res = material_list.data[a].id
        return res

    def scm_material_api(self, id):
        """
        物料详情
        :param id:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.scm_material(id=id)
        data = endpoint(op)
        res = (op + data).scm_material
        return res

    def update_scm_material_api(self,variables):
        """
        更新物料
        :param variables:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_scm_material(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_scm_material
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_scm_material_api(self,ids):
        """
        删除物料
        :param ids:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_scm_material(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).delete_scm_material
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res