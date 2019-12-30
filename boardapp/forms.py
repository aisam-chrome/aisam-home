from typing import List


# 検索フォーム
class Search:
    @staticmethod
    def parse_search_params(words: str) -> List[str]:
        search_words = words.replace('　', ' ').split()
        return search_words