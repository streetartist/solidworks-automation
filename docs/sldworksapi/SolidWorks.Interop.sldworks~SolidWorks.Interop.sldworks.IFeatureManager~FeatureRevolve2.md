# FeatureRevolve2 Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve2`

Creates a base-, boss-, or cut-revolve feature.
Creates a base-, boss-, or cut-revolve feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureRevolve2( _
   ByVal SingleDir As System.Boolean, _
   ByVal IsSolid As System.Boolean, _
   ByVal IsThin As System.Boolean, _
   ByVal IsCut As System.Boolean, _
   ByVal ReverseDir As System.Boolean, _
   ByVal BothDirectionUpToSameEntity As System.Boolean, _
   ByVal Dir1Type As System.Integer, _
   ByVal Dir2Type As System.Integer, _
   ByVal Dir1Angle As System.Double, _
   ByVal Dir2Angle As System.Double, _
   ByVal OffsetReverse1 As System.Boolean, _
   ByVal OffsetReverse2 As System.Boolean, _
   ByVal OffsetDistance1 As System.Double, _
   ByVal OffsetDistance2 As System.Double, _
   ByVal ThinType As System.Integer, _
   ByVal ThinThickness1 As System.Double, _
   ByVal ThinThickness2 As System.Double, _
   ByVal Merge As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim SingleDir As System.Boolean
Dim IsSolid As System.Boolean
Dim IsThin As System.Boolean
Dim IsCut As System.Boolean
Dim ReverseDir As System.Boolean
Dim BothDirectionUpToSameEntity As System.Boolean
Dim Dir1Type As System.Integer
Dim Dir2Type As System.Integer
Dim Dir1Angle As System.Double
Dim Dir2Angle As System.Double
Dim OffsetReverse1 As System.Boolean
Dim OffsetReverse2 As System.Boolean
Dim OffsetDistance1 As System.Double
Dim OffsetDistance2 As System.Double
Dim ThinType As System.Integer
Dim ThinThickness1 As System.Double
Dim ThinThickness2 As System.Double
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim value As Feature
 
value = instance.FeatureRevolve2(SingleDir, IsSolid, IsThin, IsCut, ReverseDir, BothDirectionUpToSameEntity, Dir1Type, Dir2Type, Dir1Angle, Dir2Angle, OffsetReverse1, OffsetReverse2, OffsetDistance1, OffsetDistance2, ThinType, ThinThickness1, ThinThickness2, Merge, UseFeatScope, UseAutoSelect)
```

```

Feature FeatureRevolve2( 
   System.bool SingleDir,
   System.bool IsSolid,
   System.bool IsThin,
   System.bool IsCut,
   System.bool ReverseDir,
   System.bool BothDirectionUpToSameEntity,
   System.int Dir1Type,
   System.int Dir2Type,
   System.double Dir1Angle,
   System.double Dir2Angle,
   System.bool OffsetReverse1,
   System.bool OffsetReverse2,
   System.double OffsetDistance1,
   System.double OffsetDistance2,
   System.int ThinType,
   System.double ThinThickness1,
   System.double ThinThickness2,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

```

Feature^ FeatureRevolve2( 
   System.bool SingleDir,
   System.bool IsSolid,
   System.bool IsThin,
   System.bool IsCut,
   System.bool ReverseDir,
   System.bool BothDirectionUpToSameEntity,
   System.int Dir1Type,
   System.int Dir2Type,
   System.double Dir1Angle,
   System.double Dir2Angle,
   System.bool OffsetReverse1,
   System.bool OffsetReverse2,
   System.double OffsetDistance1,
   System.double OffsetDistance2,
   System.int ThinType,
   System.double ThinThickness1,
   System.double ThinThickness2,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
) 
```

#### Parameters

*SingleDir*
:   True if the revolve is in one direction, false if in two directions (see **Remarks**)

*IsSolid*
:   True if this is a solid revolve feature, false if not

*IsThin*
:   True if this is a thin revolve feature, false if not

*IsCut*
:   True if this is a cut revolve feature, false if not

*ReverseDir*
:   True reverses the angle of the revolution, false does not; only applies if Dir1Type is not swEndConditions\_e.swEndCondMidPlane

*BothDirectionUpToSameEntity*
:   True if the revolve is up to the same entity in both directions, false if not; only applies if SingleDir is false and Dir1Type and Dir2Type are swEndConditions\_e.swEndCondUpToVertex, swEndConditions\_e.swEndCondUpToSurface, or swEndConditions\_e.swEndCondOffsetFromSurface) (see **Remarks**)

*Dir1Type*
:   Revolve end condition as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html)

