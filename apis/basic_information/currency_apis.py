from random import randint
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Currency(GetTokenHeader):

    def create_currency_api(self, variables):
        """
        创建币种
        :param variables:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_currency(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_currency
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def currency_list_api(self, args=None):
        """
        币种列表
        :param args:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        currency_list = op.currency_list()
        if args is not None:
            currency_list.__fields__(*args)
        data = endpoint(op)
        res = (op + data).currency_list
        return res

    def random_currency_id(self):
        """
        随机取一个币种的id
        :return:
        """
        cur_list = self.currency_list_api()
        a = randint(0, cur_list.total_count - 1)
        res = cur_list.data[a].id
        return res

    def update_currency_api(self, input_data):
        """
        更新一个币种
        :param input_data:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_currency(input=input_data)
        data = endpoint(op)
        try:
            res = (op + data).update_currency
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_currency_api(self, ids: list):
        """
        删除币种
        :param ids:id 的列表
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_currency(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).delete_currency
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def set_default_currency_api(self, id):
        """
        设置默认币种
        :param id:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.set_default_currency(id=id)
        data = endpoint(op)
        try:
            res = (op + data).set_default_currency
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    c = Currency()
    res = c.random_currency_id()
    print(res)
