

       
.. index:: 
	single: simple.util.LookAhead

======================
simple.util.LookAhead
======================


The LookAhead module is ideal for walking through a text base source or string. 
Most of the module in the `parser`_ uses the LookAhead module to implement 
it objects such as the `parser.json.JsonParser`_, `parser.rst.rstParser`_

:copyright: 2018-2019, Azeez Adewale
:license: MIT License Copyright (c) 2018 simple
:author: Azeez Adewale <azeezadewale98@gmail.com>
:date: 11 Febuary 2017
:time: 
:filename: LookAhead.sim


================
Table Of Content
================
====================================== ==============================================================================================================================================================================
 Fields/Blocks/Classes                  Summary                                                                                                                                                                      
====================================== ==============================================================================================================================================================================
 `class LookAhead inherit Object`_                                                                                                                                                                                   
 `int Position`_                            The current position in the object                                                                                                                                       
 `string Value`_                            The value of the object, string on ordinary instance, file descriptor pointer     on file instance                                                                       
 `long Length`_                             The length of the string, the size of the file stream                                                                                                                    
 `block LookAhead(string value)`_           The constructor accept                                                                                                                                                   
 `block peek(number params...)`_            Check the character at the current position in the stream, the peek also accept     an extra number parameter which will be added to the current position before         
 `block pop()`_                             Check the character at the current position in the stream, the peek also accept     an extra number parameter which will be added to the current position before         
 `block position()`_                        Get the current position of the look ahead object in a printable string                                                                                                  
 `block skip(number num)`_                  Move the position **X** forward. The number sent as parameter is used to     advance the position forward. The method ensure that a valid number is                      
 `block equals(object obj)`_                Check if the argument sent is the same as this object. It is false if the obj is     of different instance, if it the same instance as simple.util.LookAhead then the    
 `block toString()`_                        The current object in a printable string                                                                                                                                 
 `private`_                                 All private methods below                                                                                                                                                
 `Line`_                                         The current line in the look ahead object                                                                                                                           
 `Column`_                                       The current column in the look ahead object                                                                                                                         
 `block setLine()`_                              Private setter method for the `Line`_ variable                                                                                                                      
 `block setColumn()`_                            Private setter method for the `Column`_ variable                                                                                                                    
====================================== ==============================================================================================================================================================================


.. index:: 
	pair: LookAhead.sim; class LookAhead inherit Object

===============================
class LookAhead inherit Object
===============================
**Source**: `class LookAhead inherit Object Source`_.
    
    


.. index:: 
	pair: LookAhead.sim; int Position

-------------
int Position
-------------
**Source**: `int Position Source`_.
    
        The current position in the object


.. index:: 
	pair: LookAhead.sim; string Value

-------------
string Value
-------------
**Source**: `string Value Source`_.
    
        The value of the object, string on ordinary instance, file descriptor pointer 
        on file instance


.. index:: 
	pair: LookAhead.sim; long Length

------------
long Length
------------
**Source**: `long Length Source`_.
    
        The length of the string, the size of the file stream


.. index:: 
	pair: LookAhead.sim; block LookAhead(string value)

------------------------------
block LookAhead(string value)
------------------------------
**Source**: `block LookAhead(string value) Source`_.
    
        The constructor accept 


.. index:: 
	pair: LookAhead.sim; block peek(number params...)

-----------------------------
block peek(number params...)
-----------------------------
**Source**: `block peek(number params...) Source`_.
    
        Check the character at the current position in the stream, the peek also accept 
        an extra number parameter which will be added to the current position before 
        peeking, the extra number does not change the current position.
    
        :: 
    
          la = new LookAhead("12345")
          stdout.println(la.peek()) #1
          stdout.println(la.peek(2)) #3
    	
    
        **Parameters**:	
          params : Number
            this method accept one optional parameter which is use to determining how 
            many number forward to peek in the current stream
    	
        **Return**:
          the character at the current position or the optional param forward, return - 1
          if it the end of the stream


.. index:: 
	pair: LookAhead.sim; block pop()

