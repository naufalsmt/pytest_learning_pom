from playwright.sync_api import Playwright

# able to find the baseurl, endpoint (login, create_order), payload of both endpoints, headers from web/network tab
# request is playwright.new_context(baseurl).post(endpoint, payload (data), headers{authorization (token), content-type}
# result of this request is response

base_url = "https://rahulshettyacademy.com/client" # base url of api
endpoint_login = "/api/ecom/auth/login" # login endpoint
endpoint_order = "/api/ecom/order/create-order" # create order endpoint
payload_login = {
    "userEmail":"alexis@mail.com",
    "userPassword":"Alex@12345"
}
payload_order = {"orders":[
    {"country":"India",
     "productOrderedId":"6960eac0c941646b7a8b3e68"
     }
]
}


class ApiUtils:
    def get_token(self, playwright: Playwright):
        api_request_login = playwright.request.new_context(base_url=base_url) # create a request with base url
        # pass the endpoint, payload with the request
        response_login = api_request_login.post(
            endpoint_login,
            data =payload_login
        )
        # verify whether the request is ok with success 200/201
        assert response_login.ok
        response_login_json = response_login.json() # assign the response json to a variable
        print(response_login_json)
        return response_login_json["token"] # retrieve the token from the response json and save to this method 'get_token'


    def create_order(self, playwright: Playwright):
        token = self.get_token(playwright) # call the token from the get_token method and saved to variable 'token'
        api_request_order = playwright.request.new_context(base_url=base_url) # create a request with base url
        # pass the endpoint, payload, headers along with request
        response_order = api_request_order.post(
            endpoint_order,
            data= payload_order,
            # for headers required to pass 'Authorization' and 'Content-type' which can found from web/network path
            headers= {
            "Authorization": token,
            "Content-Type": "application/json",
        })
        response_order_json = response_order.json() # assign order response json to variable
        print(response_order_json)
        order_id = response_order_json["orders"][0] # retrieve the first value in the response dictionary. here first
        # object in the dictionary is orders and in the orders first value is order id. here orders is a list
        print(order_id)
        return order_id # return the value of order_id into this method 'create_order'
