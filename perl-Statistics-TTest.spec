%define upstream_name    Statistics-TTest
%define	upstream_version 1.1.0

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	11

Summary:	Perl module to perform T-test on 2 independent samples
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Statistics/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Statistics::Descriptive)   >= 2.60.0
BuildRequires:	perl(Statistics::Distributions) >= 0.70.0

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Statistics/*.pm
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-10mdv2012.0
+ Revision: 765655
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-9
+ Revision: 764167
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-8
+ Revision: 676912
- rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.0-7mdv2011.0
+ Revision: 505027
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-6mdv2010.0
+ Revision: 430544
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-5mdv2009.0
+ Revision: 258387
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-4mdv2009.0
+ Revision: 246470
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.1.0-2mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-2mdv2008.0
+ Revision: 86920
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdv2007.0
- rebuild

* Mon Jul 11 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdk
- initial Mandriva package

