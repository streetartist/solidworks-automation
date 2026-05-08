# GetCenterPoint2 Method (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetCenterPoint2`

Gets the center point of the mapping for texture-based appearances.
Gets the center point of the mapping for texture-based appearances.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetCenterPoint2( _
   ByRef CenterPt_X As System.Double, _
   ByRef CenterPt_Y As System.Double, _
   ByRef CenterPt_Z As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim CenterPt_X As System.Double
Dim CenterPt_Y As System.Double
Dim CenterPt_Z As System.Double
 
instance.GetCenterPoint2(CenterPt_X, CenterPt_Y, CenterPt_Z)
```

```

void GetCenterPoint2( 
   out System.double CenterPt_X,
   out System.double CenterPt_Y,
   out System.double CenterPt_Z
)
```

```

void GetCenterPoint2( 
   [Out] System.double CenterPt_X,
   [Out] System.double CenterPt_Y,
   [Out] System.double CenterPt_Z
) 
```

#### Parameters

*CenterPt\_X*
:   X coordinate of the center point

*CenterPt\_Y*
:   Y coordinate of the center point

*CenterPt\_Z*
:   Z coordinate of the center point

Example

See [IRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::SetCenterPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetCenterPoint2.md)
