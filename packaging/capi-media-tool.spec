Name:       capi-media-tool
Summary:    A Core API media tool library in Tizen Native API
Version:    0.1.1
Release:    0
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(capi-base-common)
BuildRequires:  pkgconfig(appcore-efl)
BuildRequires:  pkgconfig(libtbm)

Requires(post): /sbin/ldconfig
Requires(post): libprivilege-control
Requires(postun): /sbin/ldconfig

%description


%package devel
Summary:  A Core API media tool library in Tizen Native API (Development)
Group:    TO_BE/FILLED_IN
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig(libtbm)

%description devel

%prep
%setup -q


%build
%if 0%{?sec_build_binary_debug_enable}
export CFLAGS="$CFLAGS -DTIZEN_DEBUG_ENABLE"
export CXXFLAGS="$CXXFLAGS -DTIZEN_DEBUG_ENABLE"
export FFLAGS="$FFLAGS -DTIZEN_DEBUG_ENABLE"
%endif
MAJORVER=`echo %{version} | awk 'BEGIN {FS="."}{print $1}'`
cmake . -DCMAKE_INSTALL_PREFIX=/usr -DFULLVER=%{version} -DMAJORVER=${MAJORVER}


make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/opt/usr/devel
cp test/media_packet_test %{buildroot}/opt/usr/devel
cp LICENSE.APLv2 %{buildroot}/usr/share/license/%{name}

%make_install

%post
/sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%manifest capi-media-tool.manifest
%{_libdir}/libcapi-media-tool.so.*
%{_datadir}/license/%{name}
/opt/usr/devel/*
#%{_bindir}/*

%files devel
%{_includedir}/media/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libcapi-media-tool.so

