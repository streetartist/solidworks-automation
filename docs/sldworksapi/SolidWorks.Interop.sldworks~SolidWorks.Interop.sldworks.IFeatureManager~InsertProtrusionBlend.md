# InsertProtrusionBlend Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionBlend`

Obsolete. Superseded by IFeatureManager::InsertProtrusionBlend2.
Obsolete. Superseded by [IFeatureManager::InsertProtrusionBlend2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionBlend2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertProtrusionBlend( _
   ByVal Closed As System.Boolean, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean, _
   ByVal TessToleranceFactor As System.Double, _
   ByVal StartMatchingType As System.Short, _
   ByVal EndMatchingType As System.Short, _
   ByVal StartTangentLength As System.Double, _
   ByVal EndTangentLength As System.Double, _
   ByVal StartTangentDir As System.Boolean, _
   ByVal EndTangentDir As System.Boolean, _
   ByVal IsThinBody As System.Boolean, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ThinType As System.Short, _
   ByVal Merge As System.Boolean, _
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
Dim StartTangentLength As System.Double
Dim EndTangentLength As System.Double
Dim StartTangentDir As System.Boolean
Dim EndTangentDir As System.Boolean
Dim IsThinBody As System.Boolean
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim ThinType As System.Short
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim value As Feature
 
value = instance.InsertProtrusionBlend(Closed, KeepTangency, ForceNonRational, TessToleranceFactor, StartMatchingType, EndMatchingType, StartTangentLength, EndTangentLength, StartTangentDir, EndTangentDir, IsThinBody, Thickness1, Thickness2, ThinType, Merge, UseFeatScope, UseAutoSelect)
```

```

Feature InsertProtrusionBlend( 
   System.bool Closed,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.double TessToleranceFactor,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.double StartTangentLength,
   System.double EndTangentLength,
   System.bool StartTangentDir,
   System.bool EndTangentDir,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.short ThinType,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

```

Feature^ InsertProtrusionBlend( 
   System.bool Closed,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.double TessToleranceFactor,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.double StartTangentLength,
   System.double EndTangentLength,
   System.bool StartTangentDir,
   System.bool EndTangentDir,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.short ThinType,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
) 
```

#### Parameters

*Closed*
:   True closes the loft, false leaves the loft open; if true and you selected less that three profiles, any selected guide curves must be closed curves

*KeepTangency*
:   True maintains the tangency as seen in the section curves, false does not

    If the section curves are tangent, then you have the option to specify whether the resulting faces are also tangent; when generating tangent surfaces, SOLIDWORKS maintains planar and cylindrical surface shapes if the section curves exhibit these characteristics

*ForceNonRational*
:   True obtains smoother surfaces, false does not

*TessToleranceFactor*
:   Factor that controls the number of intermediate sections used for loft with centerline; the default value is 1.0; the greater the value, the more intermediate sections are created

*StartMatchingType*
:   Tangency type at the start profile:

    - 0 = none
    - 1 = tangent to the normal of the profile
    - 2 = tangent to a selected vector
    - 3 = tangency to all the adjacent faces sharing an edge with the start profile
    - 4 = tangent to some of the selected faces sharing an edge with the start profile (not available)

*EndMatchingType*
:   Tangency type at the end profile:

    - 0 = none
    - 1 = tangent to the normal of the profile
    - 2 = tangent to a selected vector
    - 3 = tangency to all the adjacent faces sharing an edge with the start profile
    - 4 = tangent to some of the selected faces sharing an edge with the start profile (not available)

*StartTangentLength*
:   Start tangent length

*EndTangentLength*
:   End tangent length

*StartTangentDir*
:   True is one direction, false is the opposite

*EndTangentDir*
:   True is one direction, false is the opposite

*IsThinBody*
:   True if this feature is a thin body, false if it is not

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

*Merge*
:   True merges the results in a multibody part, false does not

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Selection of guide curves and centerline is optional. However, you must select the profiles in an order consistent with the desired direction of the loft. Because a solid is being created, the section profiles must be closed.

It is best to use guide curves, especially when you select profiles in the FeatureManager design tree.

You can use any number of profiles; however, if you select only one profile, then any selected guide curves must be closed curves.

Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the profiles and guide curves. Set the mark for:

- profile selections to 1
- any guide curve selection to 2
- centerline selection to 4
- start tangency vector selection to 8
- start tangency faces selection to 16 (not available)
- end tangency vector selection to 32
- end tangency faces selection to 64 (not available)

NOTE: Linear edge, sketch line, axis, plane and planar faces are qualified for tangency vector sections.

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::InsertCutBlend Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutBlend.md)  
[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)
