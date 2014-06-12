Name:       agilent_vxi11
Version:    1.03
Release:    1

License:    GPL-2
Group:      Hardware/Other

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

URL:        http://optics.eee.nottingham.ac.uk
Source:     https://github.com/applied-optics/agilent_vxi11/archive/v%{version}.tar.gz

Summary:    RPC protocol for communicating with Agilent Infiniium scopes over ethernet.

%if "%_lib" == "lib64"
%define LIB_SUFFIX 64
%else
%define LIB_SUFFIX %nil
%endif

%if %{defined suse_version}
Requires: libvxi11-0, libagilent_vxi11-0, libagilent_vxi11-devel
BuildRequires:  gcc-c++, libvxi11-devel
%endif

%if %{defined rhel_version}
Requires: libvxi11-0, libagilent_vxi11-0, libagilent_vxi11-devel
BuildRequires:  gcc-c++, libvxi11-devel
%endif

%if %{defined centos_version}
Requires: libvxi11-0, libagilent_vxi11-0, libagilent_vxi11-devel
BuildRequires:  gcc-c++, libvxi11-devel
%endif

%if %{defined fedora_version}
Requires: libvxi11-0, libagilent_vxi11-0, libagilent_vxi11-devel
BuildRequires:  gcc-c++, libvxi11-devel
%endif

%if %{defined mdkversion}
Requires: libvxi11-0, libagilent_vxi11-0, libagilent_vxi11-devel
BuildRequires:  gcc-c++, libvxi11-devel
%endif

%description
This is a collection of source code that will allow you to talk to Tektronix
scopes (currently TDS3000/DPO4000 series) and Abitrary Function Generators
using the VXI11 protocol, from Linux.

%package -n libagilent_vxi11-0
Summary: agilent vxi11 user library
Group: Development/Libraries/C and C++

%description -n libagilent_vxi11-0
Library with Tektronix scope/afg support.

%package -n libagilent_vxi11-devel
Summary: agilent library development files
Requires: libagilent_vxi11-0
Group: Development/Libraries/C and C++

%description -n libagilent_vxi11-devel
Library with Tektronix scope/afg support.

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

%post -n libagilent_vxi11-0
/sbin/ldconfig

%postun -n libagilent_vxi11-0
/sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/bin/agetwf
/usr/bin/agetwf_debug
/usr/bin/agilent_load_setup
/usr/bin/agilent_save_setup
/usr/bin/agilent_report_status
/usr/bin/agilent_debug

%files -n libagilent_vxi11-0
%defattr(-,root,root,-)
%{_libdir}/libagilent_vxi11.so.*

%files -n libagilent_vxi11-devel
%defattr(-,root,root,-)
/usr/include/agilent_vxi11.h
%{_libdir}/libagilent_vxi11.so

%changelog

