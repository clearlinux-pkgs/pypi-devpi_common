#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-devpi_common
Version  : 3.7.2
Release  : 2
URL      : https://files.pythonhosted.org/packages/4b/cd/ca7ccc051af5ff7569d79685afd2e51c103c0b1bd9743ee69384717e1b5a/devpi-common-3.7.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4b/cd/ca7ccc051af5ff7569d79685afd2e51c103c0b1bd9743ee69384717e1b5a/devpi-common-3.7.2.tar.gz
Summary  : utilities jointly used by devpi-server and devpi-client
Group    : Development/Tools
License  : MIT
Requires: pypi-devpi_common-license = %{version}-%{release}
Requires: pypi-devpi_common-python = %{version}-%{release}
Requires: pypi-devpi_common-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This package contains utility functions used by devpi-server and devpi-client.
See http://doc.devpi.net for more information.

%package license
Summary: license components for the pypi-devpi_common package.
Group: Default

%description license
license components for the pypi-devpi_common package.


%package python
Summary: python components for the pypi-devpi_common package.
Group: Default
Requires: pypi-devpi_common-python3 = %{version}-%{release}

%description python
python components for the pypi-devpi_common package.


%package python3
Summary: python3 components for the pypi-devpi_common package.
Group: Default
Requires: python3-core
Provides: pypi(devpi_common)
Requires: pypi(lazy)
Requires: pypi(packaging)
Requires: pypi(py)
Requires: pypi(requests)

%description python3
python3 components for the pypi-devpi_common package.


%prep
%setup -q -n devpi-common-3.7.2
cd %{_builddir}/devpi-common-3.7.2
pushd ..
cp -a devpi-common-3.7.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680188365
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . packaging
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . packaging
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-devpi_common
cp %{_builddir}/devpi-common-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-devpi_common/cf3eaf29116a37a7d9ba773e776104c067c8e5fc || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} packaging
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-devpi_common/cf3eaf29116a37a7d9ba773e776104c067c8e5fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
