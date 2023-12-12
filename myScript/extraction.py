

def create_extraction_chain(
	schema: dict, llm: BaseLanguageModel, verbose: bool = False
) -> Chain:
	"""Creates a chain that extracts information from a passage.
	Args:
		schema: The schema of the entities to extract.
		llm: The language model to use.
		verbose: Whether to run in verbose mode. In verbose mode, some intermediate
		logs will be printed to the console. Defaults to'langchain.verbose' value.
	Returns:
		Chain that can be used to extract information from a passage.
	"""
	function = _get_extraction_function(schema)
	prompt = ChatPromptTemplate.from_template(_EXTRACTION_TEMPLATE)
	output_parser = JsonKeyOutputFunctionsParser(key_name="info")
	llm_kwargs = get_llm_kwargs(function)
	chain = LLMChain(
		llm=llm,
		prompt=prompt,
		llm_kwargs=llm_kwargs,
		output_parser=output_parser,
		verbose=verbose,
	)
	return chain