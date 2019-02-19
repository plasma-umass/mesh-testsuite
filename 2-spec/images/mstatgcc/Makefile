PREFIX = /usr/local

all:	mstatgcc mstatg++ mstatgfortran

clean:
	rm -f mstatgcc mstatg++ mstatgfortran

mstatgcc: mstatgcc.cc

mstatg++:
	ln -s mstatgcc mstatg++

mstatgfortran:
	ln -s mstatgcc mstatgfortran

install: mstatgcc mstatg++ mstatgfortran
	install -c -m 0755 mstatgcc $(PREFIX)/bin/mstatgcc
	install -c -m 0755 mstatg++ $(PREFIX)/bin/mstatg++
	install -c -m 0755 mstatgfortran $(PREFIX)/bin/mstatgfortran

.PHONY: all clean install
