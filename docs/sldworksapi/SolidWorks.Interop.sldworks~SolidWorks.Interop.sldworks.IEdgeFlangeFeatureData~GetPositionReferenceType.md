# GetPositionReferenceType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~GetPositionReferenceType`

Gets the position reference type from the edge flange.
Gets the position reference type from the edge flange.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPositionReferenceType() As System.Integer
```

```

Dim instance As IEdgeFlangeFeatureData
Dim value As System.Integer
 
value = instance.GetPositionReferenceType()
```

```

System.int GetPositionReferenceType()
```

```

System.int GetPositionReferenceType(); 
```

#### Return Value

Position reference type as defined in [swSelectionReferenceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectionReferenceTypes_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)  
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.md)  
[IEdgeFlangeFeatureData::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionType.md)  
[IEdgeFlangeFeatureData::UsePositionTrimSideBends Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionTrimSideBends.md)
