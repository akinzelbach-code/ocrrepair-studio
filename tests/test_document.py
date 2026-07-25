from app.core.document import Document


def test_new_document_is_empty():
    document = Document()

    assert document.paragraph_count == 0