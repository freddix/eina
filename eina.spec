Summary:	Enlightenment Foundation Library
Name:		eina
Version:	1.7.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	7583cf781bdc91d34b4ab0ee4d67ae28
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Eina library is a library that implements an API for data types
in an efficient way. It also provides some useful tools like opening
shared libraries, errors management, type conversion, time accounting
and memory pool.

%package devel
Summary:	Header files for Eina library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for Eina library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4/common -I m4/eina
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libeina.so.1
%attr(755,root,root) %{_libdir}/libeina.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeina.so
%{_includedir}/eina-1
%{_pkgconfigdir}/eina.pc

