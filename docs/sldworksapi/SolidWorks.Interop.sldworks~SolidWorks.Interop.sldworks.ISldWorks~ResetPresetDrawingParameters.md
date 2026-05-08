# ResetPresetDrawingParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ResetPresetDrawingParameters`

Resets SOLIDWORKS back to its default behavior after calling ISldWorks::PresetNewDrawingParameters (i.e., display Sheet Format/Size dialog when opening a new drawing document).
Resets SOLIDWORKS back to its default behavior after calling [ISldWorks::PresetNewDrawingParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PresetNewDrawingParameters.md) (i.e., display Sheet Format/Size dialog when opening a new drawing document).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ResetPresetDrawingParameters() 
```

```

Dim instance As ISldWorks
 
instance.ResetPresetDrawingParameters()
```

```

void ResetPresetDrawingParameters()
```

```

void ResetPresetDrawingParameters(); 
```

Example

[Preset and Reset Template and Sheet Parameters for New Drawing Documents (VBA)](Preset_and_Reset_Template_and_Sheet_Parameters_for_New_Drawing_Documents_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
