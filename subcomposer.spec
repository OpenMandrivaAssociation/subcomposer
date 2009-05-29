Summary:	Subtitle Composer
Name:		subcomposer
Version: 	0.5.3
Release: 	%mkrel 1
Source0: 	http://ovh.dl.sourceforge.net/sourceforge/subcomposer/subtitlecomposer-%version.tar.bz2
Patch0:		subtitlecomposer-0.5.3-fix-linkage.patch
License: 	GPLv2+
Group: 		Video
Url: 		http://subcomposer.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
BuildRequires:	libxine-devel
BuildRequires:	libgstreamer0.10-plugins-base-devel
Provides:	subtitlecomposer = %version

%description 
A text-based subtitles editor supporting the basic operations (text, time,
and style edition) as well as real time preview, spell checking and more;
aiming to become an improved version of Subtitle Workshop for UNIX-like OSes.

%if %mdkversion < 200900
%post
%update_menus
%update_mime_database

%postun
%clean_menus
%clean_mime_database

%endif

%files -f subtitlecomposer.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_configdir/*
%_kde_appsdir/subtitlecomposer
%_kde_iconsdir/*/*/*/*
%_kde_datadir/mime/packages/*.xml

#--------------------------------------------------------------------

%prep
%setup -q -n subtitlecomposer-%version
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang subtitlecomposer

%clean
rm -rf %{buildroot}
