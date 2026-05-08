# SetWallThickness Method (ILoftFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetWallThickness`

Sets the wall thickness for this loft feature in the forward or reverse direction.
Sets the wall thickness for this loft feature in the forward or reverse direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetWallThickness( _
   ByVal Forward As System.Boolean, _
   ByVal WallThickness As System.Double _
) 
```

```

Dim instance As ILoftFeatureData
Dim Forward As System.Boolean
Dim WallThickness As System.Double
 
instance.SetWallThickness(Forward, WallThickness)
```

```

void SetWallThickness( 
   System.bool Forward,
   System.double WallThickness
)
```

```

void SetWallThickness( 
   System.bool Forward,
   System.double WallThickness
) 
```

#### Parameters

*Forward*
:   True for forward feature direction, false for reverse

*WallThickness*
:   Wall thickness

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.md)  
[ILoftFeatureData::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetWallThickness.md)  
[ILoftFeatureData::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IsThinFeature.md)  
[ILoftFeatureData::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ThinWallType.md)
