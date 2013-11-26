%define		fversion	%(echo %{version} |tr r -)
%define		modulename	RCurl
Summary:	General network (HTTP/FTP/...) client interface for R
Name:		R-cran-%{modulename}
Version:	1.95r4.1
Release:	1
License:	BSD
Group:		Applications/Network
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	ae05762f9dceb92e9aa95417399ce931
BuildRequires:	R >= 2.8.1
BuildRequires:	R-cran-bitops
BuildRequires:	texlive-fonts-cmsuper
BuildRequires:	texlive-latex-ae
BuildRequires:	texlive-latex-bibtex
BuildRequires:	texlive-xetex
BuildRequires:	curl-devel
Requires:	R-cran-bitops
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package allows one to compose general HTTP requests and provides
convenient functions to fetch URIs, get & post forms, etc. and process
the results returned by the Web server. This provides a great deal of
control over the HTTP/FTP/... connection and the form of the request
while providing a higher-level interface than is available just using
R socket connections. Additionally, the underlying implementation is
robust and extensive, supporting FTP/FTPS/TFTP (uploads and
downloads), SSL/HTTPS, telnet, dict, ldap, and also supports cookies,
redirects, authentication, etc.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
