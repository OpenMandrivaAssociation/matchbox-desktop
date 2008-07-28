%define name 	matchbox-desktop
%define version 2.0
%define release %mkrel 3

Summary: 	Desktop for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox-project.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://matchbox-project.org/sources/%name/%version/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig libmatchbox-devel startup-notification-devel
BuildRequires:	gtk+2-devel
Requires:	matchbox-panel matchbox-window-manager matchbox-common

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the main desktop from Matchbox.

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
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%make_session

%postun
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%make_session

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%_bindir/%name
%config(noreplace) %_sysconfdir/X11/wmsession.d/*
