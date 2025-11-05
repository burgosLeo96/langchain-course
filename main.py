from groq.groq import implement_compare_models, implement_set_api_key, check_api_key, implement_llama_4_model, \
    implement_query_model, implement_llama_3_3_model


def main():
    """
    Main function to test your implementations.
    """
    print("🚀 Groq Model Switching Exercise (LangChain Integration)")
    print("=" * 55)
    print("📝 This exercise simulates langchain-groq package behavior!")
    print("🌐 Model names should match console.groq.com exactly")
    print()

    try:
        # Test your set_api_key implementation
        print("🔑 Setting API key...")
        implement_set_api_key("mock_api_key_for_testing")

        # Check if API key was set correctly
        check_api_key()
        print("✓ API key validation working!")

        # Test prompt
        test_prompt = "Explain the concept of machine learning in one sentence."

        # Test your model implementations
        print(f"\n🤖 Testing your Llama 4 implementation:")
        llama4 = implement_llama_4_model()
        response4 = implement_query_model(llama4, test_prompt)
        print(f"Llama 4: {response4}\n")

        print(f"🤖 Testing your Llama 3.3 implementation:")
        llama33 = implement_llama_3_3_model()
        response33 = implement_query_model(llama33, test_prompt)
        print(f"Llama 3.3: {response33}\n")

        # Test your comparison implementation
        print("🔄 Testing your model comparison:")
        comparison = implement_compare_models(test_prompt)
        print("Comparison results:")
        for model, response in comparison.items():
            print(f"  {model}: {response}")

        print("\n🎉 All implementations working!")
        print("✅ Great job implementing the LangChain-Groq patterns!")

    except Exception as e:
        print(f"❌ Error: {e}")
        if "GROQ_API_KEY" in str(e):
            print("\n💡 Check your implement_set_api_key() function!")
        else:
            print("📝 Check your function implementations!")
            print("🌐 Verify model names match console.groq.com exactly")


if __name__ == "__main__":
    main()
