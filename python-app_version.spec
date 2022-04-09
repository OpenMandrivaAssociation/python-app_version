%global pypi_name app_version

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        4
Summary:        A tiny utility to get application version from pkg_resouces
Group:          Development/Python
License:        MIT
URL:            https://github.com/lambdalisue/app_version
Source0:        https://files.pythonhosted.org/packages/7d/07/1089c21119a1ea49326779d9e89dc57845a785f91cd52561f3492def4049/app_version-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(tomli)

%description
This tiny application allow you to access version information of setup.py from __init__.py

%prep
%autosetup -n app_version-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/app_version*

