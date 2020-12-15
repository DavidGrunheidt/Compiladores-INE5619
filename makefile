QUICKSORT_PATH=./programs/quicksort.ccc
MERGESORT_PATH=./programs/mergesort.ccc
PONETHIC_PATH=./programs/phonetic.ccc

QUICSORT_OUTPUT=./outputs/quicksort.txt
MERGESORT_OUTPUT=./outputs/mergesort.txt
PHONETIC_OUTPUT=./outputs/phonetic.txt

install:
	pip3 install ply

quicksort:
	rm -f ${QUICSORT_OUTPUT}
	python3 lexer.py ${QUICKSORT_PATH} \&>> ${QUICSORT_OUTPUT}
	python3 parser.py ${QUICKSORT_PATH}

mergesort:
	rm -f ${MERGESORT_OUTPUT}
	python3 lexer.py ${MERGESORT_PATH} \&>> ${MERGESORT_OUTPUT}
	python3 parser.py ${MERGESORT_PATH}

phonetic:
	rm -f ${PHONETIC_OUTPUT}
	python3 parser.py ${PONETHIC_PATH} \&>> ${PHONETIC_OUTPUT}
	python3 parser.py ${PONETHIC_PATH}

all: quicksort mergesort phonetic