from .category import Category
from .topic import Topic
from .document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for category in self.categories:
            if category.id == category_id:
                category.name = new_name
                break

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.topic = new_topic
                topic.storage_folder = new_storage_folder
                break

    def edit_document(self, document_id: int, new_file_name: str):
        for document in self.documents:
            if document.id == document_id:
                document.file_name = new_file_name
                break

    def delete_category(self, category_id: int):
        for x in range(len(self.categories)):
            if self.categories[x].id == category_id:
                self.categories.pop(x)
                break

    def delete_topic(self, topic_id: int):
        for x in range(len(self.topics)):
            if self.topics[x].id == topic_id:
                self.topics.pop(x)
                break

    def delete_document(self, document_id: int):
        for x in range(len(self.documents)):
            if self.documents[x].id == document_id:
                self.documents.pop(x)
                break

    def get_document(self, document_id: int):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        return '\n'.join([str(doc) for doc in self.documents])
