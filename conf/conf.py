#### Input and Output files config parameters ####
csv_filename='./csv/output3.csv'
output_docs_folder='./output_docs/'

#### VCF Conversion config parameters ####
num_variants=10000000
allele_frequency=1 # introduce float number, leave 1 if you want to convert all the variants
reference_genome='GRCh38' # Choose one between NCBI36, GRCh37, GRCh38

### MongoDB parameters ###
database_host = 'mongo'
database_port = 27017
database_user = 'root'
database_password = 'example'
database_name = 'beacon'
database_auth_source = 'admin'
