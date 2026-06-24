# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import google.auth
from google.auth.exceptions import DefaultCredentialsError

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

# Gracefully initialize Google Cloud credentials or fall back for offline/testing mode.
try:
    _, project_id = google.auth.default()
    os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
    os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
except (DefaultCredentialsError, Exception):
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", "mock-project-id")
    os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"


class CropDiseaseAgent(Agent):
    """An AI agent designed to diagnose crop diseases and provide remedies."""

    def __init__(self, **kwargs):
        if "name" not in kwargs:
            kwargs["name"] = "crop_disease_agent"
        if "instruction" not in kwargs:
            kwargs["instruction"] = (
                "You are an AI agricultural assistant specializing in crop disease diagnosis and remedies. "
                "Use your tools to diagnose diseases from plant symptoms and recommend remedies."
            )
        if "model" not in kwargs:
            kwargs["model"] = Gemini(
                model="gemini-flash-latest",
                retry_options=types.HttpRetryOptions(attempts=3),
            )
        if "tools" not in kwargs:
            from app.tools import get_remedy, diagnose_by_symptoms, list_diseases, find_diseases_by_crop
            kwargs["tools"] = [get_remedy, diagnose_by_symptoms, list_diseases, find_diseases_by_crop]
        super().__init__(**kwargs)


# Instantiate the root agent
root_agent = CropDiseaseAgent()

# Create the ADK App
app = App(
    root_agent=root_agent,
    name="crop-disease-app",
)

if __name__ == "__main__":
    print("==================================================")
    print("Crop Disease Diagnosis Agent - Terminal Interface")
    print("==================================================")
    print("Available Commands/Tools:")
    print("  1. List Supported Diseases")
    print("  2. Diagnose Symptoms")
    print("  3. Get Remedy for a Disease")
    print("  4. Find Diseases by Crop")
    print("  5. Exit")
    print("==================================================")
    
    from app.tools import list_diseases, diagnose_by_symptoms, get_remedy, find_diseases_by_crop
    
    # We will simulate a user interaction loop in the terminal
    while True:
        try:
            choice = input("\nSelect an option (1-5): ").strip()
            if choice == "1":
                print("\nSupported Diseases:")
                for d in list_diseases():
                    print(f"  - {d}")
            elif choice == "2":
                symptoms = input("Enter plant symptoms: ").strip()
                print("\nDiagnosis Result:")
                print(diagnose_by_symptoms(symptoms))
            elif choice == "3":
                disease = input("Enter disease name/ID (e.g., potato_late_blight): ").strip()
                print("\nRemedy Details:")
                print(get_remedy(disease))
            elif choice == "4":
                crop = input("Enter crop name (e.g., Potato): ").strip()
                print(f"\nDiseases affecting '{crop}':")
                matches = find_diseases_by_crop(crop)
                if matches:
                    for m in matches:
                        print(f"  - {m}")
                else:
                    print("  No matching diseases found for this crop.")
            elif choice == "5" or choice.lower() == "exit":
                print("Exiting. Keep your crops healthy!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

