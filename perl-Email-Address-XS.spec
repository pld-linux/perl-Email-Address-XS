#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Email
%define		pnam	Address-XS
Summary:	Email::Address::XS - Parse and format RFC 5322 email addresses and groups
Summary(pl.UTF-8):	Email::Address::XS - analiza i formatowanie adresów zgodnych z RFC 5322
Name:		perl-Email-Address-XS
Version:	1.04
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e756fc09d24e2aa4fafd97f30a2fd27b
URL:		http://search.cpan.org/dist/Email-Address-XS/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements RFC 5322 parser and formatter of email
addresses and groups. It parses an input string from email headers
which contain a list of email addresses or a groups of email addresses
(like From, To, Cc, Bcc, Reply-To, Sender, ...). Also it can generate
a string value for those headers from a list of email addresses
objects. Module is backward compatible with RFC 2822 and RFC 822.

%description -l pl.UTF-8
Ten moduł implementuje parser adresów email zgodnych z RFC 5322.
Parsowane są dane z nagłówków email zawierające adresy lub
ich grupy (takie jak From, To, Cc, Bcc, Reply-To, Sender, ...).
Dodatkowo, potrafi generować łańcuchy znakowe z listy podanych
adresów. Moduł jest kompatybilny wstecznie z RFC 2822 i RFC 822.

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
%{perl_vendorarch}/Email/Address/XS.pm
%dir %{perl_vendorarch}/auto/Email/Address/XS
%attr(755,root,root) %{perl_vendorarch}/auto/Email/Address/XS/XS.so
%{_mandir}/man3/Email::Address::XS.3pm*
