import pytest
from hamcrest import *
import allure
from apis.material.unit_apis import Unit
from case_data.material_data.unit_data import UnitData


class TestUnit:
    def setup_class(self):
        self.unit = Unit()
        self.unit_Data = UnitData()

    @pytest.fixture(scope="class")
    def pre_unit(self):
        data = self.unit_Data.create_scm_unit_data()
        unit_id = self.unit.create_scm_unit_api(data)
        yield unit_id
        if len([i["id"] for i in self.unit.scm_unit_list_api().data if i["id"] == unit_id]) > 0:
            self.unit.delete_scm_unit_api([unit_id])

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/181?id=0", name="查询")
    def test_scm_list(self):
        res = self.unit.scm_unit_list_api()
        assert_that(res.total_count >= 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/182?id=0", name="新增单位")
    def test_create_scm_unit(self):
        data=self.unit_Data.create_scm_unit_data()
        res=self.unit.create_scm_unit_api(data)
        self.unit.delete_scm_unit_api([res])
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/183?id=0", name="编辑单位")
    def test_update_scm_unit(self,pre_unit):
        data=self.unit_Data.update_scm_unit_data(pre_unit)
        res=self.unit.update_scm_unit_api(data)
        assert_that(res,equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/184?id=0", name="删除")
    def test_delete_scm_unit(self,pre_unit):
        res=self.unit.delete_scm_unit_api([pre_unit])
        assert_that(res.is_used >=0)


