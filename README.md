## How to run?

### *nix OS

```bash
# Prepare virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# Run analysis
python run_analysis_and_print_report.py datasets/**YOUR-CHOSEN-DATASET-IN-CSV-FROMAT**
```

### Docker
```bash
docker build -t dataframe_serialization_formats_analysis .
docker run -it dataframe_serialization_formats_analysis \
  python run_analysis_and_print_report.py datasets/**YOUR-CHOSEN-DATASET-IN-CSV-FROMAT**
```

## Looking for some test datasets?

Many great datasets examples can be found on Kaggle:
+ https://www.kaggle.com/datasets
