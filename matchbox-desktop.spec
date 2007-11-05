%define name 	matchbox-desktop
%define version 0.9.1
%define release 1mdk

Summary: 	Desktop for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox.handhelds.org/
License: 	GPL
Group: 		Graphical desktop/Other
Source: 	%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
BuildRequires:	pkgconfig libmatchbox-devel startup-notification-devel
Requires:	matchbox-panel matchbox-window-manager matchbox-common

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the main desktop from Matchbox.

%package devel
Group:		Development/C
Summary:	Headers and static libraries from %name

%description devel
Headers and static libraries from %name.

%prep
%setup -q

%build
%configure2_5x --enable-dnotify --enable-startup-notification
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# wmsession config
mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/X11/wmsession.d
cat > $RPM_BUILD_ROOT/%_sysconfdir/X11/wmsession.d/22Matchbox <<EOF
NAME=Matchbox
ICON=/usr/share/pixmaps/mbdesktop.png
EXEC=/usr/bin/matchbox-session
DESC=Matchbox
SCRIPT:
exec /usr/bin/matchbox-session
EOF

%post
/sbin/ldconfig
%make_session

%postun
/sbin/ldconfig
%make_session

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%_bindir/%name
%config(noreplace) %_sysconfdir/X11/wmsession.d/*
%config %_sysconfdir/matchbox/
#%_datadir/%name
%dir %_libdir/matchbox/desktop
%_libdir/matchbox/desktop/*.so
%_datadir/pixmaps/*
%_datadir/applications/*

%files devel
%defattr(-,root,root)
%_includedir/%name
%_libdir/pkgconfig/*.pc
%_libdir/matchbox/desktop/*.a
%_libdir/matchbox/desktop/*.la

