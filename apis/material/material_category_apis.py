from random import randint

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class MaterialCategory(GetTokenHeader):

    def create_scm_material_category_api(self,variables):
        """
        创建物料分类
        :param variables:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_scm_material_category(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_scm_material_category
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def scm_material_category_list_api(self, args=None):
        """
        物料列表
        :param args:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        scm_material_category_list = op.scm_material_category_list()
        if args is not None:
            scm_material_category_list.__fields__(*args)
        data = endpoint(op)
        res = (op + data).scm_material_category_list
        return res

    def random_material_category_id(self):
        """
        随机取一个物料分类的id
        :return:
        """
        # 有问题，不是最终子节点的id
        material_category_list = self.scm_material_category_list_api()
        a = randint(0, len(material_category_list))
        res = material_category_list[a].id
        return res

    def update_scm_material_category_api(self,variables):
        """
        更新分类
        :param variables:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_scm_material_category(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_scm_material_category
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_scm_material_category_api(self,id):
        """
        删除分类
        :param id:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_scm_material_category(id=id)
        data = endpoint(op)
        try:
            res = (op + data).delete_scm_material_category
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

if __name__ == '__main__':
    m=MaterialCategory()
    res=m.scm_material_category_list_api()
    for s in res:
        if s.name=="办公用品":
            res=s.id
    print(res)