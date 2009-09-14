%define name ndisc6
%define version 0.9.8
%define release %mkrel 2

Summary: IPv6 diagnostic tools
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Networking/Other
Url: http://www.remlab.net/ndisc6/
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
This package gathers a few diagnostic tools for IPv6 networks:
- ndisc6, which performs ICMPv6 Neighbor Discovery in userland,
- rdisc6, which performs ICMPv6 Router Discovery in userland,
- rltraceroute6, yet another IPv6 implementation of traceroute,
- tcptraceroute6, a TCP/IPv6-based traceroute implementation,
- tracert6, a ICMPv6 Echo Request based traceroute,
- tcpspray6, a TCP/IP Discard/Echo bandwidth metter.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%_bindir/*
%_sbindir/*
%_sysconfdir/rdnssd/merge-hook
%_mandir/man?/*
