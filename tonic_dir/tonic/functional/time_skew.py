import numpy as np
import warnings


def time_skew_numpy(events: np.ndarray, coefficient: float, offset: int = 0):
    """Skew all event timestamps according to a linear transform,
    potentially sampled from a distribution of acceptable functions.

    Parameters:
        events: ndarray of shape [num_events, num_event_channels].
        coefficient: a real-valued multiplier applied to the timestamps of the events.
                     E.g. a coefficient of 2.0 will double the effective delay between any
                     pair of events.
        offset: value by which the timestamps will be shifted after multiplication by
                the coefficient. Negative offsets are permissible but may result in
                in an exception if timestamps are shifted below 0.

    Returns:
        the input events with rewritten timestamps.
    """

    assert "t" in events.dtype.names

    events["t"] = events["t"] * coefficient + offset

    return events
