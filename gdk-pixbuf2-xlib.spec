#
# Conditional build:
%bcond_without	apidocs		# API documentation

Summary:	Deprecated API for integrating GdkPixbuf with Xlib data types
Summary(pl.UTF-8):	Przestarzałe API do integracji GdkPixbuf z typami danych Xlib
Name:		gdk-pixbuf2-xlib
Version:	2.40.2
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/gdk-pixbuf-xlib/2.40/gdk-pixbuf-xlib-%{version}.tar.xz
# Source0-md5:	fbd57e867e039a8cf9164d145c0f0434
URL:		https://gitlab.gnome.org/Archive/gdk-pixbuf-xlib
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gdk-pixbuf2-devel >= 2.39.2
BuildRequires:	glib2-devel >= 1:2.48.0
BuildRequires:	gtk-doc >= 1.20
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	gdk-pixbuf2 >= 2.42.0
Requires:	glib2 >= 1:2.48.0
Requires:	shared-mime-info
Suggests:	librsvg >= 2.31
Conflicts:	gtk+2 < 2:2.21.3-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GdkPixbuf-Xlib contains the deprecated API for integrating GdkPixbuf
with Xlib data types. This library was originally shipped by
GdkPixbuf, and has since been moved out of the original repository.

No newly written code should ever use this library.

%description -l pl.UTF-8
Biblioteka GdkPixbuf-Xlib zawiera przestarzałe API do integracji
GdkPixbuf z typami danych Xlib. Pierwotnie była dostarczana wraz z
GdkPixbuf, ale później została usunięta z oryginalnego repozytorium.

Żaden nowy kod nie powinien używać tej biblioteki.

%package devel
Summary:	Header files for gdk-pixbuf-xlib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gdk-pixbuf-xlib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdk-pixbuf2-devel >= 2.42.0
Requires:	glib2-devel >= 1:2.48.0
Requires:	xorg-lib-libX11-devel
Conflicts:	gtk+2-devel < 2:2.21.3-1

%description devel
Header files for gdk-pixbuf-xlib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gdk-pixbuf-xlib.

%package static
Summary:	Static gdk-pixbuf-xlib library
Summary(pl.UTF-8):	Biblioteka statyczna gdk-pixbuf-xlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gdk-pixbuf-xlib library.

%description static -l pl.UTF-8
Biblioteka statyczna gdk-pixbuf-xlib.

%package apidocs
Summary:	gdk-pixbuf-xlib API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gdk-pixbuf-xlib
Group:		Documentation
Conflicts:	gdk-pixbuf2-apidocs < 2.42
Conflicts:	gtk+2-apidocs < 2:2.21.3-1
BuildArch:	noarch

%description apidocs
API documentation for gdk-pixbuf-xlib library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gdk-pixbuf-xlib.

%prep
%setup -q -n gdk-pixbuf-xlib-%{version}

%build
%meson build \
	-Dgtk_doc=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -j1 -C build

%{!?with_apidocs:%{__rm} -r $RPM_BUILD_ROOT%{_gtkdocdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libgdk_pixbuf_xlib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdk_pixbuf_xlib-2.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdk_pixbuf_xlib-2.0.so
%{_includedir}/gdk-pixbuf-2.0/gdk-pixbuf-xlib
%{_pkgconfigdir}/gdk-pixbuf-xlib-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdk_pixbuf_xlib-2.0.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdk-pixbuf-xlib
%endif
