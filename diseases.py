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
"""Disease and remedy mapping data for the Crop Disease Diagnosis Agent."""

from typing import TypedDict, List

class DiseaseInfo(TypedDict):
    crop: str
    disease: str
    symptoms: List[str]
    remedy: str

DISEASE_REMEDY_MAPPING: dict[str, DiseaseInfo] = {
    "potato_late_blight": {
        "crop": "Potato",
        "disease": "Late Blight",
        "symptoms": [
            "dark water-soaked spots on leaves",
            "white fungal growth on the underside of leaves in humid conditions",
            "rapidly rotting tubers",
        ],
        "remedy": (
            "Apply copper-based fungicides. Remove and destroy infected plant debris. "
            "Plant resistant potato varieties and ensure good soil drainage."
        ),
    },
    "tomato_black_rot": {
        "crop": "Tomato",
        "disease": "Black Rot",
        "symptoms": [
            "v-shaped yellow spots on leaf margins",
            "blackening leaf veins",
            "dark sunken lesions on the stem or fruit",
        ],
        "remedy": (
            "Use certified pathogen-free seeds. Avoid overhead irrigation to minimize wet foliage. "
            "Apply copper sprays and rotate crops every 2-3 years."
        ),
    },
    "wheat_powdery_mildew": {
        "crop": "Wheat",
        "disease": "Powdery Mildew",
        "symptoms": [
            "white to light gray powdery spots on leaves and stems",
            "yellowing of leaves",
            "premature defoliation in severe cases",
        ],
        "remedy": (
            "Apply systemic fungicides if the disease exceeds economic thresholds. "
            "Use resistant wheat cultivars and manage nitrogen fertilization to avoid dense foliage."
        ),
    },
    "rice_blast": {
        "crop": "Rice",
        "disease": "Rice Blast",
        "symptoms": [
            "diamond-shaped spots on leaves",
        ],
        "remedy": "Use resistant varieties, manage nitrogen fertilization, and apply fungicides."
    },
    "tomato_blight": {
        "crop": "Tomato",
        "disease": "Tomato Blight",
        "symptoms": [
            "dark water-soaked spots on leaves",
        ],
        "remedy": "Remove infected leaves and improve air circulation around plants."
    },
}
