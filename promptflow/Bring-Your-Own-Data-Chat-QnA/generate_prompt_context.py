from typing import List
from promptflow import tool
from promptflow_vectordb.core.contracts import SearchResultEntity
import logging
import argparse


arg_parser = argparse.ArgumentParser(description="Argument parser.")
arg_parser.add_argument("--logging_level", type=str, help="logging level")
args, unknown_args = arg_parser.parse_known_args()

logger = logging.getLogger(__name__)



@tool
def generate_prompt_context(search_result: List[dict]) -> str:
    def format_doc(doc: dict):
        return f"Content: {doc['Content']}\nSource: {doc['Source']}"

    logger.info("Test logging")
    #return f"test output: {len(search_result)}"
    SOURCE_KEY = "source"
    URL_KEY = "url"

    retrieved_docs = []
    for item in search_result:
        
        entity = SearchResultEntity.from_dict(item)
       
        content = entity.original_entity['content'] or ""
        source = ""
        if entity.metadata is not None:
            if SOURCE_KEY in entity.metadata:
                if URL_KEY in entity.metadata[SOURCE_KEY]:
                    source = entity.metadata[SOURCE_KEY][URL_KEY] or ""

        retrieved_docs.append({
            "Content": content,
            "Source": source
        })
    doc_string = "\n\n".join([format_doc(doc) for doc in retrieved_docs])
    return doc_string
