# 🧠 Mee AI Cognitive Architecture

This document describes the architectural layers of Mee AI as a localized cognitive engine for Linux-based systems.

## 1. Data Ingestion Layer (`baca_pdf.py`)
Parses unstructured static knowledge from documents (e.g., `data.pdf`) into machine-readable structures without external API calls.

## 2. Learning & Optimization Layer (`latih_otak.py`)
Handles local weight adjustments and contextual indexing, ensuring the system evolves within the local environment.

## 3. Core Execution Layer (`app.py`)
The central orchestrator that manages communication between the user input and the cognitive datasets.

## 4. Resource Management
Designed for low-overhead operation, making it suitable for integration into Linux distributions as a background service (Daemon).
