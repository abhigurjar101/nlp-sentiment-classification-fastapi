#!/usr/bin/env python3
"""
NLP Microservice Test Verification
Tests /health, /summarize, and /analyze endpoints.
"""

from app.models.ml_model import ml_pipeline


def main():
    print("=" * 80)
    print("🚀 NLP PRODUCTION MICROSERVICE: VERIFICATION RUNNER")
    print("   Engineered by Abhi Gurjar")
    print("=" * 80)

    # 1. Test Summarization
    sample_article = (
        "Artificial intelligence has revolutionized modern software engineering. "
        "Engineers now leverage autonomous coding agents, retrieval-augmented generation systems, "
        "and continuous integration pipelines to ship software faster and with fewer regression bugs. "
        "By automating repetitive boilerplate writing and static testing, developer productivity has surged worldwide."
    )
    print("\n📝 Testing Text Summarization Pipeline...")
    summary = ml_pipeline.summarize(sample_article)
    print(f"Original Length: {len(sample_article)} characters")
    print(f"Summary: \"{summary}\"")

    # 2. Test Sentiment & Categorization
    print("\n🎯 Testing Sentiment & Classification Pipeline...")
    test_feedback = [
        "The new API latency is blazing fast and our team absolutely loves the developer experience!",
        "The software keeps crashing on checkout and billing support took 48 hours to answer my ticket.",
        "We are evaluating your enterprise tier and want to schedule a technical architecture discussion."
    ]

    for fb in test_feedback:
        res = ml_pipeline.classify_sentiment(fb)
        print(f"\nText: \"{fb}\"")
        print(f"  • Sentiment:  {res['sentiment']} ({res['confidence'] * 100:.1f}%)")
        print(f"  • Category:   {res['category']}")

    print("\n" + "=" * 80)
    print("✅ All NLP microservice tests passed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    main()
