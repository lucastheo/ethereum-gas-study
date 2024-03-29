from v2__estagios_5_data import LoadCrudeData, Mapping, Filter, Summarize, Plot ,Categorize

def summarize(domain_data , path , filter):
    summarize_data = Mapping.domain_summarize(domain_data)
    value_data = Summarize.get_list_value(summarize_data)
    Plot.graph_value(value_data,path , f'Consumo de gas para função \"{filter}\"', 'Tamanho do array' , 'Gas utilizado')

def summarize_sum( domain_data , path):
    summarize_data = Mapping.domain_summarize(domain_data)
    value_sum_data = Summarize.get_list_sum_value(summarize_data)
    Plot.graph_value(value_sum_data,path , f'Soma dos consumos de gas para função \"{filter}\"', 'Tamanho do array' , 'Gas utilizado')

def categorize(domain_data,path):
    categorize_data = Mapping.domain_categorize(domain_data)
    value_dict_list = Categorize.get_dataset_categorize(categorize_data)
    Plot.graph_subplot(value_dict_list,path, 'Consumo de gas por método' ,'Tamanho do array' , 'Gas utilizado', 'upper left')

def categorize_sum(domain_data,path):
    categorize_data = Mapping.domain_categorize_sum(domain_data)
    value_dict_list = Categorize.get_dataset_categorize(categorize_data)
    Plot.graph_subplot(value_dict_list,path, 'Consumo de gas por método' ,'Tamanho do array' , 'Gas utilizado', 'upper left')

def categorize_normalize(domain_data,path):
    categorize_data = Mapping.domain_categorize(domain_data)
    value_normalize_dict_list = Categorize.get_dataset_categorize_normalize(categorize_data)
    Plot.graph_subplot(value_normalize_dict_list,path, 'Consumo de gas por método normalizado por ciclo' ,'Tamanho do array' , 'Gas utilizado', 'upper left')

'''
    Realiza a orquestração das chamadas de funções para gerar a vizalização
    categorizada dos dados limitado ao max_size.

    domain_data: list de DomainExecution
    path: caminho do arquivo
    max_size: tamanho que vai ser tratados os dados
'''
def categorize_limit_size(domain_data: list,path: str, max_size: int ):
    categorize_data = Mapping.domain_categorize_limite_size( domain_data, max_size )
    value_dict_list = Categorize.get_dataset_categorize( categorize_data )
    Plot.graph_subplot( value_dict_list,path , 'Consumo de gas por método' , 'Tamanho do array' , 'Gas utilizado', 'upper left')

'''
    Realiza a orquestração das chamadas de funções para gerar a vizalização
    sumarizada e categorizada dos dados limitado ao max_size.

    domain_data: list de DomainExecution
    path: caminho do arquivo
    max_size: tamanho que vai ser tratados os dados
'''
def categorize_sum_limit_size(domain_data,path, max_size: int ):
    categorize_data = Mapping.domain_categorize_sum_limite_size( domain_data , max_size )
    value_dict_list = Categorize.get_dataset_categorize( categorize_data )
    Plot.graph_subplot( value_dict_list,path, 'Consumo de gas por método' ,'Tamanho do array' , 'Gas utilizado', 'upper left')

'''
    Realiza a orquestração das chamadas de funções para gerar a vizalização
    nomalizada e categorizada dos dados limitado ao max_size.

    domain_data: list de DomainExecution
    path: caminho do arquivo
    max_size: tamanho que vai ser tratados os dados
'''
def categorize_normalize_limit_size(domain_data,path , max_size: int ):
    categorize_data = Mapping.domain_categorize_limite_size( domain_data, max_size )
    value_normalize_dict_list = Categorize.get_dataset_categorize_normalize( categorize_data )
    Plot.graph_subplot( value_normalize_dict_list , path, 'Consumo de gas por método normalizado por ciclo' ,'Tamanho do array' , 'Gas utilizado', 'upper left' )

load_crude_data = LoadCrudeData('../../results/milestone_3/crude/v2_array' , 123 )
crude_data = load_crude_data.get()

domain_data = Mapping.crude_to_domain(crude_data)

summarize(domain_data,'../../results/milestone_3/generate/v2.2.array.geral.png', 'geral')
summarize_sum(domain_data, '../../results/milestone_3/generate/v2.2.array.geral-sum.png')

categorize(domain_data,'../../results/milestone_3/generate/v2.2.array.subplot.geral.png')
categorize_sum(domain_data,'../../results/milestone_3/generate/v2.2.array.subplot-sum.geral.png')
categorize_normalize(domain_data,'../../results/milestone_3/generate/v2.2.array.subplot-normalize.geral.png')

categorize_limit_size(domain_data,'../../results/milestone_3/generate/v2.2.array.subplot.geral-50.png' , 50 )
categorize_sum_limit_size(domain_data,'../../results/milestone_3/generate/v2.2.array.subplot-sum.geral-50.png', 50 )
categorize_normalize_limit_size(domain_data,'../../results/milestone_3/generate/v2.2.array.subplot-normalize.geral-50.png', 50 )

for filter in {'inserirElemento','contaElemento','percorre','percorreConta'}:
    
    filter_data_inserir_elemento = Filter.domain_filter(domain_data, {filter})
    summarize(filter_data_inserir_elemento,f'../../results/milestone_3/generate/v2.2.array.{filter}.png', filter)
    summarize_sum(filter_data_inserir_elemento, f'../../results/milestone_3/generate/v2.2.array.{filter}-sum.png')

