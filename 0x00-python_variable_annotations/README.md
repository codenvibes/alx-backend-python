<h1 align="center"><b>0X00. PYTHON - VARIABLE ANNOTATIONS</b></h1>
<div align="center"><code>Python</code> <code>Back-end</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Resources
<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/5j0OtdWh36_HVAHKJX2gaA">Python 3 typing documentation</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/Eud-nrUG7x3iT6JD2Sas-g">MyPy cheat sheet</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!--==================================================-->
<br>

## Learning Objectives
<h3>General</h3>


<br>
<details>
<summary><b><a href=" "> </a>Type annotations in Python 3</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How you can use type annotations to specify function signatures and variable types</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>Duck typing</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to validate your code with <code>mypy</code></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

<!--==================================================-->
<br>

## Requirements
<h3>General</h3>

- Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly <code>#!/usr/bin/env python3</code>
- A <code>README.md</code> file, at the root of the folder of the project, is mandatory
- Your code should use the <code>pycodestyle</code> style (version 2.5.)
- All your files must be executable
- The length of your files will be tested using <code>wc</code>
- All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)
- All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)
- All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. Basic annotations - add
`mandatory`

File: [0-add.py]()
</summary>

<p>Write a type-annotated function <code>add</code> that takes a float <code>a</code> and a float <code>b</code> as arguments and returns their sum as a float. </p>

<pre><code>bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./0-main.py
True
{'a':  &lt;class 'float'&gt;, 'b': &lt;class 'float'&gt;, 'return': &lt;class 'float'&gt;}
</code></pre>


</details>

<details>
<summary>

### 1. Basic annotations - concat
`mandatory`

File: [1-concat.py]()
</summary>

<p>Write a type-annotated function <code>concat</code> that takes a string <code>str1</code> and a string <code>str2</code> as arguments and returns a concatenated string</p>

<pre><code>bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)

bob@dylan:~$ ./1-main.py
True
{'str1': &lt;class 'str'&gt;, 'str2': &lt;class 'str'&gt;, 'return': &lt;class 'str'&gt;}
</code></pre>


</details>

<details>
<summary>

### 2. Basic annotations - floor
`mandatory`

File: [2-floor.py]()
</summary>

<p>Write a type-annotated function <code>floor</code> which takes a float <code>n</code> as argument and returns the floor of the float.</p>

<pre><code>bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import math

floor = __import__('2-floor').floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))

bob@dylan:~$ ./2-main.py
True
{'n': &lt;class 'float'&gt;, 'return': &lt;class 'int'&gt;}
floor(3.14) returns 3, which is a &lt;class 'int'&gt;
</code></pre>


</details>

<details>
<summary>

### 3. Basic annotations - to string
`mandatory`

File: [3-to_str.py]()
</summary>

<p>Write a type-annotated function <code>to_str</code> that takes a float <code>n</code> as argument and returns the string representation of the float.</p>

<pre><code>bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
to_str = __import__('3-to_str').to_str

pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))

bob@dylan:~$ ./3-main.py
True
{'n': &lt;class 'float'&gt;, 'return': &lt;class 'str'&gt;}
to_str(3.14) returns 3.14, which is a &lt;class 'str'&gt;
</code></pre>


</details>

<details>
<summary>

### 4. Define variables
`mandatory`

File: [4-define_variables.py]()
</summary>

<p>Define and annotate the following variables with the specified values:</p>

<ul>
<li><code>a</code>, an integer with a value of 1</li>
<li><code>pi</code>, a float with a value of 3.14</li>
<li><code>i_understand_annotations</code>, a boolean with a value of True</li>
<li><code>school</code>, a string with a value of “Holberton”</li>
</ul>

<pre><code>bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

a = __import__('4-define_variables').a
pi = __import__('4-define_variables').pi
i_understand_annotations = __import__('4-define_variables').i_understand_annotations
school = __import__('4-define_variables').school

print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))

bob@dylan:~$ ./4-main.py
a is a &lt;class 'int'&gt; with a value of 1
pi is a &lt;class 'float'&gt; with a value of 3.14
i_understand_annotations is a &lt;class 'bool'&gt; with a value of True
school is a &lt;class 'str'&gt; with a value of Holberton
</code></pre>


</details>

<details>
<summary>

### 5. Complex types - list of floats
`mandatory`

File: [5-sum_list.py]()
</summary>

<p>Write a type-annotated function <code>sum_list</code> which takes a list <code>input_list</code> of floats as argument and returns their sum as a float.</p>

<pre><code>bob@dylan:~$ cat 5-main.py
#!/usr/bin/env python3

sum_list = __import__('5-sum_list').sum_list

floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum == sum(floats))
print(sum_list.__annotations__)
print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))

