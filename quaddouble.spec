%define devname	%mklibname -d -s qd

Epoch:		1
Name:		quaddouble
Group:		Sciences/Mathematics
License:	BSD
Summary:	Double-Double and Quad-Double Arithmetic
Version:	2.3.12
Release:	1
Source0:	http://crd.lbl.gov/~dhbailey/mpdist/qd-%{version}.tar.gz
URL:		http://www.cs.berkeley.edu/~yozo/

%define debug_package %{nil}

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
%configure --enable-fortran=no
%make CXXFLAGS='%{optflags} -fPIC'

%install
%makeinstall_std
rm -fr %{buildroot}%{_libdir}/qd

%files	-n %{devname}
%{_bindir}/qd-config
%dir %{_includedir}/qd
%{_includedir}/qd/*
%doc %dir %{_datadir}/doc/qd
%doc %{_datadir}/doc/qd/*
%{_libdir}/*.a


%changelog
* Wed Feb 08 2012 Alexander Khrukin <akhrukin@mandriva.org> 1:2.3.12-1
+ Revision: 771911
- little tab fixes
- version update 2.3.12

* Tue Sep 01 2009 Paulo Andrade <pcpa@mandriva.com.br> 1:2.2.p9-1mdv2010.0
+ Revision: 424034
- Use sagemath version of quaddouble due to clear problems in the upstream version

* Fri May 15 2009 Paulo Andrade <pcpa@mandriva.com.br> 2.3.7-4mdv2010.0
+ Revision: 376247
+ rebuild (emptylog)

* Thu May 14 2009 Paulo Andrade <pcpa@mandriva.com.br> 2.3.7-3mdv2010.0
+ Revision: 375751
+ rebuild (emptylog)

* Fri May 08 2009 Paulo Andrade <pcpa@mandriva.com.br> 2.3.7-2mdv2010.0
+ Revision: 373559
+ rebuild (emptylog)

* Fri Mar 27 2009 Paulo Andrade <pcpa@mandriva.com.br> 2.3.7-1mdv2009.1
+ Revision: 361542
- Initial import of quaddouble (qd) version 2.3.7
  Double-Double and Quad-Double Arithmetic
  http://www.cs.berkeley.edu/~yozo/
- quaddouble

