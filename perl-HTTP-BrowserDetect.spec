%include	/usr/lib/rpm/macros.perl

%define	pdir	HTTP
%define	pnam	BrowserDetect

Summary:	HTTP-BrowserDetect perl module
Summary(pl):	Modu³ perla HTTP-BrowserDetect
Name:		perl-%{pdir}-%{pnam}
Version:	0.96
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP-BrowserDetect perl module.

%description -l pl
Modu³ perla HTTP-BrowserDetect.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

gzip -9nf Changes README

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTTP/BrowserDetect.pm
%{_mandir}/man3/*
