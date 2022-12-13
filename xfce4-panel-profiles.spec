%define url_ver	%(echo %{version} | cut -d. -f1,2)

%global __requires_exclude ^typelib\\(libxfce4ui

Name:		xfce4-panel-profiles
Summary:	Simple application to manage Xfce panel layouts
Version:	1.0.13
Release:	2
License:	GPLv3
Group:		Graphical desktop/Xfce
Url:		https://git.xfce.org/apps/xfce4-panel-profiles/about/
Source0:	https://archive.xfce.org/src/apps/xfce4-panel-profiles/%{url_ver}/xfce4-panel-profiles-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:	python3dist(pygobject)

%description
Xfce4 Panel Profiles (xfce4-panel-profiles, formerly known as xfpanel-switch)
is a simple application to manage Xfce panel layouts.

With the modular Xfce Panel, a multitude of panel layouts can be created.
This tool makes it possible to backup, restore, import, and export these
panel layouts.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--python=python3
%make_build

%install
%make_install

#handle docs in files section
rm -rf %{buildroot}%{_docdir}

#fix perms
chmod 0644 %{buildroot}%{_datadir}/%{name}/layouts/*

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.xfce.PanelProfiles.desktop
%{_datadir}/metainfo/org.xfce.PanelProfiles.appdata.xml
%{_mandir}/man1/xfce4-panel-profiles.1.*
%{_iconsdir}/hicolor/*/apps/org.xfce.PanelProfiles.{png,svg}
