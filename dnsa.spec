Summary:	DNS Auditing tool
Name:		dnsa
Version:	0.5
Release:	%mkrel 0.6
License:	GPL
Group:		Networking/Other
URL:		http://www.packetfactory.net/projects/dnsa/
Source:		%{name}-%{version}-beta.tar.bz2
BuildRequires:	libpcap-devel
BuildRequires:	net-devel >= 1.1.3
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%configure2_5x

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 sources/dnsa %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc sources/AUTHORS sources/ChangeLog sources/INSTALL sources/KNOWN_BUGS sources/README sources/TODO docs
%{_bindir}/dnsa


%changelog
* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 0.5-0.6mdv2011.0
+ Revision: 571917
- use configure2_5x

* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 0.5-0.6mdv2010.0
+ Revision: 382716
- rebuilt against libnet 1.1.3

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5-0.5mdv2009.1
+ Revision: 298239
- rebuilt against libpcap-1.0.0

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.4mdv2008.1-current
+ Revision: 136367
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5-0.4mdv2007.0
+ Revision: 101644
- Import dnsa

* Fri Mar 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5-0.4mdk
- rebuilt against libnet1.1.2

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5-0.3mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Wed May 11 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5-0.2mdk
- lib64 fixes

* Tue Nov 23 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5-0.1mdk
- initial mandrake package

