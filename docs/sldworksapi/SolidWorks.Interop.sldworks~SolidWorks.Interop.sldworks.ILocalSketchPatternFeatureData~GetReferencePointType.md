# GetReferencePointType Method (ILocalSketchPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetReferencePointType`

Gets the type of reference point of this sketch-driven component pattern feature.
Gets the type of reference point of this sketch-driven component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReferencePointType() As System.Integer
```

```

Dim instance As ILocalSketchPatternFeatureData
Dim value As System.Integer
 
value = instance.GetReferencePointType()
```

```

System.int GetReferencePointType()
```

```

System.int GetReferencePointType(); 
```

#### Return Value

Type of reference point as defined in [swLocalSketchPatternReferencePoint\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalSketchPatternReferencePoint_e.html); -1 for default, orgin, or none

Example

[Create Local Sketch-driven Pattern (C#)](Create_Local_Sketch-driven_Pattern_Example_CSharp.htm)  
[Create Local Sketch-driven Pattern (VB.NET)](Create_Local_Sketch-driven_Pattern_Example_VBNET.htm)  
[Create Local Sketch-driven Pattern (VBA)](Create_Local_Sketch-driven_Pattern_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.md)  
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.md)  
[ILocalSketchPatternFeatureData::ReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~ReferencePoint.md)  
[ILocalSketchPatternFeatureData::SelectedPoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~SelectedPoint.md)
