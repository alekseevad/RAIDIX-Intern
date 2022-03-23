Name:           main
Version:        1.0
Release:        1%{?dist}
Summary:	Short program that prints some text, written in C++       

License:        GPLv3+
URL:            https://github.com/alekseevad/RAIDIX-Intern
Source0:        main-1.0.tar.gz
Patch0:		main-output-first-patch.patch

BuildRequires:  g++
BuildRequires:  make

%description


%prep
%autosetup


%build 
make %{?_smp_mflags}
%configure
%make_build


%install
%make_install


%files
%license LICENSE
%{_bindir}/%{name}
%doc add-docs-here



%changelog
* Wed Mar 23 2022 alekseevad <alkseev2001ad@gmail.com>
- 
