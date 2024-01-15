# %%
from datetime import datetime
import math
from hypothesis import given, strategies as st, settings
from hypothesis.provisional import domains


# %% function with single parameter
def print_positive_int(int_input: int) -> None:
    print(f"The input is: {int_input}.")


# %%
print_positive_int(int_input=5)

# %%
print_positive_int(int_input=22)


# %% right input
@given(st.integers(min_value=1))
# @settings(max_examples=3)
def test_print_positive_int(int_input):
    assert int_input > 0


# %%
test_print_positive_int()


# %% wrong input
@given(st.integers(max_value=0))
def test_print_positive_int(int_input):
    assert int_input > 0


# %%
test_print_positive_int()

# %% function with more parameters


def short_introduction(
    name: str, birth_date: datetime, height: float, number: int, email: str
):
    age = math.floor((datetime.today() - birth_date).days / 365.25)

    print(
        f"""
    Hi!
    My name is {name}.
    I am {age} years old and {height} cm tall.
    Feel free to contact me at {number} or {email}.
    """
    )


# %%
short_introduction(
    name="Alexa",
    birth_date=datetime(2014, 11, 6),
    height=120.8,
    number=12345678,
    email="dummy@gmail.com",
)


# %%
@given(
    st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=5, max_size=9),
    st.datetimes(min_value=datetime(1940, 1, 1), max_value=datetime(2010, 12, 31)),
    st.decimals(min_value=120.0, max_value=200.0),
    st.integers(min_value=10000000, max_value=99999999),
    st.emails(domains=domains(max_length=20)),
)
@settings(max_examples=3)
def test_short_introduction(name, birth_date, height, number, email):
    assert len(name) > 3
    assert birth_date < datetime.today()
    assert height > 100
    assert len(str(number)) == 8
    assert len(email) < 21


# %%
test_short_introduction()
# %%
