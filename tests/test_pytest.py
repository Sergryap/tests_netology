import unittest.mock
import pytest
import secretary
from pytest import MarkGenerator
from secretary import remove_doc_from_shelf, check_document_existance, add_new_shelf, \
	append_doc_to_shelf, get_doc_owner_name, get_doc_shelf, add_new_doc


FIXTURE_true_doc_number = [s["number"] for s in secretary.documents]
FIXTURE_false_doc_number = ["2247 876234", "11-7", "10996", "5465 878994", "5488 546687"]
FIXTURE_shelf_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
FIXTURE_doc_number = FIXTURE_true_doc_number + FIXTURE_false_doc_number
FIXTURE_name_doc_number = [(s["number"], s["name"]) for s in secretary.documents] + [(n, None) for n in
                                                                                     FIXTURE_false_doc_number]


@pytest.mark.parametrize("doc_number1", FIXTURE_true_doc_number)
@pytest.mark.parametrize("doc_number2", FIXTURE_false_doc_number)
def test_check_document_existance(doc_number1, doc_number2):
	assert check_document_existance(doc_number1)
	assert not check_document_existance(doc_number2)


@pytest.mark.parametrize("doc_number, name", FIXTURE_name_doc_number)
def test_get_doc_owner_name(doc_number, name):
	with unittest.mock.patch('builtins.input', return_value=doc_number):
		assert get_doc_owner_name() == name


@pytest.mark.parametrize("doc_number", FIXTURE_doc_number)
def test_remove_doc_from_shelf(doc_number):
	remove_doc_from_shelf(doc_number)
	test = True
	for directory_docs_list in secretary.directories.values():
		if doc_number in directory_docs_list:
			test = False
	assert test


@pytest.mark.parametrize("shelf_number", FIXTURE_shelf_number)
def test_add_new_shelf(shelf_number):
	with unittest.mock.patch('builtins.input', return_value=shelf_number):
		add_new_shelf()
		assert shelf_number in secretary.directories.keys()


@pytest.mark.parametrize("doc_number", FIXTURE_doc_number)
@pytest.mark.parametrize("shelf_number", FIXTURE_shelf_number)
def test_append_doc_to_shelf(doc_number, shelf_number):
	append_doc_to_shelf(doc_number, shelf_number)
	assert doc_number in secretary.directories[shelf_number]


@pytest.mark.parametrize("user_doc_number", FIXTURE_true_doc_number)
def test_get_doc_shelf(user_doc_number):
	with unittest.mock.patch('builtins.input', return_value=user_doc_number):
		shelf_number = get_doc_shelf()
		assert user_doc_number in secretary.directories[shelf_number]


@pytest.mark.parametrize("new_doc_shelf_number", FIXTURE_shelf_number)
@pytest.mark.parametrize("new_doc_owner_name", ["Артем Сидоров", "Анатолий Чубайс", "Максим Галкин"])
@pytest.mark.parametrize("new_doc_type", ["passport", "invoice", "insurance"])
@pytest.mark.parametrize("new_doc_number", FIXTURE_doc_number)
def test_add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number):
	add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number)
	new_doc = {
		"type": new_doc_type,
		"number": new_doc_number,
		"name": new_doc_owner_name
	}
	assert new_doc in secretary.documents
	assert new_doc_number in secretary.directories[new_doc_shelf_number]
