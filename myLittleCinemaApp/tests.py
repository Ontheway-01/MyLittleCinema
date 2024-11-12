from datetime import datetime

from django.test import TestCase
from .elasticsearch_client import es, create_document, get_document, update_document, delete_document
from myLittleCinemaApp.document import MovieDocument, Review
from dataclasses import asdict


class ElasticsearchCRUDTest(TestCase):
    index_name = 'test_movies'
    document_id = 1

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        if not es.ping():
            raise Exception("Elasticsearch 서버에 연결할 수 없습니다.")

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        #es.indices.delete(index=cls.index_name, ignore=[400, 404])

    # def test_create_document(self):
    #     review = Review(user="eunhwa813", review="Amazing movie!", rating=5, review_date=datetime.now())
    #
    #     movie = MovieDocument(
    #         title="Inception",
    #         release_date=datetime(2010, 7, 16),
    #         director="Christopher Nolan",
    #         genres=["Sci-Fi", "Thriller"],
    #         reviews=[review]
    #     )
    #     movie_dict = asdict(movie)
    #
    #     create_document(self.index_name, self.document_id, document=movie_dict)
    #     print("create document test success")
    #
    # def test_get_document(self):
    #     doc = get_document(self.index_name, self.document_id)
    #     print(doc)
    #     print("get document test success")
    #
    # def test_update_review(self):
    #     new_review = Review(
    #         user="ontheway813",
    #         review="Great visuals and storytelling.",
    #         rating=4,
    #         review_date=datetime.now()
    #     )
    #     new_review_dict = asdict(new_review)
    #
    #     update_response = update_document(
    #         self.index_name,
    #         self.document_id,
    #         {
    #             "reviews": {
    #                 "script": {
    #                     "source": "ctx._source.reviews.add(params.review)",
    #                     "lang": "painless",
    #                     "params": {
    #                         "review": new_review_dict
    #                     }
    #                 }
    #             }
    #         }
    #     )
    #
    #     self.assertEqual(update_response["result"], "updated")
    #
    #     updated_movie = get_document(self.index_name, self.document_id)
    #     print(updated_movie)
    #     print("update document test success")
    #
    def test_delete_document(self):
        response = delete_document(self.index_name, self.document_id)
        self.assertEqual(response['result'], 'deleted')

        with self.assertRaises(Exception):
            get_document(self.index_name, self.document_id)
        print("delete document test success")
