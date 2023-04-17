# Python 3.8 Protocol for a HttpApi as used to implement the Canvas API
# Strictly speaking this is probably overkill, but it does allow us decouple the Canvas API methods
# and the underlying implementation, which may assist if/when the API changes.
# Brodie Hicks, 2021.

from abc import abstractmethod
from typing import Protocol

class HttpApi(Protocol):
    Scheme: str = "https"
    Host: str

    @abstractmethod
    def get(self, path):
        """
        Performs a HTTP GET operation and returns the result
        """
        raise NotImplementedError

    # Add other HTTP verbs as required here.