%global desc Implements support for python plugins in Nvim. Also works as a library for\
connecting to and scripting Nvim processes through its msgpack-rpc API.

# For old Fedora versions
%{!?python3_pkgversion:%global python3_pkgversion 3}

# EPEL7 Sphinx is too old, disable doc building by default
%if 0%{?el7}
%bcond_with sphinx
%else
%bcond_without sphinx
%endif

Name:           python-neovim
Version:        0.3.1
Release:        1%{?dist}

License:        ASL 2.0
Summary:        Python client to Neovim
URL:            https://github.com/neovim/pynvim
Source0:        https://github.com/neovim/pynvim/archive/%{version}/pynvim-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python2-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with sphinx}
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

%description
%{desc}

%package -n python2-neovim
Summary:        %{summary}
%{?python_provide:%python_provide python2-neovim}
Requires:       neovim
%if 0%{?el7}
Requires:       python-greenlet
Requires:       python-trollius
%else
Requires:       python2-greenlet
Requires:       python2-trollius
%endif
Requires:       python2-msgpack

%description -n python2-neovim
%{desc}

%package -n python%{python3_pkgversion}-neovim
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-neovim}
Requires:       neovim
Requires:       python%{python3_pkgversion}-greenlet
Requires:       python%{python3_pkgversion}-msgpack

%description -n python%{python3_pkgversion}-neovim
%{desc}

%if %{with sphinx}
%package doc
Summary:        Documentation for %{name}

%description doc
%{desc}

This package contains documentation in HTML format.
%endif

%prep
%autosetup -n pynvim-%{version}

%build
%py2_build
%py3_build

%if %{with sphinx}
pushd docs
make html
rm -f _build/html/.buildinfo
popd
%endif

%install
%py2_install
%py3_install

%files -n python2-neovim
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-neovim
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%if %{with sphinx}
%files doc
%license LICENSE
%doc docs/_build/html
%endif

%changelog
* Wed Jan 02 2019 Andreas Schneider <asn@redhat.com> - 0.3.1-1
- Update to version 0.3.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-2
- Rebuilt for Python 3.7

* Thu May 03 2018 Andreas Schneider <asn@redhat.com> - 0.2.6-1
- resolves: #1574026 - Update to 0.2.6

* Mon Mar 12 2018 Filip Szymański <fszymanski@fedoraproject.org> - 0.2.4-1
- resolves: #1541621 - Update to 0.2.4
- Add -doc subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Dec 30 2017 Filip Szymański <fszymanski@fedoraproject.org> - 0.2.0-1
- resolves: #1511245 - Update to 0.2.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.1.13-3
- Use %%{python3_pkgversion} macro for EPEL compatibility
- special-case python2 greenlet dependency on EL7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Filip Szymański <fszymanski at, fedoraproject.org> - 0.1.13-1
- Update to 0.1.13
- Use %%{summary} macro

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.12-4
- Rebuild for Python 3.6

* Wed Dec 07 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 0.1.12-3
- Add requires on python-trollius

* Mon Dec 05 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 0.1.12-2
- Add python2- package

* Sun Dec 04 2016 Andreas Schneider <asn@redhat.com> - 0.1.12-1
- Initial release
