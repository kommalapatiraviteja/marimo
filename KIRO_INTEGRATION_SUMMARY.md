# Kiro AI Engine Integration for Marimo

## Summary

Successfully added Kiro AI as a supported AI engine in Marimo. This integration allows users to use Kiro AI models through Marimo's AI interface.

## Changes Made

### 1. Configuration Support (`marimo/_server/ai/config.py`)
- Added `for_kiro()` class method to `AnyProviderConfig`
- Configured default base URL: `https://api.kiro.ai/v1/`
- Added support for `KIRO_API_KEY` environment variable
- Added kiro provider case to `for_model()` method

### 2. Provider Implementation (`marimo/_server/ai/providers.py`)
- Created `KiroProvider` class extending `OpenAIClientMixin` and `PydanticProvider`
- Implemented OpenAI-compatible API integration
- Added kiro provider case to `get_completion_provider()` factory function
- Uses OpenAI dependencies for compatibility

### 3. Model ID Support (`marimo/_server/ai/ids.py`)
- Added `is_kiro()` function to detect Kiro models
- Updated `_guess_provider()` to recognize models starting with "kiro"
- Enables automatic provider detection for Kiro models

### 4. Testing
- Created basic integration test to verify all components work together
- Verified configuration, provider instantiation, and model ID parsing

## Usage

Users can now configure Kiro AI in Marimo by:

1. **Environment Variable**: Set `KIRO_API_KEY=your-api-key`
2. **Configuration**: Add kiro section to AI config with api_key
3. **Model Format**: Use `kiro/model-name` or `kiro-model-name`

Example model usage:
- `kiro/kiro-1`
- `kiro/kiro-large`
- `kiro-chat` (auto-detected as kiro provider)

## Files Modified

1. `marimo/_server/ai/config.py` - Added Kiro configuration support
2. `marimo/_server/ai/providers.py` - Added KiroProvider class and factory integration
3. `marimo/_server/ai/ids.py` - Added Kiro model detection logic
4. `test_kiro_integration.py` - Basic integration test (new file)

## Next Steps

To create the PR:

1. Set up GitHub authentication (personal access token or SSH)
2. Push the branch: `git push origin add-kiro-ai-engine`
3. Create PR on GitHub from the `add-kiro-ai-engine` branch
4. Add appropriate labels and description
5. Request review from maintainers

## Technical Notes

- Kiro integration follows the same pattern as other OpenAI-compatible providers
- Uses minimal code approach - only essential functionality added
- Leverages existing OpenAI client infrastructure for compatibility
- No external dependencies required beyond existing marimo dependencies
