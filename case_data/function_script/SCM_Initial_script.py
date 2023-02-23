from apis.material.material_apis import Material
from apis.material.material_category_apis import MaterialCategory
from apis.material.unit_apis import Unit
from utils.readfile import readexecl


class SCMInitialScript():
    def __init__(self):
        self.mc = MaterialCategory()
        self.m = Material()
        self.u = Unit()

    def category_script(self):
        """
        分类导入
        :return:
        """

        input_va = dict()
        category_list = readexecl("./script_data/scm脚本数据.xlsx", "产品分类")
        parent_id_list = [{"name": None, "no": None, "id": None},
                          {"name": None, "no": None, "id": None},
                          {"name": None, "no": None, "id": None}]
        for category in category_list:
            for i in range(3):
                if category[2 * i] is None:
                    continue
                elif category[2 * i] == parent_id_list[i]["name"] and category[2 * i + 1] == parent_id_list[i]["no"]:
                    continue
                else:
                    input_va["name"] = category[2 * i]
                    input_va["no"] = category[2 * i + 1]
                    if i == 0:
                        input_va["parentId"] = None
                    else:
                        input_va["parentId"] = parent_id_list[i - 1]["id"]
                    res = self.mc.create_scm_material_category_api(input_va)
                    parentId = res
                    parent_id_list[i]["id"] = parentId
                    parent_id_list[i]["name"] = input_va["name"]
                    parent_id_list[i]["no"] = input_va["no"]

    def unit_script(self):
        """
        单位导入
        :return:
        """

        input_un = dict()
        unit_list = readexecl("./script_data/scm脚本数据.xlsx", "单位")
        for unit in unit_list:
            input_un["name"] = unit[0]
            input_un["numDigits"] = unit[1]
            res = self.u.create_scm_unit_api(input_un)
            print(res)

    def material_script(self):

        input_un = dict()
        material_list = readexecl("./script_data/scm脚本数据.xlsx", "物料编码")
        print(material_list)
        for k in range(len(material_list)):
            for s in self.mc.scm_material_category_list_api():
                if s.name == material_list[k][6]:
                    cate_id = s.id
            input_un["category"] = {"id": cate_id}
            for i in self.u.scm_unit_list_api().data:
                if i.name == material_list[k][11]:
                    unit_id = i.id
            input_un["inventoryUnit"] = {"id": unit_id}
            input_un["materialQuality"] = material_list[k][10]
            input_un["materialType"] = material_list[k][12]
            input_un["model"] = material_list[k][9]
            input_un["name"] = material_list[k][1]
            input_un["no"] = material_list[k][0] + "{:0>6d}".format(k+1)
            input_un["specification"] = material_list[k][8]
            res = self.m.create_scm_material_api(input_un)
            print(res)


if __name__ == '__main__':
    c = SCMInitialScript()
    c.material_script()
