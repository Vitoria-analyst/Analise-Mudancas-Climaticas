# Monitoramento Global do Impacto Climático na Saúde (2015-2025)
#
# Grupo:
# Vitória da Conceição Rodrigues - 130557

# ==================================================================
# Importações
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time 

# ==================================================================
# FUNÇÂO: OBTER CAMINHO
def obter_caminho_resultados(nome_arquivo):
    # Diretório do script atual
    pasta_script = os.path.dirname(os.path.abspath(__file__))
    
    # Caminho da pasta 'resultados'
    pasta_resultados = os.path.join(pasta_script, "resultados")
    
    # Cria a pasta se não existir
    if not os.path.exists(pasta_resultados):
        os.makedirs(pasta_resultados)
        print(f"Pasta 'resultados' criada em: {pasta_resultados}")

    return os.path.join(pasta_resultados, nome_arquivo)

# FUNÇÃO: LER DADOS
def ler_dados():
    # 1. Descobrir a pasta onde este script está salvo
    pasta_script = os.path.dirname(os.path.abspath(__file__))

    # 2. Criar o caminho completo para o CSV
    nome_do_arquivo = "global_climate_2015_2025.csv"  
    caminho_completo = os.path.join(pasta_script, nome_do_arquivo)

    try:
        # O pandas lê o caminho exato
        df = pd.read_csv(caminho_completo)
        df["date"] = pd.to_datetime(df["date"])

        print("\nDados carregados com sucesso!")
        print("Registos:", len(df)) 
        print("Colunas:", len(df.columns))
        print("Países disponíveis:", df["country_name"].nunique())
        print("Período:", df["year"].min(), "-", df["year"].max())
        
        
        if df.isnull().sum().sum() == 0:
            print("Integridade verificada: Não existem valores nulos no dataset.")
        else:
            print(f"Aviso: Foram encontrados {df.isnull().sum().sum()} valores nulos.")
        return df

    except FileNotFoundError:
        print(f"ERRO: Ficheiro não encontrado no caminho:\n{caminho_completo}")
        print("DICA: Verifique se o nome do arquivo é exatamente 'global_climate_2015_2025.csv'")
        return None
    
# FUNÇÃO: VISUALIZAR AMOSTRA 
def visualizar_amostra(df, historico):
    # Seleciona apenas as colunas desejadas
    colunas_relevantes = [
        "country_name",
        "temperature_celsius",
        "income_level",
        "population_millions"
    ]

    # Renomeia colunas para cabeçalhos legíveis
    colunas_legiveis = [
        "País",
        "Temp (°C)",
        "Nível Renda",
        "População (M)"
    ]

    # Garante 10 países diferentes e seleciona as colunas
    df_amostra = df.drop_duplicates(subset="country_name").head(10)[colunas_relevantes]

    # Larguras das colunas
    largura = [18, 15, 15, 18]
    margem = "   " # 3 espaços

    # --- IMPRESSÃO DO CABEÇALHO ---
    cabecalho = (
        f"{colunas_legiveis[0]:<{largura[0]}}"  
        f"{colunas_legiveis[1]:>{largura[1]}}" 
        f"{margem}" 
        f"{colunas_legiveis[2]:>{largura[2]}}" 
        f"{colunas_legiveis[3]:>{largura[3]}}"  
    )
    
    print(cabecalho)
    historico.append(cabecalho)

    # Linha de separação
    largura_total = sum(largura) + len(margem)
    print("-" * largura_total)
    historico.append("-" * largura_total)

    # --- IMPRESSÃO DAS LINHAS ---
    for _, linha in df_amostra.iterrows():
        linha_formatada = (
            f"{str(linha['country_name']):<18}"        
            f"{str(linha['temperature_celsius']):>15}" 
            f"{margem}"
            f"{str(linha['income_level']):>15}"        
            f"{str(linha['population_millions']):>18}" 
        )
        print(linha_formatada)
        historico.append(linha_formatada)
 
