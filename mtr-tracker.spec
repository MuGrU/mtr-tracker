#
# spec file for package mtr-tracker
#
# Copyright (c) 2020 Thiago Ramos de Oliveira, Sao Paulo, Brazil.
# Contact: https://github.com/MuGrU/
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define name mtr-tracker
%define version 1.0
%define skip_python2 1

Name:           %{name}
Version:        %{version}
Release:        0
Summary:        Traceroute ISP location with API to http://ip-api.com
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Routing
Url:            https://github.com/MuGrU/mtr-tracker
source0:        https://github.com/MuGrU/mtr-tracker/%{name}-%{version}.tar.gz
BuildRequires: %{python_module setuptools}
BuildRequires: python-rpm-macros
Requires:  mtr
BuildArch: noarch 

%description
Motivation: My self-study to cover the lack of information about the ISP's to troubleshoot routing switching performance issues.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build
# remove pycache directories
find . -name __pycache__ -type d -exec rm -fr {} +

%install
export PYTHONDONTWRITEBYTECODE=1
%py3_install

%files

%doc README.md
%license LICENSE
%{_bindir}/mtr-tracker
%{python_sitelib}/*egg-info/

%changelog
