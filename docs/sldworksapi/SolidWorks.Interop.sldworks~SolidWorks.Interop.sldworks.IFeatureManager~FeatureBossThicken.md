# FeatureBossThicken Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureBossThicken`

Thickens the selected reference surface, and then generates a boss.
Thickens the selected reference surface, and then generates a boss.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureBossThicken( _
   ByVal Thickness As System.Double, _
   ByVal Direction As System.Integer, _
   ByVal FaceIndex As System.Integer, _
   ByVal FillVolume As System.Boolean, _
   ByVal Merge As System.Boolean, _
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
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim value As Feature
 
value = instance.FeatureBossThicken(Thickness, Direction, FaceIndex, FillVolume, Merge, UseFeatScope, UseAutoSelect)
```

```

Feature FeatureBossThicken( 
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex,
   System.bool FillVolume,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

```

Feature^ FeatureBossThicken( 
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex,
   System.bool FillVolume,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
) 
```

#### Parameters

*Thickness*
:   Wall thickness

*Direction*
:   Direction as defined in [swThickenThicknessType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThickenThicknessType_e.html)

*FaceIndex*
:   Not used

*FillVolume*
:   True if you want to make a solid from the knitted surface, false if not (see **Remarks**)

*Merge*
:   True if you want to merge the results in a multibody part, false if not

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects (see **Remarks**)

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

This method generates a boss feature by thickening a selected reference surface.  The surface must be selected with a mark of 1. See [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) for details.

If FillVolume is true, other arguments are ignored. A closed surface is required when FillVolume is true.

If UseAutoSelect is false, the user must select the bodies that the feature will affect.

Example

[Create Thicken Feature (VBA)](Create_Thicken_Feature_Example_VB.htm)  
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)  
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)  
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)  
[Thicken Surface and Generate Boss (VBA)](Thicken_Surface_and_Generate_Boss_Example_VB.htm)  
[Thicken Surface and Generate Boss (VB.NET)](Thicken_Surface_and_Generate_Boss_Example_VBNET.htm)  
[Thicken Surface and Generate Boss (C#)](Thicken_Surface_and_Generate_Boss_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.md)  
[IFeatureManager::FeatureCutThicken Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThicken.md)
