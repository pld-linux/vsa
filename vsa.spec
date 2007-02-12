# TODO:
#	- missing BRs
Summary:	A sound visualizer for the GNOME panel and EsounD
Summary(pl.UTF-8):   Wizualizator dźwięku dla panelu GNOME oraz EsounD
Name:		vsa
Version:	0.9.2
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://vsa.linuxcore.com/%{name}-%{version}.tgz
# Source0-md5:	88c21938fb0eaee31d7c507de1ea1eb3
URL:		http://vsa.linuxcore.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw-devel
BuildRequires:	gtkxmhtml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
VSA is a visual sound analyzer applet (eye candy to go along with
audio) for the GNOME panel and EsounD. VSA supports layering any
number of visualization, background or filter plug-ins, in any order.
If you want to develop plug-ins for VSA, you'll also need to install
vsa-devel.

%description -l pl.UTF-8
VSA jest wizualnym analizatorem dźwięku napisanym jako aplet panelu
GNOME i EsounD. VSA obsługuje wiele wizualizacji, tła i wtyczki
filtrów.

%package devel
Summary:	The header files for compiling VSA plug-ins
Summary(pl.UTF-8):   Pliki nagłówkowe do tworzenia wtyczek VSA
Group:		Development/Libraries

%description devel
The vsa-devel package contains the header files needed to compile
plug-ins for the VSA visual sound analyzer applet for GNOME and
EsounD. Install vsa-devel if you want to develop plug-ins for VSA.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilowania wtyczek
dla wizualngo analizatora dźwięku VSA.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure --prefix=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/vsa

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install vsa-plugin.h $RPM_BUILD_ROOT%{_includedir}/vsa


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog CONTRIBUTORS WISHLIST THEMES PLUGINS
%attr(755,root,root) %{_bindir}/vsa_applet
%{_datadir}/applets/Multimedia/vsa_applet.desktop
%{_sysconfdir}/CORBA/servers/vsa_applet.gnorba
%{_datadir}/vsa

%files devel
%defattr(644,root,root,755)
%{_includedir}/vsa
