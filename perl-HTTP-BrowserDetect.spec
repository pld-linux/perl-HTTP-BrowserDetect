#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	BrowserDetect
Summary:	Determine the Web browser, version, and platform from an HTTP user agent string
Summary(pl):	Modu³ okre¶laj±cy przegl±darkê WWW, wersjê i platformê z nag³ówka HTTP User-Agent
Name:		perl-HTTP-BrowserDetect
Version:	0.97
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTTP::BrowserDetect object does a number of tests on an HTTP user
agent string.  The results of these tests are available via methods of
the object.

%description -l pl
Obiekt HTTP::BrowserDetect wykonuje wiele testów na nag³ówku HTTP
User-Agent. Wyniki tych testów s± dostêpne poprzez metody obiektu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/HTTP/BrowserDetect.pm
%{_mandir}/man3/*
