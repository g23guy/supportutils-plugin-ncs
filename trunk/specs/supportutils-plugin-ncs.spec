#
# spec file for package supportutils-plugin-ncs (Version 1.0-1)
#
# Copyright (C) 2011 Novell, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

Name:         supportutils-plugin-ncs
URL:          https://code.google.com/p/supportutils-plugin-ncs/
License:      GPLv2
Group:        Documentation/SuSE
Autoreqprov:  on
Version:      1.0
Release:      1
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for Novell Cluster Service Volume Resources
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     novell-cluster-services
Requires:     supportutils

%description
Validates NCS volume resource objects and attributes.

Please submit bug fixes or comments via:
    https://code.google.com/p/supportutils-plugin-ncs/issues/list

Authors:
--------
    Jason Record <jrecord@novell.com>

%prep
%setup -q
%build
gzip -9f ncsvr.8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0544 ncsvr $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -m 0644 ncsvr.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/ncsvr.8.gz

%files
%defattr(-,root,root)
/usr/lib/supportconfig
/usr/lib/supportconfig/plugins
/usr/lib/supportconfig/plugins/ncsvr
/usr/share/man/man8/ncsvr.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog -n supportutils-plugin-ncs

