Name:       vxi11
Version:    1.11
Release:    1

License:    GPL-2
Group:      Hardware/Other

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

URL:        http://optics.eee.nottingham.ac.uk
Source:     https://github.com/applied-optics/vxi11/archive/v%{version}.tar.gz

Summary:    RPC protocol for communicating with VXI11-enabled devices over ethernet

%if "%_lib" == "lib64"
%define LIB_SUFFIX 64
%else
%define LIB_SUFFIX %nil
%endif

%if %{defined suse_version}
Requires: libvxi11-devel, libvxi11-0
BuildRequires:  gcc-c++, python
%py_requires

%endif

%if %{defined rhel_version}
Requires: libvxi11-devel, libvxi11-0
BuildRequires:  gcc-c++, python
%endif

%if %{defined centos_version}
Requires: libvxi11-devel, libvxi11-0
BuildRequires:  gcc-c++, python
%endif

%if %{defined fedora_version}
Requires: libvxi11-devel, libvxi11-0
BuildRequires:  gcc-c++, python, python-devel
%endif

%if %{defined mdkversion}
Requires: libvxi11-devel, libvxi11-0
BuildRequires:  gcc-c++, python, python-devel
%endif

%description
This is a collection of source code that will allow you to talk to ethernet-
enabled instruments that use the VXI11 protocol, from Linux. This includes a
wide range of instruments (including oscilloscopes, logic analysers, function
generators etc) by a wide range of manufacturers (including Tektronix and
Agilent to name just a couple). An interactive "send and receive" utility is
included as an example.

%package -n libvxi11-0
Summary: vxi11 user library
Group: Development/Libraries/C and C++

%description -n libvxi11-0
Library for accessing vxi11 functionality.

%package -n libvxi11-devel
Summary: vxi11 library development files
Requires: libvxi11-0
Group: Development/Libraries/C and C++

%description -n libvxi11-devel
Library for accessing vxi11 functionality.

#%package -n python-vxi11
#Summary: vxi11 Python library
#Group: Development/Libraries/Python
#Requires: python, libvxi11-0

#%description -n python-vxi11
#Library for accessing vxi11 functionality.

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

%post -n libvxi11-0
/sbin/ldconfig

%postun -n libvxi11-0
/sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/bin/vxi11_cmd
/usr/bin/vxi11_send

%files -n libvxi11-0
%defattr(-,root,root,-)
%{_libdir}/libvxi11.so.*

%files -n libvxi11-devel
%defattr(-,root,root,-)
/usr/include/vxi11_user.h
%{_libdir}/libvxi11.so

#%if 0%{?sles_version} == 10
#%else

#%files -n python-vxi11
#%defattr(-,root,root,-)
#%if ( %{undefined rhel_version} || 0%{?rhel_version} > 599 ) && ( %{undefined centos_version} || 0%{?centos_version} > 599 )
#/usr/lib*/python*/site-packages/vxi11-%{version}*.egg-info
#%endif
#/usr/lib*/python*/site-packages/vxi11.py*
#%endif

%changelog

