

## Libraries

List of dependency injection libraries for Python, sorted by stars:

+ [dependency_injector](https://github.com/ets-labs/python-dependency-injector)
+ [dry-python/dependencies](https://dependencies.readthedocs.io/en/latest/usage.html)
+ [antidote](https://antidote.readthedocs.io/en/stable/tutorial.html)
+ [diay](https://github.com/anlutro/diay.py)

## Tests

|                    | dependencies       | antidote            | diay               |dependency_injector |
|--------------------|--------------------|---------------------|--------------------|--------------------|
| Easy to use        | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :x:                |
| Good docs          | :heavy_check_mark: | :heavy_check_mark:  | :x:                | :x:                |
| Explicit container | :heavy_check_mark: | :x:                 | :x:                | :heavy_check_mark: |
| Type annotation    | :x:                | :heavy_check_mark:  | :heavy_check_mark: | :x:                |
| Lazy annotation    | :x:                | :heavy_check_mark:  | :heavy_check_mark: | :x:                |
| Name detection     | :heavy_check_mark: | :x:                 | :x:                | :x:                |
| Function as target | :x:                | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark: |
| Partial injection  | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark: |
| Overload deps      | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :x:                |
| Deps for deps      | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark: |

Test description:

+ **Easy to use** -- you don't have to know about some difficult conceptions and write much of code.
+ **Good docs** -- documentation exists and contains many examples and API reference.
+ **Explicit container** -- you define set of dependencies explicitly that helps you to find out which dependencies was used here without debugging.
+ **Type annotation** -- library can detect right dependency by type in annotations.
+ **Lazy annotation** -- library can work with lazy type annotations (defined as string). In Python 4.0 all annotations will be lazy.
+ **Name detection** -- library can detect right dependency by variable name.
+ **Function as target** -- you can inject dependencies into function.
+ **Partial injection** -- you can mix up dependencies with not injected arguments.
+ **Overload deps** -- you can pass your own dependencies to override dependencies in container.
+ **Deps for deps** -- dependencies can be injected into other dependencies.

## Usage

See [tests](./tests/) dir and docs for libraries for usage examples.

## Run tests

```bash
pip3 install --user -r requirements.txt
pytest --tb=short
```
