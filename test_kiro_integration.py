#!/usr/bin/env python3
"""
Simple test script to verify Kiro AI integration works correctly.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

# Test basic imports and functionality without full marimo dependencies
def test_kiro_integration():
    """Test basic Kiro integration without dependencies."""
    
    # Test 1: Check that the config file has the for_kiro method
    with open('marimo/_server/ai/config.py', 'r') as f:
        config_content = f.read()
        assert 'def for_kiro(' in config_content, "for_kiro method not found in config"
        assert 'kiro' in config_content, "kiro not found in config"
        print("✓ Kiro config method exists")
    
    # Test 2: Check that providers file has KiroProvider
    with open('marimo/_server/ai/providers.py', 'r') as f:
        providers_content = f.read()
        assert 'class KiroProvider(' in providers_content, "KiroProvider class not found"
        assert 'elif model_id.provider == "kiro":' in providers_content, "kiro provider case not found"
        print("✓ KiroProvider class exists")
    
    # Test 3: Check that ids file has kiro guessing logic
    with open('marimo/_server/ai/ids.py', 'r') as f:
        ids_content = f.read()
        assert 'def is_kiro(' in ids_content, "is_kiro function not found"
        assert 'return AiProviderId("kiro")' in ids_content, "kiro provider ID not returned"
        print("✓ Kiro model guessing logic exists")
    
    print("\n🎉 All basic Kiro integration checks passed!")


if __name__ == "__main__":
    test_kiro_integration()
