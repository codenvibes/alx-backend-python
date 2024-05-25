<h1 align="center"><b>0X02. PYTHON - ASYNC COMPREHENSION</b></h1>
<div align="center"><code>Python</code> <code>Back-end</code></div>

<br>
<div align="center"><img alt="" width="50%" src="https://github.com/codenvibes/alx-backend-python/blob/master/0x02-python_async_comprehension/images/ee85b9f67c384e29525b.png"></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Resources
<details>
<summary><b><a href="https://peps.python.org/pep-0530/">PEP 530 – Asynchronous Comprehensions</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/">What’s New in Python: Asynchronous Comprehensions / Generators</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3">Type-hints for generators</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!--==================================================-->
<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>How to write an asynchronous generator</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use async comprehensions</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to type-annotate generators</b></summary><br>


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
- Your code should use the <code>pycodestyle</code> style (version 2.5.x)
- The length of your files will be tested using <code>wc</code>
- All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)
- All your functions should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code>
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.


<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. Async Generator
`mandatory`

File: [0-async_generator.py]()
</summary>

<p>Write a coroutine called <code>async_generator</code> that takes no arguments. </p>

<p>The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the <code>random</code> module. </p>

<pre><code>bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
</code></pre>


</details>

<details>
<summary>

### 1. Async Comprehensions
`mandatory`

File: [1-async_comprehension.py]()
</summary>

<p>Import <code>async_generator</code> from the previous task and then write a coroutine called <code>async_comprehension</code> that takes no arguments. </p>

<p>The coroutine will collect 10 random numbers using an async comprehensing over <code>async_generator</code>, then return the 10 random numbers.</p>

<pre><code>bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())

bob@dylan:~$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]

</code></pre>


</details>

<details>
<summary>

### 2. Run time for four parallel comprehensions
`mandatory`

File: [2-measure_runtime.py]()
</summary>

<p>Import <code>async_comprehension</code> from the previous file and write a <code>measure_runtime</code> coroutine that will execute <code>async_comprehension</code> four times in parallel using <code>asyncio.gather</code>.</p>

<p><code>measure_runtime</code> should measure the total runtime and return it.</p>

<p>Notice that the total runtime is roughly 10 seconds, explain it to yourself.</p>

<pre><code>bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)

bob@dylan:~$ ./2-main.py
10.021936893463135

</code></pre>


</details>

