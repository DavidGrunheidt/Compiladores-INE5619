install:
	pip3 install ply

quicksort:
	rm -f ./outputs/quicksort.txt
	python3 lexer.py ./programs/quicksort.ccc \&>> ./outputs/quicksort.txt

mergesort:
	rm -f ./outputs/mergesort.txt
	python3 lexer.py ./programs/mergesort.ccc \&>> ./outputs/mergesort.txt

phonetic:
	rm -f ./outputs/phonetic.txt
	python3 lexer.py ./programs/phonetic.ccc \&>> ./outputs/phonetic.txt

all: quicksort mergesort phonetic