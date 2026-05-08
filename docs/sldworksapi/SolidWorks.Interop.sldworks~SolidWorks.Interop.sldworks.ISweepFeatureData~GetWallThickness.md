# GetWallThickness Method (ISweepFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetWallThickness`

Gets the wall thickness, forward (Direction 1) or reverse (Direction 2), of this thin-walled sweep feature.
Gets the wall thickness, forward (Direction 1) or reverse (Direction 2), of this thin-walled sweep feature.

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

Dim instance As ISweepFeatureData
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
:   True for Direction 1, false for Direction 2

#### Return Value

Wall thickness

Remarks

This method is:

- valid only if [ISweepFeatureData::IsThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsThinFeature.md) is true.
- not valid for swept-surface features.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)  
[ISweepFeatureData::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetWallThickness.md)  
[ISweepFeatureData::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ThinWallType.md)  
[ISweepFeatureData::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsThinFeature.md)
