Summary:	NSS update DB tool
Name:		nss_updatedb
Version:	7
Release:	1
Source0:	http://www.padl.com/download/%{name}-7.tar.gz
# Source0-md5:	3f6cfe1221a350fcacc3f96779be4da1
License:	GPL
Group:		Base
URL:		http://www.padl.com/OSS/nss_updatedb.html
BuildRequires:	autoconf
BuildRequires:	db-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The nss_updatedb utility maintains a local cache of network directory
user and group information. Used in conjunction with the pam_ccreds
module, it provides a mechanism for disconnected use of network
directories. These tools are designed to work with pam_ldap and
nss_ldap

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install nss_updatedb $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS COPYING README ChangeLog
%attr(755,root,root) %{_sbindir}/*
