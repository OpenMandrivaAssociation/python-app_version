%global pypi_name app_version

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        8
Summary:        Read an application version from installed metadata
Group:          Development/Python
License:        MIT
URL:            https://github.com/lambdalisue/app_version
Source0:        https://files.pythonhosted.org/packages/7d/07/1089c21119a1ea49326779d9e89dc57845a785f91cd52561f3492def4049/app_version-%{version}.tar.gz
Patch0:         python-app_version-importlib.patch
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools-scm)

%description
Read an installed distribution's version from inside the package.

%prep
%autosetup -n app_version-%{version}

%build
# The sdist is not a git checkout, so setuptools-scm needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/app_version*

