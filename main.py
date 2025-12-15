from fastmcp import FastMCP
import asyncio

mcp = FastMCP("Math Tool")
def _as_numbers(x):
    if isinstance(x,(float,int)):
        return float(x)
    if isinstance(x,str):
        return float(x.strip())
    raise TypeError("Excpected a number(int/float)")

@mcp.tool
async def add(a:float,b:float)->float:
    "add two numbers a and b"
    return _as_numbers(a)+_as_numbers(b)

@mcp.tool
async def substract(a:float,b:float)->float:
    "substraction of two numbers a and b"
    return _as_numbers(a)-_as_numbers(b)

@mcp.tool
async def multiply(a:float,b:float)->float:
    "multiplication of two numbers a and b"
    return _as_numbers(a)*_as_numbers(b)

@mcp.tool
async def pow(a:float,b:float)->float:
    "this tool give a raise to power b"
    return _as_numbers(a)**_as_numbers(b)

@mcp.tool
async def modulus(a:float,b:float)->float:
    "it gives a modulus b"
    return _as_numbers(a)%_as_numbers(b)

if __name__ == "__main__":
    mcp.run()
