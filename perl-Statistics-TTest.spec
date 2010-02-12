%define upstream_name    Statistics-TTest
%define	upstream_version 1.1.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 7

Summary:	Perl module to perform T-test on 2 independent samples
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Statistics/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Statistics::Descriptive)   >= 2.60.0
BuildRequires:	perl(Statistics::Distributions) >= 0.70.0

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is the Statistical T-Test module to compare 2 independent
samples. It takes 2 array of point measures, compute the confidence
intervals using the PointEstimation module (which is also included in
this package) and use the T-statistic to test the null hypothesis. If
the null hypothesis is rejected, the difference will be given as the
lower_clm and upper_clm of the TTest object. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# perl path hack
find -type f | xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/Statistics/*.pm
%{_mandir}/man3/*
