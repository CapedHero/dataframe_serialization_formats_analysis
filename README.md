## How to run?

### *nix OS

```bash
# Prepare virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# Run Analysis
python run_analysis_and_print_report.py datasets/**YOUR-CHOSEN-DATASET-IN-CSV-FROMAT**
```

### Docker
```bash
# Build Image
docker build -t dataframe_serialization_formats_analysis .

# Run Container
docker run -it \
  --volume=${PWD}:/dataframe_serialization_formats_analysis \
  dataframe_serialization_formats_analysis \
  python run_analysis_and_print_report.py datasets/**YOUR-CHOSEN-DATASET-IN-CSV-FROMAT**
```

## Looking for some test datasets?

Many great datasets examples can be found on Kaggle:
+ https://www.kaggle.com/datasets


## Report Example

```text
>>> docker run -it \
       --volume=${PWD}:/dataframe_serialization_formats_analysis \
       dataframe_serialization_formats_analysis \
       python run_analysis_and_print_report.py datasets/environmental-remediation-sites.csv


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

=========================  ==========================  =========================  ===================  =============  ===============  ==========================
Serialization File           Serialized DF Size (KBs)    Serialization Speed (s)    Size/Speed (KB/s)   Format Type    Applicability   Extra Dependencies
=========================  ==========================  =========================  ===================  =============  ===============  ==========================
df.brotli.parquet                               1,892                      0.419                4,518     binary           great       fastparquet, brotli
df.gzip.parquet                                 1,911                      0.695                2,751     binary           great       fastparquet
df.snappy.parquet                               2,287                      0.310                7,379     binary           great       fastparquet, python-snappy
df.gzip.pickle                                  2,434                      7.364                  330     binary        ONLY Python
df.no-compression.parquet                       2,579                      0.483                5,341     binary           great       fastparquet
df.gzip.csv                                     5,156                      3.126                1,649      text          universal
df.gzip.json                                   10,150                      7.587                1,338      text          universal
df.no-compression.pickle                       18,931                      0.300               63,113     binary        ONLY Python
df.no-compression.csv                          30,907                      4.128                7,487      text          universal
df.no-compression.feather                      38,187                      0.411               92,800     binary          limited      pyarrow (100MB+! Ugh!)
df.no-compression.json                         58,880                      0.862               68,269      text          universal
=========================  ==========================  =========================  ===================  =============  ===============  ==========================


DATAFRAME SERIALIZATION REPORT - BY SPEED
=========================================

=========================  ==========================  =========================  ===================  =============  ===============  ==========================
Serialization File           Serialized DF Size (KBs)    Serialization Speed (s)    Size/Speed (KB/s)   Format Type    Applicability   Extra Dependencies
=========================  ==========================  =========================  ===================  =============  ===============  ==========================
df.no-compression.pickle                       18,931                      0.300               63,113     binary        ONLY Python
df.snappy.parquet                               2,287                      0.310                7,379     binary           great       fastparquet, python-snappy
df.no-compression.feather                      38,187                      0.411               92,800     binary          limited      pyarrow (100MB+! Ugh!)
df.brotli.parquet                               1,892                      0.419                4,518     binary           great       fastparquet, brotli
df.no-compression.parquet                       2,579                      0.483                5,341     binary           great       fastparquet
df.gzip.parquet                                 1,911                      0.695                2,751     binary           great       fastparquet
df.no-compression.json                         58,880                      0.862               68,269      text          universal
df.gzip.csv                                     5,156                      3.126                1,649      text          universal
df.no-compression.csv                          30,907                      4.128                7,487      text          universal
df.gzip.pickle                                  2,434                      7.364                  330     binary        ONLY Python
df.gzip.json                                   10,150                      7.587                1,338      text          universal
=========================  ==========================  =========================  ===================  =============  ===============  ==========================


DATAFRAME SERIALIZATION REPORT - BY SIZE/SPEED
==============================================

=========================  ==========================  =========================  ===================  =============  ===============  ==========================
Serialization File           Serialized DF Size (KBs)    Serialization Speed (s)    Size/Speed (KB/s)   Format Type    Applicability   Extra Dependencies
=========================  ==========================  =========================  ===================  =============  ===============  ==========================
df.no-compression.feather                      38,187                      0.411               92,800     binary          limited      pyarrow (100MB+! Ugh!)
df.no-compression.json                         58,880                      0.862               68,269      text          universal
df.no-compression.pickle                       18,931                      0.300               63,113     binary        ONLY Python
df.no-compression.csv                          30,907                      4.128                7,487      text          universal
df.snappy.parquet                               2,287                      0.310                7,379     binary           great       fastparquet, python-snappy
df.no-compression.parquet                       2,579                      0.483                5,341     binary           great       fastparquet
df.brotli.parquet                               1,892                      0.419                4,518     binary           great       fastparquet, brotli
df.gzip.parquet                                 1,911                      0.695                2,751     binary           great       fastparquet
df.gzip.csv                                     5,156                      3.126                1,649      text          universal
df.gzip.json                                   10,150                      7.587                1,338      text          universal
df.gzip.pickle                                  2,434                      7.364                  330     binary        ONLY Python
=========================  ==========================  =========================  ===================  =============  ===============  ==========================
```
