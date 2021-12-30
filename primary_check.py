import argparse
import re
import yaml

class DBPrimaryCheck:
    def __init__(self, dumpfile, ymlfile):
        self.state = "none"
        self.table = None
        self.dumpfile = dumpfile
        self.ymlfile = ymlfile

    def set_state(self, state):
        self.state = state

    def set_table(self, table):
        self.table = table

    def load_yml(self):
        with open(self.ymlfile) as f:
            yml_dict = yaml.load(f, Loader=yaml.FullLoader)
        yml_info = dict()
        for each in yml_dict['dbs']:
            for x in each['tables']:
                yml_info[x['name']]={'col':[ [e['column']] if e['cvt_option']!='random_address' else [x['column'] for x in e['params']] for e in x['object_list']]}
                yml_info[x['name']]['col'] = [item for sublist in yml_info[x['name']]['col'] for item in sublist]
        return yml_info

    def primary_check(self):
        table_info = dict()
        with open(self.dumpfile) as f:
            for line in f:
                if self.state == "none":
                    if line.strip().lower().startswith('create table'):
                        table = re.findall('\`.*?\`', line)
                        if not table:
                            continue
                        self.set_table(table[0].strip('`'))
                        self.set_state('create_table')
                        table_info[self.table] = {'col': [], 'primary_key': [], 'unique_key':[]}
                elif self.state == "create_table":
                    if line.strip().lower().startswith('create table'):
                        continue
                    if line.strip().lower().startswith('`'):
                        col = re.findall('\`.*?\`', line)[0].strip('`')
                        table_info[self.table]['col'].append(col)
                    if line.strip().lower().startswith('primary key'):
                        table_info[self.table]['primary_key'] = [each.strip('`') for each in re.findall('\`.*?\`', line)]
                    if line.strip().lower().startswith('unique key'):
                        table_info[self.table]['unique_key'] = [each.strip('`') for each in re.findall('\`.*?\`',re.findall('\(.*?\)', line)[0])]
                    if line.strip().endswith(';'):
                        self.set_state('none')
        yml_info = self.load_yml()


        for key, val in yml_info.items():
            yml_info[key]['col_primary_key'] =list(set(table_info[key]['primary_key']).intersection(set(val['col'])))
            yml_info[key]['col_unique_key'] = list(set(table_info[key]['unique_key']).intersection(set(val['col'])))
            yml_info[key]['col_non_exist'] = list(set(val['col'])-set(table_info[key]['col']))
            yml_info[key].pop('col')


        return yml_info


parser = argparse.ArgumentParser(description='convert or validate sqldump file')
parser.add_argument('--dumpfile', type=str, default='test_dump.sql')
parser.add_argument('--ymlfile', type=str, default='convert_info.yml')
args = parser.parse_args()

pc = DBPrimaryCheck(dumpfile=args.dumpfile,
                    ymlfile=args.ymlfile)
yml_info = pc.primary_check()
print(yaml.dump(yml_info))
