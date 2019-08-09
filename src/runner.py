import time
from collections import namedtuple, OrderedDict
from pathlib import Path
from typing import Callable, List, Tuple

import pandas as pd
import yaml

from src import serializers as df_serializers
from tabulate import tabulate


FileName = str
Serializer = Callable[[pd.DataFrame, FileName], None]
PipelineItem: Tuple[Serializer, FileName] = namedtuple("PipelineItem", ["serializer", "file_name"])
Report = pd.DataFrame

tabulate.PRESERVE_WHITESPACE = True


def run_dataframe_serialization_formats_analysis_and_print_report(dataset_name: str) -> None:
    _print_dataset_name(dataset_name)

    df = pd.read_csv(Path(".") / "datasets" / dataset_name)

    _print_dataframe_info(df)

    pipeline = _build_df_serializations_pipeline()
    report = _run_df_serializations_pipeline(df, pipeline)

    _print_report_for_df_serialization_analysis(report)


############
# PIPELINE #
############


def _build_df_serializations_pipeline() -> List[PipelineItem]:
    pipeline = [
        # CSV
        PipelineItem(df_serializers.serialize_to_uncompressed_csv, "df.no-compression.csv"),
        PipelineItem(df_serializers.serialize_to_gzipped_csv, "df.gzip.csv"),
        # JSON
        PipelineItem(df_serializers.serialize_to_uncompressed_json, "df.no-compression.json"),
        PipelineItem(df_serializers.serialize_to_gzipped_json, "df.gzip.json"),
        # Parquet
        PipelineItem(df_serializers.serialize_to_uncompressed_parquet, "df.no-compression.parquet"),
        PipelineItem(df_serializers.serialize_to_gzipped_parquet, "df.gzip.parquet"),
        PipelineItem(df_serializers.serialize_to_brotli_parquet, "df.brotli.parquet"),
        PipelineItem(df_serializers.serialize_to_snappy_parquet, "df.snappy.parquet"),
        # Feather
        PipelineItem(df_serializers.serialize_to_uncompressed_feather, "df.no-compression.feather"),
        # YAML
        # ====
        # Note that YAML serialization is disabled by default. It is because
        # YAML serialization usually takes longer by two or even three orders
        # of magnitude than the slowest alternative!
        #
        # PipelineItem(df_serializers.serialize_to_uncompressed_yaml, "df.no-compression.yaml"),
    ]
    return pipeline


def _run_df_serializations_pipeline(df: pd.DataFrame, pipeline: List[PipelineItem]) -> Report:
    report = OrderedDict()
    extra_info = _get_extra_info()

    for serializer, file_name in pipeline:
        start_time = time.perf_counter()

        serializer(df, file_name)

        finish_time = time.perf_counter()
        serialization_speed = finish_time - start_time

        serialized_df_path = df_serializers.SERIALIZED_DATAFRAMES_DIR / file_name

        serialized_df_size_in_bytes = serialized_df_path.stat().st_size
        serialized_df_size_in_kilobytes = serialized_df_size_in_bytes / 1_024

        report[file_name] = {
            "Serialized DF Size (KBs)": serialized_df_size_in_kilobytes,
            "Serialization Speed (s)": serialization_speed,
            "Size/Speed (KB/s)": serialized_df_size_in_kilobytes / serialization_speed,
            "Format Type": extra_info[file_name]["format_type"],
            "Applicability": extra_info[file_name]["applicability"],
            "Extra Dependencies": extra_info[file_name]["extra_dependencies"],
        }

    report_df = pd.DataFrame.from_dict(data=report).T
    report_df = report_df.astype(
        {
            "Serialized DF Size (KBs)": float,
            "Serialization Speed (s)": float,
            "Size/Speed (KB/s)": float,
            "Format Type": str,
            "Applicability": str,
            "Extra Dependencies": str,
        }
    )
    report_df.index.name = "Serialization File"

    return report_df


def _get_extra_info() -> dict:
    with open("src/extra_info.yaml") as extra_info_file:
        extra_info = yaml.safe_load(extra_info_file)
    return extra_info


############
# PRINTERS #
############


def _print_dataset_name(dataset_name: str) -> None:

    print()
    print(f"DATASET NAME: {dataset_name}")
    print(f"=============={len(dataset_name) * '='}")


def _print_dataframe_info(df: pd.DataFrame) -> None:
    print()
    print("DATAFRAME INFO")
    print("==============")
    print()
    df.info(memory_usage="deep")
    print()


def _print_report_for_df_serialization_analysis(report: pd.DataFrame) -> None:
    report_by_serialized_df_size = report.sort_values(by="Serialized DF Size (KBs)")
    report_by_serialization_speed = report.sort_values(by="Serialization Speed (s)")
    report_by_size_speed_ratio = report.sort_values(by="Size/Speed (KB/s)", ascending=False)

    print()
    print("DATAFRAME SERIALIZATION REPORT - BY SIZE")
    print("========================================")
    print()
    print(_format_report(report_by_serialized_df_size))
    print()

    print()
    print("DATAFRAME SERIALIZATION REPORT - BY SPEED")
    print("=========================================")
    print()
    print(_format_report(report_by_serialization_speed))
    print()

    print()
    print("DATAFRAME SERIALIZATION REPORT - BY SIZE/SPEED")
    print("==============================================")
    print()
    print(_format_report(report_by_size_speed_ratio))
    print()


def _format_report(report: pd.DataFrame) -> str:
    formatted_report = tabulate(
        report,
        headers="keys",
        tablefmt="rst",
        floatfmt=(None, ",.0f", ",.3f", ",.0f"),
        colalign=["left", "right", "right", "right", "center", "center", "left"],
    )
    return formatted_report
