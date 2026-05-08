# SetWallThickness Method (IRevolveFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~SetWallThickness`

Sets the wall thickness of the thin revolution feature in forward/reverse direction.
Sets the wall thickness of the thin revolution feature in forward/reverse direction.

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

Dim instance As IRevolveFeatureData2
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

Remarks

This method only affects thin features.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)  
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.md)  
[IRevolveFeatureData2::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetWallThickness.md)  
[IRevolveFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IsThinFeature.md)  
[IRevolveFeatureData2::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ThinWallType.md)
