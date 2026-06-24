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
"""Tools for the Crop Disease Diagnosis Agent."""

from app.diseases import DISEASE_REMEDY_MAPPING


def get_remedy(disease_name: str) -> str:
    """Retrieve the recommended remedy, crop type and formal name for a given disease identifier.

    Args:
        disease_name: The identifier of the disease (e.g., 'potato_late_blight', 'tomato_black_rot', or 'wheat_powdery_mildew').

    Returns:
        A detailed string describing the crop, disease, and recommended remedy.
    """
    key = disease_name.lower().strip().replace(" ", "_")
    if key in DISEASE_REMEDY_MAPPING:
        info = DISEASE_REMEDY_MAPPING[key]
        return (
            f"Crop: {info['crop']}\n"
            f"Disease: {info['disease']}\n"
            f"Remedy: {info['remedy']}"
        )
    return f"Disease '{disease_name}' not found. Please use list_diseases to see available diseases."

def diagnose_by_symptoms(symptoms: str) -> str:
    """Diagnose a disease based on the plant symptoms provided.

    Args:
        symptoms: A string describing the symptoms observed on the plant (e.g. 'yellow spots', 'powdery', 'rotting').

    Returns:
        A recommendation of possible diseases that match the description.
    """
    symptoms_lower = symptoms.lower().strip()
    matches = []
    for key, info in DISEASE_REMEDY_MAPPING.items():
        # Match if the query contains the crop name, disease name, or has any overlap with symptoms
        crop_match = info["crop"].lower() in symptoms_lower
        disease_match = info["disease"].lower() in symptoms_lower
        symptom_match = any(symptoms_lower in s or s in symptoms_lower for s in info["symptoms"])
        
        if crop_match or disease_match or symptom_match:
            matches.append(key)
    
    if not matches:
        return "No specific disease matching those symptoms was found in our database."
    
    response = "Based on the symptoms provided, the following matching diseases were found:\n"
    for m in matches:
        info = DISEASE_REMEDY_MAPPING[m]
        response += f"- {info['crop']} - {info['disease']} (ID: {m})\n"
    response += "\nTo get specific remedies for any of these, use the get_remedy tool with the disease ID."
    return response

def list_diseases() -> list[str]:
    """List all the supported diseases in the database.

    Returns:
        A list of disease identifiers that can be looked up.
    """
    return list(DISEASE_REMEDY_MAPPING.keys())

def find_diseases_by_crop(crop_name: str) -> list[str]:
    """Find diseases that affect a specific crop.

    Args:
        crop_name: The name of the crop (e.g. 'potato', 'tomato', 'wheat', 'rice').

    Returns:
        A list of disease identifiers/IDs matching the crop name.
    """
    crop_lower = crop_name.lower().strip()
    return [
        key
        for key, info in DISEASE_REMEDY_MAPPING.items()
        if info["crop"].lower() == crop_lower
    ]