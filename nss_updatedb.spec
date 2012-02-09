Summary:	NSS update DB tool
Summary(pl.UTF-8):	Narzędzie do uaktualniania bazy NSS
Name:		nss_updatedb
Version:	10
Release:	1
License:	GPL
Group:		Base
Source0:	http://www.padl.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	e8d53b07050557972d6cb9de63a8162a
URL:		http://www.padl.com/OSS/nss_updatedb.html
BuildRequires:	autoconf
BuildRequires:	db-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The nss_updatedb utility maintains a local cache of network directory
user and group information. Used in conjunction with the pam_ccreds
module, it provides a mechanism for disconnected use of network
directories. These tools are designed to work with pam_ldap and
nss_ldap.

%description -l pl.UTF-8
Narzędzie nss_updatedb utrzymuje lokalną pamięć podręczną sieciowego
katalogu informacji o użytkownikach i grupach. Używane w połączeniu z
modułem pam_ccreds udostępnia mechanizm do używania katalogów
sieciowych przy braku połączenia. Narzędzia te są zaprojektowane do
użytku z pam_ldap i nss_ldap.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p nss_updatedb $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_sbindir}/nss_updatedb
