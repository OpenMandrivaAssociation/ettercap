Summary:	Ncurses/Gtk2 based sniffer/interceptor utility
Name:		ettercap
Version:	0.8.1
Release:	2
License:	GPLv2+
Group:		Networking/Other
Url:		https://ettercap.github.io/ettercap/
Source0:	https://github.com/Ettercap/ettercap/archive/v%{version}.tar.gz
BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	flex
BuildRequires:	ghostscript
BuildRequires:	groff
BuildRequires:	libnet-devel
BuildRequires:	libtool-devel
BuildRequires:	pcap-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
%rename ettercap-ng

%description
Ettercap is a suite for man in the middle attacks on LAN.

It features sniffing of live connections, content filtering
on the fly and many other interesting tricks.

It supports active and passive dissection of many protocols
(even ciphered ones) and includes many feature for network
and host analysis.

%files
%doc AUTHORS CHANGELOG INSTALL LICENSE README* THANKS TODO TODO.TESTING doc/*
%{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/ettercap
%{_datadir}/applications/ettercap.desktop
%{_datadir}/pixmaps/ettercap.svg
%{_datadir}/polkit-1/actions/org.pkexec.ettercap.policy
%{_libdir}/ettercap
%{_libdir}/libettercap.so
%dir %{_sysconfdir}/ettercap
%config(noreplace) %{_sysconfdir}/ettercap/*

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%cmake \
	-DENABLE_IPV6=yes \
	-DENABLE_SSL=ON \
	-DCMAKE_BUILD_TYPE=Release
%make

%install
%makeinstall_std -C build
