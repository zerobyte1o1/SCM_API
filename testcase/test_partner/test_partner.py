import pytest
from hamcrest import *
import allure
from apis.partner.partner_information_apis import PartnerInformation
from case_data.partner_data.partner_information_data import PartnerInformationData


class TestPartner:
    def setup_class(self):
        self.partner = PartnerInformation()
        self.partner_data = PartnerInformationData()

    @pytest.fixture(scope="class")
    def pre_partner(self):
        data = self.partner_data.create_partner_data()
        p_id = self.partner.create_partner_api(data)
        yield p_id
        if len([i["id"] for i in self.partner.partner_list_api().data if i["id"] == p_id]) > 0:
            self.partner.delete_partner_api([p_id])

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/191?id=0", name="查询业务伙伴")
    def test_partner_list(self):
        res = self.partner.partner_list_api()
        assert_that(res.total_count >= 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/189?id=0", name="新增业务伙伴")
    def test_create_partner(self):
        data = self.partner_data.create_partner_data()
        res = self.partner.create_partner_api(data)
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/190?id=0", name="编辑业务伙伴")
    def test_update_partner(self, pre_partner):
        data = self.partner_data.update_partner_data(pre_partner)
        res = self.partner.update_partner_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/192?id=0", name="激活")
    def test_active_partner(self, pre_partner):
        res = self.partner.active_partner_api([pre_partner])
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/193?id=0", name="冻结")
    def test_frozen_partner(self, pre_partner):
        res = self.partner.frozen_partner_api([pre_partner])
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/194?id=0", name="删除")
    def test_delete_partner(self, pre_partner):
        res = self.partner.delete_partner_api([pre_partner])
        assert_that(res.is_used == 0)
