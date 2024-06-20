<h1 align="center"><b>0X01. PYTHON - ASYNC</b></h1>
<div align="center"><code>Python</code> <code>Back-end</code></div>

<br>
<div align="center"><img alt="" src="https://github.com/codenvibes/alx-backend-python/blob/master/0x01-python_async_function/images/4aeaa9c3cb1f316c05c4.png"></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Resources
<details>
<summary><b><a href="https://realpython.com/async-io-python/">Async IO in Python: A Complete Walkthrough</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.python.org/3/library/asyncio.html">asyncio - Asynchronous I/O</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.python.org/3/library/random.html#random.uniform">random.uniform</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!--==================================================-->
<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a><code>async</code> and <code>await</code> syntax</b></summary><br>

In Python, `async` and `await` are used to write asynchronous code, which allows for concurrency without having to use threads or processes. This can be particularly useful for I/O-bound tasks such as network requests, file I/O, or any operations that would benefit from being able to pause and resume execution. Here's a detailed explanation of how `async` and `await` work:

### `async` Syntax

The `async` keyword is used to define an asynchronous function, which is a function that returns a coroutine. A coroutine is a special type of function that can pause its execution to allow other tasks to run.

```python
async def my_async_function():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
```

In the example above, `my_async_function` is defined as an asynchronous function using the `async` keyword. Inside this function, `await` is used to pause its execution until the `asyncio.sleep(1)` coroutine is complete.

### `await` Syntax

The `await` keyword is used to pause the execution of an `async` function until the awaited coroutine is done. It can only be used inside `async` functions.

```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    await say_hello()

# Run the main function
asyncio.run(main())
```

In this example, the `say_hello` function is defined as an asynchronous function. The `main` function calls `say_hello` using `await`, meaning it will wait for `say_hello` to complete before continuing. The `asyncio.run(main())` line is used to run the `main` coroutine and start the event loop.

### Using `async` and `await` with I/O Bound Operations

Asynchronous code is particularly useful for I/O-bound operations. Here is an example using `aiohttp` to make asynchronous HTTP requests:

```python
import aiohttp
import asyncio

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = 'https://www.example.com'
    html = await fetch_url(url)
    print(html)

# Run the main function
asyncio.run(main())
```

In this example, `fetch_url` is an asynchronous function that fetches the content of a URL using `aiohttp`. The `main` function calls `fetch_url` and prints the result.

### Error Handling in Asynchronous Code

You can handle errors in asynchronous code using try-except blocks:

```python
async def risky_operation():
    await asyncio.sleep(1)
    raise ValueError("Something went wrong!")

async def main():
    try:
        await risky_operation()
    except ValueError as e:
        print(f"Caught an error: {e}")

# Run the main function
asyncio.run(main())
```

In this example, if `risky_operation` raises an exception, it is caught and handled in the `main` function.

These examples demonstrate the basics of using `async` and `await` in Python to write asynchronous, non-blocking code.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to execute an async program with <code>asyncio</code></b></summary><br>

Executing an async program in Python using `asyncio` involves creating one or more asynchronous functions (coroutines) and then running these functions within an event loop. Here is a step-by-step guide to executing an async program with `asyncio`:

### Step 1: Define Asynchronous Functions

Define the asynchronous functions (coroutines) that will perform the tasks you want to run concurrently. Use the `async` keyword to define these functions and `await` to pause their execution until the awaited task is complete.

```python
import asyncio

async def async_task_1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")

async def async_task_2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")
```

### Step 2: Define the Main Coroutine

Create a main coroutine that will run the asynchronous tasks. Use `asyncio.gather` to run multiple coroutines concurrently if needed.

```python
async def main():
    await asyncio.gather(
        async_task_1(),
        async_task_2()
    )
```

### Step 3: Run the Main Coroutine

Use `asyncio.run` to execute the main coroutine. This function starts the event loop, runs the specified coroutine, and closes the loop when the coroutine is finished.

```python
if __name__ == "__main__":
    asyncio.run(main())
```

### Full Example

Here is a complete example combining all the steps:

```python
import asyncio

async def async_task_1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")

async def async_task_2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")

async def main():
    await asyncio.gather(
        async_task_1(),
        async_task_2()
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### Explanation

1. **Define Asynchronous Functions**:
   - `async_task_1` and `async_task_2` are defined as asynchronous functions using the `async` keyword.
   - They use `await asyncio.sleep(x)` to simulate a delay, representing an asynchronous task.

2. **Define the Main Coroutine**:
   - The `main` coroutine is defined to manage and run multiple asynchronous tasks concurrently using `asyncio.gather`.

3. **Run the Main Coroutine**:
   - `asyncio.run(main())` is used to run the `main` coroutine. This starts the event loop, executes `main`, and stops the loop when `main` completes.


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to run concurrent coroutines</b></summary><br>

### Using `asyncio.gather`

The `asyncio.gather` function is the simplest way to run multiple coroutines concurrently. It runs the given coroutines in parallel and waits for all of them to finish.

```python
import asyncio

