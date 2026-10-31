import unittest

from backend.server.maritime_nuclear import (
    build_maritime_nuclear_task,
    build_maritime_nuclear_role,
)


class MaritimeNuclearTaskTests(unittest.TestCase):
    def test_builds_a_searchable_task(self):
        task = build_maritime_nuclear_task(
            "比较船用小型模块化反应堆的公开技术路线",
            domain="核能应用",
            vessel_type="商船",
            region="中国与国际规则",
            focus="安全、法规、维护",
        )

        self.assertIn("船用小型模块化反应堆", task)
        self.assertIn("核能应用", task)
        self.assertIn("商船", task)
        self.assertIn("中国与国际规则", task)
        # 简洁任务不应包含分析师规则长文
        self.assertNotIn("authoritative public sources", task)
        self.assertNotIn("Do not provide instructions", task)
        self.assertLess(len(task), 200)

    def test_builds_a_cited_domain_role_prompt(self):
        role = build_maritime_nuclear_role(
            "比较船用小型模块化反应堆的公开技术路线",
            domain="核能应用",
            vessel_type="商船",
            region="中国与国际规则",
            focus="安全、法规、维护",
        )

        self.assertIn("船用小型模块化反应堆", role)
        self.assertIn("核能应用", role)
        self.assertIn("Technology domain", role)
        self.assertIn("商船", role)
        self.assertIn("中国与国际规则", role)
        self.assertIn("authoritative public sources", role)
        self.assertIn("Do not provide instructions", role)
        self.assertIn("Simplified Chinese", role)

    def test_role_supports_all_three_domains(self):
        role = build_maritime_nuclear_role(
            "比较不同平台的工程与安全规范",
            domain="综合",
            vessel_type="船舶与海洋平台",
        )

        self.assertIn("船舶与海洋平台", role)
        self.assertIn("Technology domain: 综合", role)
        self.assertIn("船海核", role)

    def test_rejects_an_empty_question(self):
        with self.assertRaises(ValueError):
            build_maritime_nuclear_task("  ")
        with self.assertRaises(ValueError):
            build_maritime_nuclear_role("  ")


if __name__ == "__main__":
    unittest.main()
