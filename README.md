# Network Traffic Classification using Machine Learning

This repository contains a machine learning implementation for network traffic classification, which can be used for network intrusion detection and traffic pattern analysis. The project implements multiple classification algorithms to compare their effectiveness in identifying different types of network traffic patterns.

## Overview

This project demonstrates the application of various machine learning algorithms to classify network traffic data. It processes network flow data including IP addresses, ports, protocols, and various TCP flags to identify and classify traffic patterns.

### Features

- Data preprocessing of network traffic features
- TCP Flag analysis (ACK, PSH, SYN, FIN, RST)
- Multiple ML algorithm implementations:
  - Naive Bayes
  - K-Nearest Neighbors (with different k values)
  - Decision Trees
  - Random Forest
- Feature importance analysis
- Recursive Feature Elimination with Cross-Validation (RFECV)
- Comprehensive performance metrics including accuracy, precision, and confusion matrices

## Requirements

- Python 3.x
- Required libraries:
  - numpy
  - pandas
  - matplotlib
  - seaborn
  - tensorflow
  - scikit-learn
  - warnings

## Dataset

The script expects a CSV file containing network traffic data with the following features:
- Source IP Address
- Destination IP Address
- Destination Port
- Protocol
- Bytes
- Packets
- TCP Flags
- Label (for classification)

## Implementation Details

### Data Preprocessing
- Converts byte values to numeric format
- Encodes categorical variables
- Splits TCP flags into individual binary features
- Normalizes labels using LabelEncoder

### Machine Learning Models
1. **Naive Bayes**
   - Implements GaussianNB for baseline classification

2. **K-Nearest Neighbors**
   - Tests multiple k values (3 to 15)
   - Evaluates performance metrics for each k value

3. **Decision Trees**
   - Implements basic decision tree classifier
   - Includes feature importance visualization

4. **Random Forest**
   - Uses 250 estimators with max depth of 50
   - Provides comprehensive performance metrics

### Feature Selection
- Implements Recursive Feature Elimination with Cross-Validation
- Identifies most important features for classification
- Provides feature ranking

## Usage

1. Prepare your network traffic data in CSV format
2. Update the file path in the script to point to your data file
3. Run the script to perform the analysis:
   ```python
   python network_traffic_classification.py
   ```

## Results

The script provides:
- Accuracy and precision scores for each algorithm
- Classification reports with detailed metrics
- Confusion matrices for performance evaluation
- Feature importance visualizations
- Cross-validation scores

## Learning Outcomes

This project is excellent for learning:
- Network traffic analysis fundamentals
- Machine learning application in cybersecurity
- Comparison of different classification algorithms
- Feature selection techniques
- Model evaluation metrics
- Data preprocessing for network traffic data

## Future Improvements

- Real-time traffic classification implementation
- Additional machine learning algorithms
- Deep learning model implementation
- Network traffic visualization enhancements
- Model optimization techniques

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
