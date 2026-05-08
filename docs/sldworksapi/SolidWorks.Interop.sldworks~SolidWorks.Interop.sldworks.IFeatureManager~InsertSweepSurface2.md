# InsertSweepSurface2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSweepSurface2`

Obsolete. Superseded by IFeatureManager::InsertSweepSurface3.
Obsolete. Superseded by [IFeatureManager::InsertSweepSurface3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSweepSurface3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSweepSurface2( _
   ByVal Propagate As System.Boolean, _
   ByVal TwistCtrlOption As System.Short, _
   ByVal KeepTangency As System.Boolean, _
   ByVal BAdvancedSmoothing As System.Boolean, _
   ByVal StartMatchingType As System.Short, _
   ByVal EndMatchingType As System.Short, _
   ByVal PathAlign As System.Short, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal TwistAngle As System.Double, _
   ByVal BMergeSmoothFaces As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Propagate As System.Boolean
Dim TwistCtrlOption As System.Short
Dim KeepTangency As System.Boolean
Dim BAdvancedSmoothing As System.Boolean
Dim StartMatchingType As System.Short
Dim EndMatchingType As System.Short
Dim PathAlign As System.Short
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim TwistAngle As System.Double
Dim BMergeSmoothFaces As System.Boolean
Dim value As Feature
 
value = instance.InsertSweepSurface2(Propagate, TwistCtrlOption, KeepTangency, BAdvancedSmoothing, StartMatchingType, EndMatchingType, PathAlign, UseFeatScope, UseAutoSelect, TwistAngle, BMergeSmoothFaces)
```

```

Feature InsertSweepSurface2( 
   System.bool Propagate,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.short PathAlign,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces
)
```

```

Feature^ InsertSweepSurface2( 
   System.bool Propagate,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.short PathAlign,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces
) 
```

#### Parameters

*Propagate*
:   True propagates the sweep to the next edge, false causes the sweep to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge

*TwistCtrlOption*
:   Twist control option as defined in [swTwistControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTwistControlType_e.html)

*KeepTangency*
:   If the sweep section has tangent segments, then true to cause the corresponding surfaces in the resulting sweep to be tangent, false to not

*BAdvancedSmoothing*
:   If the sweep section has circular or elliptical arcs, then true to approximate the sections and smooth the surfaces, false to not

*StartMatchingType*
:   Tangency type as defined in [swTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html)

*EndMatchingType*
:   Tangency type as defined in [swTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html)

*PathAlign*
:   Align path type (see **Remarks**)

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects (see **Remarks**)

*TwistAngle*
:   If TwistCtrlOption set to swTwistControlType\_e.swTwistControlConstantTwistAlongPath, then specify end twist angle

*BMergeSmoothFaces*
:   True to merge smooth faces, false to not

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Because you are creating a surface, the sections can be open.

Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the profile and sweep curves. The mark for:

- 1 = Profile selection
- 2 = Guide curve selection, if provided
- 4 = Sweep path

The PathAlign argument is available when TwistCtrlOption is set to swTwistControlFollowPath and can take one of these values:

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
