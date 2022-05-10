import csv
import json
import requests
class Utils:
    def csv_read(self,path):
        with open(path, 'r') as file:
            self.reader= csv.reader(file)
            return list(self.reader)

    def csv_writerow(self,path,datum):
        with open(path, 'w') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(datum)

    def csv_writerows(self,path,data):
        with open(path, 'w', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerows(data)

    def json_read(self,path):
        with open(path, 'r') as file:
            return json.load(file)

    def json_write(self,path,data):
        with open(path, 'w') as file:
            json.dump(data, file, indent=2)
    def get_mapping(self,url):
        return requests.get(url, verify=False)
    def get_mapping_auth(self,url,head):
        return requests.get(url, headers=head, verify=False)
    def post_mapping(self,url,data):
        return requests.post(url, json=data, verify=False)
    def post_mapping_auth(self,url,data,head):
        return requests.post(url, json=data, headers=head, verify=False)
    def delete_mapping(self,url):
        return requests.delete(url, verify=False)
    def delete_mapping_auth(self,url,head):
        return requests.delete(url,headers=head, verify=False)
