from vector import Vector3D
import pytest


def test_vector_str():
    v = Vector3D(1,2,3)
    assert str(v) == "(1, 2, 3)"

def test_vector_repr():
    v = Vector3D(1,2,3)
    assert repr(v) == "Vector3D(1, 2, 3)"

def test_vector_add():
    v = Vector3D(1,2,3)
    u = Vector3D(1,1,1)
    w = u + v
    assert w.x == 2
    assert w.y == 3
    assert w.z == 4 

def test_vector_add_eq():
    v = Vector3D(1,2,3)
    u = Vector3D(1,1,1)
    w = u + v
    assert w == Vector3D(2,3,4)

def test_vector_add_int():
    v = Vector3D(1,2,3)
    u = 1
    w = v + u
    assert w == Vector3D(2,3,4)

def test_vector_add_int_right():
    v = Vector3D(1,2,3)
    u = 1
    w = u + v
    assert w == Vector3D(2,3,4)

def test_vector_add_string_raises_TypeError():
    v = Vector3D(1,2,3)
    u = "Hello"
    with pytest.raises(TypeError):
        u + v

def test_vector_dot_product():
    v = Vector3D(1,2,3)
    u = Vector3D(1,1,1)
    w = u.dot(v)
    assert isinstance(w, (int, float))
    assert abs(w - 6) < 1e-12