# BloomFilter_Analysis
Implemented for Concepts of Data Science Project 2025-2026.

### Team Members
- Longkong Rawlings Kamta 240785
- Ihame Gilbert 2504417

---

# Project Overview

This project implements a Bloom Filter in Python using an object-oriented approach.  
The Bloom Filter is a probabilistic data structure designed for efficient membership testing with minimal memory usage.

The project includes:

- Core Bloom Filter implementation
- Hash family generation
- Correctness testing
- Performance benchmarking
- False positive analysis
- Compression analysis
- HPC benchmarking experiments

---

## Implemented Features

### Hash Function Generation

The hashing module generates multiple deterministic hash positions for a given element.

Implemented functionality:

- Generation of k hash positions
- Deterministic hashing behavior
- Position mapping within filter bounds
- Support for multiple hash functions

### Bloom Filter Implementation

Current Bloom Filter functionality includes:

- Bloom Filter initialization
- Bit-array management
- Element insertion
- Membership queries
- Configurable filter size
- Configurable number of hash functions

### Unit Testing

Pytest is used to verify correctness.

#### Hashing Tests

- Correct number of generated positions
- Position bounds validation
- Deterministic hashing verification
- Different inputs produce different positions

#### Bloom Filter Tests

- Bloom Filter initialization
- Element insertion
- Membership checking
- General correctness validation

---

## Planned Analysis

### Performance Benchmarking

Measure:

- Insertion speed
- Query speed
- Scalability with increasing dataset sizes

### False Positive Analysis

Evaluate:

- False positive rate
- Impact of filter size
- Impact of number of hash functions

### Compression Analysis

Investigate:

- Memory efficiency
- Storage requirements
- Compression opportunities

### HPC Experiments

High-performance computing experiments will explore:

- Parallel execution
- Scalability on larger datasets
- Runtime optimization

---
## Environment Setup

Create the Conda environment:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate bloomfilter_analysis
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Run hashing tests only:

```bash
pytest tests/test_hashing.py
```

Run Bloom Filter tests only:

```bash
pytest tests/test_bloom.py
```

---