async def async_task_1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")

async def async_task_2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")

async def async_task_3():
    print("Task 3 started")
    await asyncio.sleep(3)
    print("Task 3 finished")

async def main():
    await asyncio.gather(
        async_task_1(),
        async_task_2(),
        async_task_3()
    )

if __name__ == "__main__":
    asyncio.run(main())
```

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to create <code>asyncio</code> tasks</b></summary><br>

Creating tasks in `asyncio` allows you to schedule coroutines to run concurrently. This can be done using `asyncio.create_task`, which returns an `asyncio.Task` object. This object can be used to manage the execution of the coroutine. Here’s a detailed guide on how to create and manage asyncio tasks:

### Step-by-Step Guide to Creating `asyncio` Tasks

1. **Import the `asyncio` Module**:
   Make sure you import the `asyncio` module to access its functions and classes.

2. **Define Asynchronous Functions**:
   Create asynchronous functions (coroutines) that you want to run as tasks using the `async` keyword.

3. **Create and Schedule Tasks**:
   Use `asyncio.create_task` to create tasks from these coroutines. This schedules them to run concurrently.

4. **Run the Event Loop**:
   Use `asyncio.run` to run the main coroutine that manages your tasks.

### Example

Here's a complete example demonstrating these steps:

```python
import asyncio

# Define asynchronous functions (coroutines)
async def async_task_1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")
    return "Result from task 1"

async def async_task_2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")
    return "Result from task 2"

async def async_task_3():
    print("Task 3 started")
    await asyncio.sleep(3)
    print("Task 3 finished")
    return "Result from task 3"

# Main coroutine to create and manage tasks
async def main():
    # Create tasks
    task1 = asyncio.create_task(async_task_1())
    task2 = asyncio.create_task(async_task_2())
    task3 = asyncio.create_task(async_task_3())

    # Optionally, await on individual tasks to get their results
    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1)
    print(result2)
    print(result3)

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())
```

### Explanation

1. **Define Asynchronous Functions**:
   - `async_task_1`, `async_task_2`, and `async_task_3` are asynchronous functions that simulate asynchronous operations using `await asyncio.sleep(x)`.

2. **Create and Schedule Tasks**:
   - In the `main` coroutine, `asyncio.create_task` is used to create tasks from these coroutines.
   - Each call to `asyncio.create_task` schedules the coroutine to run concurrently.

3. **Await Task Results**:
   - `await task1`, `await task2`, and `await task3` are used to wait for the tasks to complete and get their results.
   - This ensures that the results are printed only after the respective tasks have finished.

4. **Run the Event Loop**:
   - `asyncio.run(main())` is used to run the `main` coroutine, which starts the event loop and manages the execution of the tasks.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use the <code>random</code> module</b></summary><br>

The `random` module in Python provides functions for generating random numbers and for working with random data. Below are some common uses and examples of how to use the `random` module.

### Importing the Module

First, you need to import the `random` module:

```python
import random
```

### Generating Random Numbers

#### 1. Random Float Between 0 and 1
```python
random_float = random.random()
print(random_float)  # Example output: 0.37444887175646646
```

#### 2. Random Float in a Range
```python
random_float_range = random.uniform(1.5, 10.5)
print(random_float_range)  # Example output: 7.892800632839505
```

#### 3. Random Integer in a Range
```python
random_int = random.randint(1, 10)
print(random_int)  # Example output: 7
```

#### 4. Random Integer with a Step
```python
random_int_step = random.randrange(0, 101, 5)
print(random_int_step)  # Example output: 20
```

### Random Choices from a Sequence

#### 1. Random Element from a List
```python
choices = ['apple', 'banana', 'cherry']
random_choice = random.choice(choices)
print(random_choice)  # Example output: 'banana'
```

#### 2. Random Sample of Elements from a List
```python
random_sample = random.sample(choices, 2)
print(random_sample)  # Example output: ['cherry', 'apple']
```

#### 3. Randomly Shuffle a List
```python
random.shuffle(choices)
print(choices)  # Example output: ['banana', 'cherry', 'apple']
```

#### 4. Random Choices with Replacement
```python
random_choices_with_replacement = random.choices(choices, k=3)
print(random_choices_with_replacement)  # Example output: ['apple', 'banana', 'apple']
```

### Setting a Seed

Setting a seed ensures that the random numbers are reproducible, which is useful for debugging or when you need reproducible results.

```python
random.seed(42)
print(random.random())  # Example output: 0.6394267984578837
print(random.randint(1, 10))  # Example output: 2
```

### Other Useful Functions

#### 1. Generating Random Bits
```python
random_bits = random.getrandbits(8)
print(random_bits)  # Example output: 239 (a random 8-bit number)
```

#### 2. Random Gaussian Distribution
```python
mu, sigma = 0, 1  # mean and standard deviation
random_gaussian = random.gauss(mu, sigma)
print(random_gaussian)  # Example output: -0.19646717322454657
```

### Putting It All Together

Here is a comprehensive example that demonstrates various functionalities of the `random` module:

```python
import random

