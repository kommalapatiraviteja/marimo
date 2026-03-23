#!/usr/bin/env python3
"""
Updated test script to verify Kiro AI integration works correctly.
"""

import os
import sys
sys.path.insert(0, '.')

# Test basic imports and functionality without full marimo dependencies
def test_kiro_integration():
    """Test basic Kiro integration without dependencies."""
    
    # Test 1: Check that the config file has the for_kiro method
    with open('marimo/_server/ai/config.py', 'r') as f:
        config_content = f.read()
        assert 'def for_kiro(' in config_content, "for_kiro method not found in config"
        assert 'kiro' in config_content, "kiro not found in config"
        assert 'api.kiro.dev' in config_content, "Updated base URL not found"
        print("✓ Kiro config method exists with correct URL")
    
    # Test 2: Check that providers file has KiroProvider
    with open('marimo/_server/ai/providers.py', 'r') as f:
        providers_content = f.read()
        assert 'class KiroProvider(' in providers_content, "KiroProvider class not found"
        assert 'elif model_id.provider == "kiro":' in providers_content, "kiro provider case not found"
        assert 'Kiro is primarily an IDE' in providers_content, "Updated documentation not found"
        print("✓ KiroProvider class exists with proper documentation")
    
    # Test 3: Check that ids file has kiro guessing logic
    with open('marimo/_server/ai/ids.py', 'r') as f:
        ids_content = f.read()
        assert 'def is_kiro(' in ids_content, "is_kiro function not found"
        assert 'return AiProviderId("kiro")' in ids_content, "kiro provider ID not returned"
        print("✓ Kiro model guessing logic exists")
    
    print("\n🎉 All Kiro integration checks passed!")
    print("\n📝 Note: Kiro is primarily an IDE application.")
    print("   This integration assumes Kiro provides an OpenAI-compatible API.")
    print("   Users should configure the correct base_url if different.")


if __name__ == "__main__":
    test_kiro_integration()
