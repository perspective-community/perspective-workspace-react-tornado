import pandas as pd
import random
import superstore
import threading
import time
from perspective import PerspectiveManager, Table


def ticking_data(table):
    # generate some initial data
    last = [
        {"symbol": "ABC", "bid": (random.random() * 100) + 50},
        {"symbol": "DEF", "bid": (random.random() * 100) + 50},
        {"symbol": "GHI", "bid": (random.random() * 100) + 50},
    ]
    for record in last:
        record["ask"] = record["bid"] + random.random()

    # load initial records into table
    table.update(last)

    # run forever
    while True:
        # take a random walk
        for record in last:
            # don't let it drop negative
            record["bid"] = max(record["bid"] + (random.random() - 0.2), 5)
            record["ask"] = record["bid"] + random.random()
        table.update(last)
        time.sleep(1)


def get_table_manager():
    # Setup tables
    tables = {
        # static categorical dataset
        "superstore": Table(superstore.superstore(1000)),
        # static TS dataset with chart type
        "timeseries": Table(pd.DataFrame(pd.util.testing.getTimeSeriesData())),
        # ticking dataset
        "ticking": Table({"symbol": "string", "bid": "float", "ask": "float"}),
    }

    # run ticking data in background
    ticking_thread = threading.Thread(target=ticking_data, args=(tables["ticking"],))
    ticking_thread.start()

    # instantiate manager
    manager = PerspectiveManager()

    # host tables with manager
    for name, table in tables.items():
        manager.host_table(name, table)

    # return manager back for use in tornado handler
    return manager
