# SetWallThickness Method (ISweepFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetWallThickness`

Sets the wall thickness, forward (Direction 1) or reverse (Direction 2), of this thin-walled sweep feature.
Sets the wall thickness, forward (Direction 1) or reverse (Direction 2), of this thin-walled sweep feature.

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

Dim instance As ISweepFeatureData
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
:   True for Direction 1, false for Direction 2 (see **Remarks**)

*WallThickness*
:   Wall thickness

Remarks

This method:

- is valid only if [ISweepFeatureData::IsThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsThinFeature.md) is true.
- sets the thickness in Direction 1 and Direction 2, depending on [ISweepFeaureData::ThinWallType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ThinWallType.md).
- is not valid for swept-surface features.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)  
[ISweepFeatureData::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsThinFeature.md)  
[ISweepFeatureData::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetWallThickness.md)  
[ISweepFeatureData::ThinFeature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ThinFeature.md)
