Summary:	A C++ Framework for Evolutionary Computing
Name:		libevocosm
Version:	3.3.1
Release:	1
License:	GPL
Group:		Libraries
URL:		http://www.coyotegulch.com/products/libcoyotl/index.html
Source0:	http://www.coyotegulch.com/distfiles/%{name}-%{version}.tar.gz
# Source0-md5:	9975e9375aaf6a9365f62ceca58518ea
BuildRequires:	libbrahe-devel
BuildRequires:	libcoyotl-devel = 3.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libevocosm, a collection of tools for creating a wide variety of
evolutionary algorithms.

%package devel
Summary:	libcoyotl headers and documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libevocosm libraries headers and documentation.

%package static
Summary:	libevocosm static libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
libevocosm static libraries.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/lib*.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/api
%{_docdir}/%{name}/api/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
