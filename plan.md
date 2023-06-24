# Real-State Scraping Tool
## The starting point will be only real-state in Sao Paulo
### The site that will be initiatly scraped will be: https://www.zapimoveis.com.br/aluguel/imoveis/sp+sao-paulo/?onde=,S%C3%A3o%20Paulo,S%C3%A3o%20Paulo,,,,,city,BR%3ESao%20Paulo%3ENULL%3ESao%20Paulo,-23.555771,-46.639557,&tipo=Im%C3%B3vel%20usado&transacao=Aluguel

The idea is to scrape houses and apartment information, the ingest it to a database, refine it (maybe use some data quality tools) and finaly join it with other information:
* Use maps api, to discover convinience arrow the houses
* Use government data, to discover maybe violence in the area and transportation (could just be google maps)