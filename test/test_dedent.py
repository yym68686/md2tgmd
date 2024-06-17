import textwrap

def example():
    text = """
    ```
    print("Hello, World!") -
    app.listen(PORT, () => {
        console.log(`Server is running on http://localhost:${PORT}`);
    });
    ```
    """
    # text = textwrap.dedent(text)
    print(text)

example()