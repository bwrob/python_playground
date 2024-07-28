"""Example of Streamlit App."""

import time
from functools import lru_cache

import pandas as pd
import streamlit as st


def make_title() -> None:
    name = "Fibonacci Sequence"
    st.set_page_config(
        page_title=name,
        page_icon="✅",
        layout="wide",
    )
    _ = st.title(body=name)


@lru_cache
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def get_input() -> int:
    input_ = st.slider("Pick a number", 0, 100, 25)
    assert isinstance(input_, int)
    return input_


def fibbonacci_df(n: int) -> tuple[pd.DataFrame, float]:
    # time creation of dataframe
    start = time.time()
    result = pd.DataFrame(
        {
            "number": list(range(n)),
            "fibonacci": [fibonacci(i) for i in range(n)],
        }
    )
    end = time.time()
    print(f"Time taken to create dataframe: {end - start}")
    return result, end - start


def web_app() -> None:
    make_title()
    n = get_input()
    df, time_ = fibbonacci_df(n)
    st.write(f"Time taken to create dataframe: {time_//1_000} mili seconds")
    st.dataframe(df)


if __name__ == "__main__":
    web_app()
