from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class MaterialSignal(GetTokenHeader):

    def create_scm_material_signal_api(self,variables):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_scm_material_signal(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_scm_material_signal
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res