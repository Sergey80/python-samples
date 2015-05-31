def convert(s):
    try:
        x = int(s)
        return x
    except ValueError as e:
        print("failed: " + str(e))
        # return None
        # raise
    finally:
        print("in any case")


result = convert("a")
print(result)   # None

result = convert("1")
print(result)   # 1

# -----------
def convert2(s):
    try:
        x = int(s)
        return x
    except ValueError:
        raise   # re-raise an exception

#  convert2("a")  # will fail here


# exception on import

try:
    import something

except ImportError:
    print("import something else")

