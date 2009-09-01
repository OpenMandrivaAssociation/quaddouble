%define devname	%mklibname -d -s qd

Epoch:		1
Name:		quaddouble
Group:		Sciences/Mathematics
License:	BSD
Summary:	Double-Double and Quad-Double Arithmetic
Version:	2.2.p9
Release:	%mkrel 1
# Modified to use sagemath spkg due to doctest failures that are clean
# problems in the previous upstream tarball
Source:		quaddouble-%{version}.tar.bz2
URL:		http://www.cs.berkeley.edu/~yozo/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

%package	-n %{devname}
Group:		Development/C++
Summary:	Double-Double and Quad-Double Arithmetic
Provides:	qd-static-devel = %{version}-%{release}

%description	-n %{devname}
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

%prep
%setup -q -n %{name}-%{version}/src

%build
%configure --enable-fortran=no
%make CXXFLAGS='%{optflags} -fPIC'

%install
%makeinstall_std
rm -fr %{buildroot}%{_libdir}/qd

%clean
rm -rf %{buildroot}

%files		-n %{devname}
%defattr(-,root,root)
%{_bindir}/qd-config
%dir %{_includedir}/qd
%{_includedir}/qd/*
%{_libdir}/*.a
%doc %dir %{_datadir}/doc/qd
%doc %{_datadir}/doc/qd/*
