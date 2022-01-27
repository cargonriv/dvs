import os
import struct
import numpy as np


events_struct = [("x", np.int16), ("y", np.int16), ("t", np.int64), ("p", bool)]

# many functions in this file have been copied from https://gitlab.com/synsense/aermanager/-/blob/master/aermanager/parsers.py
def make_structured_array(x, y, t, p, dtype=events_struct):
    """
    Make a structured array given lists of x, y, t, p

    Args:
        x: List of x values
        y: List of y values
        t: List of times
        p: List of polarities boolean
    Returns:
        xytp: numpy structured array
    """
    return np.fromiter(zip(x, y, t, p), dtype=dtype)

def read_aedat4(in_file):
    import loris
    """
    Get the aer events from version 4 of .aedat file

    Args:
        in_file: str The name of the .aedat file
    Returns:
        xytp:   numpy structured array of events
    """
    event_data = loris.read_file(in_file)
    events = event_data["events"]
    return events


def read_dvs_128(filename):
    """
    Get the aer events from DVS with resolution of rows and cols are (128, 128)

    Args:
        filename: filename
    Returns:
        shape (tuple):
            (height, width) of the sensor array
        xytp: numpy structured array of events
    """
    data_version, data_start = read_aedat_header_from_file(filename)
    all_events = get_aer_events_from_file(filename, data_version, data_start)
    all_addr = all_events["address"]
    t = all_events["timeStamp"]

    x = (all_addr >> 8) & 0x007F
    y = (all_addr >> 1) & 0x007F
    p = all_addr & 0x1

    xytp = make_structured_array(x, y, t, p)
    shape = (128, 128)
    return shape, xytp


def read_dvs_ibm(filename):
    """
    Get the aer events from DVS with ibm gesture dataset

    Args:
        filename:   filename
    Returns:
        shape (tuple):
            (height, width) of the sensor array
        xytp: numpy structured array of events
    """
    data_version, data_start = read_aedat_header_from_file(filename)
    all_events = get_aer_events_from_file(filename, data_version, data_start)
    all_addr = all_events["address"]
    t = all_events["timeStamp"]

    x = (all_addr >> 17) & 0x00001FFF
    y = (all_addr >> 2) & 0x00001FFF
    p = (all_addr >> 1) & 0x00000001

    xytp = make_structured_array(x, y, t, p)
    shape = (128, 128)
    return shape, xytp


def read_dvs_red(filename):
    """
    Get the aer events from DVS with resolution of (260, 346)
    Args:
        filename:   filename
    Returns:
        shape (tuple):
            (height, width) of the sensor array

        xytp: numpy structured array of events
    """
    data_version, data_start = read_aedat_header_from_file(filename)
    all_events = get_aer_events_from_file(filename, data_version, data_start)
    all_addr = all_events["address"]
    t = all_events["timeStamp"]

    x = (all_addr >> 17) & 0x7FFF
    y = (all_addr >> 2) & 0x7FFF
    p = (all_addr >> 1) & 0x1

    xytp = make_structured_array(x, y, t, p)
    shape = (346, 260)
    return shape, xytp


def read_dvs_346mini(filename):
    """
    Get the aer events from DVS with resolution of (132,104)

    Args:
        filename: filename
    Returns:
        shape (tuple):
            (height, width) of the sensor array
        xytp: numpy structure of xytp

    """
    data_version, data_start = read_aedat_header_from_file(filename)
    all_events = get_aer_events_from_file(filename, data_version, data_start)
    all_addr = all_events["address"]
    t = all_events["timeStamp"]

    x = (all_addr >> 22) & 0x01FF
    y = (all_addr >> 12) & 0x03FF
    p = (all_addr >> 11) & 0x1

    xytp = make_structured_array(x, y, t, p)
    shape = (132, 104)
    return shape, xytp


def read_mnist_file(bin_file, dtype):
    """
    Reads in the TD events contained in the N-MNIST/N-CALTECH101 dataset file specified by 'filename'
    (Code adapted from https://github.com/gorchard/event-Python/blob/master/eventvision.py)
    """
    f = open(bin_file, "rb")
    raw_data = np.fromfile(f, dtype=np.uint8)
    f.close()
    raw_data = np.uint32(raw_data)

    all_y = raw_data[1::5]
    all_x = raw_data[0::5]
    all_p = (raw_data[2::5] & 128) >> 7  # bit 7
    all_ts = ((raw_data[2::5] & 127) << 16) | (raw_data[3::5] << 8) | (raw_data[4::5])

    # Process time stamp overflow events
    time_increment = 2 ** 13
    overflow_indices = np.where(all_y == 240)[0]
    for overflow_index in overflow_indices:
        all_ts[overflow_index:] += time_increment

    # Everything else is a proper td spike
    td_indices = np.where(all_y != 240)[0]

    xytp = make_structured_array(
        all_x[td_indices],
        all_y[td_indices],
        all_ts[td_indices],
        all_p[td_indices],
        dtype,
    )
    return xytp


def read_aedat_header_from_file(filename):
    """
    Get the aedat file version and start index of the binary data.

    Args:

        filename (str):     The name of the .aedat file

    Returns:
        data_version (float):   The version of the .aedat file
        data_start (int):       The start index of the data
    """
    filename = os.path.expanduser(filename)
    assert os.path.isfile(filename), f"The .aedat file '{filename}' does not exist."
    f = open(filename, "rb")
    count = 1
    is_comment = "#" in str(f.read(count))

    while is_comment:
        # Read the rest of the line
        head = str(f.readline())
        if "!AER-DAT" in head:
            data_version = float(head[head.find("!AER-DAT") + 8 : -5])
        is_comment = "#" in str(f.read(1))
        count += 1
    data_start = f.seek(-1, 1)
    f.close()
    return data_version, data_start


def get_aer_events_from_file(filename, data_version, data_start):
    """
    Get aer events from an aer file.

    Args:
        filename (str):         The name of the .aedat file
        data_version (float):   The version of the .aedat file
        data_start (int):       The start index of the data

    Returns:
         all_events:          Numpy structured array:
                                  ['address'] the address of a neuron which fires
                                  ['timeStamp'] the timeStamp in mus when a neuron fires
    """
    filename = os.path.expanduser(filename)
    assert os.path.isfile(filename), "The .aedat file does not exist."
    f = open(filename, "rb")
    f.seek(data_start)

    if 2 <= data_version < 3:
        event_dtype = np.dtype([("address", ">u4"), ("timeStamp", ">u4")])
        all_events = np.fromfile(f, event_dtype)
    elif data_version > 3:
        event_dtype = np.dtype([("address", "<u4"), ("timeStamp", "<u4")])
        event_list = []
        while True:
            header = f.read(28)
            if not header or len(header) == 0:
                break

            # read header
            capacity = struct.unpack("I", header[16:20])[0]
            event_list.append(np.fromfile(f, event_dtype, capacity))
        all_events = np.concatenate(event_list)
    else:
        raise NotImplementedError()
    f.close()
    return all_events
