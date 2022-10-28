import pytest
from hamcrest import *
import allure
from apis.material.material_category_apis import MaterialCategory
from case_data.material_data.material_category_data import MaterialCategoryData


class TestMaterialCategory:
    def setup_class(self):
        self.mc = MaterialCategory()
        self.mc_data = MaterialCategoryData()

    @pytest.fixture(scope="class")
    def pre_mc(self):
        data = self.mc_data.create_scm_material_category_data()
        mc_id = self.mc.create_scm_material_category_api(data)
        yield mc_id
        if len([i["id"] for i in self.mc.scm_material_category_list_api() if i["id"] == mc_id]) > 0:
            self.mc.delete_scm_material_category_api(mc_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/179?id=0", name="查询物料分类")
    def test_scm_material_category_list(self):
        res=self.mc.scm_material_category_list_api()
        assert_that(len(res)>=0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/172?id=0", name="新增根分类")
    def test_create_scm_material_category(self):
        data=self.mc_data.create_scm_material_category_data()
        res=self.mc.create_scm_material_category_api(data)
        self.mc.delete_scm_material_category_api(res)
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/173?id=0", name="新增二级分类")
    def test_create_scm_material_category_second(self,pre_mc):
        data=self.mc_data.create_scm_material_category_data(pre_mc)
        res=self.mc.create_scm_material_category_api(data)
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/174?id=0", name="编辑分类")
    def test_update_scm_material_category(self,pre_mc):
        data=self.mc_data.update_scm_material_category_data(pre_mc)
        res=self.mc.update_scm_material_category_api(data)
        assert_that(res,equal_to(None))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/175?id=0", name="删除分类")
    def test_delete_scm_material_category(self,pre_mc):
        res=self.mc.delete_scm_material_category_api(pre_mc)
        assert_that(res is None)
