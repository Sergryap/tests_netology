import unittest.mock
import pytest
import secretary
from secretary import delete_doc

FIXTURE_true_doc_number = [s["number"] for s in secretary.documents]
FIXTURE_false_doc_number = ["2247 876234", "11-7", "10996", "5465 878994", "5488 546687"]
FIXTURE_doc_number = FIXTURE_true_doc_number + FIXTURE_false_doc_number


@pytest.mark.parametrize("doc_number", FIXTURE_doc_number)
def test_delete_doc(doc_number):
	with unittest.mock.patch('builtins.input', return_value=doc_number):
		delete_doc()
		test = True
		for document in secretary.documents:
			if document['number'] == doc_number:
				test = False
		for numbers in secretary.directories.values():
			if doc_number in numbers:
				test = False
		assert test