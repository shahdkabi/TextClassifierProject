from sklearn.datasets import fetch_20newsgroups


def load_data():
    # Original dataset categories
    raw_categories = ['rec.autos', 'sci.med']
    # Clear names for the API
    clear_names = ['Cars', 'Medical']

    data = fetch_20newsgroups(
        subset='train',
        categories=raw_categories,
        remove=('headers', 'footers', 'quotes')
    )

    texts = data.data[:100]  # first 100 samples
    labels = data.target[:100]  # numeric labels

    return texts, labels, clear_names  # must return 3 values!
