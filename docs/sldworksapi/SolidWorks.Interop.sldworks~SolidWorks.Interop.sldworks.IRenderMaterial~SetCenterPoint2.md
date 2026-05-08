# SetCenterPoint2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetCenterPoint2`

Sets the center point of the mapping for texture-based appearances.
Sets the center point of the mapping for texture-based appearances.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetCenterPoint2( _
   ByVal CenterPt_X As System.Double, _
   ByVal CenterPt_Y As System.Double, _
   ByVal CenterPt_Z As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim CenterPt_X As System.Double
Dim CenterPt_Y As System.Double
Dim CenterPt_Z As System.Double
 
instance.SetCenterPoint2(CenterPt_X, CenterPt_Y, CenterPt_Z)
```

```

void SetCenterPoint2( 
   System.double CenterPt_X,
   System.double CenterPt_Y,
   System.double CenterPt_Z
)
```

```

void SetCenterPoint2( 
   System.double CenterPt_X,
   System.double CenterPt_Y,
   System.double CenterPt_Z
) 
```

#### Parameters

*CenterPt\_X*
:   X coordinate of the center point

*CenterPt\_Y*
:   Y coordinate of the center point

*CenterPt\_Z*
:   Z coordinate of the center point

Remarks

This method is required to properly position a texture-based appearance (e.g., if you need a specific corner of a face to have the black square of a checkered-pattern appearance).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::GetCenterPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetCenterPoint2.md)
