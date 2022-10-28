import pytest
from hamcrest import *
import allure
from apis.material.unit_conversion_apis import UnitConversion
from case_data.material_data.unit_conversion_data import UnitConversionData


class TestUnitConversion:
    def setup_class(self):
        self.unit_c = UnitConversion()
        self.unit_c_data = UnitConversionData()

    @pytest.fixture(scope="class")
    def pre_unit_c(self):
        data = self.unit_c_data.create_scm_unit_conversion_data()
        unit_c_id = self.unit_c.create_scm_unit_conversion_api(data)
        yield unit_c_id
        if len([i["id"] for i in self.unit_c.scm_unit_conversion_list_api().data if i["id"] == unit_c_id]) > 0:
            self.unit_c.delete_scm_unit_conversion_api([unit_c_id])

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/188?id=0", name="查询")
    def test_scm_unit_conversion_list(self):
        res = self.unit_c.scm_unit_conversion_list_api()
        assert_that(res.total_count >= 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/185?id=0", name="查询")
    def test_create_scm_unit_conversion(self):
        data = self.unit_c_data.create_scm_unit_conversion_data()
        res = self.unit_c.create_scm_unit_conversion_api(data)
        self.unit_c.delete_scm_unit_conversion_api([res])
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/186?id=0", name="编辑物料单位换算")
    def test_update_scm_unit_conversion(self, pre_unit_c):
        data = self.unit_c_data.update_scm_unit_conversion_data(pre_unit_c)
        res = self.unit_c.update_scm_unit_conversion_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/187?id=0", name="删除物料单位换算")
    def test_delete_scm_unit_conversion(self, pre_unit_c):
        res = self.unit_c.delete_scm_unit_conversion_api([pre_unit_c])
        assert_that(res.is_used >= 0)
