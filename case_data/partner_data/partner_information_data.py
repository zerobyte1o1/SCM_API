from apis.base.base_api import BaseApi
from apis.partner.partner_information_apis import PartnerInformation


class PartnerInformationData(BaseApi):

    def create_partner_data(self):
        args = list()
        variables_temp = self.get_variables(module_name="partner", variables_name="create_partner_data")

        args.append(("abbreviation", self.faker.company_prefix()))
        args.append(("companyAddr:address", self.faker.street_address()))
        args.append(("contactList>0:phone", self.faker.phone_number()))
        args.append(("contactList>0:name", self.faker.first_name()))
        args.append(("contactList>0:position", self.faker.job()))
        args.append(("contactList>0:remark", self.faker.ean13()))
        args.append(("creditCode", self.faker.ean13()))
        # args.append(("defaultCurrency:id", ))
        args.append(("licenseCode", self.faker.ean13()))
        args.append(("name", self.faker.company()))
        args.append(("no", self.faker.ean8()))
        args.append(("remark", self.faker.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_partner_data(self,id):
        args = list()
        variables_temp = self.get_variables(module_name="partner", variables_name="update_partner_data")
        args.append(("id",id))
        args.append(("abbreviation", self.faker.company_prefix()))
        args.append(("companyAddr:address", self.faker.street_address()))
        args.append(("contactList>0:phone", self.faker.phone_number()))
        args.append(("contactList>0:name", self.faker.first_name()))
        args.append(("contactList>0:position", self.faker.job()))
        args.append(("contactList>0:remark", self.faker.ean13()))
        args.append(("creditCode", self.faker.ean13()))
        # args.append(("defaultCurrency:id", ))
        args.append(("licenseCode", self.faker.ean13()))
        args.append(("name", self.faker.company()))
        args.append(("remark", self.faker.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    p = PartnerInformation()
    for i in range(100):
        pd = PartnerInformationData()
        data = pd.create_partner_data()

        res = p.create_partner_api(data)
        print(res)
