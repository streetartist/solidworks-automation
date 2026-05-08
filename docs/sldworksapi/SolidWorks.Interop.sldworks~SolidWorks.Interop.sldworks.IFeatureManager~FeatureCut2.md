# FeatureCut2 Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCut2`

Obsolete. Superseded by IFeatureManager::FeatureCut3.
Obsolete. Superseded by [IFeatureManager::FeatureCut3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCut3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureCut2( _
   ByVal Sd As System.Boolean, _
   ByVal Flip As System.Boolean, _
   ByVal Dir As System.Boolean, _
   ByVal T1 As System.Integer, _
   ByVal T2 As System.Integer, _
   ByVal D1 As System.Double, _
   ByVal D2 As System.Double, _
   ByVal Dchk1 As System.Boolean, _
   ByVal Dchk2 As System.Boolean, _
   ByVal Ddir1 As System.Boolean, _
   ByVal Ddir2 As System.Boolean, _
   ByVal Dang1 As System.Double, _
   ByVal Dang2 As System.Double, _
   ByVal OffsetReverse1 As System.Boolean, _
   ByVal OffsetReverse2 As System.Boolean, _
   ByVal TranslateSurface1 As System.Boolean, _
   ByVal TranslateSurface2 As System.Boolean, _
   ByVal NormalCut As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal AssemblyFeatureScope As System.Boolean, _
   ByVal AutoSelectComponents As System.Boolean, _
   ByVal PropagateFeatureToParts As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Sd As System.Boolean
Dim Flip As System.Boolean
Dim Dir As System.Boolean
Dim T1 As System.Integer
Dim T2 As System.Integer
Dim D1 As System.Double
Dim D2 As System.Double
Dim Dchk1 As System.Boolean
Dim Dchk2 As System.Boolean
Dim Ddir1 As System.Boolean
Dim Ddir2 As System.Boolean
Dim Dang1 As System.Double
Dim Dang2 As System.Double
Dim OffsetReverse1 As System.Boolean
Dim OffsetReverse2 As System.Boolean
Dim TranslateSurface1 As System.Boolean
Dim TranslateSurface2 As System.Boolean
Dim NormalCut As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim AssemblyFeatureScope As System.Boolean
Dim AutoSelectComponents As System.Boolean
Dim PropagateFeatureToParts As System.Boolean
Dim value As Feature
 
value = instance.FeatureCut2(Sd, Flip, Dir, T1, T2, D1, D2, Dchk1, Dchk2, Ddir1, Ddir2, Dang1, Dang2, OffsetReverse1, OffsetReverse2, TranslateSurface1, TranslateSurface2, NormalCut, UseFeatScope, UseAutoSelect, AssemblyFeatureScope, AutoSelectComponents, PropagateFeatureToParts)
```

```

Feature FeatureCut2( 
   System.bool Sd,
   System.bool Flip,
   System.bool Dir,
   System.int T1,
   System.int T2,
   System.double D1,
   System.double D2,
   System.bool Dchk1,
   System.bool Dchk2,
   System.bool Ddir1,
   System.bool Ddir2,
   System.double Dang1,
   System.double Dang2,
   System.bool OffsetReverse1,
   System.bool OffsetReverse2,
   System.bool TranslateSurface1,
   System.bool TranslateSurface2,
   System.bool NormalCut,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents,
   System.bool PropagateFeatureToParts
)
```

```

Feature^ FeatureCut2( 
   System.bool Sd,
   System.bool Flip,
   System.bool Dir,
   System.int T1,
   System.int T2,
   System.double D1,
   System.double D2,
   System.bool Dchk1,
   System.bool Dchk2,
   System.bool Ddir1,
   System.bool Ddir2,
   System.double Dang1,
   System.double Dang2,
   System.bool OffsetReverse1,
   System.bool OffsetReverse2,
   System.bool TranslateSurface1,
   System.bool TranslateSurface2,
   System.bool NormalCut,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents,
   System.bool PropagateFeatureToParts
) 
```

#### Parameters

*Sd*
:   True for single-ended, false for doubled-ended

*Flip*
:   Flip to side cut; true if you want to remove material outside of the profile, false if not

*Dir*
:   Reverse direction; true if you want Direction 1 to be opposite of the default direction (see **Remarks**)

*T1*
:   Termination type for first end as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

*T2*
:   Termination type for second end as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

*D1*
:   Depth of extrusion for first end in meters

*D2*
:   Depth of extrusion for second end in meters

*Dchk1*
:   True allows draft angle in first direction, false does not allow drafting

*Dchk2*
:   True allows draft angle in second direction, false does not allow drafting

*Ddir1*
:   True for first draft angle to be inward, false to be outward

*Ddir2*
:   True for second draft angle to be inward, false be outward

*Dang1*
:   Draft angle for first end

*Dang2*
:   Draft angle for second end

*OffsetReverse1*
:   If you chose to offset the first end condition from another face or plane, then true specifies offset in direction away from the sketch, false specifies offset from the face or plane in a direction toward the sketch

*OffsetReverse2*
:   If you chose to offset the second end condition from another face or plane, then true specifies offset in direction away from the sketch, false specifies offset from the face or plane in a direction toward the sketch

*TranslateSurface1*
:   When you choose swEndcondOffsetFromSurface as the termination type for the first end, then true specifies that the end of the extrusion is a translation of the reference surface, false specifies to use a true offset

*TranslateSurface2*
:   When you choose swEndcondOffsetFromSurface as the termination type for the second end, then true specifies that the end of the extrusion is a translation of the reference surface, false specifies to use a true offset

*NormalCut*
:   True ensures that the cut is created normal to the sheet metal thickness, false does not (this argument applies only to sheet metal parts, use false for non-sheet metal parts)

*UseFeatScope*
:   True if the feature only affects selected bodies or components, false if the feature affects all bodies or components

*UseAutoSelect*
:   True to automatically select all bodies or components and have the feature affect those bodies or components, false to select the bodies or components the feature affects

*AssemblyFeatureScope*
:   True if the assembly feature only affects selected components in the assembly, false if the assembly feature affects all components in the assembly

*AutoSelectComponents*
:   True to auto-select all affected components, false to not (use the selected components only)

*PropagateFeatureToParts*
:   True to propagate the assembly feature to the components in the model that it affects, false to not

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

The default direction for cut operations are opposite the sketch normal. The default direction for boss operations is along the sketch normal. Setting the direction arguments to true reverse the default direction. For double-ended extrusions, Direction 2 is always be opposite to Direction 1.

The default sketch normal is the same as the face or plane normal where the sketch was placed. To determine this normal vector, see [IFace2::Normal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Normal.md) and [IRefPlane::Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~Transform.md), respectively.

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

When using cut or cavity features that result in multiple bodies, you cannot select to keep all of the resulting bodies or one or more selected bodies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IFeatureManager::FeatureCutThicken Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThicken.md)  
[IFeatureManager::FeatureCutThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThin.md)
