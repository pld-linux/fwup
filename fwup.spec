Summary:	Configurable, image-based firmware update utility for embedded Linux-based systems
Summary(pl.UTF-8):	Konfigurowalne narzędzie do aktualizacji firmware'u dla wbudowanych systemów linuksowych
Name:		fwup
Version:	1.15.0
Release:	1
License:	Apache v2.0
Group:		Applications/System
#Source0Download: https://github.com/fwup-home/fwup/releases
Source0:	https://github.com/fwup-home/fwup/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	31a4b67dedfd234252f784be34b9f3a3
URL:		https://github.com/fwup-home/fwup
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	help2man
BuildRequires:	libarchive-devel
BuildRequires:	libconfuse-devel >= 2.8
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	libconfuse >= 2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fwup utility is a configurable image-based firmware update utility
for embedded Linux-based systems.

%description -l pl.UTF-8
Narzędzie fwup to konfigurowalne, oparte na obrazach narzędzie do
aktualizacji firmware'u dla systemów wbudowanych opartych na Linuksie.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/fwup
%attr(755,root,root) %{_bindir}/img2fwup
%{bash_compdir}/fwup
%{_mandir}/man1/fwup.1*
