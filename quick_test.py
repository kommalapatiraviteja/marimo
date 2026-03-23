#!/usr/bin/env python3
"""Test Kiro AI integration"""

import os
import sys
sys.path.insert(0, '.')

# Set test environment
os.environ['KIRO_API_KEY'] = 'test-key-123'

try:
    from marimo._server.ai.config import AnyProviderConfig
    from marimo._server.ai.ids import AiModelId
    from marimo._server.ai.providers import get_completion_provider
    
    # Test 1: Model ID parsing
    model_id = AiModelId.from_model("kiro/kiro-1")
    assert model_id.provider == "kiro"
    print("✓ Model parsing works")
    
    # Test 2: Config creation
    config = {"kiro": {"api_key": "test-key"}}
    kiro_config = AnyProviderConfig.for_kiro(config)
    assert "kiro.ai" in kiro_config.base_url
    print("✓ Config works")
    
    # Test 3: Provider creation
    provider = get_completion_provider(kiro_config, "kiro/test")
    assert "KiroProvider" in str(type(provider))
    print("✓ Provider works")
    
    print("\n🎉 All tests passed!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Install dependencies: pip install marimo")
except Exception as e:
    print(f"❌ Test failed: {e}")
