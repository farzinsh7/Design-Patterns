import xmltodict

class Application:
    def send_request(self):
        return 'Structural/data.xml'


class Analytic:
    def recieve_request(self, json):
        return json


class Adapter:
    def convert_xml_json(self, file):
        with open(file, 'r') as myfile:
            obj = xmltodict.parse(myfile.read())
            return obj
        
        
def client_adapter():
    sender = Application().send_request() # get file
    converted_data = Adapter().convert_xml_json(sender) # convert to json
    reciever = Analytic().recieve_request(converted_data) # recieve file
    print(reciever)
    
client_adapter()