# Setting a seed
random.seed(42)

# Random float between 0 and 1
print("Random float:", random.random())

# Random float in a range
print("Random float between 1.5 and 10.5:", random.uniform(1.5, 10.5))

# Random integer in a range
print("Random integer between 1 and 10:", random.randint(1, 10))

# Random integer with a step
print("Random integer between 0 and 100 with step 5:", random.randrange(0, 101, 5))

# Random element from a list
choices = ['apple', 'banana', 'cherry']
print("Random choice from list:", random.choice(choices))

# Random sample from a list
print("Random sample of 2 from list:", random.sample(choices, 2))

# Shuffle a list
random.shuffle(choices)
print("Shuffled list:", choices)

# Random choices with replacement
print("Random choices with replacement:", random.choices(choices, k=3))

# Random bits
print("Random 8-bit number:", random.getrandbits(8))

# Random Gaussian distribution
mu, sigma = 0, 1
print("Random Gaussian number:", random.gauss(mu, sigma))
```

This guide should provide a solid foundation for using the `random` module in Python for generating random numbers and making random selections.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!--==================================================-->
<br>

## Requirements
<h3>General</h3>

- A <code>README.md</code> file, at the root of the folder of the project, is mandatory
- Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)
- All your files should end with a new line
- All your files must be executable
- The length of your files will be tested using <code>wc</code>
- The first line of all your files should be exactly <code>#!/usr/bin/env python3</code>
- Your code should use the <code>pycodestyle</code> style (version 2.5.x)
- All your functions and coroutines must be type-annotated.
- All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)
- All your functions should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code>
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. The basics of async
`mandatory`

File: [0-basic_async_syntax.py]()
</summary>

<p>Write an asynchronous coroutine that takes in an integer argument (<code>max_delay</code>, with a default value of 10) named <code>wait_random</code> that waits for a random delay between 0 and <code>max_delay</code> (included and float value) seconds and eventually returns it.</p>

<p>Use the <code>random</code> module.</p>

<pre><code>bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
</code></pre>


</details>

<details>
<summary>

### 1. Let's execute multiple coroutines at the same time with async
`mandatory`

File: [1-concurrent_coroutines.py]()
</summary>

<p>Import <code>wait_random</code> from the previous python file that you’ve written and write an async routine called <code>wait_n</code> that takes in 2 int arguments (in this order): <code>n</code> and <code>max_delay</code>. You will spawn <code>wait_random</code> <code>n</code> times with the specified <code>max_delay</code>.</p>

<p><code>wait_n</code> should return the list of all the delays (float values). The list of the delays should be in ascending order without using <code>sort()</code> because of concurrency.</p>

<pre><code>bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
</code></pre>

<p>The output for your answers might look a little different and that’s okay.</p>


</details>

<details>
<summary>

### 2. Measure the runtime
`mandatory`

File: [2-measure_runtime.py]()
</summary>

<p>From the previous file, import <code>wait_n</code> into <code>2-measure_runtime.py</code>.</p>

<p>Create a <code>measure_time</code> function with integers <code>n</code> and <code>max_delay</code> as arguments that measures the total execution time for <code>wait_n(n, max_delay)</code>, and returns <code>total_time / n</code>.  Your function should return a float.</p>

<p>Use the <code>time</code> module to measure an approximate elapsed time.</p>

<pre><code>bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

bob@dylan:~$ ./2-main.py
1.759705400466919
</code></pre>


</details>

<details>
<summary>

### 3. Tasks
`mandatory`

File: [3-tasks.py]()
</summary>

<p>Import <code>wait_random</code> from <code>0-basic_async_syntax</code>.</p>

<p>Write a function (do not create an async function, use the regular function syntax to do this) <code>task_wait_random</code> that takes an integer <code>max_delay</code> and returns a <code>asyncio.Task</code>.</p>

<pre><code>bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -&gt; float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

bob@dylan:~$ ./3-main.py
&lt;class '_asyncio.Task'&gt;
</code></pre>


</details>

<details>
<summary>

### 4. Tasks
`mandatory`

File: [4-tasks.py]()
</summary>

<p>Take the code from <code>wait_n</code> and alter it into a new function <code>task_wait_n</code>.  The code is nearly identical to <code>wait_n</code> except <code>task_wait_random</code> is being called.</p>

<pre><code>bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

bob@dylan:~$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
</code></pre>


</details>

