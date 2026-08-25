---

# 🗺️ Google Maps Scraper

Este projeto realiza **web scraping no Google Maps** para coletar informações detalhadas sobre locais de interesse. Embora o exemplo esteja configurado para buscar **quadras em Curitiba**, o mesmo código pode ser facilmente adaptado para diferentes tipos de buscas, como **empresas, restaurantes, academias, escolas** e muito mais.

### 🚀 Funcionalidades
- Pesquisa automática de locais no Google Maps.  
- Extração de informações como:  
  - Nome da empresa/local  
  - Endereço  
  - Telefone  
  - Website  
  - Descrição  
  - Avaliações e notas  
  - Plus Code  
  - URL da imagem de capa  
  - Acessibilidade  
- Paginação e rolagem automática para coletar múltiplos resultados.  
- Salvamento dos dados em arquivo **CSV** (`"companies_data_ctba.csv"`).  
- Registro detalhado do processo em arquivo de **log** (`"process_log_ctba.log"`).  

### 🛠️ Tecnologias utilizadas
- `"Python 3"`  
- `"Selenium WebDriver"` (com ChromeDriver Manager)  
- `"BeautifulSoup4"`  
- `"CSV"`  
- `"Logging"`  

### 📂 Estrutura do projeto
- `"driver.get()"`: Define a URL de busca no Google Maps (pode ser alterada para qualquer cidade ou tipo de local).  
- `"scroll"`: Rolagem automática para carregar mais resultados.  
- `"collect"`: Extração de dados de cada local.  
- `"save_to_csv()"`: Exporta os dados coletados para um arquivo CSV.  
- `"logging"`: Registra cada etapa do processo e possíveis erros.  

### ⚙️ Como executar
1. Clone este repositório:
   ```bash
   "git clone https://github.com/seuusuario/google-maps-scraper.git"
   ```
2. Instale as dependências:
   ```bash
   "pip install -r requirements.txt"
   ```
   *(Certifique-se de incluir `"selenium"`, `"beautifulsoup4"`, `"webdriver-manager"` no `requirements.txt`.)*  
3. Ajuste a URL de busca no código para o que deseja coletar:
   ```python
   "driver.get('https://www.google.com.br/maps/search/curitiba+quadras/')"
   ```
   Exemplos de outras buscas:
   - `"https://www.google.com.br/maps/search/restaurantes+curitiba/"`  
   - `"https://www.google.com.br/maps/search/empresas+joinville/"`  
   - `"https://www.google.com.br/maps/search/academias+são+josé+dos+pinhais/"`  
4. Execute o script:
   ```bash
   "python main.py"
   ```
5. Os resultados serão salvos em `"companies_data_ctba.csv"`.  

### 📊 Exemplo de saída
```csv
"Company","Description","Phone","Address","Website","Total reviews","Rate reviews","Plus code","Image url","Accessibility"
"Quadra Esportiva X","","(41) 99999-9999","Rua das Flores, Curitiba","www.quadraX.com","120","4.5","J9P2+X5 Curitiba","https://maps.gstatic.com/...","true"
"Academia Y","Musculação e esportes","(41) 98888-8888","Av. Brasil, Curitiba","","85","4.2","J9P3+Y6 Curitiba","","false"
```

### ⚠️ Observações
- O Google Maps pode alterar sua estrutura de HTML, o que pode exigir ajustes no código.  
- O uso excessivo de scraping pode levar a bloqueios temporários. Recomenda-se adicionar **delays** ou técnicas de **rotacionamento de IP** para evitar restrições.  
- Este projeto é apenas para fins educacionais e de aprendizado.  

---
