%define devname	%mklibname -d -s qd

Name:		quaddouble
Group:		Sciences/Mathematics
License:	BSD
Summary:	Double-Double and Quad-Double Arithmetic
Version:	2.3.7
Release:	%mkrel 3
Source:		http://www.cs.berkeley.edu/~yozo/software/qd-%{version}.tar.gz
URL:		http://www.cs.berkeley.edu/~yozo/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	gcc-gfortran

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
%setup -q -n qd-%{version}

%build
%configure
%make

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files		-n %{devname}
%defattr(-,root,root)
%{_bindir}/qd-config
%dir %{_includedir}/qd
%{_includedir}/qd/*
%{_libdir}/*.a
%dir %{_libdir}/qd
%{_libdir}/qd/*
%doc %dir %{_datadir}/doc/qd
%doc %{_datadir}/doc/qd/*
