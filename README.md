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


## Report Example

```text
>>> docker run -it dataframe_serialization_formats_analysis \
>>>   python run_analysis_and_print_report.py datasets/environmental-remediation-sites.csv

DATASET NAME: environmental-remediation-sites.csv
=================================================

DATAFRAME INFO
==============

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 70329 entries, 0 to 70328
Data columns (total 42 columns):
Program Number              70329 non-null object
Program Type                70329 non-null object
Program Facility Name       70329 non-null object
Site Class                  70329 non-null object
Address1                    70329 non-null object
Address2                    21171 non-null object
Locality                    70123 non-null object
County                      70329 non-null object
ZIPCode                     70329 non-null object
SWIS Code                   70329 non-null int64
DEC Region                  70329 non-null int64
Latitude                    70329 non-null float64
Longitude                   70329 non-null float64
Control Code                70329 non-null object
Control Type                70329 non-null object
OU                          70329 non-null object
Project Name                57930 non-null object
Project Completion Date     70259 non-null object
Waste Name                  42098 non-null object
Contaminants                40756 non-null object
Owner Name                  67350 non-null object
Owner Address1              66690 non-null object
Owner Address2              40318 non-null object
Owner City                  66833 non-null object
Owner State                 67350 non-null object
Owner ZIP                   67350 non-null object
Disposal Name               25132 non-null object
Disposal Address1           6446 non-null object
Disposal Address2           20161 non-null object
Disposal City               6492 non-null object
Disposal ZIP                25179 non-null object
Disposal State              25179 non-null object
Operator Name               48966 non-null object
Operator Address1           46671 non-null object
Operator Address2           42098 non-null object
Operator City               46836 non-null object
Operator State              49001 non-null object
Operator Zip                49001 non-null object
Location 1                  70329 non-null object
NYS Municipal Boundaries    70329 non-null int64
New York Zip Codes          69936 non-null float64
Counties                    70248 non-null float64
dtypes: float64(4), int64(3), object(35)
memory usage: 147.3 MB


DATAFRAME SERIALIZATION REPORT - BY SIZE
========================================

=========================  ==========================  =========================  ===================  =============  ==========================
Serialization File           Serialized DF Size (KBs)    Serialization Speed (s)    Size/Speed (KB/s)   Format Type   Extra Dependencies
=========================  ==========================  =========================  ===================  =============  ==========================
df.brotli.parquet                               1,892                      0.316                5,984     binary      fastparquet, brotli
df.gzip.parquet                                 1,911                      0.421                4,539     binary      fastparquet
df.snappy.parquet                               2,287                      0.212               10,802     binary      fastparquet, python-snappy
df.no-compression.parquet                       2,579                      0.266                9,712     binary      fastparquet
df.gzip.csv                                     5,156                      2.345                2,198      text
df.gzip.json                                   10,150                      6.522                1,556      text
df.no-compression.csv                          30,907                      1.324               23,343      text
df.no-compression.feather                      38,187                      0.155              246,269     binary      pyarrow (100MB+! Ugh!)
df.no-compression.json                         58,880                      0.543              108,470      text
=========================  ==========================  =========================  ===================  =============  ==========================


DATAFRAME SERIALIZATION REPORT - BY SPEED
=========================================

=========================  ==========================  =========================  ===================  =============  ==========================
Serialization File           Serialized DF Size (KBs)    Serialization Speed (s)    Size/Speed (KB/s)   Format Type   Extra Dependencies
=========================  ==========================  =========================  ===================  =============  ==========================
df.no-compression.feather                      38,187                      0.155              246,269     binary      pyarrow (100MB+! Ugh!)
df.snappy.parquet                               2,287                      0.212               10,802     binary      fastparquet, python-snappy
df.no-compression.parquet                       2,579                      0.266                9,712     binary      fastparquet
df.brotli.parquet                               1,892                      0.316                5,984     binary      fastparquet, brotli
df.gzip.parquet                                 1,911                      0.421                4,539     binary      fastparquet
df.no-compression.json                         58,880                      0.543              108,470      text
df.no-compression.csv                          30,907                      1.324               23,343      text
df.gzip.csv                                     5,156                      2.345                2,198      text
df.gzip.json                                   10,150                      6.522                1,556      text
=========================  ==========================  =========================  ===================  =============  ==========================


DATAFRAME SERIALIZATION REPORT - BY SIZE/SPEED
==============================================

=========================  ==========================  =========================  ===================  =============  ==========================
Serialization File           Serialized DF Size (KBs)    Serialization Speed (s)    Size/Speed (KB/s)   Format Type   Extra Dependencies
=========================  ==========================  =========================  ===================  =============  ==========================
df.no-compression.feather                      38,187                      0.155              246,269     binary      pyarrow (100MB+! Ugh!)
df.no-compression.json                         58,880                      0.543              108,470      text
df.no-compression.csv                          30,907                      1.324               23,343      text
df.snappy.parquet                               2,287                      0.212               10,802     binary      fastparquet, python-snappy
df.no-compression.parquet                       2,579                      0.266                9,712     binary      fastparquet
df.brotli.parquet                               1,892                      0.316                5,984     binary      fastparquet, brotli
df.gzip.parquet                                 1,911                      0.421                4,539     binary      fastparquet
df.gzip.csv                                     5,156                      2.345                2,198      text
df.gzip.json                                   10,150                      6.522                1,556      text
=========================  ==========================  =========================  ===================  =============  ==========================
```
