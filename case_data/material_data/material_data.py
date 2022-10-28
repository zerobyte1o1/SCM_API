from apis.base.base_api import BaseApi
from apis.material.material_apis import Material
from apis.material.material_category_apis import MaterialCategory
from apis.material.unit_apis import Unit
from apis.material.material_signal_apis import MaterialSignal


class MaterialData(BaseApi):
    def __init__(self):
        self.category=MaterialCategory()
        self.unit=Unit()
        self.signal=MaterialSignal()

    def create_scm_material_data(self):
        args = list()
        variables_temp = self.get_variables(module_name="material", variables_name="create_scm_material_data")
        args.append(("category:id", self.category.random_material_category_id()))
        args.append(("inventoryUnit:id", self.unit.random_unit_id()))
        args.append(("materialSignal:id", self.signal.random_material_signal_id()))
        args.append(("figureNo", self.mock.mock_data("图号", 10)))
        args.append(("materialQuality", self.mock.mock_data("材质", 10)))
        args.append(("model", self.mock.mock_data("型号", 10)))
        args.append(("name", self.mock.mock_data("物料", 10)))
        args.append(("no", self.mock.mock_data("no", 7)))
        args.append(("specification", self.mock.mock_data("规格", 10)))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_scm_material_data(self, id):
        args = list()
        variables_temp = self.get_variables(module_name="material", variables_name="update_scm_material_data")
        args.append(("category:id", self.category.random_material_category_id()))
        args.append(("inventoryUnit:id", self.unit.random_unit_id()))
        args.append(("materialSignal:id", self.signal.random_material_signal_id()))
        args.append(("figureNo", self.mock.mock_data("图号", 10)))
        args.append(("materialQuality", self.mock.mock_data("材质", 10)))
        args.append(("model", self.mock.mock_data("型号", 10)))
        args.append(("name", self.mock.mock_data("物料", 10)))
        args.append(("id", id))
        args.append(("specification", self.mock.mock_data("规格", 10)))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    m = Material()

    for i in range(500000):
        md = MaterialData()
        data = md.create_scm_material_data()
        res = m.create_scm_material_api(data)
        print(res)
