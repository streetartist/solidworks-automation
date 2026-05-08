# InsertProtrusionSwept3 Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionSwept3`

Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept4.
Obsolete. Superseded by [IFeatureManager::InsertProtrusionSwept4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionSwept4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertProtrusionSwept3( _
   ByVal Propagate As System.Boolean, _
   ByVal Alignment As System.Boolean, _
   ByVal TwistCtrlOption As System.Short, _
   ByVal KeepTangency As System.Boolean, _
   ByVal BAdvancedSmoothing As System.Boolean, _
   ByVal StartMatchingType As System.Short, _
   ByVal EndMatchingType As System.Short, _
   ByVal IsThinBody As System.Boolean, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ThinType As System.Short, _
   ByVal PathAlign As System.Short, _
   ByVal Merge As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal TwistAngle As System.Double, _
   ByVal BMergeSmoothFaces As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Propagate As System.Boolean
Dim Alignment As System.Boolean
Dim TwistCtrlOption As System.Short
Dim KeepTangency As System.Boolean
Dim BAdvancedSmoothing As System.Boolean
Dim StartMatchingType As System.Short
Dim EndMatchingType As System.Short
Dim IsThinBody As System.Boolean
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim ThinType As System.Short
Dim PathAlign As System.Short
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim TwistAngle As System.Double
Dim BMergeSmoothFaces As System.Boolean
Dim value As Feature
 
value = instance.InsertProtrusionSwept3(Propagate, Alignment, TwistCtrlOption, KeepTangency, BAdvancedSmoothing, StartMatchingType, EndMatchingType, IsThinBody, Thickness1, Thickness2, ThinType, PathAlign, Merge, UseFeatScope, UseAutoSelect, TwistAngle, BMergeSmoothFaces)
```

```

Feature InsertProtrusionSwept3( 
   System.bool Propagate,
   System.bool Alignment,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.short ThinType,
   System.short PathAlign,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces
)
```

```

Feature^ InsertProtrusionSwept3( 
   System.bool Propagate,
   System.bool Alignment,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.short ThinType,
   System.short PathAlign,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces
) 
```

#### Parameters

*Propagate*
:   True propagates the swept protrusion to the next tangent edge, false does not

*Alignment*
:   True causes the swept protrusion to go through the end faces if the curve used for the sweep goes from one face to another or from one edge to another, false causes the swept protrusion to begin and end perpendicular to the sweep curve and it cannot break through the two end faces of the body

*TwistCtrlOption*
:   Twist control options as defined in [swTwistControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTwistControlType_e.html)

*KeepTangency*
:   If the sweep section has tangent segments, then true to cause the corresponding surfaces in the resulting sweep to be tangent, false to not

*BAdvancedSmoothing*
:   If the sweep section has circular or elliptical arcs, then true to approximate the sections and smooth the surfaces, false to not

*StartMatchingType*
:   Tangency type as defined in [swTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html)

*EndMatchingType*
:   Tangency type as defined in [swTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html)

*IsThinBody*
:   True if this feature is a thin body, false if not

*Thickness1*
:   Thickness value for the first direction

*Thickness2*
:   Thickness value for the second direction

*ThinType*
:   Thin wall type as defined in [swThinWallType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThinWallType_e.html)

*PathAlign*
:   Align path type (see **Remarks**)

*Merge*
:   True to merge the results in a multibody part, false to not

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects (see **Remarks**)

*TwistAngle*
:   If TwistCtrlOption set to swTwistControlType\_e.swTwistControlConstantTwistAlongPath, then specify end twist angle

*BMergeSmoothFaces*
:   True to merge smooth faces, false to not

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the profile and sweep curves. The mark for:

- 1 = Profile selection
- 2 = Guide curve selection, if provided
- 4 = Sweep path

The PathAlign argument is available when TwistCtrlOption is set to 0 (follow path) and can take one of these values:

- 0 = None; no correction (default)
- 2 = Direction vector; a plane, planar face, or line defines the path
- 3 = All faces; includes neighboring faces

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[IFeatureManager::InsertCutSwept3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutSwept3.md)  
[IFeatureManager::InsertSweepSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSweepSurface2.md)
