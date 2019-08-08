import os
import sys

from src.runner import run_dataframe_serialization_formats_analysis_and_print_report


dataset_path = sys.argv[1]
_, dataset_name = os.path.split(dataset_path)

run_dataframe_serialization_formats_analysis_and_print_report(dataset_name)
