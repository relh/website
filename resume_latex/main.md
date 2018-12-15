%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Deedy - One Page Two Column Resume
% LaTeX Template
% Version 1.1 (30/4/2014)
%
% Original author:
% Debarghya Das (http://debarghyadas.com)
%
% Original repository:
% https://github.com/deedydas/Deedy-Resume
%
% IMPORTANT: THIS TEMPLATE NEEDS TO BE COMPILED WITH XeLaTeX
%
% This template uses several fonts not included with Windows/Linux by
% default. If you get compilation errors saying a font is missing, find the line
% on which the font is used and either change it to a font included with your
% operating system or comment the line out to use the default font.
% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% TODO:
% 1. Integrate biber/bibtex for article citation under publications.
% 2. Figure out a smoother way for the document to flow onto the next page.
% 3. Add styling information for a "Projects/Hacks" section.
% 4. Add location/address information
% 5. Merge OpenFont and MacFonts as a single sty with options.
% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% CHANGELOG:
% v1.1:
% 1. Fixed several compilation bugs with \renewcommand
% 2. Got Open-source fonts (Windows/Linux support)
% 3. Added Last Updated
% 4. Move Title styling into .sty
% 5. Commented .sty file.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Known Issues:
% 1. Overflows onto second page if any column's contents are more than the
% vertical limit
% 2. Hacky space on the first bullet point on the second column.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\documentclass[]{deedy-resume-openfont}


\begin{document}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%     LAST UPDATED DATE
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\lastupdated

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%     TITLE NAME
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\namesection{Richard}{Higgins}{
\href{mailto:richard@relh.net}{richard@relh.net} | 240.441.9132
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%     COLUMN ONE
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{minipage}[t]{0.33\textwidth} 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     EDUCATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Education} 

\subsection{University Of Michigan}
\descript{Masters in Computer Science}
\location{Expected April 2019 | Ann Arbor, MI}
\sectionsep

\subsection{University of Maryland}
\descript{BS in Computer Science\\}
\descript{BS in Neurobiology and Physiology\\}
\location{Dec 2014 | College Park, MD}
Presidential Scholarship (Merit) \\
Citation in Life Sciences \\
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     COURSEWORK
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Coursework}
\subsection{Graduate}
Reinforcement Learning \\
Self-Driving Cars, Perception + Control \\

Machine Learning \\
Matrix Methods for Signal Processing \\

Advanced Topics in Computer Vision \\
Natural Language Processing \\
\sectionsep

\subsection{Undergraduate}
Artificial Intelligence \\
Evolutionary Computation \\
Bio-Inspired Robotics \\
Mammalian Physiology {\footnotesize (TA)}
\sectionsep

\subsection{Coursera}
Neural Networks for ML \\
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     SKILLS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Skills}
\subsection{Programming}
\textbf{Python} \textbullet{}   \textbf{Java} \textbullet{} \textbf{MATLAB} \\
C \textbullet{} Unix \textbullet{} R \textbullet{} Javascript \textbullet{} C\# \textbullet{} Go \\
\sectionsep

\subsection{Technology}
\textbf{PyTorch} \textbullet{} \textbf{Keras} \textbullet{}  \textbf{AWS} \textbullet{} \textbf{Vim}\\
\textbf{Docker} \textbullet{} \textbf{Git} \textbullet{} \textbf{Flask} \textbullet{} \textbf{Android} \\
Tensorflow \textbullet{} Chainer \textbullet{} Unity \textbullet{} Kubernetes \textbullet{} React \textbullet{} JQuery \\
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     GRES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{GRE} 
\begin{tabular}{rll}
{\custombold{168 (95\%)}}& Quantitative \\
{\custombold{163 (92\%)}}& Verbal\\
{\custombold{4.5 (80\%)}}& Analytical Writing \\
\end{tabular}
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     PROJECTS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{PROJECTS} 

\begin{tabular}{rll}

