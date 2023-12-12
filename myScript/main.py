import asyncio
import pprint
from ai_extractor import extract
from schemas import SchemaNewsWebsites, ecommerce_schema 
from scrape import ascrape_playwright
# TESTING
if __name__ == "__main__":
	token_limit = 4000
	
	cnn_url = "https://www.cnn.com"
	ecommerce_url ="https://appsumo.com"
	wsj_url = "https://www.wsj.com"
	async def scrape_with_playwright(url: str, **kwargs):
		html_content = await ascrape_playwright(url)
		print("Extracting content with LLM")
		html_content_fits_context_window_llm = html_content[:token_limit]
		extracted_content = extract(**kwargs,
									content=html_content_fits_context_window_llm)
		pprint.pprint(extracted_content)
	# Scrape and Extract with LLM 
	asyncio.run(scrape_with_playwright(
	url=wsj_url,
	schema_pydantic=SchemaNewsWebsites,
	#schema=ecommerce_schema
	))