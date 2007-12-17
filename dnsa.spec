Summary:	DNS Auditing tool
Name:		dnsa
Version:	0.5
Release:	%mkrel 0.4
License:	GPL
Group:		Networking/Other
URL:		http://www.packetfactory.net/projects/dnsa/
Source:		%{name}-%{version}-beta.tar.bz2
BuildRequires:	libpcap-devel
BuildRequires:	libnet1.1.2-devel

%description
DNS Auditing tool

%prep

%setup -q -n %{name}-%{version}-beta

# lib64 fixes
perl -pi -e "s|/lib\ |/%{_lib}\ |g" sources/configure*

# anti recheck hack
touch sources/*

%build
cd sources

%configure

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 sources/dnsa %{buildroot}%{_bindir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc sources/AUTHORS sources/ChangeLog sources/INSTALL sources/KNOWN_BUGS sources/README sources/TODO docs
%{_bindir}/dnsa


