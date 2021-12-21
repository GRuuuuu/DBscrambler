#!bin/sh

fileName=${1}

# 전화번호
echo "---PHONE NUMBER---"
grep --color -E -n "01[0-9]-[0-9]{4}-[0-9]{4}" ${fileName}
grep --color -E -n "01[0-9][0-9]{8}" ${fileName}
echo "------------------\n\n"

echo "---ADDRESS---"
grep --color -E -n "[0-9]{3,4}동" ${fileName}
grep --color -E -n "[0-9]{3,4}호" ${fileName}
echo "------------------\n\n"

echo "---EMAIL---"
grep --color -E -n "[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}" ${fileName}
echo "------------------\n\n"

echo "---RRN---"
grep --color -E -n "[0-9]{6}\s?-?[0-9]{7}" ${fileName}
echo "------------------\n\n"