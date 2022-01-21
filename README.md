# DBscrambler
scrambling data from sql dump

~~~
$ python3 main.py --help

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  parse     parse each SELECT line into multi line
  prechk    validate each column in metadata-yaml whether It is correct or primary key or unique key
  scramble  scramble the data from parsed sql dump
  valid     validate any exist PI in scrambled sql dump file
~~~

# DB Dump Guideline
sql dump file should include table information.

# Yaml Guideline
Form:  
~~~
dbs:
  - name: <DB NAME>
    tables:
      - name: <TABLE NAME>
        object_list:
            - column: <COLUMN NAME>
              cvt_option: <CHANGE OPTION>
            - column: <COLUMN NAME>
              cvt_option: <CHANGE OPTION>
              ...
~~~

## Convert Options
1. `fake_email`  
return [12~14 random english+number]@['naver.com', 'daum.net', 'nate.com', 'kakao.com', 'gmail.com', 'outlook.com', 'icloud.com']   
ex. YEJvmAFkXprd@daum.net

2. `fake_ip`  
reture random ipv4  
ex. 150.166.176.6


3. `korean_name`  
return 3 random korean letter  
ex. 기끟이

4. `phone_withdash`  
return phone number with dash. it remain initial 3 numbers of original data.  
ex. 010-1111-1111 -> 010-1234-5678  

5. `phone_nodash`  
return phone number without dash. it remain initial 3 numbers of original data.  
ex. 01711111111 -> 01712345678

6. `random_string`  
    ~~~
    - column: <COLUMN NAME>
        cvt_option: random_string
        params:
        - object:
            - digit
            - en_lowercase
            - en_uppercase
            - symbol
            - blank
            - kr
        - length: 14
    ~~~
    return random string include [digit, en_lowercase, en_uppercase, symbol, blank, kr].  
    ex. )3(.힉(!뿐}퓏~뚕hk

7. `set_string`  
    ~~~
    - column: <COLUMN NAME>
        cvt_option: set_string
        params:
        - string: "hololy"
    ~~~
    return input string  
    ex. hololy

8. `fake_birth`   
return birth date (yymmdd)  
ex. 960509

9. `rand_int`  
return random integer  
ex. 1234567

10. `rand_element`  
    ~~~
    - column: <COLUMN NAME>
        cvt_option: rand_element
        params:
        - object:
            - '1'
            - '0'
            - '호롤'
    ~~~
    return random element from given list  
    ex. 호롤

11. `korean_rid`  
return random Korean resident registration number(RRN)  
ex. 880218-1013010

12. `kr_zipcode`, `kr_doro`, `kr_doro_detail`  
This options return Korean address.
    ~~~
    - column: <first COLUMN NAME>
        cvt_option: random_address
        params:
            - column: <first COLUMN NAME>
            cvt_option: kr_zipcode
            - column: <second COLUMN NAME>
            cvt_option: kr_doro
            - column: <third COLUMN NAME>
            cvt_option: kr_doro_detail
    ~~~
    Since It scramble data by reading one line of [random_zipcodeKR.txt](https://github.com/GRuuuuu/DBscrambler/releases/tag/zipcode), If you want to scramble columns at the same time you need to bind as same `params`.   
    ex. '04417', '서울특별시 용산구 한남대로42길','한남동 12층'

# HOW-TO
## STEP 0. Install dependencies
~~~
$ pip3 install --no-index --no-dependencies --find-links="./packages" -r ./requirements.txt
~~~

download Random ZIP code(KR)
~~~
$ wget https://github.com/GRuuuuu/DBscrambler/releases/download/zipcode/random_zipcodeKR.txt
~~~
move into `/DBscrambler`
~~~
$ mv random_zipcodeKR.txt /DBscrambler
~~~

## STEP 1. Parsing
~~~
$ python3 main.py parse --help
Usage: main.py parse [OPTIONS]

  parse each SELECT line into multi line

Options:
  --orig PATH    add file path to the commands to store original sql dump file
  --parsed TEXT  add file path to the commands to store parsed sql dump file
  --help         Show this message and exit.
~~~
It will make parsed dump file.  

ex.
~~~
$ python3 main.py parse --orig example/test_dump.sql --parsed example/parsed_test_dump.sql
~~~


## STEP 2. Pre check yaml form
~~~
$ python3 main.py prechk --help
Usage: main.py prechk [OPTIONS]

  validate each column in metadata-yaml whether It is correct or primary key
  or unique key

Options:
  --file PATH  add sql dump file to the commands to provide column information
  --yaml PATH  add metadata-yaml file to the commands to validate
  --help       Show this message and exit.
~~~
Use this command to make sure your yaml file is correct and find out Primary&Unique key   

ex. 
~~~
$ python3 main.py prechk --file example/parsed_test_dump.sql --yaml example/convert_info.yml
~~~

It will compare your yaml and dump.sql and Let you know there is wrong name or primary&unique key in the yaml.  

ex.  
result:  
~~~
sample_table1:
  col_non_exist: 
  col_primary_key: []
  col_unique_key:
  - name
sample_table2:
  col_non_exist: []
  col_primary_key: []
  col_unique_key:
  - name
sample_table3:
  col_non_exist: []
  col_primary_key: []
  col_unique_key:
  - name
~~~

> Primary and Unique key should not be duplicated. Be aware when you generating random string.

## STEP 3. Scrambling data
~~~
$ python3 main.py scramble --help
Usage: main.py scramble [OPTIONS]

  scramble the data from parsed sql dump

Options:
  --file PATH              add "PARSED" sql dump file to the commands to be
                           scrambled
  --yaml PATH              add metadata-yaml file to the commands to provide
                           information on how to scramble
  --output_scrambled TEXT  filepath where scrambled sql dump file is stored
  --output_blank TEXT      filepath where scrambled data erased sql dump file
                           is stored
  --help                   Show this message and exit.
~~~

> **BE SURE TO USE PARSED SQL!**   
>if not, scrambler can not scramble all data.

ex.
~~~
$ python3 main.py scramble --file example/parsed_test_dump.sql --yaml example/convert_info.yml --output_scrambled scrambled.sql --output_blank blank.sql
~~~

It will create two file, scramble.sql and blank.sql.  
`scramble.sql` is the result of scrambling according to the rules defined in yaml,  
`blank.sql` is a file which all data scrambled has been erased.(For the next step: Validation)  

## STEP 4. Find out existing Personal Information(PI) 
~~~
$ python3 main.py valid --help
Usage: main.py valid [OPTIONS]

  validate any exist PI in scrambled sql dump file

Options:
  --sql PATH     add scrambled dump file path to commands to detect PI
  --result TEXT  add file path to commands to store result
  --help         Show this message and exit.
~~~
This is a step for finding out existing Personal Information. You should use `blank.sql`. if not, all the scrambled data can be detected  

ex.  
~~~
$ python3 main.py valid --sql blank.sql --result res.txt
~~~

>If some PI is detected, make new yaml and scramble your data again.  

----