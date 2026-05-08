# GetCenterPoint Method (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetCenterPoint`

Obsolete. Superseded by IRenderMaterial::GetCenterPoint2.
Obsolete. Superseded by [IRenderMaterial::GetCenterPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetCenterPoint2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetCenterPoint( _
   ByRef CenterPt As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim CenterPt As System.Double
 
instance.GetCenterPoint(CenterPt)
```

```

void GetCenterPoint( 
   out System.double CenterPt
)
```

```

void GetCenterPoint( 
   [Out] System.double CenterPt
) 
```

#### Parameters

*CenterPt*
:   Array of doubles (x, y, z) representing the centerpoint of the mapping for texture-based appearances

#### Return Value

Array of doubles (x, y, z) representing the centerpoint of the mapping for texture-based appearances

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::SetCenterPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetCenterPoint.md)