*Dir2Type*
:   Revolve end condition in direction 2; as defined in swEndConditions\_e and only applies if Dir1Type is not swEndConditions\_e.swEndCondMidPlane

*Dir1Angle*
:   Angle in radians of revolution in direction 1; only applies if Dir1Type is swEndConditions\_e.swEndCondBlind

*Dir2Angle*
:   Angle in radians of revolution in direction 2; only applies if Dir2Type is swEndConditions\_e.swEndCondBlind

*OffsetReverse1*
:   True to reverse the offset direction in direction 1, false to not; only applies if Dir1Type is swEndConditions\_e.swEndCondOffsetFromSurface

*OffsetReverse2*
:   True to reverse the offset direction in direction 2, false to not; only applies if Dir2Type is swEndConditions\_e.swEndCondOffsetFromSurface

*OffsetDistance1*
:   Offset distance in direction 1; only applies if Dir1Type is swEndConditions\_e.swEndCondOffsetFromSurface

*OffsetDistance2*
:   Offset distance in direction 2; only applies if Dir2Type is swEndConditions\_e.swEndCondOffsetFromSurface

*ThinType*
:   Type and direction as defined in [swThinWallType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThinWallType_e.html)

*ThinThickness1*
:   Wall thickness in direction 1 (if ThinType is swThinWallType\_e.swThinWallMidPlane, (ThinThickness1)/2 is used for each direction)

*ThinThickness2*
:   Wall thickness in direction 2 (only applies if ThinType is swThinWallType\_e.swThinWallTwoDirection)

*Merge*
:   True to merge the results into a multi-body part, false to not

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies (see **Remarks**)

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies or components that the feature affects (see **Remarks**)

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select:

- the sketch to revolve, using Mark = 0.
- the axis of revolution, using Mark = 4 or 16.
- the up-to surface, up-to vertex, or offset-from surface, using Mark = 32.
- one or more affected bodies or components (only if UseFeatScope is set to true and UseAutoSel is set to false), using Mark = 1 for each.

If SingleDir is false and the revolve is up to or offset from the same entity in both directions, select the entity once and set BothDirectionUpToSameEntity to true. If you select the same entity for each direction, the second selection negates the first, and the revolve feature is not created.

**NOTE**: This method provides more functionality, i.e., additional end conditions, than the now obsolete [IFeatureManager::FeatureRevolveCut2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveCut2.md), [IFeatureManager::FeatureRevolveThin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThin.md), and [IFeatureManager::FeatureRevolveThinCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut.md).

Example

[Create Revolve Features (VBA)](Create_Revolve_Features_Example_VB.htm)  
[Create Revolve Features (VB.NET)](Create_Revolve_Features_Example_VBNET.htm)  
[Create Revolve Features (C#)](Create_Revolve_Features_Example_CSharp.htm)  
[Create Thin Feature Revolve in Two Directions (VBA)](Create_Thin_Feature_Revolve_in_Two_Directions_Example_VB.htm)  
[Create Thin Feature Revolve in Two Directions (VB.NET)](Create_Thin_Feature_Revolve_in_Two_Directions_Example_VBNET.htm)  
[Create Thin Feature Revolve in Two Directions (C#)](Create_Thin_Feature_Revolve_in_Two_Directions_Example_CSharp.htm)  
[Create 360-degree Revolve Feature (VBA)](Create_360-degree_Revolve_Feature_Example_VB.htm)  
[Create 360-degree Revolve Feature (VB.NET)](Create_360-degree_Revolve_Feature_Example_VBNET.htm)  
[Create 360-degree Revolve Feature (C#)](Create_360-degree_Revolve_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)
