#Context Managers with Custom Resource Management:
from contextlib import contextmanager

@contextmanager
def managed_resource(resource_name):
    print(f"Acquiring resource: {resource_name}")
    resource = f"Resource {resource_name}"
    try:
        yield resource
    finally:
        print(f"Releasing resource: {resource_name}")

# Example usage
with managed_resource("File Handle") as res:
    print(f"Using {res}")
