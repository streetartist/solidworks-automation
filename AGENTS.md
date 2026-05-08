# AGENTS.md

This repository is a Python wrapper and workflow harness for SOLIDWORKS COM automation. Use it to create, open, refine, save, and export native SOLIDWORKS parts and assemblies through `solidworks_com` scripts.

## Hybrid CAD-to-SOLIDWORKS Workflow

When the user asks for a complex model or complex assembly and does not require a fully traceable native SOLIDWORKS feature tree, use the bundled CAD skill in `D:\agent\text-to-cad-main\text-to-cad-main\.agents\skills\cad\SKILL.md` first to create the initial B-Rep geometry.

Hybrid workflow:

1. Use the CAD skill to create a STEP-first build123d source model.
2. Generate explicit `.step/.stp` output and run the CAD skill inspection checks.
3. Bring the inspected STEP result into the SOLIDWORKS workflow in this repository.
4. Use `solidworks_com` scripts for micro-adjustment, detail cleanup, reference features, mates, final save/export, and deliverables such as `.SLDPRT`, `.SLDASM`, and final `.step`.
5. Keep the build123d source and inspection output as upstream provenance for the imported geometry.

Use this hybrid workflow only when it materially reduces complexity for a complex shape or assembly. The CAD skill produces editable imported solids and selectable faces/edges in SOLIDWORKS, but it does not preserve a SOLIDWORKS-native feature history.

## When Not To Use The CAD-First Step

Do not start with the CAD skill in these cases:

- The user asks for fully traceable SOLIDWORKS modeling steps, a native feature tree, or history that can be replayed and edited feature-by-feature.
- The task is a simple part, ordinary single-body feature model, or non-complex assembly that can be scripted directly with `solidworks_com`.
- The user explicitly says not to use STEP, build123d, the CAD skill, imported solids, or the hybrid workflow.

In those cases, write the SOLIDWORKS automation source directly in this repository and create the model with native SOLIDWORKS sketches, features, mates, and saves through `solidworks_com`.

## Output Policy

- Treat `.SLDPRT` and `.SLDASM` as the final SOLIDWORKS deliverables when requested.
- Treat STEP from the CAD skill as an upstream intermediate unless the user asks for STEP as a final deliverable too.
- Do not hand-edit generated binary CAD outputs. Edit the owning Python source or SOLIDWORKS automation script, then regenerate.
- Report which route was used: direct SOLIDWORKS COM or hybrid CAD-to-SOLIDWORKS.
