#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Fatal
Version  : 0.014
Release  : 13
URL      : http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Test-Fatal-0.014.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Test-Fatal-0.014.tar.gz
Summary  : 'incredibly simple helpers for testing code with exceptions'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Fatal-doc
BuildRequires : perl(Test::More)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Test-Fatal,
version 0.014:
incredibly simple helpers for testing code with exceptions

%package doc
Summary: doc components for the perl-Test-Fatal package.
Group: Documentation

%description doc
doc components for the perl-Test-Fatal package.


%prep
%setup -q -n Test-Fatal-0.014

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/Test/Fatal.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