# FUNÇÃO: PESQUISAR POR PAÍS
def pesquisar_pais(df, historico):
    while True:  
        pais = input("\nDigite o nome do país: ").strip()
        dados = df[df["country_name"].str.contains(pais, case=False)]

        if dados.empty:
            msg = "Nenhum país encontrado!"
            print(msg)
            historico.append(msg)
        else:
            cabecalho = f"\n====== Resultados para {pais} ======="
            print(cabecalho)
            historico.append(cabecalho)

            linha = f"Período: {dados['year'].min()} - {dados['year'].max()}"
            print(linha)
            historico.append(linha)

            linha = f"Temperatura média: {round(dados['temperature_celsius'].mean(), 2)} °C"
            print(linha)
            historico.append(linha)

            linha = f"PM2.5 médio (partículas no ar): {round(dados['pm25_ugm3'].mean(), 2)} µg/m³"
            print(linha)
            historico.append(linha)

            linha = f"AQI médio (qualidade do ar - 0 a 500): {round(dados['air_quality_index'].mean(), 2)}"
            print(linha)
            historico.append(linha)

            linha = f"Doenças respiratórias (média): {round(dados['respiratory_disease_rate'].mean(), 2)}%"
            print(linha)
            historico.append(linha)

            linha = f"Mortalidade cardiovascular (média): {round(dados['cardio_mortality_rate'].mean(), 2)}%"
            print(linha)
            historico.append(linha)

            linha = f"Acesso à saúde (médio): {round(dados['healthcare_access_index'].mean(), 2)}%"
            print(linha)
            historico.append(linha)

        # --- 2. Pergunta se quer continuar ---
        continuar = input("\nDeseja pesquisar outro país? (s/n): ").strip().lower()
        
        if continuar != 's':
            print("\nVoltando ao menu principal...")
            break  # Quebra o ciclo while e a função termina (voltando ao menu)

# FUNÇÃO: ESTATÍSTICAS GERAIS 
def estatisticas(df, historico):
    titulo = "\n================================== ESTATÍSTICAS ================================== "
    print(titulo)
    historico.append(titulo)

    secao1 = "1. DADOS GEOGRÁFICOS"
    print(secao1)
    historico.append(secao1)

    linha = f"Número de países: {df['country_name'].nunique()}"
    print(linha)
    historico.append(linha)

    linha = f"Regiões representadas: {', '.join(df['region'].unique())}"
    print(linha)
    historico.append(linha)

    print()
    historico.append("")

    secao2 = "2. DADOS CLIMÁTICOS"
    print(secao2)
    historico.append(secao2)

    linha = f"Temperatura média global: {round(df['temperature_celsius'].mean(), 2)} °C"
    print(linha)
    historico.append(linha)

    linha = f"Quant. de ondas de calor (média): {round(df['heat_wave_days'].sum()/25, 2)} dias para cada país"
    print(linha)
    historico.append(linha)

    linha = f"PM2.5 global médio (presença de partículas no ar): {round(df['pm25_ugm3'].mean(), 2)} µg/m³"
    print(linha)
    historico.append(linha)

    linha = f"AQI médio global (qualidade do ar de 0 a 500): {round(df['air_quality_index'].mean(), 2)}"
    print(linha)
    historico.append(linha)

    print()
    historico.append("")

    secao3 = "3. DADOS SOCIAIS"
    print(secao3)
    historico.append(secao3)

    linha = f"Média de mortes por doenças respiratórias: {round(df['respiratory_disease_rate'].mean(), 2)}"
    print(linha)
    historico.append(linha)

    linha = f"Média de mortalidade cardiovascular: {round(df['cardio_mortality_rate'].mean(), 2)}"
    print(linha)
    historico.append(linha)

    linha = f"Média global de acesso à saúde: {round(df['healthcare_access_index'].mean(), 2)}"
    print(linha)
    historico.append(linha)

    print()
    historico.append("")

    secao4 = "4. TOP CINCO PAÍSES COM MAIOR:"
    print(secao4)
    historico.append(secao4)

    top_pm25 = "  I. Presença de partículas no ar (PM2.5):"
    print(top_pm25)
    historico.append(top_pm25)
    for pais, valor in df.groupby("country_name")["pm25_ugm3"].mean().sort_values(ascending=False).head(5).items():
        linha = f"{pais}: {valor:.2f}"
        print(linha)
        historico.append(linha)

    top_cardio = "\n  II. Mortalidade cardiovascular (%):"
    print(top_cardio)
    historico.append(top_cardio)
    for pais, valor in df.groupby("country_name")["cardio_mortality_rate"].mean().sort_values(ascending=False).head(5).items():
        linha = f"{pais}: {valor:.2f}"
        print(linha)
        historico.append(linha)

    top_agua = "\n  III. Incidência de doenças transmitidas por água (%):"
    print(top_agua)
    historico.append(top_agua)
    for pais, valor in df.groupby("country_name")["waterborne_disease_incidents"].mean().sort_values(ascending=False).head(5).items():
        linha = f"{pais}: {valor:.2f}"
        print(linha)
        historico.append(linha)

