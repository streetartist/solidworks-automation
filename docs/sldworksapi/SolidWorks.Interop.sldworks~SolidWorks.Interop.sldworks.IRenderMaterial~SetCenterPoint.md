# SetCenterPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetCenterPoint`

Obsolete. Superseded by IRenderMaterial::SetCenterPoint2.
Obsolete. Superseded by [IRenderMaterial::SetCenterPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetCenterPoint2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetCenterPoint( _
   ByRef CenterPt As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim CenterPt As System.Double
 
instance.SetCenterPoint(CenterPt)
```

```

void SetCenterPoint( 
   ref System.double CenterPt
)
```

```

void SetCenterPoint( 
   System.double% CenterPt
) 
```

#### Parameters

*CenterPt*
:   Array of doubles (x, y, z) representing the centerpoint of the mapping for texture-based appearances

Remarks

This method is required to properly position a texture-based appearance (e.g., if you need a specific corner of a face to have the black square of a checkered-pattern appearance).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::GetCenterPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetCenterPoint.md)
