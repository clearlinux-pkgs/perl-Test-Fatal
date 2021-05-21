#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Fatal
Version  : 0.016
Release  : 41
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Fatal-0.016.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Fatal-0.016.tar.gz
Summary  : 'incredibly simple helpers for testing code with exceptions'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Fatal-license = %{version}-%{release}
Requires: perl-Test-Fatal-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::More)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Test-Fatal,
version 0.016:
incredibly simple helpers for testing code with exceptions

%package dev
Summary: dev components for the perl-Test-Fatal package.
Group: Development
Provides: perl-Test-Fatal-devel = %{version}-%{release}
Requires: perl-Test-Fatal = %{version}-%{release}

%description dev
dev components for the perl-Test-Fatal package.


%package license
Summary: license components for the perl-Test-Fatal package.
Group: Default

%description license
license components for the perl-Test-Fatal package.


%package perl
Summary: perl components for the perl-Test-Fatal package.
Group: Default
Requires: perl-Test-Fatal = %{version}-%{release}

%description perl
perl components for the perl-Test-Fatal package.


%prep
%setup -q -n Test-Fatal-0.016
cd %{_builddir}/Test-Fatal-0.016

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Fatal
cp %{_builddir}/Test-Fatal-0.016/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Fatal/463828319c148499572f64a01d56c380eb64ee67
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Fatal.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Fatal/463828319c148499572f64a01d56c380eb64ee67

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Test/Fatal.pm