# FUNÇÃO: GUARDAR RESULTADOS EM FICHEIRO
def guardar_resultados(historico):
    if not historico:
        print("Nenhum resultado disponível para salvar. Execute alguma operação primeiro!")
        return

    # Nome do arquivo
    nome_arquivo = "Pesquisa realizada.txt"

    # Obtém o caminho completo já dentro da pasta 'resultados'
    caminho_arquivo = obter_caminho_resultados(nome_arquivo)

    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            for linha in historico:
                f.write(linha + "\n")
        print(f"\n Relatório salvo com sucesso em: \n{caminho_arquivo}")
    except Exception as e:
        print("Erro ao salvar os resultados:", e)

# ==================================================================
# GRÁFICOS
# 1. Temperatura média anual global
def grafico_temperatura_global(df):
    temp_anual = df.groupby("year")["temperature_celsius"].mean()

    plt.figure(figsize=(8,5))
    plt.plot(temp_anual.index, temp_anual.values)
    plt.title("Temperatura Média Global por Ano")
    plt.xlabel("Ano")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True)

    # Salvar gráfico em arquivo PNG
    caminho = obter_caminho_resultados("grafico_temperatura_global.png")
    plt.savefig(caminho, dpi=300, bbox_inches="tight")
    
    plt.show()

# 2. PM2.5 (qualidade do ar) médio por país
def grafico_pm25_por_pais(df):
    print("\nGerar gráfico de evolução da qualidade do ar por país\n")

    # Listar países disponíveis
    print("Países disponíveis:")
    for p in sorted(df["country_name"].unique()):
        print("-", p)

    pais = input("\nDigite o nome do país exatamente como aparece acima: ")

    # Validar país
    if pais not in df["country_name"].unique():
        print("País não encontrado.")
        return

    # Agrupar valores por ano
    dados = (
        df[df["country_name"] == pais]
        .groupby("year")["pm25_ugm3"]
        .mean()
    )

    # Criar gráfico
    plt.figure(figsize=(10,5))
    plt.plot(dados.index, dados.values, marker="o")
    plt.title(f"Evolução da qualidade do ar - {pais}")
    plt.xlabel("Ano")
    plt.ylabel("PM2.5 médio (µg/m³)")
    plt.grid(True)
    plt.tight_layout()

    # Salvar gráfico em arquivo PNG
    caminho = obter_caminho_resultados(f"evolucao_qualidade_do_ar_{pais}.png")
    plt.savefig(caminho, dpi=300, bbox_inches="tight")

    plt.show()

