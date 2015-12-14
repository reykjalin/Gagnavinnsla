%% $Header: https://projects.cs.ru.is/svn/template/tvd/techreport/rureport.cls 39 2015-01-19 16:44:54Z foley $
%% Reykjavik University Report Class file
%% Initial version by Joe Foley <foley@RU.IS>
%% Created on 2013-02-04
%% This code is distributed under the Perl Artistic License
%% http://language.per.com/misc/Artistic.html
%% Some code is derived from the template on stackoverfrow by Chris M. Hughes
%% http://tex.stackexchange.com/questions/158638/make-beamer-not-look-like-beamer

%% --------------- Identification ----------------------------
\newcommand{\fileversion@rubeamer}{v0.1}
\newcommand{\filedate@rubeamer}{2015/09/09}
\newcommand{\fileauthor@rubeamer}{Joe Foley, foley@RU.IS}
\ProvidesClass{rubeamer}[\filedate@rubeamer by \fileauthor@rubeamer]
\NeedsTeXFormat{LaTeX2e}
%\typeout{Reykjavik University Beamer Basic template for School of
 % Science and Engineering: \fileversion@rubeamer from <\filedate@rubeamer>, by \fileauthor@rubeamer}

%% ---------------- Initial Code -----------------------------
%% Critical packages are here that everything else depends upon
\RequirePackage{ifthen}
% This package allows you to create conditionals on booleans
\RequirePackage{ifdraft}
\newboolean{svn}

% Better handling of arguments, particularly for defaults
\RequirePackage{xargs}

%% ---------------- Declaration of Options--------------------
%% Remember that we have \AtEndOfClass{},\AtEndOfPackage{}
%%     \AtBeginDocument{}, \AtEndDocument{}
%% If you want execution conditional on file existence
%%     \IfFileExists{filename}{true}{false}
%%     \InputIfFileExists{filename}{true}{false}
%% For error beamering
%%     \ClassError{class-name}{error-text}{help-text}
%%     \PackageError{class-name}{error-text}{help-text}
%\DeclareOption{rulogotitle}{
% % TODO: finish this.  RU logo on the title page
% 
% }
%% otherwise, just a generic title page


%% When loading packages, use the \PassOptionsToPackage{option}{package}
%% This way if a package is loaded with options somewhere else, you don't get a clash

\DeclareOption{svn}{
  \setboolean{svn}{true}
}

\DeclareOption{isbabel}{ % set Icelandic labels on figures, tables, etc.
  \AtEndOfClass{
    \RequirePackage[icelandic]{babel}
  }
}

%% suggested options to beamer:  handout, mathserif

%% now we pass the remaining unused options to our parent class
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{beamer}}
%% ---------------- Execution of Options -----------------------------
\ProcessOptions \relax % this stops searching for a * in
                       % \ProcessOtions*

%% Alternative way to subclass.  Disable the other option processing
%% if you enable it.  This will dump all options onto the parent class
%\ProcessOptions\LoadClassWithOptions{article}
%% ---------------- Package Loading -----------------------------
\LoadClass{beamer}  % our parent class.  Article is a little easier
                     % to work with than the beamer class.
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}  % allows UTF encoding, needed for Icelandic characters
%\RequirePackage[margin=2cm,a4paper]{geometry}
%% Some slighly more sensible margins on an A4 page
%% This can be tuned for your given beamer

% Some useful fonts, particularly for listings
\RequirePackage{lipsum}
\RequirePackage{courier}

\ifthenelse{\boolean{svn}}{
        % switching to the svn-multi package which is much smarter
  %\RequirePackage[today,fancyhdr]{svninfo} 
  % grab the SVN revision information from a \svninfo $Id: rubeamer.cls 39 2015-01-19 16:44:54Z foley $
  %% today option sets the current day to the latest SVN date
  %% Remember that you will need to put a \svninfo and \svnKeyword
  %% into your document or it will only grab the revision information
  %% of the class file!  Also, you will need to set the svn:keywords properties.
  %\svnInfo $Id: rubeamer.cls 39 2015-01-19 16:44:54Z foley $
  %\svnKeyword $HeadURL: https://projects.cs.ru.is/svn/template/tvd/techbeamer/rubeamer.cls $
  \RequirePackage{svn-multi}
}{ % If svninfo not installed, we load it invisibly to avoid problems
  %\RequirePackage[notoday,nofancy,final]{svninfo} 
    \RequirePackage{svn-multi}
}

\RequirePackage{fancyhdr}
%% Nice options for tweaking the header and footer

