.PHONY: all clean install uninstall

ifeq ($(BINDIR),)
BINDIR := bin
endif

ifeq ($(DESTDIR),)
DESTDIR := $(HOME)
endif

all:
	g++ -o raidix raidix.cpp

clean:
	rm -f raidix	

install:
	mkdir -p $(DESTDIR)/usr/bin
	install -m 0755 raidix $(DESTDIR)/usr/bin/raidix

check: all
	./raidix | grep -q 'Test task in RAIDIX'



  
