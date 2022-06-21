import pytest
import secretary
from secretary import documents, directories, remove_doc_from_shelf, check_document_existance

FIXTURE1 = [("2207 876234", "23323"), ("11-2", "23231676"), ("10006", "rerew")]
FIXTURE2 = ['2207 876234', '11-2', '5455 028765', '10006']


def setup():
	pass


def teardown():
	pass


@pytest.mark.parametrize("doc_number1, doc_number2", FIXTURE1)
def test_check_document_existance(doc_number1, doc_number2):
	assert check_document_existance(doc_number1)
	assert not check_document_existance(doc_number2)


@pytest.mark.parametrize("doc_number", FIXTURE2)
def test_remove_doc_from_shelf(doc_number):
	remove_doc_from_shelf(doc_number)
	test = True
	for directory_docs_list in directories.values():
		if doc_number in directory_docs_list:
			test = False
	assert test
