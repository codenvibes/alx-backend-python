<h1 align="center"><b>0X00. PYTHON - VARIABLE ANNOTATIONS</b></h1>
<div align="center"><code>Python</code> <code>Back-end</code></div>

## Concepts
<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/5j0OtdWh36_HVAHKJX2gaA">Advanced Python</a></b></summary><br>

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<br>
<div align="center"><img alt="" src="https://github.com/codenvibes/alx-backend-python/blob/master/0x00-python_variable_annotations/images/y9y25tefi5401.png"></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Resources
<details>
<summary><b><a href="https://docs.python.org/3/library/typing.html">Python 3 typing documentation</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html">MyPy cheat sheet</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!--==================================================-->
<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>Type annotations in Python 3</b></summary><br>

Type annotations in Python 3 are a feature that allows developers to specify the types of variables, function parameters, and return values. This feature was introduced in Python 3.5 through PEP 484 and has since been improved in subsequent versions. Type annotations help with code readability, provide hints for IDEs and linters, and facilitate static type checking using tools like `mypy`.

Here's an overview of how to use type annotations in Python 3:

### Basic Type Annotations

#### Variables

You can annotate the type of variables using the syntax:
```python
variable_name: type = value
```

Example:
```python
name: str = "John"
age: int = 30
height: float = 5.9
is_active: bool = True
```

#### Functions

You can annotate the types of function parameters and return values:
```python
def function_name(param1: type1, param2: type2) -> return_type:
    pass
```

Example:
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b
```

### Complex Types

#### Lists, Tuples, and Dictionaries

For collections, you can use the `List`, `Tuple`, and `Dict` types from the `typing` module:
```python
from typing import List, Tuple, Dict

names: List[str] = ["Alice", "Bob", "Charlie"]
point: Tuple[int, int] = (10, 20)
scores: Dict[str, int] = {"Alice": 85, "Bob": 92}
```

#### Optional and Union Types

To indicate that a variable can be of more than one type, or that it can be `None`, you can use `Union` and `Optional` from the `typing` module:
```python
from typing import Union, Optional

# A variable that can be either an int or a float
number: Union[int, float] = 3.14

# A variable that can be either a string or None
name: Optional[str] = None
```

### Type Aliases

You can create type aliases to simplify complex type annotations:
```python
from typing import List, Dict

# Define a type alias
Address = Dict[str, str]

# Use the type alias
addresses: List[Address] = [{"street": "Main St", "city": "Springfield"}]
```

### Generics

Generics can be used to create functions and classes that can work with any type. This is done using `TypeVar` from the `typing` module:
```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

def get_first_element(elements: List[T]) -> T:
    return elements[0]

# Example usage
print(get_first_element([1, 2, 3]))  # Output: 1
print(get_first_element(["a", "b", "c"]))  # Output: "a"
```

### Annotating Class Methods

You can also annotate class methods, including `self` and `cls`:
```python
from typing import List

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name}."

    @classmethod
    def from_dict(cls, data: dict) -> "Person":
        return cls(name=data["name"], age=data["age"])
```

### Type Checking with `mypy`

To perform static type checking, you can use `mypy`, a static type checker for Python:
```sh
pip install mypy
```

Then run `mypy` on your Python files:
```sh
mypy your_script.py
```

### Summary

Type annotations are a powerful feature in Python that can improve code clarity and facilitate debugging and maintenance. By using type annotations, you can make your code more understandable and leverage tools for static type checking to catch potential issues early in the development process.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How you can use type annotations to specify function signatures and variable types</b></summary><br>

Type annotations in Python provide a way to specify the types of variables, function parameters, and return values. They can improve code readability, facilitate static type checking, and help with IDE autocompletion. Here's a guide on how to use type annotations for function signatures and variable types:

### 1. Variable Type Annotations

To specify the type of a variable, use a colon followed by the type:

```python
# Basic types
name: str = "Alice"
age: int = 30
is_student: bool = True
height: float = 5.7

# List and dictionary types
numbers: list[int] = [1, 2, 3, 4, 5]
grades: dict[str, int] = {"math": 90, "science": 85}
```

### 2. Function Signatures

Type annotations can also be used to specify the types of function parameters and return values:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(x: int, y: int) -> int:
    return x + y

def get_top_students(students: dict[str, int]) -> list[str]:
    return [name for name, grade in students.items() if grade > 90]
```

### 3. Optional Types

