# original dtype
from collections import deque
from typing import Deque
import pandas as pd
import numpy as np
from typing import NewType
from typing import Dict, Tuple, Sequence
from typing import List
from typing import Union


def greeting(name: str) -> str:
    return 'Hello' + name


# Type aliases
Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


# More Type aliases
# Build complex data structure
ConnectionOptions = Dict[str, str]
Adress = Tuple[str, str]
Server = Tuple[Adress, ConnectionOptions]

# New Type
UserId = NewType('UserId', int)
some_id = UserId(524313)


def get_user_name(user_id: UserId) -> str:
    return 'hello'


def this_function_accept_array(arr: np.ndarray) -> np.ndarray:
    return arr.reshape(-1)


def this_function_accept_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    return df.head()


class Pose:
    def __init__(self, k: str, yx: list, score: float):
        self.k = k
        self.yx = yx
        self.score = score


pose_seq = Deque[Union[Pose, None]]


def check_pose_seq(pose_seq: pose_seq):
    return sum([pose for pose in pose_seq
                if not pose is None]) == pose_seq.maxlen


def main():
    greeting('Joe')
    this_function_accept_array(np.arange(10))
    # this_function_accept_array([i for i in range(5)])
    this_function_accept_dataframe(
        pd.DataFrame(
            {'col': [i for i in range(10)]}
        )
    )
    # new_vector = scale(2.0, [1.0, -4.2, 5.4])


if __name__ == "__main__":
    main()
