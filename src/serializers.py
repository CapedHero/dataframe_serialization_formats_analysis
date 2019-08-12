from pathlib import Path

import pandas as pd
import yaml


SERIALIZED_DATAFRAMES_DIR = Path("serialized_dataframes")


#######
# CSV #
#######


def serialize_to_uncompressed_csv(df: pd.DataFrame, file_name: str) -> None:
    df.to_csv(SERIALIZED_DATAFRAMES_DIR / file_name, compression=None)


def serialize_to_gzipped_csv(df: pd.DataFrame, file_name: str) -> None:
    df.to_csv(SERIALIZED_DATAFRAMES_DIR / file_name, compression="gzip")


########
# JSON #
########


def serialize_to_uncompressed_json(df: pd.DataFrame, file_name: str) -> None:
    df.to_json(SERIALIZED_DATAFRAMES_DIR / file_name, compression=None)


def serialize_to_gzipped_json(df: pd.DataFrame, file_name: str) -> None:
    df.to_json(SERIALIZED_DATAFRAMES_DIR / file_name, compression="gzip")


########
# YAML #
########


def serialize_to_uncompressed_yaml(df: pd.DataFrame, file_name: str) -> None:
    with open(SERIALIZED_DATAFRAMES_DIR / file_name, "w") as file:
        yaml.dump(df.to_dict(orient="records"), file, default_flow_style=False)
        # yaml.dump({"result": df.to_dict(orient="records")}, file, default_flow_style=False)


###########
# PARQUET #
###########


def serialize_to_uncompressed_parquet(df: pd.DataFrame, file_name: str) -> None:
    df.to_parquet(SERIALIZED_DATAFRAMES_DIR / file_name, compression=None)


def serialize_to_gzipped_parquet(df: pd.DataFrame, file_name: str) -> None:
    df.to_parquet(SERIALIZED_DATAFRAMES_DIR / file_name, compression="gzip")


def serialize_to_snappy_parquet(df: pd.DataFrame, file_name: str) -> None:
    df.to_parquet(SERIALIZED_DATAFRAMES_DIR / file_name, compression="snappy")


def serialize_to_brotli_parquet(df: pd.DataFrame, file_name: str) -> None:
    df.to_parquet(SERIALIZED_DATAFRAMES_DIR / file_name, compression="brotli")


###########
# FEATHER #
###########


def serialize_to_uncompressed_feather(df: pd.DataFrame, file_name: str) -> None:
    df.to_feather(SERIALIZED_DATAFRAMES_DIR / file_name)
