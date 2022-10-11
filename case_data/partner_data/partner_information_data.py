from apis.base.base_api import BaseApi
from apis.partner.partner_information_apis import Partner


class PartnerInformationData(BaseApi):

    def create_partner_data(self):
        args = list()
        variables_temp = self.get_variables(module_name="partner", variables_name="create_partner_data")

        args.append(("companyAddr:address", self.mock.mock_data("n",3)))
        args.append(("companyAddr:area", self.mock.mock_data("n", 3)))

        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    pd = PartnerInformationData()
    data=pd.create_partner_data()
    print(data)

