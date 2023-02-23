from apis.base.base_api import BaseApi
from apis.basic_information.reason_apis import Reason


class ReasonData(BaseApi):

    def create_reason_data(self):
        args = list()
        variables_temp = self.get_variables(module_name="reason", variables_name="create_reason_data")
        args.append(("explain", self.faker.sentence()))
        args.append(("no", self.mock.mock_data("b",3)))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_reason_data(self,id):
        args = list()
        variables_temp = self.get_variables(module_name="reason", variables_name="update_reason_data")
        args.append(("explain", self.faker.sentence()))
        args.append(("id",id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

if __name__ == '__main__':
    r=Reason()
    for i in range(100):
        rd=ReasonData()
        data=rd.create_reason_data()
        res=r.create_reason_api(data)
        print(res)