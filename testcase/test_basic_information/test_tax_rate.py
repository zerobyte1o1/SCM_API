import pytest
from hamcrest import *
import allure
from apis.basic_information.tax_rate_apis import TaxRate


class TestTaxRate:
    def setup_class(self):
        self.tax_rate = TaxRate()

    @pytest.fixture(scope="class")
    def pre_tax_rate(self):
        tax_id = self.tax_rate.create_tax_rate_api(97)
        yield tax_id
        if self.tax_rate.tax_rate_list_api(97).total_count > 0:
            self.tax_rate.delete_tax_rate_api(tax_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/203?id=0", name="查询")
    def test_tax_rate_list(self):
        res = self.tax_rate.tax_rate_list_api()
        assert_that(res.total_count >= 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/199?id=0", name="新增税率")
    def test_create_tax_rate(self):
        res = self.tax_rate.create_tax_rate_api(85)
        self.tax_rate.delete_tax_rate_api(85)
        assert_that("-" in res)


    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/200?id=0", name="生效税率")
    def test_effective_tax_rate(self, pre_tax_rate):
        res = self.tax_rate.effective_tax_rate_api(pre_tax_rate)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/201?id=0", name="失效税率")
    def test_expired_tax_rate(self, pre_tax_rate):
        res = self.tax_rate.expired_tax_rate_api(pre_tax_rate)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/202?id=0", name="删除税率")
    def test_delete_tax_rate(self, pre_tax_rate):
        res = self.tax_rate.delete_tax_rate_api(pre_tax_rate)
        assert_that(res, equal_to(True))
