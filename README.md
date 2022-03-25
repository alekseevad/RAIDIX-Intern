## How To build rpm package
Prepare build tools

	sudo yum install gcc-c++ rpm-build rpm-devel rpmlint make bash \
		coreutils diffutils patch rpmdevtools

#### Checkout sources

	cd $HOME \
	mkdir rpmbuild \
	git clone https://github.com/alekseevad/RAIDIX-Intern

#### Build

	rpmbuild -ba SPECS/raidix.spec

#### Install

	sudo rpm -ihv RPMS/x86_64/raidix-1.0-1.el8.x86_64.rpm

#### Check and Remove

	raidix \
	sudo rpm -ev raidix
