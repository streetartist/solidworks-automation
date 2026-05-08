# GetReferencePointType Method (ISketchPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetReferencePointType`

Gets the type of reference point for this sketch pattern feature.
Gets the type of reference point for this sketch pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReferencePointType() As System.Integer
```

```

Dim instance As ISketchPatternFeatureData
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

Type of reference point:

- -1 = centroid
- 0 = closed curve
- 1 = sketch point
- 2 = vertex

Example

See the [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.md)  
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.md)  
[ISketdhPatternFeatureData::ReferencePoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ReferencePoint.md)
