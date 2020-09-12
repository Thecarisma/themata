
# libcester

A robust header only unit testing framework for C programming language. Support function mocking, memory leak detection, crash report. 

cester is a header only automated testing framework for the C programming language, it requires no dependency and can be downloaded and used in a project immediately. Works on various platorms including embedded systems and compatible with various compilers. Allows shared instance `TestInstance` object in which each test cases can use to share data and access the command line arguments. 

```c
#include <exotic/cester.h>

CESTER_TEST(test_one, inst,
    cester_assert_equal(NULL, ((void*)0));    
)
```

The test results can be outputed as various format JunitXML, Test Anything Protocol, Test Anything Protocol Version 13 and text. Visit [https://exoticlibraries.github.io/libcester/docs/](https://exoticlibraries.github.io/libcester/docs/) for documentation and tutorials. 
___

## Table of content
- [Standards Compliance and Portability](#standards-compliance-and-portability)
- [Installation](#installation)
    - [Install](#install)
        - [Windows](#windows)
        - [Linux](#linux)
        - [Other platforms](#other-platforms)
- [Documentation](#documentation)
- [Usage](#usage)
    - [Writing and Running test](#writing-test)
    - [Cester options](#cester-options)
    - [Macros](#macros)
- [Mocking](#mocking)
- [FAQ](#faq)
    - [No test case detected](#no-test-case-detected)
- [How it works](#how-it-works)
- [Contributing](#contributing)
- [References](#references)
- [License](#license)

## Standards Compliance and Portability

The project is compliant with the original C language specification ISO/IEC 9899:1990 and the first POSIX specification IEEE Std 1003.1-1988 which ensures the project compatibility in various environments. It also makes use of features in the newer revisions ISO/IEC 9899:1999 and IEEE Std 1003.1-2001 whenever possible. 

Even though the project is designed for C, but also works with C++ as it is compatible with C++98 Standard (ISO/IEC 14882:1998), C++03 Standard (ISO/IEC 14882:2003) and C++11 Standard (ISO/IEC 14882:2011).

The project can be used with any C or C++ compiler. There are optional macros and options that can be used to attain the desired output in the case of undesired results.

## Installation

If you install the library file `cester.h` using any of the commands below, it can be included in your test like `<exotic/cester.h>`.

### Windows

Install the library using powershell. It auto detect your insalled C and C++ compilers include directory and install libcester into the include folder. Execute the command in powershell as admin.
