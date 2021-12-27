# DBscrambler
scrambling data from sql dump

## Package Install guide
pip3 install --no-index --no-dependencies --find-links="./packages" -r ./requirements.txt

## Download Random ZIP code
~~~
$ wget https://github.com/GRuuuuu/DBscrambler/releases/download/zipcode/random_zipcodeKR.txt
~~~

move into `/DBscrambler`
~~~
$ mv random_zipcodeKR.txt /DBscrambler
~~~

## Usage guide

1. Preprocess: `preproc ./input_dump_file.sql > parsed_dump_file.sql`
2. Scramble: `python main.py --file convert_info.yml --input parsed_dump_file.sql --output_scrambled out_dump_file.sql --output_blank out_dump_blank_file.sql`
3. Validation: `sh -x valid.sh ./out_dump_file`

> Highly Recommend run as background job during scramble step.