# 3. Doenças respiratórias ao longo do tempo
def barras_doencas_respiratorias(df):
    print("\nGerando gráfico de médias de doenças respiratórias por país...\n")

    # Calcula média por país
    media_resp = df.groupby("country_name")["respiratory_disease_rate"].mean().sort_values(ascending=False)

    plt.figure(figsize=(12,6))
    media_resp.plot(kind="bar", color="red", edgecolor="k")
    plt.title("Média da Taxa de Doenças Respiratórias por País (2015–2025)")
    plt.xlabel("País")
    plt.ylabel("Taxa média de doenças respiratórias")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.subplots_adjust(bottom=0.2)
    plt.figtext(0.5, 0.05,
                "Valores médios da taxa de doenças respiratórias por país de 2015 a 2025.",
                ha="center", fontsize=9)

    # Salvar gráfico em arquivo PNG
    caminho = obter_caminho_resultados("taxas_doencas_respiratórias.png")
    plt.savefig(caminho, dpi=300, bbox_inches="tight")

    plt.show()

# 4. Heatmap temperatura por região e ano
def heatmap_temperatura_regiao(df):
    print("\nGerando Heatmap de Temperatura por Região...\n")

    # Agrupamento: média da temperatura por região e ano
    tabela = df.groupby(["region", "year"])["temperature_celsius"].mean().unstack()

    # Criar gráfica
    plt.figure(figsize=(12, 6))
    sns.heatmap(
        tabela,
        annot=True,          # mostra valores
        fmt=".1f",           # 1 casa decimal
        cmap="coolwarm",     # mapa de cores
        linewidths=.5
    )

    plt.title("Heatmap — Temperatura Média por Região (2015–2025)")
    plt.xlabel("Ano")
    plt.ylabel("Região")
    plt.tight_layout()

    # Salvar gráfico
    caminho = obter_caminho_resultados("heatmap_temperatura_por_regiao.png")
    plt.savefig(caminho, dpi=300, bbox_inches="tight")

    plt.show()

# 5. PIB per Capita × Índice de Saúde Mental
def scatter_pib_saude_mental(df):
    df_media_pais = df.groupby("country_name")[["gdp_per_capita_usd", "mental_health_index"]].mean()

    plt.figure(figsize=(10,6))
    plt.scatter(
        df_media_pais["gdp_per_capita_usd"],
        df_media_pais["mental_health_index"],
        alpha=0.7,
        c="teal",
        edgecolor="k"
    )

    # Adiciona nomes dos países usando iloc
    for i, pais in enumerate(df_media_pais.index):
        plt.text(
            df_media_pais["gdp_per_capita_usd"].iloc[i]+100, 
            df_media_pais["mental_health_index"].iloc[i], 
            pais, 
            fontsize=8
        )

    plt.title("Relação entre PIB per Capita e Índice de Saúde Mental (média por país)")
    plt.xlabel("PIB per Capita (USD)")
    plt.ylabel("Índice de Saúde Mental 0 a 100")
    plt.grid(True)
    plt.tight_layout()

    # Salvar gráfico
    caminho = obter_caminho_resultados("relacao_entre_pib_e_saude_mental.png")
    plt.savefig(caminho, dpi=300, bbox_inches="tight")

    plt.show()
   
# 6. Eventos climáticos extremos por país
def barras_eventos_extremos(df):
    print("\nGerando gráfico de eventos climáticos extremos por país...\n")

    eventos_pais = df.groupby("country_name")["extreme_weather_events"].sum().sort_values(ascending=False)

    plt.figure(figsize=(12,6))
    eventos_pais.plot(kind="bar", color="orange", edgecolor="k")
    plt.title("Eventos Climáticos Extremos por País (2015–2025)")
    plt.xlabel("País")
    plt.ylabel("Número de eventos")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.subplots_adjust(bottom=0.2)

    # Salvar gráfico
    caminho = obter_caminho_resultados("eventos_extremos.png")
    plt.savefig(caminho, dpi=300, bbox_inches="tight")

    plt.show()

