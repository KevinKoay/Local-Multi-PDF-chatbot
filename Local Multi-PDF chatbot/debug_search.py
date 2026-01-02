import langchain_community
import langchain_core
print("Checking langchain_community:")
print(dir(langchain_community))
try:
    from langchain_community.chat_models import ChatOllama
    print("Found ChatOllama in community")
except ImportError:
    print("ChatOllama not in community")

print("\nChecking langchain_core:")
print(dir(langchain_core))

# Check for ConversationBufferMemory
import pkgutil
def find_module(module, name):
    if hasattr(module, "__path__"):
        for importer, modname, ispkg in pkgutil.walk_packages(module.__path__, prefix=module.__name__ + "."):
            if name.lower() in modname.lower():
                print(f"Found match: {modname}")

import langchain
print("\nSearching langchain namespace:")
find_module(langchain, "memory")