\PassOptionsToPackage{final}{graphicx}
\RequirePackage{graphicx}
%% We give the "final" option so that it always includes graphics
%% Take out this option if you want draft mode to skip pics

\DeclareGraphicsExtensions{.pdf,.jpeg,.jpg,.png,.gif,.PDF,.JPEG,.JPG,.PNG,.GIF}
%% The extensions that it will search for as valid graphics files
%% We need To include the UPPERCASE versions For windows people

\graphicspath{{graphics/}{Graphics/}{./}}
%% This is a list of folders to search for graphics files to include
%% Each path should be in a {}.  
%% Make sure that the upper/lowercase of the letters matches the folder or
%% you may have weird problems with partners using other operating systems.
%% Note that you don't have to put the folder where the .tex file is, it is
%% included automatically, though it is bad practice to put your 
%% graphics there
\PassOptionsToPackage{final}{pdfpages}
\RequirePackage{pdfpages}
%% The "pdfpages" package lets you include PDF documents into your
%% document but keeps the formatting consistent (headers, footers,
%% etc.)

%\RequirePackage{lastpage}
% The "lastpage" package allows you to set a command that knows
% what the last page was e.g. page 1 of 4

%% declare the paths(s) where you graphics files can be found
%% This allows you to skip putting the full path in
%% If you put a // at the end, it will recursively search for graphics
%% files, but be careful!
\RequirePackage{pseudocode}


\RequirePackage{url}
%% The url package typesets url's and unix file paths nicely when they
%% become long.  Warning: windows paths such as C:\window do not work!
%% You need another verbatime to make those typeset properly.

\RequirePackage{xspace}
%% The xspace package will try to figure out if you meant to have a
%% space after a new command if you don't give it any arguments (in
%% braces: {} ).  

%% Color is already included in the beemer class
%\RequirePackage{color}
\definecolor{rugray}{rgb}{0.2,0.2,0.2}
\definecolor{rured}{rgb}{0.84,0.10,0.13}
%% The "color" package allows us to set the color of text and other
%% objects in a document

%% Creates macros to adjust the line spacing more easily
%\onehalfspacing
%% By default, set to 1.5 spacing
%\linespread{1.3}  % this method does not require the setspace package

% % some font package possibilities
% % From http://www.macfreek.nl/memory/Fonts_in_LaTeX
%\RequirePackage{lmodern}
%\RequirePackage{times}
%\RequirePackage{palatino}
%\RequirePackage{bookman}
%\RequirePackage{newcent}
\RequirePackage{helvet}

% The old template uses san-serif, let's also do so 
\renewcommand{\familydefault}{\sfdefault}

%% ---------------- Main Code -----------------------------
%%  Remember that we can declar commands (to make fragile things safe)
%%  The * form is for ``short'' commands, not longer than a paragraph
%%       \DeclareRobustCommand{cmd}[num][default]{definition}
%%       \DeclareRobustCommand*{cmd}[num][default]{definition}
%%  For checking if commands are redefined
%%       \CheckCommand{cmd}[num][default]{definition}

% this is for the picture environment
\setlength{\unitlength}{1cm}

\RequirePackage{amsfonts}
\RequirePackage{siunitx}  % replacement for SIunits, less problems
%% AMS is American Mathematics Society.  They have a bunch of nice
%% math fonts and symbols

\RequirePackage{examplep} % another verbatim environment
\RequirePackage[final]{listings} % force final or included files are skipped, invisibly!
% This allows you to include code easily
% \begin{lstlisting}[language=bash]
%  $ wget http://blah
% \end{lstlisting}
% or for simpler snippets
%  \lstinline^cp -rp foo bar^
%  You can replace ^ with any character not in your code
\lstset{%
        language=, %default similar to verbatim
  basicstyle=\footnotesize\ttfamily,%
  frame=lines,%
  breaklines=true,%
  postbreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\color{red}\hookrightarrow\space}}, % red arrow
  % from http://tex.stackexchange.com/questions/116534/lstlisting-line-wrapping
}
% Here are listings macros I use a lot
\newcommand{\fpath}{\lstinline}  % magic, do not try to give it arguments
\newcommand{\shcmd}{\lstinline}  
% ex:  \fpath{\\AFS\.rnd.ru.is\course\T-411-MECH}

\RequirePackage{subfig}
%% Nice package for making sub figures inside of a figure.  Keeps all
%% the reference labels correct and makes "sub captions"
% % WARNING: this is completely different than the subfigure package


\RequirePackage[layout=inline]{fixme}
% FIXME system for making notes to each other for what needs to 
% be completed in a group document.

