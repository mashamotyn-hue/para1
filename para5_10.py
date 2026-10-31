import random
import inspect
import sys

for method in dir(random):
    print(method)

print(hasattr(random, "uniform"))
print(callable(random.uniform))
print(callable(random.randrange))
print(inspect.ismodule(random))
print(inspect.isclass(random))
print(inspect.isfunction(random.uniform))
print(inspect.getmodule(random.uniform))
print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)
for module_name, module_path in sys.modules.items():
    print(module_name, module_path)

for component in dir(__builtins__):
    print(component)