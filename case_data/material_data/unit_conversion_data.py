from apis.base.base_api import BaseApi
from apis.material.unit_conversion_apis import UnitConversion
from apis.material.material_apis import Material
from apis.material.unit_apis import Unit
from apis.material.material_signal_apis import MaterialSignal


class UnitConversionData(BaseApi):
    def __init__(self):
        self.material = Material()
        self.unit = Unit()
        self.signal = MaterialSignal()

    def create_scm_unit_conversion_data(self):
        args = list()
        variables_temp = self.get_variables(module_name="unit_conversion",
                                            variables_name="create_scm_unit_conversion_data")
        args.append(("targetRatio", self.faker.random_digit()))
        args.append(("baseUnit:id", self.unit.random_unit_id()))
        args.append(("material:id", self.material.random_material_id()))
        args.append(("targetUnit:id", self.unit.random_unit_id()))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_scm_unit_conversion_data(self, id):
        args = list()
        variables_temp = self.get_variables(module_name="unit_conversion",
                                            variables_name="update_scm_unit_conversion_data")
        args.append(("targetRatio", self.faker.random_digit()))
        args.append(("baseUnit:id", self.unit.random_unit_id()))
        args.append(("material:id", self.material.random_material_id()))
        args.append(("targetUnit:id", self.unit.random_unit_id()))
        args.append(("id", id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    b = UnitConversion()
    for i in range(100):
        c = UnitConversionData()
        data = c.create_scm_unit_conversion_data()
        res = b.create_scm_unit_conversion_api(data)
        print(res)
