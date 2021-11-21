
.. index:: 
	single: Introduction
	
Introduction
=============

.. code-block::

	display "Hello world!"
	
simple is a post-modern, powerful, general-purpose, efficient, lightweight, multi-paradigm, embeddable programming language 
that make it easy to build efficient projects. 

The language combines various paradigm and syntax to create a powerful constructs. The following paradigms are supported.

* Functional
* Procedural
* Object-Oriented
* Declarative using nested structure
* Imperative
* Meta Programming

simple is dynamically and weakly typed, that compiles the source code to bytecode that is executed by the Simple Virtual Machine 
and has smart generational garbage collector that puts the memory under control which make it a go to for scripting, 
configuration and program extension.

simple recursively stand for **simple intelligent modular programming language and environment**. simple should not capitalized 
and can be referred to as **simple-lang** as alias.


Powerful Construct
-------------------

simple combines various paradigm to create a very powerful language construct. All the paradigms are each of pure implementation 
and behave in expected manner. 

simple is a pure class and prototype base object-oriented language which support all the features of a complete OOP paradigm 
such as encapsulation, composition, inheritance, polymorphism and open recursion. OOP and meta-programming can be combined to 
create a prototype based object.

Functions in simple are first class citizens such that it can behave as a variable, object e.t.c. Functions can be returned 
from a block, pass a function as parameter, create and invoke anonymous, function declaration in list items, check functions 
equality e.t.c.

simple add support for meta-programming which allows inspecting the VM stack, prototyping, semantic extension 
and tuning the program behavior at runtime.

	
Portability
------------

simple is available in small package and execute independently in all the currently supported platforms.

* Windows
* Linux
* Unix
* MacOSX
* Android

simple can be extended to any platform that have a standard C compiler with minimal effort which makes it ideal for 
building cross-platform project that is guaranteed to function exactly the same on the platforms with no code change 
except if system specific function are used. The language can be ported to new platform following this post 
`Porting to New Platform`_ which describe the structure of the core program which is the Compiler and VM. 


Embeddable
------------

simple is a pretty fast embeddable language with memory management that can be embedded easily into any application. 
simple has a simple, straight-forward and well documented `C/C++ API`_ that allows it integration with code written in any other 
languages that support interfacing with Native C. It can also be used to extend program written in simple itself. 
simple can be used to extend program written in C, C++, Java, C# and in other scripting languages such as Perl, Python and Ruby


License
---------

simple is distributed under the very liberal MIT license. Extended dynamic modules such as curl which is part of the 
standard module has their own license which is permissible also and should be included in distribution.
It may be used for any purpose, including commercial purposes, at absolutely no cost

::

	MIT License

	Copyright (c) 2018 simple

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.
	
.. _`Porting to New Platform`: ./
.. _`C/C++ API`: ./
	
.. TODOS
.. link to article for Procedural Programming
.. link to article for garbage collector
.. link to article for Functional Programming
.. link to article for Object-Oriented Programming
.. link to article for Meta Programming
.. documentation on Porting to New Platform
.. documentation on C/C++ API