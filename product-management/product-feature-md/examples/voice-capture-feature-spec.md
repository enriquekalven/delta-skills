# Worked Example: Field Inspection Multimodal Defect Capture (`docs/product-feature.md`)

```yaml
product_vision: FieldLens Hands-Free Substation Defect Capture
user_persona:
  identity: Elena Rostova, Senior High-Voltage Substation Inspector (11 years in utility field operations).
  psychographics: Prioritizes crew safety and regulatory accuracy; hates spending 90 minutes in her truck at the end of every shift re-typing handwritten inspection notes and matching photo filenames.
  context: Inspects 6 outdoor electrical substations per day wearing insulated PPE gloves in high-glare, high-noise environments using a ruggedized tablet strapped to her vest.
problem_statement:
  trigger: Elena spots a hairline porcelain bushing crack and oil weep on a 138kV transformer during a routine walk-around.
  friction: Removing insulated gloves to type asset serial numbers, defect severity codes, and work-order notes into a 7-inch form breaks safety protocol and slows inspection throughput by 40%.
  consequence: Inspectors defer documentation until the end of the shift, resulting in 18% mismatched asset photos and delayed emergency maintenance dispatch.
  why_now: Aging grid infrastructure and stricter FERC/NERC audit rules require timestamped, photo-verified defect records within 15 minutes of visual detection.
ideal_user_journey:
  1: Elena spots an oil weep on Transformer Bank 4 and aims her chest-mounted tablet camera at the asset nameplate and bushing.
  2: She presses a single physical side-button with her gloved hand to start a multimodal capture session.
  3: A short audible tone confirms recording is active as she speaks naturally, describing the oil level drop and hairline crack while panning across the bushing.
  4: She presses the side-button again to finish; the system extracts the nameplate serial number, pins her spoken observations to the exact video keyframes, and matches the failure mode to the utility's NERC defect taxonomy.
  5: An high-contrast summary card appears on screen showing the asset ID, Priority-2 maintenance code, and keyframe photo; Elena confirms with a single voice "Approve" or glove tap.
  6: The maintenance work order is queued immediately for the regional dispatch crew while Elena moves directly to the next bay.
emotional_arc:
  1: Alert (Spotting a potentially hazardous transformer leak in the field).
  2: Unencumbered (Capturing visual and spoken evidence in 20 seconds without removing safety gloves).
  3: Assured (Seeing the exact nameplate ID, annotated photo, and NERC code matched on the high-contrast confirmation card).
  4: Relieved (Finishing the shift at 4:00 PM with zero truck-cab paperwork backlog).
stakeholder_impact:
  end_users: Eliminates 90 minutes of daily post-shift data entry per inspector while keeping hands gloved and eyes on energized equipment.
  google_business: Anchors multimodal Gemini video/audio + Vertex AI field-service workloads across enterprise energy and manufacturing fleets.
  ecosystem_participants:
    knowledge_creators: Senior inspectors effortlessly turn field observations into annotated training cases for junior apprentices.
    skills_creators: Reliability engineers can build downstream diagnostic skills (e.g., thermal-anomaly comparison and replacement part ordering) consuming the standardized capture packet.
    app_developers: SAP EAM and Maximo integrators consume a single validated multimodal defect event instead of building custom voice/photo synchronization pipelines.
```
