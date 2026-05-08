# GetDirectionReference Method (IMoveFaceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetDirectionReference`

Gets the direction reference for this Move Face feature.
Gets the direction reference for this Move Face feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDirectionReference( _
   ByRef DirRefType As System.Integer _
) As System.Object
```

```

Dim instance As IMoveFaceFeatureData
Dim DirRefType As System.Integer
Dim value As System.Object
 
value = instance.GetDirectionReference(DirRefType)
```

```

System.object GetDirectionReference( 
   out System.int DirRefType
)
```

```

System.Object^ GetDirectionReference( 
   [Out] System.int DirRefType
) 
```

#### Parameters

*DirRefType*
:   Direction reference type as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

Direction reference:

- If a translated, then a [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), [planar face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [linear edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), or [reference axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)
- If rotated, then a [linear edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) or [reference axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)

Example

[Change Direction Reference of Move Face Feature (VBA)](Change_Direction_Reference_of_Move_Face_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)  
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.md)  
[IMoveFaceFeatureData::SetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetDirectionReference.md)  
[IMoveFaceFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ReverseDirection.md)