------------
block pop()
------------
**Source**: `block pop() Source`_.
    
        Check the character at the current position in the stream, the peek also accept 
        an extra number parameter which will be added to the current position before 
        peeking, the extra number does not change the current position.
    
        The character is returned and the position advances by 1 
    
        For every pop the `Column`_ increase by one except 
        if the character is a new line which resets `Column`_ to zero and increase the 
        `Line`_ by one.
    
    
        :: 
    
          la = new LookAhead("12345")
          stdout.println(la.pop()) #1
          stdout.println(la.pop()) #2
          stdout.println(la.pop()) #3
          stdout.println(la.pop()) #4
          stdout.println(la.pop()) #5
    	
        **Return**:
          the character at the current position or the optional param forward, return - 1
          if it the end of the stream


.. index:: 
	pair: LookAhead.sim; block position()

-----------------
block position()
-----------------
**Source**: `block position() Source`_.
    
        Get the current position of the look ahead object in a printable string
    
        **Return**:
          the current current `Line`_ and `Column`_ in a printable string


.. index:: 
	pair: LookAhead.sim; block skip(number num)

-----------------------
block skip(number num)
-----------------------
**Source**: `block skip(number num) Source`_.
    
        Move the position **X** forward. The number sent as parameter is used to 
        advance the position forward. The method ensure that a valid number is 
        skipped by using the **min** function from the Math module to keep the 
        number in range.
    
        :: 
    
          la = new LookAhead("12345")
          stdout.println(la.skip(2))  #2
          stdout.println(la.skip(60)) #3 # min(60, Length:5 - Position:2 ) = 3
    	
    
        **Parameters**:	
          num : Number
            the number to skip in the stream
    	
        **Return**:
          the number that is been skipped in the stream


.. index:: 
	pair: LookAhead.sim; block equals(object obj)

-------------------------
block equals(object obj)
-------------------------
**Source**: `block equals(object obj) Source`_.
    
        Check if the argument sent is the same as this object. It is false if the obj is 
        of different instance, if it the same instance as simple.util.LookAhead then the 
        Key fields are compared to check it equality.
    	
    
        **Parameters**:	
          obj : Object
            the object to compare with the current object
    
        **Return**:
          true if the argument object has the same attributes as this object


.. index:: 
	pair: LookAhead.sim; block toString()

-----------------
block toString()
-----------------
**Source**: `block toString() Source`_.
    
        The current object in a printable string 
    
        **Return**:
          the object in a printable string 


.. index:: 
	pair: LookAhead.sim; private

--------
private
--------
**Source**: `private Source`_.
    
        All private methods below


.. index:: 
	pair: LookAhead.sim; Line

-----
Line
-----
**Source**: `Line Source`_.
    
             The current line in the look ahead object


.. index:: 
	pair: LookAhead.sim; Column

-------
Column
-------
**Source**: `Column Source`_.
    
             The current column in the look ahead object


.. index:: 
	pair: LookAhead.sim; block setLine()

----------------
block setLine()
----------------
**Source**: `block setLine() Source`_.
    
             Private setter method for the `Line`_ variable


.. index:: 
	pair: LookAhead.sim; block setColumn()

------------------
block setColumn()
------------------
**Source**: `block setColumn() Source`_.
    
             Private setter method for the `Column`_ variable



-------

.


.. code-block:: 

  call simple.core.Object
  call simple.util.Console
  call simple.util.LookAhead

  forCode = ""
  la = new LookAhead("
   {
    for a = 0 to 100
     display a
    end
   }
  ")

  while la.peek() != -1 {
		
   if la.peek() == '{' {
    la.pop()
			
    while la.peek() != '}' {
     forCode += la.pop()
    }
   }
		
   la.pop() 
  }

  stdout.print(forCode)

  #check all the character until it EOF
  #check if the current character is open brace
  #move ahead by 1 to pass curent '{'
  #append to the forCode variable until a closing brace is met
  #pop the current character so we can advance forward
	
	
.. _parser.json.JsonParser: ../../parser/json/JsonParser.html
.. _parser.rst.rstParser: ../../parser/rst/rstParser.html
.. _parser: ../../parser/index.html


.

.. _class LookAhead inherit Object Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L22
.. _int Position Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L27
.. _string Value Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L33
.. _long Length Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L38
.. _block LookAhead(string value) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L43
.. _block peek(number params...) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L68
.. _block pop() Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L110
.. _block position() Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L130
.. _block skip(number num) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L153
.. _block equals(object obj) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L171
.. _block toString() Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L183
.. _private Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L189
.. _Line Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L194
.. _Column Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L199
.. _block setLine() Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L204
.. _block setColumn() Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/LookAhead.sim#L209

