%define name vsa
%define ver 0.9.2
%define rel 1
%define prefix /usr

Summary: A sound visualizer for the GNOME panel and EsounD.
Name: %{name}
Version: %{ver}
Release: %{rel}
Copyright: GPL
Packager: Charles <int@linuxcore.com>
Vendor: Charles <int@linuxcore.com>
Group: Applications/Multimedia
Source: http://vsa.linuxcore.com/vsa-%{ver}.tgz
BuildRoot: /var/tmp/%{name}-%{version}-root
URL: http://vsa.linuxcore.com/
Requires: fftw

%package devel
Summary: The header files for compiling VSA plug-ins.
Group: Development/Libraries
%description devel
The vsa-devel package contains the header files needed to compile
plug-ins for the VSA visual sound analyzer applet for GNOME and
EsounD. Install vsa-devel if you want to develop plug-ins for VSA.

%description
VSA is a visual sound analyzer applet (eye candy to go along with
audio) for the GNOME panel and EsounD.  VSA supports layering any
number of visualization, background or filter plug-ins, in any
order. If you want to develop plug-ins for VSA, you'll also need to
install vsa-devel.

%prep

%setup -q

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=${RPM_BUILD_ROOT}%{prefix} install
install -m755 -d ${RPM_BUILD_ROOT}%{prefix}/include/vsa
install -m644 vsa-plugin.h ${RPM_BUILD_ROOT}%{prefix}/include/vsa/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING TODO ChangeLog CONTRIBUTORS WISHLIST THEMES PLUGINS
%{prefix}/bin/vsa_applet
%{prefix}/share/applets/Multimedia/vsa_applet.desktop
/etc/CORBA/servers/vsa_applet.gnorba
%{prefix}/share/vsa/*

%files devel
%defattr(-,root,root)
%{prefix}/include/vsa/

%changelog
* Mon Aug 30 1999 Tim Powers <timp@redhat.com>
- changed group

* Wed Aug 18 1999 Tim Powers <timp@redhat.com>
- added Requires: fftw

* Fri Aug 6 1999 Tim Powers <timp@redhat.com>
- origional spec from http://vsa.linuxcore.com/
- minor changes in spec file, mainly changed buildroot, and use of %{prefix}
  etc.
- built for Powertools
