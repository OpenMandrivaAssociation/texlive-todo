Name:		texlive-todo
Version:	17746
Release:	2
Summary:	Make a to-do list for a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/todo
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todo.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows you to insert "to do" marks in your
document, to make lists of such items, and to cross-reference
to them.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/todo/todo.sty
%doc %{_texmfdistdir}/doc/latex/todo/README
%doc %{_texmfdistdir}/doc/latex/todo/todo-spl.pdf
%doc %{_texmfdistdir}/doc/latex/todo/todo-spl.tex
%doc %{_texmfdistdir}/doc/latex/todo/todo.pdf
#- source
%doc %{_texmfdistdir}/source/latex/todo/todo.dtx
%doc %{_texmfdistdir}/source/latex/todo/todo.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