# 7. Índice de segurança alimentar por país
def barras_food_security(df):
    print("\nGerando gráfico de índice de segurança alimentar por país...\n")

    food_index = df.groupby("country_name")["food_security_index"].mean().sort_values(ascending=False)

    plt.figure(figsize=(12,6))
    food_index.plot(kind="bar", color="green", edgecolor="k")
    plt.title("Índice de Segurança Alimentar Médio por País (2015–2025)")
    plt.xlabel("País")
    plt.ylabel("Índice de Segurança Alimentar")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.subplots_adjust(bottom=0.2)
    plt.figtext(0.5, 0.05,
                "Valores médios do índice de segurança alimentar de 2015 a 2025 por país.",
                ha="center", fontsize=9)

    # Salvar gráfico
    caminho = obter_caminho_resultados("seguranca_alimentar.png")
    plt.savefig(caminho, dpi=300, bbox_inches="tight")

    plt.show()

# # ========================= MENU PRINCIPAL ========================
historico_resultados = [] # Acumular saídas

def menu():
    df = None

    while True:
        print("\n" * 2) 
        print("""
==============================================
      Observatório do Clima (2015 a 2025)
==============================================
1. Ler dados
2. Visualizar amostra dos dados
3. Pesquisar informações por país
4. Estatísticas gerais
5. Visualizar gráficos
6. Guardar resultados analisados
7. Sair do programa
""")

        opcao = input("Escolha uma opção: ")

        # --- Lógica de Saída (ÚNICA FORMA DE FECHAR) ---
        if opcao == "7":
            print("\nPrograma finalizado!!")
            break  # Sai do loop principal e termina o script

        # --- Opções Funcionais ---
        elif opcao == "1":
            df = ler_dados()

        elif opcao == "2":
            if df is not None:
                visualizar_amostra(df, historico_resultados)
            else:
                print("Carregue os dados primeiro (Opção 1).")

        elif opcao == "3":
            if df is not None:
                pesquisar_pais(df, historico_resultados)
            else:
                print("Carregue os dados primeiro (Opção 1).")

        elif opcao == "4":
            if df is not None:
                estatisticas(df, historico_resultados)
            else:
                print("Carregue os dados primeiro (Opção 1).")

        elif opcao == "5":
            if df is None:
                print("Carregue os dados primeiro (Opção 1).")
            else:
                print("""
   ---- Qual gráfico deseja visualizar? ----
   1. Temperatura global anual
   2. Evolução da qualidade do ar por país
   3. Doenças respiratórias por país
   4. Heatmap temperatura por região e ano
   5. PIB per Capita vs Índice de Saúde Mental
   6. Eventos climáticos extremos por país
   7. Índice de Segurança Alimentar por país
                """)
                g = input("Escolha: ")
                if g == "1": grafico_temperatura_global(df)
                elif g == "2": grafico_pm25_por_pais(df)
                elif g == "3": barras_doencas_respiratorias(df)
                elif g == "4": heatmap_temperatura_regiao(df)
                elif g == "5": scatter_pib_saude_mental(df)
                elif g == "6": barras_eventos_extremos(df)
                elif g == "7": barras_food_security(df)
                else: print("Opção de gráfico inválida.")

        elif opcao == "6":
            if df is not None:
                guardar_resultados(historico_resultados)
            else:
                print("Carregue os dados primeiro (Opção 1).")

        else:
            print("Opção inválida! Escolha um número de 1 a 7.")

        # --- BLOCO DE ESPERA E VALIDAÇÃO ---
        time.sleep(1)
        print("\n-------------------------------------------")
        

        while True:
            voltar = input("\nDigite 's' para voltar ao menu principal: ").strip().lower()
            
            if voltar == 's':
                # Sai deste loop pequeno e volta para o topo do 'while True' grande (Menu)
                break 
            else:
                # Se digitar qualquer outra coisa, avisa e pergunta de novo. O programa não é finalizado.
                print("Entrada inválida! Você precisa digitar 's' para continuar.")


# EXECUÇÃO DO PROGRAMA
menu()
