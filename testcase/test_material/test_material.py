import pytest
from hamcrest import *
import allure

from apis.material.material_apis import Material
from case_data.material_data.material_data import MaterialData


class TestMaterial:
    def setup_class(self):
        self.m = Material()
        self.m_data = MaterialData()

    @pytest.fixture(scope="class")
    def pre_m(self):
        data = self.m_data.create_scm_material_data()
        m_id = self.m.create_scm_material_api(data)
        yield m_id
        if len([i["id"] for i in self.m.scm_material_list_api().data if i["id"] == m_id]) > 0:
            self.m.delete_scm_material_api([m_id])

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/167?id=0", name="查询物料")
    def test_scm_material_category_list(self):
        res = self.m.scm_material_list_api()
        assert_that(res.total_count >= 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/168?id=0", name="新增物料")
    def test_create_scm_material_category(self):
        data = self.m_data.create_scm_material_data()
        res = self.m.create_scm_material_api(data)
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/170?id=0", name="编辑物料")
    def test_update_scm_material_category(self, pre_m):
        data = self.m_data.update_scm_material_data(pre_m)
        res = self.m.update_scm_material_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/171?id=0", name="删除物料")
    def test_delete_scm_material_category(self, pre_m):
        res = self.m.delete_scm_material_api([pre_m])
        assert_that(res.is_used >= 0)
