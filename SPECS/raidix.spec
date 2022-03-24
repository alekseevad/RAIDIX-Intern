Name:           raidix
Version:        1.0
Release:        1%{?dist}
Summary:	Short program that prints some text, written in C++       

License:        GPLv3+
URL:            https://github.com/alekseevad/RAIDIX-Intern
Source0:        raidix-1.0.tar.gz
Patch0:		raidix-output-first-patch.patch

BuildRequires:  make, gcc-c++
Provides: 	raidix

%description
This is a test task for RAIDIX, where I create and build
rpm for a simple program, written in c++.

%global debug_package %{nil}

%prep
%setup -q
%patch0

%build
export CXX="%{__cxx}" 
export CPP="%{__cpp}"
export CFLAGS=""
make
make check

%install
%make_install

%post

%preun

%files
%license LICENSE
%{_bindir}/%{name}



%changelog
* Wed Mar 23 2022 alekseevad <alkseev2001ad@gmail.com>
- 
