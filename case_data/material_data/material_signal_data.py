from apis.base.base_api import BaseApi
from apis.material.material_signal_apis import MaterialSignal


class MaterialSignalData(BaseApi):

    def create_scm_material_signal_data(self):
        args = list()
        variables_temp = self.get_variables(module_name="material_signal", variables_name="create_scm_material_signal_data")

        args.append(("name", self.mock.mock_data("description")))
        args.append(("no", self.mock.mock_data("b",3)))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_scm_material_signal_data(self,id):
        args = list()
        variables_temp = self.get_variables(module_name="material_signal", variables_name="update_scm_material_signal_data")

        args.append(("name", self.mock.mock_data("description")))
        args.append(("id", id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

if __name__ == '__main__':
    m = MaterialSignal()
    for i in range(100):
        a = MaterialSignalData()
        data=a.create_scm_material_signal_data()
        res=m.create_scm_material_signal_api(data)
        print(res)