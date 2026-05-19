from tools.open_library import search_book, search_author_id, search_author_works

def test_found():
    result = search_book("Dune")
    assert result["status"] == "found"
    assert "Frank Herbert" in result["authors"]

def test_not_found():
    result = search_book("xyzzy_this_does_not_exist_99")
    assert result["status"] == "not_found"

def test_author_id():
    result = search_author_id("J.R.R. Tolkien")
    assert result == "OL26320A"

def test_author_works():
    result = search_author_works("OL26320A")
    assert isinstance(result["works"], list)
    assert len(result["works"]) > 0
    assert result is not None 

def test_invalid_author_id():
    result = search_author_works("OL00000000A")
    assert result["status"] in ("not_found", "error")

def test_empty_string():
    result = search_author_works("")
    assert result["status"] in ("not_found", "error")

