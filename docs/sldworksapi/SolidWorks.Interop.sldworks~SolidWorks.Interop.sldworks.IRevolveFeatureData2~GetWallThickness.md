# GetWallThickness Method (IRevolveFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetWallThickness`

Gets the wall thickness of the thin revolution feature in forward or reverse direction.
Gets the wall thickness of the thin revolution feature in forward or reverse direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetWallThickness( _
   ByVal Forward As System.Boolean _
) As System.Double
```

```

Dim instance As IRevolveFeatureData2
Dim Forward As System.Boolean
Dim value As System.Double
 
value = instance.GetWallThickness(Forward)
```

```

System.double GetWallThickness( 
   System.bool Forward
)
```

```

System.double GetWallThickness( 
   System.bool Forward
) 
```

#### Parameters

*Forward*
:   True for forward feature direction, false for reverse

#### Return Value

Wall thickness

Remarks

This method only affects thin features.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)  
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.md)  
[IRevolveFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IsThinFeature.md)  
[IRevolveFeatureData2::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~SetWallThickness.md)  
[IRevolveFeatureData2::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ThinWallType.md)
