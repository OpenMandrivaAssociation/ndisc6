Name:		ndisc6
Version:	1.0.2
Release:	%mkrel 1
Summary:	IPv6 diagnostic tools
Group:		Networking/Other
License:	GPLv2 or GPLv3
URL:		http://www.remlab.net/ndisc6/
Source0:	http://www.remlab.net/files/ndisc6/%{name}-%{version}.tar.bz2
Source1:	rdnssd.rc
Patch1:		ndisc6-var_run.patch

%description
This package gathers a few diagnostic tools for IPv6 networks:
- ndisc6, which performs ICMPv6 Neighbor Discovery in userland,
- rdisc6, which performs ICMPv6 Router Discovery in userland,
- rltraceroute6, yet another IPv6 implementation of traceroute,
- tcptraceroute6, a TCP/IPv6-based traceroute implementation,
- tracert6, a ICMPv6 Echo Request based traceroute,
- tcpspray6, a TCP/IP Discard/Echo bandwidth metter.

%package -n rdnssd
Summary:IPv6 recursive DNS server discovery daemon

%description -n rdnssd
rdnssd autoconfigures recursive DNS servers on IPv6 networks 
using ICMPv6 Neighbor Discovery (RFC 5006), and can update 
the DNS resolvers configuration (/etc/resolv.conf) accordingly.

%prep
%setup -q
%patch1 -p0

%build
%configure2_5x --disable-suid-install
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std
%__mkdir_p %{buildroot}%{_initrddir}
%__install -m755 %{SOURCE1} %{buildroot}%{_initrddir}/rdnssd

%find_lang %{name}

%pre -n rdnssd
%_pre_useradd rdnssd %{_var}/run/rdnssd /bin/false

%postun -n rdnssd
%_postun_userdel rdnssd

%post -n rdnssd
%_post_service rdnssd

%preun -n rdnssd
%_preun_service rdnssd

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/addr2name
%{_bindir}/dnssort
%{_bindir}/name2addr
%{_sbindir}/rdisc6
%{_sbindir}/ndisc6
%{_sbindir}/rltraceroute6
%{_bindir}/tcpspray
%{_bindir}/tcpspray6
%{_sbindir}/tcptraceroute6
%{_sbindir}/tracert6
%doc %{_mandir}/man1/addr2name.1.*
%doc %{_mandir}/man1/dnssort.1.*
%doc %{_mandir}/man1/name2addr.1.*
%doc %{_mandir}/man1/tcpspray.1.*
%doc %{_mandir}/man1/tcpspray6.1.*
%doc %{_mandir}/man8/ndisc6.8.*
%doc %{_mandir}/man8/rdisc6.8.*
%doc %{_mandir}/man8/rltraceroute6.8.*
%doc %{_mandir}/man8/tcptraceroute6.8.*
%doc %{_mandir}/man8/tracert6.8.*

%files -n rdnssd
%defattr(-,root,root)
%doc COPYING README
%doc %{_mandir}/man8/rdnssd.8.*
%{_sbindir}/rdnssd
%dir %{_sysconfdir}/rdnssd
%{_initrddir}/rdnssd
%attr(755,root,root) %{_sysconfdir}/rdnssd/merge-hook
%dir %attr(0755,rdnssd,nogroup) %{_var}/run/rdnssd

