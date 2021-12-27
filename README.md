# DBscrambler
scrambling data from sql dump

## Package Install guide
pip3 install --no-index --no-dependencies --find-links="./packages" -r ./requirements.txt

## Usage guide
1. preproc ./input_dump_file
2. python main.py --file convert_info.yml --input parsed_dump_file --output_scrambled out_dump_file --output_blank out_dump_blank_file