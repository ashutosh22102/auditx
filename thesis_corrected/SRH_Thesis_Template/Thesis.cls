%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Thesis LaTeX Template - THESIS CLASS FILE
%
% This template has been downloaded from:
% http://www.latextemplates.com
%
% This class file defines the structure and design of the template.
%
% Adapted to the SRH Hochschule Heidelberg "Guidelines for Academic Writing,
% Scientific Papers & Theses" (February 2022):
%   - DIN A4, single-sided, 2.5 cm margins on all sides       (Guidelines 4.1.4)
%   - Arial 12 pt, justified with hyphenation, 1.5 spacing    (Guidelines 4.1.4)
%   - Headings 14 pt bold / 12 pt bold / 12 pt / 12 pt italic (Guidelines 4.1.5)
%   - Roman page numbers before chapter 1 and again from the
%     bibliography onwards, Arabic in the main text           (Guidelines 4.1.4)
%   - Title page contents as required                         (Guidelines 4.1.2)
%
% The thesis details (title, author, supervisor, ...) are set in main.tex.
%
% Original header:
%% This is file `Thesis.cls', based on 'ECSthesis.cls', by Steve R. Gunn
%% generated with the docstrip utility.
%%
%% Created by Steve R. Gunn, modified by Sunil Patel: www.sunilpatel.co.uk
%% Further modified by www.latextemplates.com
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\NeedsTeXFormat{LaTeX2e}[1996/12/01]
\ProvidesClass{Thesis}
              [2026/10/22 v2.0 SRH thesis class]
\def\baseclass{book}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{\baseclass}}
\def\@checkoptions#1#2{
  \edef\@curroptions{\@ptionlist{\@currname.\@currext}}
  \@tempswafalse
  \@tfor\@this:=#2\do{
    \@expandtwoargs\in@{,\@this,}{,\@curroptions,}
    \ifin@ \@tempswatrue \@break@tfor \fi}
  \let\@this\@empty
  \if@tempswa \else \PassOptionsToClass{#1}{\baseclass}\fi
}
\@checkoptions{12pt}{{10pt}{11pt}{12pt}} % SRH: 12 pt text
\PassOptionsToClass{a4paper,oneside}{\baseclass} % SRH: DIN A4, single-sided
\ProcessOptions\relax
\LoadClass{\baseclass}
\newcommand\bhrule{\typeout{------------------------------------------------------------------------------}}
\newcommand\btypeout[1]{\bhrule\typeout{\space #1}\bhrule}

%----------------------------------------------------------------------------------------
%	FONT AND LANGUAGE (SRH: Arial)
%----------------------------------------------------------------------------------------
\RequirePackage{iftex}
\ifPDFTeX
  % pdfLaTeX cannot load Arial itself; Helvetica has the same letter widths,
  % so the text looks and runs the same. Compile with XeLaTeX or LuaLaTeX
  % to get Arial itself.
  \RequirePackage[T1]{fontenc}
  \RequirePackage[utf8]{inputenc} % Allows the use of international characters (e.g. Umlauts)
  \RequirePackage{helvet}
  \renewcommand{\familydefault}{\sfdefault}
\else
  \RequirePackage{fontspec}
  \IfFontExistsTF{Arial}
    {\setmainfont{Arial}\setsansfont{Arial}}
    {\setmainfont{TeX Gyre Heros}\setsansfont{TeX Gyre Heros}}
  \renewcommand{\familydefault}{\sfdefault}
\fi
\RequirePackage[english]{babel} % Hyphenation; text is justified by default

%----------------------------------------------------------------------------------------
%	SPACING (SRH: 1.5 lines)
%----------------------------------------------------------------------------------------
\usepackage{setspace}
\onehalfspacing
\setlength{\parindent}{0pt}
\setlength{\parskip}{2.0ex plus0.5ex minus0.2ex}

%----------------------------------------------------------------------------------------
%	MARGINS (SRH: 2.5 cm right, left, top and bottom)
%----------------------------------------------------------------------------------------
\RequirePackage[a4paper,margin=2.5cm,headheight=15pt,headsep=0.6cm]{geometry}
%----------------------------------------------------------------------------------------
\raggedbottom
\setlength{\topskip}{1\topskip \@plus 5\p@}
\doublehyphendemerits=10000       % No consecutive line hyphens.
\brokenpenalty=10000              % No broken words across columns/pages.
\widowpenalty=9999                % Almost no widows at bottom of page.
\clubpenalty=9999                 % Almost no orphans at top of page.
\interfootnotelinepenalty=9999    % Almost never break footnotes.

%----------------------------------------------------------------------------------------
%	HEADINGS (SRH: 14 pt bold / 12 pt bold / 12 pt normal / 12 pt italic,
%	all numbered, no full stop after the last number)
%----------------------------------------------------------------------------------------
\usepackage{titlesec}
\titleformat{\chapter}[hang]
    {\fontsize{14}{17}\selectfont\bfseries}{\thechapter}{1em}{}
\titlespacing*{\chapter}{0pt}{0pt}{12pt}

\titleformat{\section}[hang]
    {\normalsize\bfseries}{\thesection}{1em}{}
\titlespacing*{\section}{0pt}{12pt}{0pt}

\titleformat{\subsection}[hang]
    {\normalsize\mdseries}{\thesubsection}{1em}{}
\titlespacing*{\subsection}{0pt}{6pt}{0pt}

\titleformat{\subsubsection}[hang]
    {\normalsize\itshape}{\thesubsubsection}{1em}{}
\titlespacing*{\subsubsection}{0pt}{6pt}{0pt}

\setcounter{secnumdepth}{3} % Number every heading down to the fourth level
\setcounter{tocdepth}{3}    % SRH: at most 3 to 4 heading levels

%----------------------------------------------------------------------------------------
%	PAGE HEADERS (SRH: page number in the right corner)
%----------------------------------------------------------------------------------------
\usepackage{fancyhdr}
\fancyhf{}
\fancyhead[L]{\nouppercase{\leftmark}}
\fancyhead[R]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
\pagestyle{fancy}
% Chapter opening pages: page number only, top right
\fancypagestyle{plain}{\fancyhf{}\fancyhead[R]{\thepage}\renewcommand{\headrulewidth}{0pt}}
\renewcommand{\chaptermark}[1]{\btypeout{\thechapter\space #1}\markboth{\thechapter\ #1}{\thechapter\ #1}}
\renewcommand{\sectionmark}[1]{}
\renewcommand{\subsectionmark}[1]{}
\def\cleardoublepage{\clearpage}

\usepackage{amsmath,amsfonts,amssymb,amscd,amsthm,xspace}
\theoremstyle{plain}
\newtheorem{example}{Example}[chapter]
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{axiom}[theorem]{Axiom}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\usepackage[font=small,labelfont=bf,margin=20pt]{caption}
\newcommand{\fref}[1]{Figure~\ref{#1}}
\newcommand{\tref}[1]{Table~\ref{#1}}
\newcommand{\eref}[1]{Equation~\ref{#1}}
\newcommand{\cref}[1]{Chapter~\ref{#1}}
\newcommand{\sref}[1]{Section~\ref{#1}}
\newcommand{\aref}[1]{Appendix~\ref{#1}}
\renewcommand{\topfraction}{0.85}
\renewcommand{\bottomfraction}{.85}
\renewcommand{\textfraction}{0.1}
\renewcommand{\dbltopfraction}{.85}
\renewcommand{\floatpagefraction}{0.75}
\renewcommand{\dblfloatpagefraction}{.75}
\setcounter{topnumber}{9}
\setcounter{bottomnumber}{9}
\setcounter{totalnumber}{20}
\setcounter{dbltopnumber}{9}
\usepackage{graphicx}
\usepackage{epstopdf}
\usepackage{booktabs}
\usepackage{rotating}
\usepackage{listings}
\usepackage{lstpatch}
\lstset{captionpos=b,
        frame=tb,
        basicstyle=\scriptsize\ttfamily,
        showstringspaces=false,
        keepspaces=true}
\lstdefinestyle{matlab} {
        language=Matlab,
        keywordstyle=\color{blue},
        commentstyle=\color[rgb]{0.13,0.55,0.13}\em,
        stringstyle=\color[rgb]{0.7,0,0} }
\usepackage[pdfpagemode={UseOutlines},bookmarks=true,bookmarksopen=true,
   bookmarksopenlevel=0,bookmarksnumbered=true,hypertexnames=false,
   colorlinks,linkcolor={blue},citecolor={blue},urlcolor={red},
   pdfstartview={FitV},unicode,breaklinks=true]{hyperref}
\pdfstringdefDisableCommands{
   \let\\\space
}

%----------------------------------------------------------------------------------------
%	DOCUMENT VARIABLES
%	Set these in main.tex, not here
%----------------------------------------------------------------------------------------
\newcommand*{\thesistitle}[1]{\def\ttitle{#1}}
\newcommand*{\authors}[1]{\def\authornames{#1}}
\newcommand*{\matriculation}[1]{\def\matrnumber{#1}}
\newcommand*{\authoremail}[1]{\def\emailaddress{#1}}
\newcommand*{\supervisor}[1]{\def\supname{#1}}
\newcommand*{\examiner}[1]{\def\examname{#1}}
\newcommand*{\degree}[1]{\def\degreename{#1}}
\newcommand*{\university}[1]{\def\univname{#1}}
\newcommand*{\department}[1]{\def\deptname{#1}}
\newcommand*{\submissiondate}[1]{\def\subdate{#1}}
\newcommand*{\subject}[1]{\def\subjectname{#1}}
\newcommand*{\keywords}[1]{\def\keywordnames{#1}}

\thesistitle{Thesis Title}
\authors{Author Name}
\matriculation{}
\authoremail{}
\supervisor{Supervisor Name}
\examiner{}
\degree{Degree Name}
\university{SRH University of Applied Sciences Heidelberg}
\department{Department Name}
\submissiondate{\today}
\subject{}
\keywords{}

%----------------------------------------------------------------------------------------
%	TITLE PAGE (SRH 4.1.2: logo, degree and institution in the upper third;
%	title at the lower end of the top third; supervisor, author contact
%	details, matriculation number and submission date in the bottom half)
%----------------------------------------------------------------------------------------
\renewcommand\maketitle{
  \btypeout{Title Page}
  \begin{titlepage}
    \setlength{\parskip}{0pt}
    \centering
    \includegraphics[width=5cm]{SRH_Logo.png}\par
    \vspace{1cm}
    {\large \univname \par}
    \ifx\deptname\@empty\else{\large \deptname \par}\fi
    \vspace{0.8cm}
    {\large Master's Thesis \par}
    {\large submitted for the degree of \degreename \par}
    \vspace{1.2cm}
    \rule{\linewidth}{0.5mm}\par
    \vspace{0.4cm}
    {\fontsize{18}{24}\selectfont\bfseries \ttitle \par}
    \vspace{0.4cm}
    \rule{\linewidth}{0.5mm}\par
    \vfill
    % Optional rows are only printed when the variable is filled in
    \def\@srh@emailrow{}\ifx\emailaddress\@empty\else\def\@srh@emailrow{E-mail: & \emailaddress \\}\fi
    \def\@srh@examrow{}\ifx\examname\@empty\else\def\@srh@examrow{Second examiner: & \examname \\}\fi
    {\large
    \begin{tabular}{@{}ll@{}}
      Author: & \authornames \\
      Matriculation number: & \matrnumber \\
      \@srh@emailrow
      Supervisor: & \supname \\
      \@srh@examrow
      Date of submission: & \subdate \\
    \end{tabular}\par}
    \vspace{1cm}
  \end{titlepage}
}

%----------------------------------------------------------------------------------------
%	FRONT MATTER PAGES (unnumbered headings, listed in the contents,
%	Roman page numbers)
%----------------------------------------------------------------------------------------
\newcounter{dummy}
\newcommand\addtotoc[1]{
\refstepcounter{dummy}
\addcontentsline{toc}{chapter}{#1}}

\newenvironment{abstract}
{
  \btypeout{Abstract Page}
  \chapter*{Abstract}
  \addtotoc{Abstract}
  \markboth{Abstract}{Abstract}
}
{
  \clearpage
}

\newcommand\acknowledgements[1]{
\btypeout{Acknowledgements}
\chapter*{Acknowledgements}
\addtotoc{Acknowledgements}
\markboth{Acknowledgements}{Acknowledgements}
{\normalsize #1}
\clearpage
}

\renewcommand\tableofcontents{
\btypeout{Table of Contents}
\begin{spacing}{1.055}{
    \setlength{\parskip}{0.5pt}
    \chapter*{\contentsname
        \@mkboth{\contentsname}{\contentsname}}
    \@starttoc{toc}
   \clearpage
}\end{spacing}
}
\renewcommand\listoffigures{
\btypeout{List of Figures}
\addtotoc{List of Figures}
\begin{spacing}{1}{
    \setlength{\parskip}{1pt}
    \chapter*{\listfigurename
      \@mkboth{\listfigurename}{\listfigurename}}
    \@starttoc{lof}
    \clearpage
}\end{spacing}
}
\renewcommand\listoftables{
\btypeout{List of Tables}
\addtotoc{List of Tables}
\begin{spacing}{1}{
    \setlength{\parskip}{1pt}
    \chapter*{\listtablename
      \@mkboth{\listtablename}{\listtablename}}
    \@starttoc{lot}
    \clearpage
}\end{spacing}
}
\newcommand\listsymbolname{List of Abbreviations}
\usepackage{longtable}
\newcommand\listofsymbols[2]{
\btypeout{\listsymbolname}
\addtotoc{\listsymbolname}
    \chapter*{\listsymbolname
      \@mkboth{\listsymbolname}{\listsymbolname}}
\begin{longtable}[l]{#1}#2\end{longtable}\par
    \clearpage
}
\newcommand\dedicatory[1]{
\btypeout{Dedicatory}
\thispagestyle{plain}
\null\vfil
\vskip 60\p@
\begin{center}{\Large \sl #1}\end{center}
\vfil\null
\clearpage
}

%----------------------------------------------------------------------------------------
%	PAGE NUMBERING (SRH 4.1.4: Roman numerals up to the main text, Arabic
%	from chapter 1, Roman numerals again from the bibliography onwards)
%----------------------------------------------------------------------------------------
\newcounter{lastromanpage}
\let\@srh@mainmatter\mainmatter
\renewcommand\mainmatter{
  \clearpage
  \setcounter{lastromanpage}{\value{page}}
  \@srh@mainmatter}
\renewcommand\backmatter{
  \clearpage
  \pagenumbering{roman}
  \setcounter{page}{\value{lastromanpage}}
  \@mainmatterfalse}

% Appendices come after the bibliography, keep Roman page numbers and are
% lettered (Appendix A, B, ...)
\newcommand\startappendices{
  \clearpage
  \@mainmattertrue
  \appendix
  \titleformat{\chapter}[hang]
    {\fontsize{14}{17}\selectfont\bfseries}{\appendixname\ \thechapter}{1em}{}
  \renewcommand{\chaptermark}[1]{\markboth{\appendixname\ \thechapter\ ##1}{\appendixname\ \thechapter\ ##1}}}

%----------------------------------------------------------------------------------------
%	DECLARATION OF HONOR (SRH 4.1.1: at the very end, not in the contents)
%----------------------------------------------------------------------------------------
\newcommand\Declaration[1]{
\btypeout{Declaration of Honor}
\clearpage
\chapter*{Declaration of Honor}
\markboth{Declaration of Honor}{Declaration of Honor}
{\normalsize #1}
}
\endinput
