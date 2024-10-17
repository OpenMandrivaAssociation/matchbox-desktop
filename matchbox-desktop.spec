Summary: 	Desktop for the Matchbox Desktop
Name: 		matchbox-desktop
Version: 	2.0
Release: 	7
Url: 		https://matchbox-project.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0:	http://downloads.yoctoproject.org/releases/matchbox/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libmb)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(dbus-1)
Requires:	matchbox-panel
Requires:	matchbox-window-manager
Requires:	matchbox-common
Obsoletes:	matchbox-desktop-devel < %{version}-%{release}

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the main desktop from Matchbox.

%prep
%setup -q
%autopatch -p1
autoreconf -fiv

%build
%configure --enable-dnotify --enable-startup-notification --with-dbus
%make

%install
%makeinstall_std

# wmsession config
mkdir -p %{buildroot}/%_sysconfdir/X11/wmsession.d
cat > %{buildroot}/%_sysconfdir/X11/wmsession.d/22Matchbox <<EOF
NAME=Matchbox
ICON=/usr/share/pixmaps/mbdesktop.png
EXEC=/usr/bin/matchbox-session
DESC=Matchbox
SCRIPT:
exec /usr/bin/matchbox-session
EOF

%files
%doc AUTHORS README ChangeLog
%_bindir/%name
%config(noreplace) %_sysconfdir/X11/wmsession.d/*
