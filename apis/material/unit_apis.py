from random import randint

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Unit(GetTokenHeader):

    def create_scm_unit_api(self, variables):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_scm_unit(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_scm_unit
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def scm_unit_list_api(self, args=None):
        """
        币种列表
        :param args:
        :return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        scm_unit_list = op.scm_unit_list()
        if args is not None:
            scm_unit_list.__fields__(*args)
        data = endpoint(op)
        res = (op + data).scm_unit_list
        return res

    def random_unit_id(self):
        """
        随机取一个币种的id
        :return:
        """
        unit_list = self.scm_unit_list_api()
        a = randint(0, unit_list.total_count - 1)
        res = unit_list.data[a].id
        return res


if __name__ == '__main__':
    u = Unit()
    res = u.scm_unit_list_api()
    print(res.data)
