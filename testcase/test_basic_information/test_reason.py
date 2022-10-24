import pytest
from hamcrest import *
import allure
from apis.basic_information.reason_apis import Reason
from case_data.basic_information_data.reason_data import ReasonData


class TestReason:
    def setup_class(self):
        self.reason = Reason()
        self.reason_data = ReasonData()

    @pytest.fixture(scope="class")
    def pre_reason(self):
        data = self.reason_data.create_reason_data()
        reason_id = self.reason.create_reason_api(data)
        yield reason_id
        if len([i["id"] for i in self.reason.reason_list_api().data if i["id"] == reason_id]) > 0:
            self.reason.delete_reason_api([reason_id])

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/204?id=0", name="新增原因")
    def test_create_reason(self):
        data = self.reason_data.create_reason_data()
        res = self.reason.create_reason_api(data)
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/207?id=0", name="查询")
    def test_reason_list(self):
        res = self.reason.reason_list_api()
        assert_that(res.total_count >= 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/205?id=0", name="编辑")
    def test_update_reason(self, pre_reason):
        data = self.reason_data.update_reason_data(pre_reason)
        res = self.reason.update_reason_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/206?id=0", name="删除")
    def test_delete_reason(self, pre_reason):
        res = self.reason.delete_reason_api([pre_reason])
        assert_that(res.is_used >= 0)
