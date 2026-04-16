# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Exam Creator** — a Python tool that uses Claude AI to generate customized English language exams. Exams are parameterized by CEFR level (A1–C2) and adaptation requirements.

## Architecture

- `prompts/` — prompt templates with `{level}` and `{adaptation}` placeholders
  - `exam.txt` — main exam generation prompt
  - `writing.txt` — writing task prompt (in progress)
- `utils.py` — shared utility functions

The intended flow: load a prompt template, inject parameters (level, adaptation), call the Claude API, and return the generated exam.

## Development Setup

This project is in early development. There is no package manager config yet. As dependencies are added, document them here.

Expected stack: Python 3, Anthropic SDK (`anthropic`).
