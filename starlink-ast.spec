Summary:	AST - Astrometry and World Coordinate System library
Summary(pl):	AST - biblioteka do astronometrii i systemu wspó³rzêdnych ziemskich
Name:		starlink-ast
Version:	2.0_9.218
Release:	1
License:	LGPL (wcslib), non-commercial use and distribution (see AST_CONDITIONS)
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/ast/ast.tar.Z
# Source0-md5:	71dec6919d6dd2bf5656415d2f1fb49c
Patch0:		%{name}-make.patch
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_AST.html
BuildRequires:	gcc-g77
BuildRequires:	pgplot-devel
BuildRequires:	starlink-ems-devel
BuildRequires:	starlink-sae-devel
BuildRequires:	starlink-sla-devel
Requires:	starlink-sae
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
The AST library provides a comprehensive range of facilities for
attaching world coordinate systems to astronomical data, for
retrieving and interpreting that information and for generating
graphical output based on it.

%description -l pl
Biblioteka AST dostarcza wyczerpuj±cy zakres mo¿liwo¶ci do
przywi±zywania systemów wspó³rzêdnych ziemskich do danych
astronomicznych, uzyskiwania i interpretowania takich informacji oraz
do generowania w oparciu o nie grafiki.

%package devel
Summary:	Header files for AST library
Summary(pl):	Pliki nag³ówkowe biblioteki AST
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	starlink-ems-devel
Requires:	starlink-sla-devel

%description devel
Header files for AST library.

%description devel -l pl
Pliki nag³ówkowe biblioteki AST.

%package static
Summary:	Static Starlink AST library
Summary(pl):	Statyczna biblioteka Starlink AST
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink AST library.

%description static -l pl
Statyczna biblioteka Starlink AST.

%prep
%setup -q -c
%patch0 -p1

%build
OPT="%{rpmcflags}" \
SYSTEM=ix86_Linux \
./mk build \
	STARLINK=%{stardir} \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AST_CONDITIONS ast.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/sun*
%{stardir}/help/fac*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/ast_dev
%attr(755,root,root) %{stardir}/bin/ast_link*
%{stardir}/include/*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a