Sometimes, a variable or a function parameter can be of multiple types or `None`. Use the `Optional` type hint from the `typing` module:

```python
from typing import Optional

def find_student(student_id: int) -> Optional[str]:
    if student_id == 1:
        return "Alice"
    return None
```

### 4. Union Types

When a variable or parameter can be one of several types, use the `Union` type hint:

```python
from typing import Union

def process_data(data: Union[str, int]) -> str:
    if isinstance(data, int):
        return f"Processing number: {data}"
    return f"Processing string: {data}"
```

### 5. Complex Data Structures

For more complex data structures, use `List`, `Dict`, `Tuple`, etc., from the `typing` module:

```python
from typing import List, Dict, Tuple

def calculate_averages(grades: List[int]) -> float:
    return sum(grades) / len(grades)

def student_info() -> Dict[str, Tuple[int, float]]:
    return {"Alice": (21, 3.5), "Bob": (22, 3.7)}
```

### 6. Custom Types

For more specific types, you can create your own type aliases:

```python
from typing import List, Dict, Tuple

Student = Dict[str, Union[int, float]]

def get_student_details() -> List[Student]:
    return [{"name": "Alice", "age": 21, "gpa": 3.5}, {"name": "Bob", "age": 22, "gpa": 3.7}]
```

### 7. Type Checking

While type annotations do not enforce types at runtime, they are useful for static type checkers like `mypy`. To check your code with `mypy`, install it and run:

```bash
pip install mypy
mypy your_script.py
```

### Example Code with Type Annotations

```python
from typing import List, Dict, Union

def student_summary(students: List[Dict[str, Union[int, str]]]) -> None:
    for student in students:
        name: str = student["name"]
        age: int = student["age"]
        print(f"Student Name: {name}, Age: {age}")

# Sample usage
students_data = [{"name": "Alice", "age": 21}, {"name": "Bob", "age": 22}]
student_summary(students_data)
```

In this example, `student_summary` takes a list of dictionaries where each dictionary represents a student with `name` as a string and `age` as an integer. The function prints the name and age of each student.

By using type annotations, you can make your code clearer and more maintainable, and leverage tools like `mypy` to catch type-related errors before they cause problems at runtime.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>Duck typing</b></summary><br>

Duck typing is a concept in dynamic typing languages like Python, where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit type. The term comes from the phrase "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

In duck typing, you don't check the type of an object to determine if it has the right interface; you just use the object and assume it has the necessary methods and attributes. This can make code more flexible and easier to extend.

Here's an example to illustrate duck typing in Python:

### Example of Duck Typing

Suppose you have a function that processes different types of animals, and you want to include a behavior where they can "speak". Instead of checking the type of each animal, you rely on the `speak` method being present:

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"

def animal_sound(animal):
    print(animal.speak())

# Sample usage
dog = Dog()
cat = Cat()
bird = Bird()

animal_sound(dog)  # Outputs: Woof!
animal_sound(cat)  # Outputs: Meow!
animal_sound(bird) # Outputs: Tweet!
```

In this example, the `animal_sound` function doesn't care about the type of the object passed to it. As long as the object has a `speak` method, it will work correctly.

### Advantages of Duck Typing

1. **Flexibility:** Allows you to write more generic and reusable code.
2. **Ease of Extension:** New types can be added without modifying existing code as long as they conform to the expected interface.
3. **Simplicity:** Reduces the need for complex type hierarchies and inheritance.

### Potential Issues

1. **Runtime Errors:** If an object doesn’t have the expected method, it will raise an `AttributeError` at runtime.
2. **Readability:** It can sometimes be less clear what types are expected, making code harder to understand.

### Duck Typing with Type Annotations

Even with duck typing, you can use type annotations to indicate the expected interface using `Protocol` from the `typing` module (available in Python 3.8+). This allows you to define the expected methods without enforcing a specific type.

```python
from typing import Protocol

class Speakable(Protocol):
    def speak(self) -> str:
        ...

def animal_sound(animal: Speakable) -> None:
    print(animal.speak())

class Dog:
    def speak(self) -> str:
        return "Woof!"

class Cat:
    def speak(self) -> str:
        return "Meow!"

# Sample usage
dog = Dog()
cat = Cat()

