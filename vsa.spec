Summary:	A sound visualizer for the GNOME panel and EsounD.
Name:		vsa
Version:	0.9.2
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source:		http://vsa.linuxcore.com/%{name}-%{version}.tgz
URL:		http://vsa.linuxcore.com/
Requires:	fftw
BuildRoot:	/tmp/%{name}-%{version}-root

%description
VSA is a visual sound analyzer applet (eye candy to go along with audio) for
the GNOME panel and EsounD.  VSA supports layering any number of
visualization, background or filter plug-ins, in any order. If you want to
develop plug-ins for VSA, you'll also need to install vsa-devel.

%package devel
Summary:	The header files for compiling VSA plug-ins.
Group:		Development/Libraries

%description devel
The vsa-devel package contains the header files needed to compile plug-ins
for the VSA visual sound analyzer applet for GNOME and EsounD. Install
vsa-devel if you want to develop plug-ins for VSA.

%prep
%setup -q

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=${RPM_BUILD_ROOT}%{prefix} install
install -m755 -d ${RPM_BUILD_ROOT}%{prefix}/include/vsa
install vsa-plugin.h ${RPM_BUILD_ROOT}%{prefix}/include/vsa/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING TODO ChangeLog CONTRIBUTORS WISHLIST THEMES PLUGINS
%{prefix}/bin/vsa_applet
%{prefix}/share/applets/Multimedia/vsa_applet.desktop
/etc/CORBA/servers/vsa_applet.gnorba
%{prefix}/share/vsa/*

%files devel
%defattr(644,root,root,755)
%{prefix}/include/vsa/
