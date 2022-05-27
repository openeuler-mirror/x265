Summary:          H.265/HEVC encoder
Name:             x265
Version:          3.5
Release:          1
URL:              http://x265.org/
License:          GPLv2

Source0:          https://bitbucket.org/multicoreware/%{name}_git/get/%{version}.tar.gz

BuildRequires:    rpm-build cmake make gcc gcc-c++ gdb git

%ifarch x86_64
BuildRequires:    nasm >= 2.13
%endif

%description
x265 is a H.265/HEVC video encoder application library, designed to encode
video or images into an H.265/HEVC encoded bitstream.

%package devel
Summary:          Development files for x265
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
x265 develop library.

%prep
%autosetup -n %{name}_%{version}

%build
%ifarch aarch64
%cmake -G "Unix Makefiles" \
 -DBIN_INSTALL_DIR:STRING="bin" \
 -DCHECKED_BUILD:BOOL=OFF \
 -DCMAKE_BUILD_TYPE:STRING="Release" \
 -DCMAKE_INSTALL_PREFIX:PATH="/usr" \
 -DDETAILED_CU_STATS:BOOL=OFF \
 -DENABLE_AGGRESSIVE_CHECKS:BOOL=OFF \
 -DENABLE_ASSEMBLY:BOOL=ON \
 -DENABLE_CLI:BOOL=ON \
 -DENABLE_HDR10_PLUS:BOOL=OFF \
 -DENABLE_LIBNUMA:BOOL=ON \
 -DENABLE_LIBVMAF:BOOL=OFF \
 -DENABLE_PIC:BOOL=OFF \
 -DENABLE_PPA:BOOL=OFF \
 -DENABLE_SHARED:BOOL=ON \
 -DENABLE_SVT_HEVC:BOOL=OFF \
 -DENABLE_TESTS:BOOL=OFF \
 -DENABLE_VTUNE:BOOL=OFF \
 -DFSANITIZE="" \
 -DLIBDL:FILEPATH="/usr/lib64/libdl.so" \
 -DLIB_INSTALL_DIR:STRING="lib64" \
 -DNASM_EXECUTABLE:FILEPATH="NASM_EXECUTABLE-NOTFOUND" \
 -DNO_ATOMICS:BOOL=OFF \
 -DNUMA_ROOT_DIR:PATH="NUMA_ROOT_DIR-NOTFOUND" \
 -DSTATIC_LINK_CRT:BOOL=OFF \
 -DVMAF:FILEPATH="VMAF-NOTFOUND" \
 -DWARNINGS_AS_ERRORS:BOOL=OFF \
 source
%endif

%ifarch x86_64
%cmake -G "Unix Makefiles" \
 -DBIN_INSTALL_DIR:STRING="bin" \
 -DCHECKED_BUILD:BOOL=OFF \
 -DCMAKE_BUILD_TYPE:STRING="Release" \
 -DCMAKE_INSTALL_PREFIX:PATH="/usr" \
 -DDETAILED_CU_STATS:BOOL=OFF \
 -DENABLE_AGGRESSIVE_CHECKS:BOOL=OFF \
 -DENABLE_ASSEMBLY:BOOL=ON \
 -DENABLE_CLI:BOOL=ON \
 -DENABLE_HDR10_PLUS:BOOL=OFF \
 -DENABLE_LIBNUMA:BOOL=ON \
 -DENABLE_LIBVMAF:BOOL=OFF \
 -DENABLE_PIC:BOOL=ON \
 -DENABLE_PPA:BOOL=OFF \
 -DENABLE_SHARED:BOOL=ON \
 -DENABLE_SVT_HEVC:BOOL=OFF \
 -DENABLE_TESTS:BOOL=OFF \
 -DENABLE_VTUNE:BOOL=OFF \
 -DFSANITIZE="" \
 -DLIBDL:FILEPATH="/usr/lib64/libdl.so" \
 -DLIB_INSTALL_DIR:STRING="lib64" \
 -DNASM_EXECUTABLE:FILEPATH="/usr/bin/nasm" \
 -DNO_ATOMICS:BOOL=OFF \
 -DNUMA_ROOT_DIR:PATH="NUMA_ROOT_DIR-NOTFOUND" \
 -DSTATIC_LINK_CRT:BOOL=OFF \
 -DVMAF:FILEPATH="VMAF-NOTFOUND" \
 -DWARNINGS_AS_ERRORS:BOOL=OFF \
 source
%endif

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/libx265.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/x265
%{_libdir}/libx265.so.199
%license COPYING

%files devel
%{_includedir}/x265.h
%{_includedir}/x265_config.h
%{_libdir}/libx265.so
%{_libdir}/pkgconfig/x265.pc

%changelog
* Thu May 26 2022 wulei <wulei80@h-partners.com> - 3.5-1
- Update package

* Mon Sep 14 2020 Xiyuan Wang <wangxiyuan1007@gmail.com> - 3.4-2
- Update Source0 in spec

* Wed Jun 03 2020 openEuler Buildteam <buildteam@openeuler.org> - 3.4-1
- Package init
