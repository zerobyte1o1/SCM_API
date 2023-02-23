from apis.base.base_api import BaseApi
from apis.material.material_category_apis import MaterialCategory


class MaterialCategoryData(BaseApi):

    def create_scm_material_category_data(self,parentId=None):
        args = list()
        variables_temp = self.get_variables(module_name="material_category", variables_name="create_scm_material_category_data")

        args.append(("name", self.mock.mock_data("类型")))
        args.append(("no", self.mock.mock_data("b",3)))
        if parentId is not None:
            args.append(("parentId", parentId))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_scm_material_category_data(self,id):
        args = list()
        variables_temp = self.get_variables(module_name="material_category", variables_name="update_scm_material_category_data")

        args.append(("name", self.mock.mock_data("类型")))
        args.append(("no", self.mock.mock_data("b",3)))
        args.append(("id", id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

if __name__ == '__main__':
    m=MaterialCategory()
    for i in range(100):
        md=MaterialCategoryData()
        data=md.create_scm_material_category_data()
        res=m.create_scm_material_category_api(data)
        for i in range(3):
            data2=md.create_scm_material_category_data(res)
            res2=m.create_scm_material_category_api(data2)
            print(res2)