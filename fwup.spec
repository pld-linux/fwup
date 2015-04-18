Summary:	Configurable, image-based firmware update utility for embedded Linux-based systems
Summary(pl.UTF-8):	Konfigurowalne narzędzie do aktualizacji firmware'u dla wbudowanych systemów linuksowych
Name:		fwup
Version:	0.1.1
Release:	1
License:	Apache v2.0
Group:		Applications/System
Source0:	https://github.com/fhunleth/fwup/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	da6a2e3046c6e9d774e79c3898b84267
URL:		https://github.com/fhunleth/fwup
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libarchive-devel
BuildRequires:	libconfuse-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The `fwup` utility is a configurable image-based firmware update
utility for embedded Linux-based systems.

%description -l pl.UTF-8
Narzędzie fwup to konfigurowalne, oparte na obrazach narzędzie do
aktualizacji firmware'u dla systemów wbudowanych opartych na Linuksie.

%prep
%setup -q

%build
%{__aclocal}
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
%doc README.md TODO.md fwupdate.conf
%attr(755,root,root) %{_bindir}/fwup
