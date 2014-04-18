%define  upstream_name PHP_CodeCoverage

Summary:	Library that provides collection, processing, and rendering functionality
Name:		php-pear-%{upstream_name}
Version:	1.2.13
Release:	1
License:	BSD
Group:		Development/PHP
URL:		http://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/PHP_CodeCoverage-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear >= 1:1.9.4
Requires:	php-channel-phpunit
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
Suggests:	php-pear-PHPUnit >= 3.6.3
Suggests:	php-pear-File_Iterator >= 1.3.0
Suggests:	php-pear-PHP_TokenStream >= 1.1.0
Suggests:	php-pear-Text_Template >= 1.1.1
Suggests:	php-dom
Suggests:	php-xdebug >= 2.0.5

%description
PHPUnit is a regression testing framework used by the developer who implements
unit tests in PHP.

This package provides a Library that provides collection, processing, and
rendering functionality for PHP code coverage information for PHPUnit.

%prep

%setup -q -c 
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/LICENSE
%{_datadir}/pear/PHP/CodeCoverage
%{_datadir}/pear/PHP/*.php
%{_datadir}/pear/packages/PHP_CodeCoverage.xml
