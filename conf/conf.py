#### Input and Output files config parameters ####
csv_folder = './csv/examples/test/'
output_docs_folder='./output_docs/'

#### VCF Conversion config parameters ####
allele_counts=False
reference_genome='GRCh37' # Choose one between NCBI36, GRCh37, GRCh38
datasetId='COVID_pop13_ger_1'
case_level_data=True
zygosity=False
num_rows=7000000

### MongoDB parameters ###
database_host = 'mongo'
database_port = 27017
database_user = 'root'
database_password = 'example'
database_name = 'beacon'
database_auth_source = 'admin'
