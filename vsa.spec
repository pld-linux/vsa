Summary:	A sound visualizer for the GNOME panel and EsounD
Summary(pl):	Wizualizator dºwiÍku dla panelu GNOME oraz EsounD
Name:		vsa
Version:	0.9.2
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://vsa.linuxcore.com/%{name}-%{version}.tgz
URL:		http://vsa.linuxcore.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
VSA is a visual sound analyzer applet (eye candy to go along with
audio) for the GNOME panel and EsounD. VSA supports layering any
number of visualization, background or filter plug-ins, in any order.
If you want to develop plug-ins for VSA, you'll also need to install
vsa-devel.

%description -l pl
VSA jest wizualnym analizatorem dºwiÍku napisanym jako aplet panelu
GNOME i EsounD. VSA obs≥uguje wiele wizualizacji, t≥a i wtyczki
filtrÛw.

%package devel
Summary:	The header files for compiling VSA plug-ins
Summary(pl):	Pliki nag≥Ûwkowe do tworzenia wtyczek VSA
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…

%description devel
The vsa-devel package contains the header files needed to compile
plug-ins for the VSA visual sound analyzer applet for GNOME and
EsounD. Install vsa-devel if you want to develop plug-ins for VSA.

%description devel -l pl
Ten pakiet zawiera pliki nag≥Ûwkowe potrzebne do kompilowania wtyczek
dla wizualngo analizatora dºwiÍku VSA.

%prep
%setup -q

%build
aclocal
autoconf
%configure --prefix=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} PREFIX=${RPM_BUILD_ROOT}%{_prefix} install
install -m755 -d ${RPM_BUILD_ROOT}%{_includedir}/vsa
install vsa-plugin.h ${RPM_BUILD_ROOT}%{_includedir}/vsa/

gzip -9nf README COPYING TODO ChangeLog CONTRIBUTORS WISHLIST THEMES PLUGINS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/vsa_applet
%{_datadir}/applets/Multimedia/vsa_applet.desktop
%{_sysconfdir}/CORBA/servers/vsa_applet.gnorba
%{_datadir}/vsa/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/vsa/