% internal layouts: inline, margin, footnote, index, marginclue
% % Warning! The pdf external layouts do not play well with hyperref
% % and must be loaded by doing \fxuselayouts{}
% external layouts: marginnote, pdfnote, pdfmargin, pdfsignote, pdfsigmargin
%     pdfcnote, pdfcmargin, pdfcsignote, pdfcsigmargin
%  pdfc stands for pdf color
%\fxuselayouts{pdfcmargin}

%\AtBeginDocument{
% \RequirePackage[final]{hyperref}
%% Hyper references (clickable links) in the document.  Very nice, but
%% MUST be the last package loaded.  If you are in draft mode, it will
%% disable itself, so we force it to be in final mode.
%}


%% for doing presentations, tikz is really nice for making graphics
\RequirePackage{pgfplots}
\usetikzlibrary{positioning}
\usetikzlibrary{fit}
\usetikzlibrary{backgrounds}
\usetikzlibrary{calc}
\usetikzlibrary{shapes}
\usetikzlibrary{mindmap}
\usetikzlibrary{decorations.text}
\pgfplotsset{compat=1.7}

% tikzmark command, for shading over items
\newcommand{\tikzmark}[1]{\tikz[overlay,remember picture] \node (#1) {};}

%% ----- Setup page layout, including title page ----- %%
\usetheme{Boadilla}
\usecolortheme{seagull}

% standard enumeration
\setbeamertemplate{enumerate items}{(\arabic{enumi})}

% default itemize
\setbeamertemplate{itemize items}[circle]

% transparency
\setbeamercovered{transparent=15}

% for resuming lists across frames
\newcounter{savedenum}
\newcommand*{\saveenum}{\setcounter{savedenum}{\theenumi}}
\newcommand*{\resume}{\setcounter{enumi}{\thesavedenum}}

\setbeamertemplate{caption}[numbered]

% if you don't set this, then the numbers don't show up in the References
% when using beamer
\setbeamertemplate{bibliography item}[text]
%% suggestions from http://tex.stackexchange.com/questions/97615/article-style-bibliography-in-beamer-class
% If bibliography goes over one page
\setbeamertemplate{frametitle continuation}[from second]
% Set all bib colors to black
\setbeamercolor*{bibliography entry title}{fg=black}
\setbeamercolor*{bibliography entry author}{fg=black}
\setbeamercolor*{bibliography entry location}{fg=black}
\setbeamercolor*{bibliography entry note}{fg=black}
% and kill the abominable icon
%\setbeamertemplate{bibliography item}{}


% helpful for math typsetting
% http://www.math.uiuc.edu/~hildebr/tex/displays.html

% This magic allows you to use captions and crossreferences
% http://tex.stackexchange.com/questions/56136/image-caption-and-cross-referenceing-in-beamer-poster
\newenvironment<>{varblock}[2][\textwidth]{%
  \setlength{\textwidth}{#1}
  \begin{actionenv}#3%
    \def\insertblocktitle{ \centering#2\par}%
    \par%
    \usebeamertemplate{block begin}}
  {\par%
    \usebeamertemplate{block end}%
  \end{actionenv}}
\newcommand{\sqsi}[1]{[\si{#1}]}


%% Reykjavik University customizations
\RequirePackage{transparent}

\setbeamercolor*{palette secondary}{use=structure,fg=white,bg=red}

\newcommand{\titlegraphicframe}[1]{
  {\usebackgroundtemplate{
      \parbox[c][\paperheight][c]{\paperwidth}{
        \centering\transparent{0.35}\includegraphics[height=0.9\paperheight]{#1}}
    }
    % Watch out, sometimes transparent doesn't work
    \begin{frame}[plain]
      \titlepage{}
    \end{frame}
  }
}
\newcommand{\rutitleframe}{\titlegraphicframe{ru-logo}}

% use biblatex and biber for easy Icelandic characters
%\usepackage[backend=biber, bibencoding=utf8, style=ieee]{biblatex}

%% APA style -- need all of these lines
%\usepackage[backend=biber, bibencoding=utf8, style=apa]{biblatex}
%\usepackage[american]{babel}
%\DeclareLanguageMapping{american}{american-apa}  % after biblatex and babel

%% Alphabetic, more compact
\usepackage[backend=biber, bibencoding=utf8, style=alphabetic]{biblatex}

% % This will load custom.tex with your custom macros and definitions if it exists
\IfFileExists{custom.tex}{\input{custom.tex}}{}

%% ----- Useful macros --- %%
