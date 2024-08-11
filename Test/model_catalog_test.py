import unittest
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from Pipeline.caller.model_catalog import (
    OAI_models, Google_models, Anthropic_models,
    is_oai_model, is_google_model, is_anthropic_model,
    is_valid_model, get_model_enum, get_all_valid_models
)

class TestModelCatalog(unittest.TestCase):
    def test_model_lists(self):
        self.assertIn("gpt-4-turbo", OAI_models.get_model_list())
        self.assertIn("gpt-4o", OAI_models.get_model_list())
        self.assertIn("gpt-4o-mini", OAI_models.get_model_list())
        self.assertIn("gemini-3.5", Google_models.get_model_list())
        self.assertIn("gemini-3.11", Google_models.get_model_list())
        self.assertIn("claude-3-opus-20240229", Anthropic_models.get_model_list())
        self.assertIn("claude-3-sonnet-20240229", Anthropic_models.get_model_list())
        self.assertIn("claude-3-haiku-20240307", Anthropic_models.get_model_list())

    def test_is_model_functions(self):
        self.assertTrue(is_oai_model("gpt-4-turbo"))
        self.assertTrue(is_oai_model("gpt-4o"))
        self.assertTrue(is_oai_model("gpt-4o-mini"))
        self.assertFalse(is_oai_model("gemini-1.5"))
        self.assertFalse(is_oai_model("claude-3-haiku-20240307"))

        self.assertTrue(is_google_model("gemini-3.11"))
        self.assertFalse(is_google_model("gpt-4o"))
        self.assertFalse(is_google_model("claude-3-haiku-20240307"))

        self.assertTrue(is_anthropic_model("claude-3-sonnet-20240229"))
        self.assertTrue(is_anthropic_model("claude-3-haiku-20240307"))
        self.assertFalse(is_anthropic_model("gpt-4-turbo"))
        self.assertFalse(is_anthropic_model("gemini-3.11"))

        self.assertFalse(is_oai_model("000"))
        self.assertFalse(is_google_model("000"))
        self.assertFalse(is_anthropic_model("000"))

        self.assertFalse(is_oai_model(None))
        self.assertFalse(is_google_model(None))
        self.assertFalse(is_anthropic_model(None))

    def test_is_valid_model(self):
        self.assertTrue(is_valid_model("gpt-4-turbo", "oai"))
        self.assertTrue(is_valid_model("gemini-1.5", "google"))
        self.assertTrue(is_valid_model("claude-3-haiku-20240307", "anthropic"))
        self.assertTrue(is_valid_model("gpt-4-turbo", "all"))
        self.assertFalse(is_valid_model("invalid-model", "oai"))
        self.assertFalse(is_valid_model("gpt-4-turbo", "invalid-company"))
        self.assertFalse(is_valid_model("gpt-4-turbo", None))

    def test_get_model_enum(self):
        self.assertEqual(get_model_enum("gpt-4-turbo"), OAI_models.GPT_4)
        self.assertEqual(get_model_enum("gemini-3.5"), Google_models.GEMINI_3_5)
        self.assertEqual(get_model_enum("claude-3-opus-20240229"), Anthropic_models.CLAUDE_3_OPUS)
        self.assertIsNone(get_model_enum("invalid-model"))
        self.assertIsNone(get_model_enum(None))

    def test_get_all_valid_models(self):
        all_models = get_all_valid_models()
        self.assertIn("gpt-4-turbo", all_models)
        self.assertIn("gemini-3.5", all_models)
        self.assertIn("claude-3-sonnet-20240229", all_models)
        self.assertEqual(len(all_models), len(OAI_models) + len(Google_models) + len(Anthropic_models))

if __name__ == '__main__':
    unittest.main()