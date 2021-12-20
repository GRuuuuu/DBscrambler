import json
import yaml;
import re;

orig_dump = open('/home/gru/dbscram/dump.sql');
parsed_dump = open('./parsed_dump.sql','wt');

yaml_meta={};
yaml_dbs=[];

db='';
table='';
lineNum=0;
start=0;
end=0;

yaml_meta["dbs"]=yaml_dbs;

while True:
    line=orig_dump.readline();

    if re.match("USE",line) is not None:
        # Find db name
        m=re.search("(?:\x60)(.*)(?:\x60)",line);
        db=m.group(1);
        
        parsed_dump.writelines(line);
        lineNum+=1;

        # [YAML] Set db name & tables
        yaml_db={}; 
        yaml_tables=[];
        yaml_db["name"]=db;
        yaml_db["tables"]=yaml_tables;
        yaml_dbs.append(yaml_db);

    elif re.match("INSERT INTO",line) is not None:
        # Find table name
        m=re.search("(?:\x60)(\S*)(?:\x60)",line);
        table=m.group(1);

        # Cut First Line (INSERT INTO~VALUES)
        v=re.search("VALUES\s",line);
        parsed_dump.writelines(line[0:v.end()]+"\n");
        lineNum+=1;

        start=lineNum+1;
        st='';
        inQuotes=0; # in Quotes=1, not in Quotes=0
        isEscape=0; # escaped character=1, nomal character=0
        newLine=0; # end of line=1, in line=0

        # [YAML] Set table name
        yaml_table={};
        yaml_tables.append(yaml_table);
        yaml_table["name"]=table;
        yaml_table["start"]=start;

        # Add new line into each lines
        for a in line[v.end():]:
            if a=='(' :
                st+=a;
            elif a==')' and inQuotes==0 :
                st+=a;
                parsed_dump.writelines(st);
                lineNum+=1;
                newLine=1;
            elif a==',' and newLine==1:
                parsed_dump.writelines(a+"\n");
                if lineNum==43:
                    print(st);
                st='';
                newLine=0;
            elif a=='\'' and inQuotes==0 and isEscape==0:
                st+=a;
                inQuotes=1;
            elif a=='\'' and inQuotes==1 and isEscape==0:
                st+=a;
                inQuotes=0;
            elif a=='\\':
                st+=a;
                isEscape=1;        
            else:
                if isEscape==1:
                    isEscape=0;
                st+=a;
        end=lineNum;
        yaml_table["end"]=end;
        parsed_dump.writelines("\n");
        
    elif line == '':
        # [YAML] save metadata as yaml
        with open("./parsed_meta.yaml","wt") as f:
            yaml.dump(yaml_meta, f, sort_keys=False);
        break;
    else:
        parsed_dump.writelines(line);
        lineNum+=1;
        continue;
