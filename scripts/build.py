"""Gera todos os ativos SVG do perfil.  uso: python scripts/build.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import activity
import hero
import projects
import sections

if __name__ == "__main__":
    for m in (hero, sections, projects, activity):
        m.build()
    print("ativos gerados em assets/")
