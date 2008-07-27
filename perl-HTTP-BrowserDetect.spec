#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTTP
%define		pnam	BrowserDetect
Summary:	HTTP::BrowserDetect - determine the Web browser, version, and platform from an HTTP user agent string
Summary(pl.UTF-8):	HTTP::BrowserDetect - moduł określający przeglądarkę WWW, wersję i platformę z nagłówka HTTP User-Agent
Name:		perl-HTTP-BrowserDetect
Version:	0.98
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ac6837e47e25a13e1c7b927f2c6d9adc
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTTP::BrowserDetect object does a number of tests on an HTTP user
agent string.  The results of these tests are available via methods of
the object.

%description -l pl.UTF-8
Obiekt HTTP::BrowserDetect wykonuje wiele testów na nagłówku HTTP
User-Agent. Wyniki tych testów są dostępne poprzez metody obiektu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTTP/BrowserDetect.pm
%{_mandir}/man3/*
