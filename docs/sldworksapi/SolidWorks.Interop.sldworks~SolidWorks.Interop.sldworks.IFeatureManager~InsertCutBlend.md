# InsertCutBlend Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutBlend`

Inserts a lofted cut based on the selected profiles, centerline, and guide curves.
Inserts a lofted cut based on the selected profiles, centerline, and guide curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCutBlend( _
   ByVal Closed As System.Boolean, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean, _
   ByVal TessToleranceFactor As System.Double, _
   ByVal StartMatchingType As System.Short, _
   ByVal EndMatchingType As System.Short, _
   ByVal IsThinBody As System.Boolean, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ThinType As System.Short, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Closed As System.Boolean
Dim KeepTangency As System.Boolean
Dim ForceNonRational As System.Boolean
Dim TessToleranceFactor As System.Double
Dim StartMatchingType As System.Short
Dim EndMatchingType As System.Short
Dim IsThinBody As System.Boolean
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim ThinType As System.Short
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim value As Feature
 
value = instance.InsertCutBlend(Closed, KeepTangency, ForceNonRational, TessToleranceFactor, StartMatchingType, EndMatchingType, IsThinBody, Thickness1, Thickness2, ThinType, UseFeatScope, UseAutoSelect)
```

```

Feature InsertCutBlend( 
   System.bool Closed,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.double TessToleranceFactor,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.short ThinType,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

```

Feature^ InsertCutBlend( 
   System.bool Closed,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.double TessToleranceFactor,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.short ThinType,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
) 
```

#### Parameters

*Closed*
:   True if you want the loft to be closed, false to leave it open (see **Remarks**)

*KeepTangency*
:   Controls whether the section curves are tangent (see Remarks)

*ForceNonRational*
:   True to force the resulting surface to be non-rational; false to not

*TessToleranceFactor*
:   A factor to control the number of intermediate sections used for loft with centerline;  
    the default value is 1.0; the greater the variable, the more intermediate sections  
    are created

*StartMatchingType*
:   Tangency type at the start profile (see Remarks)

*EndMatchingType*
:   Tangency type at the end profile (see Remarks)

*IsThinBody*
:   True if this feature is a thin body, false is not

*Thickness1*
:   Thickness value for the first direction

*Thickness2*
:   Thickness value for the second direction

*ThinType*
:   Thin wall type:

    - 0 = One direction
    - 1 = One direction reverse
    - 2 = Mid-plane
    - 3 = Two direction

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all  
    bodies

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies,  
    false to select the bodies the feature affects (see Remarks)

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Selection of guide curves and centerline is optional; however, selection of the profiles must be in an order consistent with the desired direction of the loft.

Use of guide curves is strongly recommended, especially when selection of profiles is done in the FeatureManager design tree.

You can use any number of profiles; however, if you selected only one profile, then any selected guide curves must be closed curves.

If Closed is True and you selected less that three profiles, then any selected guide curves must be closed curves.

If the section curves are tangent, then KeepTangency controls whether the resulting surfaces are also be tangent. Specify True to maintain the tangency as seen in the section curves; false to not. When generating tangent surfaces, SOLIDWORKS maintains planar and cylindrical surface shapes if the section curves exhibit these characteristics.

Use [IModelDocExtension::SelectById2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the profiles and guide curves. The mark for the profile selections should be 1; the mark for any guide curve selection, if provided, should be a 2; the mark for the centerline selection, if provided, should be a 4; the mark for the start tangency vector selection, if provided, should be a 8; the mark for the start tangency faces selection, if provided, should be a 16 (not available); the mark for the end tangency vector selection, if provided, should be a 32; the mark for the end tangency faces selection, if provided, should be a 64 (not available); linear edge, sketch line, axis, plane and planar faces are qualified for tangency vector sections.

The tangency type arguments can take the following values:

- 0 - none
- 1 - tangent to the normal of the profile
- 2 - tangent to a selected vector
- 3 - tangency to all the adjacent faces sharing an edge with the start profile
- 4 - tangent to some of the selected faces sharing an edge with the start profile (not currently available )

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

When using cut or cavity features that result in multiple bodies, you cannot select to keep all of the resulting bodies or one or more selected bodies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[IFeatureManager::InsertProtrusionBlend Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionBlend.md)
