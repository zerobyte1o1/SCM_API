from apis.base.base_api import BaseApi
from apis.basic_information.currency_apis import Currency


class CurrencyData(BaseApi):

    def create_currency_data(self):
        args = list()
        variables_temp = self.get_variables(module_name="currency", variables_name="create_currency_data")
        args.append(("name", self.mock.mock_data("币种")))
        args.append(("no", self.mock.mock_data("b", 3)))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_currency_data(self, id):
        args = list()
        variables_temp = self.get_variables(module_name="currency", variables_name="update_currency_data")
        args.append(("name", self.mock.mock_data("币种")))
        args.append(("id", id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    c = Currency()
    for i in range(100):
        cd = CurrencyData()
        data = cd.create_currency_data()
        res = c.create_currency_api(data)
        print(res)
