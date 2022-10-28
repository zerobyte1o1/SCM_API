import pytest
from hamcrest import *
import allure
from apis.material.material_signal_apis import MaterialSignal
from case_data.material_data.material_signal_data import MaterialSignalData


class TestMaterialSignal:
    def setup_class(self):
        self.ms = MaterialSignal()
        self.ms_data = MaterialSignalData()

    @pytest.fixture(scope="class")
    def pre_ms(self):
        data = self.ms_data.create_scm_material_signal_data()
        ms_id = self.ms.create_scm_material_signal_api(data)
        yield ms_id
        if len([i["id"] for i in self.ms.scm_material_signal_list_api().data if i["id"] == ms_id]) > 0:
            self.ms.delete_scm_material_signal_api([ms_id])

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/180?id=0", name="查询物料信号")
    def test_scm_material_signal_list(self):
        res = self.ms.scm_material_signal_list_api()
        assert_that(res.total_count >= 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/176?id=0", name="新增物料信号")
    def test_create_scm_material_signal(self):
        data = self.ms_data.create_scm_material_signal_data()
        res = self.ms.create_scm_material_signal_api(data)
        self.ms.delete_scm_material_signal_api([res])
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/177?id=0", name="编辑物料信号")
    def test_update_scm_material_signal(self, pre_ms):
        data = self.ms_data.update_scm_material_signal_data(pre_ms)
        res = self.ms.update_scm_material_signal_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/178?id=0", name="删除物料信号")
    def test_delete_scm_material_signal(self, pre_ms):
        res = self.ms.delete_scm_material_signal_api(pre_ms)
        assert_that(res.is_used >= 0)
