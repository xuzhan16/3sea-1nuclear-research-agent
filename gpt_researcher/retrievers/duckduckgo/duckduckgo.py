import os
import time
from itertools import islice
from ..utils import check_pkg


class Duckduckgo:
    """
    Duckduckgo API Retriever
    """
    def __init__(self, query, query_domains=None):
        check_pkg('ddgs')
        from ddgs import DDGS
        # ddgs 不读取 HTTP(S)_PROXY 环境变量，需显式传入（国内访问 DuckDuckGo 需要代理）
        proxy = os.getenv("HTTPS_PROXY") or os.getenv("https_proxy") or os.getenv("HTTP_PROXY")
        self.ddg = DDGS(proxy=proxy) if proxy else DDGS()
        self.query = query
        self.query_domains = query_domains or None

    def search(self, max_results=5):
        """
        Performs the search
        :param query:
        :param max_results:
        :return:
        """
        # TODO: Add support for query domains
        # DuckDuckGo 对机房 IP 会间歇性限流：空结果时重试（最多 3 次，间隔递增）
        search_response = []
        for attempt in range(3):
            try:
                search_response = list(self.ddg.text(self.query, region='wt-wt', max_results=max_results))
            except Exception as e:
                print(f"Error: {e}. Failed fetching sources. Retrying ({attempt + 1}/3).")
                search_response = []
            if search_response:
                return search_response
            time.sleep(1.5 * (attempt + 1))
        print(f"Warning: Duckduckgo returned no results after 3 attempts for query: {self.query[:80]}")
        return []
