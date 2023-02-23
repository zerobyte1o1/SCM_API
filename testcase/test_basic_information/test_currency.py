import pytest
from hamcrest import *
import allure
from apis.basic_information.currency_apis import Currency
from case_data.basic_information_data.currency_data import CurrencyData


class TestCurrency:
    def setup_class(self):
        self.currency = Currency()
        self.currency_data = CurrencyData()

    @pytest.fixture(scope="class")
    def pre_currency(self):
        data = self.currency_data.create_currency_data()
        currency_id = self.currency.create_currency_api(data)
        yield currency_id
        if len([i["id"] for i in self.currency.currency_list_api().data if i["id"] == currency_id]) > 0:
            self.currency.delete_currency_api(currency_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/208?id=0", name="币种查询")
    def test_currency_list(self):
        res = self.currency.currency_list_api()
        assert_that(res.total_count >= 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/195?id=0", name="新增币种")
    def test_create_currency(self):
        data = self.currency_data.create_currency_data()
        res = self.currency.create_currency_api(data)
        assert_that("-" in res)
        self.currency.delete_currency_api([res])

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/196?id=0", name="编辑币种")
    def test_update_currency(self, pre_currency):
        data = self.currency_data.update_currency_data(pre_currency)
        res = self.currency.update_currency_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/197?id=0", name="设置默认币种")
    def test_set_default_currency(self, pre_currency):
        res = self.currency.set_default_currency_api(pre_currency)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/198?id=0", name="删除币种")
    def test_delete_currency(self, pre_currency):
        res = self.currency.delete_currency_api([pre_currency])
        assert_that(res.is_used >= 0)
