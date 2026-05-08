# FeatureCutThicken Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThicken`

Thickens the selected reference surface feature, and then generates a cut.
Thickens the selected reference surface feature, and then generates a cut.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureCutThicken( _
   ByVal Thickness As System.Double, _
   ByVal Direction As System.Integer, _
   ByVal FaceIndex As System.Integer, _
   ByVal FillVolume As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Thickness As System.Double
Dim Direction As System.Integer
Dim FaceIndex As System.Integer
Dim FillVolume As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim value As Feature
 
value = instance.FeatureCutThicken(Thickness, Direction, FaceIndex, FillVolume, UseFeatScope, UseAutoSelect)
```

```

Feature FeatureCutThicken( 
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex,
   System.bool FillVolume,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

```

Feature^ FeatureCutThicken( 
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex,
   System.bool FillVolume,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
) 
```

#### Parameters

*Thickness*
:   Wall thickness

*Direction*
:   - 0 = Thicken side 1
    - 1 = Thicken side 2
    - 2 = Thicken both sides

*FaceIndex*
:   Not currently used

*FillVolume*
:   True to make the solid from a knitted surface, false to not (see **Remarks**)

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect  those bodies, false to select the bodies the feature affects (see Remarks)

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

This method creates a cut feature by thickening a selected reference surface. If FillVolume is True, other arguments are ignored. A closed surface is required when FillVolume is True.

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

When using cut or cavity features that result in multiple bodies, you cannot select to keep all of the resulting bodies or one or more selected bodies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::FeatureCut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCut2.md)  
[IFeatureManager::FeatureCutThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThin.md)  
[IFeatureManager::FeatureBossThicken Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureBossThicken.md)  
[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.md)
