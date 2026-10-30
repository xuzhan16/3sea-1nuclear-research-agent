import unittest

from backend.server.maritime_nuclear import build_maritime_nuclear_task


class MaritimeNuclearTaskTests(unittest.TestCase):
    def test_builds_a_cited_domain_research_task(self):
        task = build_maritime_nuclear_task(
            "比较船用小型模块化反应堆的公开技术路线",
            domain="核能应用",
            vessel_type="商船",
            region="中国与国际规则",
            focus="安全、法规、维护",
        )

        self.assertIn("船用小型模块化反应堆", task)
        self.assertIn("核能应用", task)
        self.assertIn("Technology domain", task)
        self.assertIn("商船", task)
        self.assertIn("中国与国际规则", task)
        self.assertIn("authoritative public sources", task)
        self.assertIn("Do not provide instructions", task)
        self.assertIn("Simplified Chinese", task)

    def test_supports_all_three_domains(self):
        task = build_maritime_nuclear_task(
            "比较不同平台的工程与安全规范",
            domain="综合",
            vessel_type="船舶与海洋平台",
        )

        self.assertIn("船舶与海洋平台", task)
        self.assertIn("Technology domain: 综合", task)
        self.assertIn("船海核", task)

    def test_rejects_an_empty_question(self):
        with self.assertRaises(ValueError):
            build_maritime_nuclear_task("  ")


if __name__ == "__main__":
    unittest.main()
