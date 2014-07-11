# revision 32457
# category Package
# catalog-ctan /macros/latex/contrib/vgrid
# catalog-date 2013-12-20 18:52:05 +0100
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-vgrid
Version:	0.1
Release:	3
Summary:	Overlay a grid on the printed page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vgrid
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vgrid.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vgrid.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vgrid.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package overlays a grid (whose spacing is \baselineskip,
which offers guidlines for considering the "rhythm" of the
document on the page.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vgrid/vgrid.sty
%doc %{_texmfdistdir}/doc/latex/vgrid/vgrid.pdf
#- source
%doc %{_texmfdistdir}/source/latex/vgrid/vgrid.dtx
%doc %{_texmfdistdir}/source/latex/vgrid/vgrid.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
