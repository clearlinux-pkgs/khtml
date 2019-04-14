#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : khtml
Version  : 5.57.0
Release  : 11
URL      : https://download.kde.org/stable/frameworks/5.57/portingAids/khtml-5.57.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.57/portingAids/khtml-5.57.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.57/portingAids/khtml-5.57.0.tar.xz.sig
Summary  : KHTML APIs
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.0 LGPL-2.1
Requires: khtml-data = %{version}-%{release}
Requires: khtml-lib = %{version}-%{release}
Requires: khtml-license = %{version}-%{release}
Requires: khtml-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules gperf
BuildRequires : gperf
BuildRequires : karchive-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kiconthemes-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kjs-dev
BuildRequires : knotifications-dev
BuildRequires : kparts-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwallet-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : kxmlgui-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : openssl-dev
BuildRequires : perl
BuildRequires : phonon-dev
BuildRequires : pkgconfig(libpng)
BuildRequires : qtbase-dev mesa-dev
BuildRequires : solid-dev
BuildRequires : sonnet-dev
BuildRequires : zlib-dev
Patch1: nogif.patch

%description
Wynn Wilkes- November 14, 2000
I've just completed a large update that fixes a large number of bugs.  The
update also adds applet security.  The security update requires a Java 2
jvm.

%package data
Summary: data components for the khtml package.
Group: Data

%description data
data components for the khtml package.


%package dev
Summary: dev components for the khtml package.
Group: Development
Requires: khtml-lib = %{version}-%{release}
Requires: khtml-data = %{version}-%{release}
Provides: khtml-devel = %{version}-%{release}
Requires: khtml = %{version}-%{release}

%description dev
dev components for the khtml package.


%package lib
Summary: lib components for the khtml package.
Group: Libraries
Requires: khtml-data = %{version}-%{release}
Requires: khtml-license = %{version}-%{release}

%description lib
lib components for the khtml package.


%package license
Summary: license components for the khtml package.
Group: Default

%description license
license components for the khtml package.


%package locales
Summary: locales components for the khtml package.
Group: Default

%description locales
locales components for the khtml package.


%prep
%setup -q -n khtml-5.57.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555203142
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555203142
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/khtml
cp COPYING.GPL3 %{buildroot}/usr/share/package-licenses/khtml/COPYING.GPL3
cp COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/khtml/COPYING.LGPL-2
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/khtml/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang khtml5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kf5/khtml/css/html4.css
/usr/share/kf5/khtml/css/presentational.css
/usr/share/kf5/khtml/css/quirks.css
/usr/share/kf5/khtml/error.html
/usr/share/kf5/kjava/kjava.jar
/usr/share/kf5/kjava/kjava.policy
/usr/share/kf5/kjava/pluginsinfo
/usr/share/kservices5/khtml.desktop
/usr/share/kservices5/khtmladaptorpart.desktop
/usr/share/kservices5/khtmlimage.desktop
/usr/share/kservices5/kjavaappletviewer.desktop
/usr/share/kservices5/kmultipart.desktop
/usr/share/xdg/khtml.categories
/usr/share/xdg/khtmlrc

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KHtml/KHTMLPart
/usr/include/KF5/KHtml/KHTMLSettings
/usr/include/KF5/KHtml/KHTMLView
/usr/include/KF5/KHtml/dom/css_rule.h
/usr/include/KF5/KHtml/dom/css_stylesheet.h
/usr/include/KF5/KHtml/dom/css_value.h
/usr/include/KF5/KHtml/dom/dom2_events.h
/usr/include/KF5/KHtml/dom/dom2_range.h
/usr/include/KF5/KHtml/dom/dom2_traversal.h
/usr/include/KF5/KHtml/dom/dom2_views.h
/usr/include/KF5/KHtml/dom/dom_core.h
/usr/include/KF5/KHtml/dom/dom_doc.h
/usr/include/KF5/KHtml/dom/dom_element.h
/usr/include/KF5/KHtml/dom/dom_exception.h
/usr/include/KF5/KHtml/dom/dom_html.h
/usr/include/KF5/KHtml/dom/dom_misc.h
/usr/include/KF5/KHtml/dom/dom_node.h
/usr/include/KF5/KHtml/dom/dom_string.h
/usr/include/KF5/KHtml/dom/dom_text.h
/usr/include/KF5/KHtml/dom/dom_xml.h
/usr/include/KF5/KHtml/dom/html_base.h
/usr/include/KF5/KHtml/dom/html_block.h
/usr/include/KF5/KHtml/dom/html_document.h
/usr/include/KF5/KHtml/dom/html_element.h
/usr/include/KF5/KHtml/dom/html_form.h
/usr/include/KF5/KHtml/dom/html_head.h
/usr/include/KF5/KHtml/dom/html_image.h
/usr/include/KF5/KHtml/dom/html_inline.h
/usr/include/KF5/KHtml/dom/html_list.h
/usr/include/KF5/KHtml/dom/html_misc.h
/usr/include/KF5/KHtml/dom/html_object.h
/usr/include/KF5/KHtml/dom/html_table.h
/usr/include/KF5/KHtml/kencodingdetector.h
/usr/include/KF5/KHtml/khtml_debug.h
/usr/include/KF5/KHtml/khtml_events.h
/usr/include/KF5/KHtml/khtml_export.h
/usr/include/KF5/KHtml/khtml_part.h
/usr/include/KF5/KHtml/khtml_settings.h
/usr/include/KF5/KHtml/khtmldefaults.h
/usr/include/KF5/KHtml/khtmlpart.h
/usr/include/KF5/KHtml/khtmlsettings.h
/usr/include/KF5/KHtml/khtmlview.h
/usr/include/KF5/khtml_version.h
/usr/lib64/cmake/KF5KHtml/KF5KHtmlConfig.cmake
/usr/lib64/cmake/KF5KHtml/KF5KHtmlConfigVersion.cmake
/usr/lib64/cmake/KF5KHtml/KF5KHtmlTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KHtml/KF5KHtmlTargets.cmake
/usr/lib64/libKF5KHtml.so
/usr/lib64/qt5/mkspecs/modules/qt_KHtml.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5KHtml.so.5
/usr/lib64/libKF5KHtml.so.5.57.0
/usr/lib64/qt5/plugins/kf5/parts/khtmladaptorpart.so
/usr/lib64/qt5/plugins/kf5/parts/khtmlimagepart.so
/usr/lib64/qt5/plugins/kf5/parts/khtmlpart.so
/usr/lib64/qt5/plugins/kf5/parts/kjavaappletviewer.so
/usr/lib64/qt5/plugins/kf5/parts/kmultipart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/khtml/COPYING.GPL3
/usr/share/package-licenses/khtml/COPYING.LGPL-2
/usr/share/package-licenses/khtml/COPYING.LIB

%files locales -f khtml5.lang
%defattr(-,root,root,-)