bob@dylan:~$ ./5-main.py
True
{'input_list': typing.List[float], 'return': &lt;class 'float'&gt;}
sum_list(floats) returns 6.470000000000001 which is a &lt;class 'float'&gt;
</code></pre>


</details>

<details>
<summary>

### 6. Complex types - mixed list
`mandatory`

File: [6-sum_mixed_list.py]()
</summary>

<p>Write a type-annotated function <code>sum_mixed_list</code> which takes a list <code>mxd_lst</code> of integers and floats and returns their sum as a float.</p>

<pre><code>bob@dylan:~$ cat 6-main.py
#!/usr/bin/env python3

sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))

bob@dylan:~$ ./6-main.py
{'mxd_lst': typing.List[typing.Union[int, float]], 'return': &lt;class 'float'&gt;}
True
sum_mixed_list(mixed) returns 679.13 which is a &lt;class 'float'&gt;
</code></pre>


</details>

<details>
<summary>

### 7. Complex types - string and int/float to tuple
`mandatory`

File: [7-to_kv.py]()
</summary>

<p>Write a type-annotated function <code>to_kv</code> that takes a string <code>k</code> and an int OR float <code>v</code> as arguments and returns a tuple. The first element of the tuple is the string <code>k</code>. The second element is the square of the int/float <code>v</code> and should be annotated as a float.</p>

<pre><code>bob@dylan:~$ cat 7-main.py
#!/usr/bin/env python3

to_kv = __import__('7-to_kv').to_kv

print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))

bob@dylan:~$ ./7-main.py
{'k': &lt;class 'str'&gt;, 'v': typing.Union[int, float], 'return': typing.Tuple[str, float]}
('eggs', 9)
('school', 0.0004)
</code></pre>


</details>

<details>
<summary>

### 8. Complex types - functions
`mandatory`

File: [8-make_multiplier.py]()
</summary>

<p>Write a type-annotated function <code>make_multiplier</code> that takes a float <code>multiplier</code> as argument and returns a function that multiplies a float by <code>multiplier</code>.</p>

<pre><code>bob@dylan:~$ cat 8-main.py
#!/usr/bin/env python3

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))

bob@dylan:~$ ./8-main.py
{'multiplier': &lt;class 'float'&gt;, 'return': typing.Callable[[float], float]}
4.928400000000001
</code></pre>


</details>

<details>
<summary>

### 9. Let's duck type an iterable object
`mandatory`

File: [9-element_length.py]()
</summary>

<p>Annotate the below function’s parameters and return values with the appropriate types</p>

<pre><code>def element_length(lst):
    return [(i, len(i)) for i in lst]
</code></pre>

<pre><code>bob@dylan:~$ cat 9-main.py 
#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)

bob@dylan:~$ ./9-main.py 
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}
</code></pre>


</details>

<details>
<summary>

### 10. Duck typing - first element of a sequence
`#advanced`

File: [100-safe_first_element.py]()
</summary>

<p>Augment the following code with the correct duck-typed annotations:</p>

<pre><code># The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
</code></pre>

<pre><code>bob@dylan:~$ cat 100-main.py 
#!/usr/bin/env python3

safe_first_element =  __import__('100-safe_first_element').safe_first_element

print(safe_first_element.__annotations__)

bob@dylan:~$ ./100-main.py 
{'lst': typing.Sequence[typing.Any], 'return': typing.Union[typing.Any, NoneType]}
</code></pre>


</details>

<details>
<summary>

### 11. More involved type annotations
`#advanced`

File: [101-safely_get_value.py]()
</summary>

<p>Given the parameters and the return values, add type annotations to the function</p>

<p>Hint: look into TypeVar</p>

<pre><code>def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
</code></pre>

<pre><code>bob@dylan:~$ cat 101-main.py 
#!/usr/bin/env python3

safely_get_value = __import__('101-safely_get_value').safely_get_value
annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print( ("{}: {}".format(k, v)))

bob@dylan:~$ ./101-main.py 
Here's what the mappings should look like
dct: typing.Mapping
key: typing.Any
default: typing.Union[~T, NoneType]
return: typing.Union[typing.Any, ~T]
</code></pre>


</details>

<details>
<summary>

### 12. Type Checking
`#advanced`

File: [102-type_checking.py]()
</summary>

<p>Use <code>mypy</code> to validate the following piece of code and apply any necessary changes.</p>

<pre><code>def zoom_array(lst: Tuple, factor: int = 2) -&gt; Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
</code></pre>

<pre><code>bob@dylan:~$ mypy 102-type_checking.py
Success: no issues found in 1 source file
bob@dylan:~$ cat 102-main.py 
#!/usr/bin/env python3

zoom_array =  __import__('102-type_checking').zoom_array

print(zoom_array.__annotations__)

bob@dylan:~$ ./102-main.py 
{'lst': typing.Tuple, 'factor': &lt;class 'int'&gt;, 'return': typing.List}
</code></pre>


</details>

