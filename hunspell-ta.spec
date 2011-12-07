Name: hunspell-ta
Summary: Tamil hunspell dictionaries
Version: 20100226
Release: 1%{?dist}
Source: http://tamil.nrcfoss.au-kbc.org.in/files/hunspell/ta_IN-hunspell-Wordlist.tar.gz 
Group: Applications/Text
URL: http://nrcfoss.au-kbc.org.in
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Tamil hunspell dictionaries.

%prep
%setup -q -c -n ta_IN-hunspell-wordlist

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell

cp -p ta_IN-hunspell-wordlist/*.dic ta_IN-hunspell-wordlist/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ta_IN-hunspell-wordlist/README ta_IN-hunspell-wordlist/LICENSE ta_IN-hunspell-wordlist/Copyright
%{_datadir}/myspell/*

%changelog
* Fri Feb 26 2010 Parag <pnemade AT redhat.com> - 20100226-1
- Resolves:rh#568225 - Fix license tag

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20090929-1.1
- Rebuilt for RHEL 6

* Tue Sep 29 2009 Parag <pnemade@redhat.com> - 20090929-1
- Update to new dictionary wordlist with new URL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060222-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060222-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 06 2008 Parag <pnemade@redhat.com> - 20060222-2
- Added Copyright and fixed License tag

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20060222-1
- Initial Fedora release
