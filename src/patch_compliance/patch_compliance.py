import os
import requests
from bs4 import BeautifulSoup
#from datetime import date,datetime
#from dateutil.relativedelta import relativedelta
import subprocess



class PatchCompliance():
    def __init__(self, host_file='', os_list=[]):
        # Intialize member variables
        self.host_file = host_file
        self.os_list = os_list
        self.kbs = {}
        self.kb_results_json = {}

        
    # retrieve patch data from official microsoft source and parse out the relevant data
    def released_patches(self):
        # TODO: add date functionality back in after implementing multipage parsing
        #today = date.today()
        #end_date = today - relativedelta(months=2)
        kbs = {}
        for os_search in self.os_list:
            url = 'https://www.catalog.update.microsoft.com/Search.aspx?q=' + os_search
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, 'html.parser')
            table = soup.find('table')
            rows = table.find_all('tr')
            for i in rows:
                table_data = i.find_all('td')
                data = [j.text for j in table_data]
        
                updates = []
                split_file = data[0].split('\n')
                for x in range(len(split_file)):
                    if 'KB' in split_file[x] and '(' in split_file[x]:
                        title = split_file[x].lstrip()

                        kb = title.split('(')[1].split(')')[0]

                        x +=1
                        kb_set = []
                        while 'KB' not in split_file[x]  and '(' not in split_file[x]:
                
                            if x+1 >= len(split_file):
                                break
                            else:
                                if split_file[x].lstrip() != '':
                                    kb_set.append(split_file[x].lstrip())
                                x +=1
                        
                        # TODO: add date functionality back in after implementing multipage parsing
                        #compare_date = datetime.strptime(kb_set[2].replace('\r',''), '%m/%d/%Y').date()
                        #if end_date > compare_date:
                        #    break
                        updates.append({'kb':kb,'title':title,'type':kb_set[1],'install_date':kb_set[2]})
        
                kbs[os]=updates
        return kbs

    # parse through patch data collected via powershell and format into JSON
    def host_patches(self):
        kb_results_json = {}

        for root, dirs, files in os.walk('.\host_data'):
            for file in files:
                if 'host_' in file:
                    
                    with open(os.path.join(root,file), "r") as f:
                        contents = f.read()
                        content_encode = contents.encode('ascii','ignore')
                        content_decode = content_encode.decode('utf-16')
                        host_data = content_decode.split('\n')

                        kb_results_json[file[5:][:-4]] = []

                        os_parsed = host_data.pop(-1)

                        for line in host_data:
                            kb = ""
                            if len(line.split()) != 0 and line.split()[0] != "Source" and "----" not in line.split()[0]:
                                for item in line.split()[0]:
                                    if "KB" in item:
                                        kb = item
                                    if "AUTHORITY" in item:
                                        install_type = item
                                    if '/' in item:
                                        item = item.split(".",1)[0]
                                        install_date = item
                                kb_results_json[file[5:][:-4]].append({"kb":kb,"installedon":install_date,"type":install_type, 'os':os_parsed})
        return kb_results_json


    # compare microsoft patch data to host patch data and return differences
    def compare_patch_data(self):
        final = {}

        for os in self.os_list:
            for kb in range(len(self.kbs[os])):

                for host in self.kb_results_json:
                    if self.kb_results_json[host]['os'] != os:
                        continue
                    final[host] = {'missing':[],'installed':[]}
                    found = False
                    install_type='Automatic'
                    if 'AUTHORITY' not in self.kb_results_json[host]['type']:
                        install_type = "Manual"
                    for host_kb in self.kb_results_json[host]['kbs']:
                        if host_kb['kb'] == self.kbs[os][kb]['kb']:
                            found = True
                            break
                    if found:
                        final[host]['installed'].append({"kb":kb,"InstalledOn":host_kb['installedon'],"InstallType":install_type,'title':self.kbs[os][kb]['title'],'update_type':self.kbs[os][kb]['type'],'release_date':self.kbs[os][kb]['install_date']})
                    else:
                        final[host]['missing'].append({"kb":kb,"InstalledOn":'NA',"InstallType":'NA',"ComputerName":host,'title':self.kbs[os][kb]['title'],'update_type':self.kbs[os][kb]['type'],'release_date':self.kbs[os][kb]['install_date']})
        return final



    def run(self):

        # run powershell script to retrieve host patch data
        cmd = ["PowerShell", "-ExecutionPolicy", "Unrestricted", "-File", ".\\get_patch.ps1",self.host_file]

        ec = subprocess.call(cmd)
        print("Powershell returned: {0:d}".format(ec))

        self.kbs = self.released_patches()
        self.kb_results_json = self.host_patches()
        final = self.compare_patch_data()

        # print report
        for host in final:
            print('REPORT for host: ' + host)
            print('------------------------------------------')
            print('')
            print('\tMissing Patches:')
            for y in final[host]['missing']:
                print('\t\t' + y)
            print('')
            print('\tInstalled Patches:')
            for y in final[host]['installed']:
                print('\t\t' + y)
            print()
            print()