Github:& \href{https://github.com/relh}{\custombold{github.com/relh}} \\
Devpost:& \href{https://devpost.com/relh}{\custombold{devpost.com/relh}} \\
Kaggle:& \href{https://www.kaggle.com/higgins
}{\custombold{kaggle.com/higgins
}} \\
LinkedIn:&  \href{https://www.linkedin.com/in/relh0
}{\custombold{linkedin.com/in/relh0
}} \\
Website:&  \href{https://www.relh.net/}{\custombold{relh.net}} \\

\end{tabular}
\sectionsep

\section{Fellowships}
NSF Graduate Research Fellowship - Applied - Oct 2018
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%     COLUMN TWO
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\end{minipage} 
\hfill
\begin{minipage}[t]{0.66\textwidth} 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     EXPERIENCE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Experience}
\runsubsection{EECS442: Computer Vision}
\descript{|  Graduate Student Instructor \\}
\location{Dec 2018 – Present | Ann Arbor, MI}
\vspace{\topsep} % Hacky fix for awkward extra vertical space
\begin{tightemize}\item Leading discussions, creating assignments in Python, and hosting office hours for 100+ students at the University of Michigan
\end{tightemize}
\sectionsep

\runsubsection{Voxel 51}
\descript{|  Computer Vision Engineering Intern \\}
\location{Nov 2018 – Present | Ann Arbor, MI}
\begin{tightemize}\item Incorporating various neural network architectures for object detection and image classification into a larger video processing platform
\end{tightemize}
\sectionsep

\runsubsection{Gigster}
\descript{|  Software Engineering Consultant \\}
\location{Aug 2016 – July 2018 | San Francisco, CA \& Remote}
\begin{tightemize}\item Developed a fast style-transfer service on AWS that processes millions of images/day for a social media company
\item Built a Generative Adversarial Network (GAN) service that performs face attribute transformation for a social media company
\item Built a Convolutional Neural Network (CNN) backend to provide object recognition in a launched iOS application for a Fortune 500 company
\item Designed multiple CNN based computer vision systems for Fortune 500 clients with applications including casinos, fashion, and appliances
\end{tightemize}
\sectionsep

\runsubsection{Unscan}
\descript{|  Founder}
\location{|  Aug 2015 – May 2016 | New York, NY}
\begin{tightemize}
\item Built a document processing pipeline on AWS using custom LSTMs for OCR\end{tightemize}
\sectionsep

\runsubsection{Redspread}
\descript{|  First Engineer}
\location{|  Mar 2015 – Aug 2015 | Mountain View, CA}
\begin{tightemize}
\item Developed machine learning tools to automatically scale Kubernetes pods
\item Founding team of a YCombinator company acquired by CoreOS \end{tightemize} 
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     RESEARCH
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Research}
\runsubsection{Vision \& Learning Lab}
\descript{| Researcher\\}
\location{May 2018 – Present | Ann Arbor, MI}
\begin{tightemize}
\item Creating new neural networks for object and relationship detection using associative embeddings, graph networks, and object parts
\end{tightemize}
\sectionsep

\runsubsection{Dept. Computational Medicine}
\descript{| Software Engineer\\}
\location{Aug 2016 – Oct 2016 | Ann Arbor, MI}
\begin{tightemize}
\item Constructed topologically associated domains and analyzed RNA-seq data to identify differential gene expression
\end{tightemize}
\sectionsep

\runsubsection{Neuroscience \& Cognitive Sciences}
\descript{| Researcher\\}
\location{Jan 2014 – Jun 2014 | College Park, MD}
\begin{tightemize}
\item Detected seizures in mouse EEG recordings using clustering and max-margin techniques in MATLAB
\end{tightemize}
\sectionsep

\runsubsection{Evolution of Visual Communication Lab}
\descript{| Researcher\\}
\location{Sep 2011 – Apr 2012 | College Park, MD}
\begin{tightemize}
\item Turned fish images into false-color analogs for different cone opsins in Java
\end{tightemize}
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     PUBLICATIONS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Publications}
\publication{Higgins GA, Georgoff P, Nikolian V, Allyn-Feuer A, \customboldtwo{Higgins R}, et al. Network Reconstruction Reveals that Valproic Acid Activates Neurogenic Transcriptional Programs in Adult Brain Following Traumatic Injury. Pharm Res. 2017;34(8):1658-1672.}
\sectionsep
\publication{Murase S, Lantz CL, Kim E, Gupta N, \customboldtwo{Higgins R}, et al. Matrix Metalloproteinase-9 Regulates Neuronal Circuit Development and Excitability. Mol Neurobiol. 2016;53(5):3477-3493.}
\sectionsep

\end{minipage} 
\end{document}
