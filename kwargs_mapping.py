kwargs = {"request_method": "GET", "data": "test data", "c": "C"}

for k, v in kwargs.items():
    print(f"----- Key={k} Value={v} -----")
    if k == "request_method":
        request_method = v
    if k == "data":
        data = v

print(request_method)
print(data)

c = kwargs.get("d", "")
print(c)


    # Need to figure out how to map multiple kwargs i.e. data and headers from postRequest()
    # for arg in kwargs.values():
    #     print("The arg is: --> ", arg)
    #     print(type(arg)) # String
    #     request_method = arg
    # for k, v in kwargs.items():
    #     print(f"----- Key={k} Value={v} -----")
    #     request_method = v
    #     print (request_method)