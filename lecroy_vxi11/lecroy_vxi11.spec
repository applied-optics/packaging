Name:       lecroy_vxi11
Version:    1.00
Release:    1

License:    GPL-2
Group:      Hardware/Other

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

URL:        http://optics.eee.nottingham.ac.uk
Source:     https://github.com/applied-optics/lecroy_vxi11/archive/v%{version}.tar.gz

Summary:    RPC protocol for communicating with Lecroy scopes over ethernet.

%if "%_lib" == "lib64"
%define LIB_SUFFIX 64
%else
%define LIB_SUFFIX %nil
%endif

%if %{defined suse_version}
Requires: libvxi11-0, liblecroy_vxi11-0, liblecroy_vxi11-devel
BuildRequires:  gcc-c++, libvxi11-devel
%endif

%if %{defined rhel_version}
Requires: libvxi11-0, liblecroy_vxi11-0, liblecroy_vxi11-devel
BuildRequires:  gcc-c++, libvxi11-devel
%endif

%if %{defined centos_version}
Requires: libvxi11-0, liblecroy_vxi11-0, liblecroy_vxi11-devel
BuildRequires:  gcc-c++, libvxi11-devel
%endif

%if %{defined fedora_version}
Requires: libvxi11-0, liblecroy_vxi11-0, liblecroy_vxi11-devel
BuildRequires:  gcc-c++, libvxi11-devel
%endif

%if %{defined mdkversion}
Requires: libvxi11-0, liblecroy_vxi11-0, liblecroy_vxi11-devel
BuildRequires:  gcc-c++, libvxi11-devel
%endif

%description
This is a collection of source code that will allow you to talk to Lecroy
scopes using the VXI11 protocol, from Linux.

%package -n liblecroy_vxi11-0
Summary: lecroy vxi11 user library
Group: Development/Libraries/C and C++

%description -n liblecroy_vxi11-0
Library with Lecroy scope/afg support.

%package -n liblecroy_vxi11-devel
Summary: lecroy library development files
Requires: liblecroy_vxi11-0
Group: Development/Libraries/C and C++

%description -n liblecroy_vxi11-devel
Library with Lecroy scope/afg support.

%prep
%setup -q

%build
make


%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=/usr LIB_SUFFIX=%{LIB_SUFFIX}

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%post -n liblecroy_vxi11-0
/sbin/ldconfig

%postun -n liblecroy_vxi11-0
/sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/bin/lgetwf

%files -n liblecroy_vxi11-0
%defattr(-,root,root,-)
%{_libdir}/liblecroy_vxi11.so.*

%files -n liblecroy_vxi11-devel
%defattr(-,root,root,-)
/usr/include/lecroy_vxi11.h
%{_libdir}/liblecroy_vxi11.so

%changelog