animal_sound(dog)  # Outputs: Woof!
animal_sound(cat)  # Outputs: Meow!
```

In this example, `Speakable` is a protocol that specifies the `speak` method. The `animal_sound` function expects any object that conforms to the `Speakable` protocol, ensuring that the object has a `speak` method.

### Summary

Duck typing is a powerful feature in Python that allows for more flexible and dynamic code by relying on the presence of methods and attributes rather than explicit types. While it offers many advantages, it also requires careful handling to avoid runtime errors. Using type annotations and protocols can help document and enforce expected behaviors, combining the best of both worlds.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to validate your code with <code>mypy</code></b></summary><br>

Validating your code with `mypy` is a straightforward process that involves a few steps:

1. **Install mypy**: First, you need to install `mypy` if you haven't already. You can do this using `pip`:
   ```bash
   pip install mypy
   ```

2. **Add Type Annotations**: Ensure your code has type annotations for variables, function parameters, and return types. Here's a simple example:
   ```python
   def add(x: int, y: int) -> int:
       return x + y

   def greet(name: str) -> str:
       return f"Hello, {name}!"
   ```

3. **Run mypy**: Run `mypy` on your Python script or module. You can do this from the command line:
   ```bash
   mypy your_script.py
   ```

4. **Fix Reported Issues**: `mypy` will report any type inconsistencies or errors it finds. Fix these issues to ensure your code conforms to the specified types.

### Detailed Example

Let's walk through an example:

#### Step 1: Create a Python Script with Type Annotations

Create a file named `example.py` with the following content:

```python
from typing import List, Optional, Union

def add(x: int, y: int) -> int:
    return x + y

def greet(name: str) -> str:
    return f"Hello, {name}!"

def find_student(student_id: int) -> Optional[str]:
    students = {1: "Alice", 2: "Bob"}
    return students.get(student_id)

def process_data(data: Union[str, int]) -> str:
    if isinstance(data, int):
        return f"Processing number: {data}"
    return f"Processing string: {data}"

def calculate_averages(grades: List[int]) -> float:
    return sum(grades) / len(grades)
```

#### Step 2: Install mypy

If you haven't installed `mypy` yet, do so using `pip`:
```bash
pip install mypy
```

#### Step 3: Run mypy

Run `mypy` on your script:

```bash
mypy example.py
```

#### Step 4: Interpret the Output and Fix Issues

`mypy` will output something like this if there are type errors:

```
example.py:14: error: Incompatible return value type (got "Optional[str]", expected "str")
example.py:19: error: Argument 1 to "sum" has incompatible type "List[float]"; expected "Iterable[int]"
```

These messages indicate that there are type mismatches in the `find_student` and `calculate_averages` functions.

### Common Fixes

1. **Optional Return Type**: Ensure that functions that can return `None` are properly annotated with `Optional`.

2. **Correct Type Usage**: Ensure that you are passing the correct types to functions and using them correctly within your code.

### Improved Example

Here’s how you can fix the issues based on `mypy` feedback:

```python
from typing import List, Optional, Union

def add(x: int, y: int) -> int:
    return x + y

def greet(name: str) -> str:
    return f"Hello, {name}!"

def find_student(student_id: int) -> Optional[str]:
    students = {1: "Alice", 2: "Bob"}
    return students.get(student_id)

def process_data(data: Union[str, int]) -> str:
    if isinstance(data, int):
        return f"Processing number: {data}"
    return f"Processing string: {data}"

def calculate_averages(grades: List[int]) -> float:
    return sum(grades) / len(grades)
```

Now, re-run `mypy`:

```bash
mypy example.py
```

If everything is correct, `mypy` should not report any errors:

```
Success: no issues found in 1 source file
```

### Additional Tips

- **Use `# type: ignore`**: If `mypy` complains about a particular line but you are certain it is correct, you can silence the warning by adding `# type: ignore` to that line.
  
  ```python
  def find_student(student_id: int) -> Optional[str]:
      students = {1: "Alice", 2: "Bob"}
      return students.get(student_id)  # type: ignore
  ```

- **Type Aliases**: Use type aliases to simplify complex type annotations.
  
  ```python
  from typing import List, Tuple

  Student = Tuple[int, str]
  def get_students() -> List[Student]:
      return [(1, "Alice"), (2, "Bob")]
  ```

- **Config File**: You can create a `mypy.ini` or `setup.cfg` configuration file to customize `mypy` behavior.

  ```ini
  [mypy]
  ignore_missing_imports = True
  disallow_untyped_defs = True
  ```

Using `mypy` helps catch type-related errors early, making your code more robust and maintainable.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>




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

