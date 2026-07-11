%global tl_name vgrid
%global tl_revision 32457

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Overlay a grid on the printed page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vgrid
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vgrid.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vgrid.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vgrid.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package overlays a grid (whose spacing is \baselineskip, which
offers guidlines for considering the "rhythm" of the document on the
page.

