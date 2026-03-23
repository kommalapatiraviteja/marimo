# Add Kiro AI Engine Support

## Description

This PR adds support for Kiro AI as a new AI engine in Marimo, enabling users to leverage Kiro's AI models through Marimo's AI interface.

## Changes

- **Configuration**: Added `for_kiro()` method to support Kiro AI configuration with default base URL and API key handling
- **Provider**: Implemented `KiroProvider` class using OpenAI-compatible API integration
- **Model Detection**: Added automatic detection for models starting with "kiro" prefix
- **Factory Integration**: Added Kiro provider to the completion provider factory

## Usage

Users can now use Kiro AI by:

1. Setting the `KIRO_API_KEY` environment variable
2. Using model format: `kiro/model-name` or `kiro-model-name`
3. Configuring through Marimo's AI settings

Example:
```python
# Model usage examples
"kiro/kiro-1"
"kiro/kiro-large" 
"kiro-chat"  # Auto-detected as kiro provider
```

## Implementation Details

- Follows existing provider patterns for consistency
- Uses OpenAI-compatible API approach for simplicity
- Minimal code footprint - only essential functionality added
- Leverages existing infrastructure and dependencies

## Testing

- Added basic integration test to verify functionality
- Tested configuration, provider instantiation, and model ID parsing
- All existing tests should continue to pass

## Files Changed

- `marimo/_server/ai/config.py` - Kiro configuration support
- `marimo/_server/ai/providers.py` - KiroProvider implementation  
- `marimo/_server/ai/ids.py` - Model detection logic
- `test_kiro_integration.py` - Integration test (new)

## Checklist

- [x] Added Kiro configuration method
- [x] Implemented KiroProvider class
- [x] Added model ID detection logic
- [x] Updated provider factory
- [x] Created integration test
- [x] Followed existing code patterns
- [x] Minimal implementation approach

This change enables Marimo users to access Kiro AI's capabilities while maintaining consistency with the existing AI provider architecture.
