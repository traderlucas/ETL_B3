import pandas as pd
from datetime import datetime, timedelta


now = datetime.now()
date = now.strftime("%d/%m/%Y")

URLS = {

    "curva_volatilidade_dolar": {
        "id" : "curva_volatilidade_dolar",
        "url": "https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-de-derivativos/precos-referenciais/superficie-de-volatilidade-de-dolar/",
        "df_index": 0
    },
    "liquidacoes_antecipadas_termo": {
        "id" : "liquidacoes_antecipadas_termo",
        "url": "https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/termo/liquidacoes-antecipadas/liquidacoes-antecipadas.htm",
        "df_index": 0
    },
    "posicoes_aberto_termo": {
        "id" : "posicoes_aberto_termo",
        "url": f"https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/termo/posicoes-em-aberto/posicoes-em-aberto-8AA8D0CC77D179750177DF167F150965.htm?data={date}&f=0",
        "df_index": 1
    }
}