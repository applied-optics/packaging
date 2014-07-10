Name:       serial_i13n
Version:    1.00
Release:    1

License:    GPL-2
Group:      Hardware/Other

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

URL:        http://optics.eee.nottingham.ac.uk
Source:     https://github.com/applied-optics/serial_i13n/archive/v%{version}.tar.gz

Summary:    User library for easy RS232 usage.

%if "%_lib" == "lib64"
%define LIB_SUFFIX 64
%else
%define LIB_SUFFIX %nil
%endif

%if %{defined suse_version}
BuildRequires:  gcc-c++
%endif

%if %{defined rhel_version}
BuildRequires:  gcc-c++
%endif

%if %{defined centos_version}
BuildRequires:  gcc-c++
%endif

%if %{defined fedora_version}
BuildRequires:  gcc-c++
%endif

%if %{defined mdkversion}
BuildRequires:  gcc-c++
%endif

%description
User library for easy RS232 serial usage.

%package -n libserial_i13n-0
Summary: RS232 serial library for instrumentation.
Group: Development/Libraries/C and C++

%description -n libserial_i13n-0
User library for easy RS232 serial usage.

%package -n libserial_i13n-devel
Summary: Serial instrumentation library development files
Requires: libserial_i13n-0
Group: Development/Libraries/C and C++

%description -n liblecroy_vxi11-devel
User library for easy RS232 serial usage.

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

%post -n libserial_i13n-0
/sbin/ldconfig

%postun -n libserial_i13n-0
/sbin/ldconfig

%files
%defattr(-,root,root,-)

%files -n libserial_i13n-0
%defattr(-,root,root,-)
%{_libdir}/libserial_i13n.so.*

%files -n libserial_i13n-devel
%defattr(-,root,root,-)
/usr/include/serial_i13n.h
%{_libdir}/libserial_i13n.so

%changelog

