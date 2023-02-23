from apis.base.base_api import BaseApi
from apis.material.unit_apis import Unit


class UnitData(BaseApi):

    def create_scm_unit_data(self):
        args = list()
        variables_temp = self.get_variables(module_name="unit", variables_name="create_scm_unit_data")
        args.append(("name", self.mock.mock_data("单位", 2)))
        args.append(("abbreviation", self.faker.random_element() + str(self.faker.random_digit())))
        args.append(("numDigits", self.faker.random_digit()))
        args.append(("remark", self.faker.sentence()))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_scm_unit_data(self, id):
        args = list()
        variables_temp = self.get_variables(module_name="unit", variables_name="update_scm_unit_data")
        args.append(("abbreviation", self.faker.random_element() + str(self.faker.random_digit())))
        args.append(("remark", self.faker.sentence()))
        args.append(("id", id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    m = Unit()
    for i in range(100):
        a = UnitData()
        data = a.create_scm_unit_data()
        res = m.create_scm_unit_api(data)
        print(res)
