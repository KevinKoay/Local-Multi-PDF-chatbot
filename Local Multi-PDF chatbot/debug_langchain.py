import sys
print(sys.path)
try:
    import langchain
    print(f"LangChain file: {langchain.__file__}")
    print(f"LangChain dir: {dir(langchain)}")
except ImportError as e:
    print(f"ImportError langchain: {e}")

try:
    import langchain.memory
    print("Success: langchain.memory")
except ImportError as e:
    print(f"ImportError langchain.memory: {e}")
