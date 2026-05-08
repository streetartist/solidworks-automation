# InsertSweepSurface3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSweepSurface3`

Obsolete. See Remarks.
Obsolete. See **Remarks**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSweepSurface3( _
   ByVal Propagate As System.Boolean, _
   ByVal TwistCtrlOption As System.Integer, _
   ByVal KeepTangency As System.Boolean, _
   ByVal BAdvancedSmoothing As System.Boolean, _
   ByVal StartMatchingType As System.Integer, _
   ByVal EndMatchingType As System.Integer, _
   ByVal PathAlign As System.Integer, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal TwistAngle As System.Double, _
   ByVal BMergeSmoothFaces As System.Boolean, _
   ByVal CircularProfile As System.Boolean, _
   ByVal CircularProfileDiameter As System.Double, _
   ByVal Direction As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Propagate As System.Boolean
Dim TwistCtrlOption As System.Integer
Dim KeepTangency As System.Boolean
Dim BAdvancedSmoothing As System.Boolean
Dim StartMatchingType As System.Integer
Dim EndMatchingType As System.Integer
Dim PathAlign As System.Integer
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim TwistAngle As System.Double
Dim BMergeSmoothFaces As System.Boolean
Dim CircularProfile As System.Boolean
Dim CircularProfileDiameter As System.Double
Dim Direction As System.Integer
Dim value As Feature
 
value = instance.InsertSweepSurface3(Propagate, TwistCtrlOption, KeepTangency, BAdvancedSmoothing, StartMatchingType, EndMatchingType, PathAlign, UseFeatScope, UseAutoSelect, TwistAngle, BMergeSmoothFaces, CircularProfile, CircularProfileDiameter, Direction)
```

```

Feature InsertSweepSurface3( 
   System.bool Propagate,
   System.int TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.int PathAlign,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces,
   System.bool CircularProfile,
   System.double CircularProfileDiameter,
   System.int Direction
)
```

```

Feature^ InsertSweepSurface3( 
   System.bool Propagate,
   System.int TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.int PathAlign,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces,
   System.bool CircularProfile,
   System.double CircularProfileDiameter,
   System.int Direction
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
:   Tangency type as defined in swTangencyType\_e

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

*CircularProfile*
:   True to use a circular profile, false to use the selected sketch profile or solid body

*CircularProfileDiameter*
:   If CircularProfile is true, then specify the diameter of the circular profile

*Direction*
:   Direction as defined in [swSweepDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweepDirection_e.html) (see **Remarks**)

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

SOLIDWORKS 2018 introduces a new sweep architecture, making this method obsolete. See [Sweep Features and SweepFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Sweep_Features_and_SweepFeatureData_Objects.htm) to create this sweep surface.

Because you are creating a surface, the sections can be open.

Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the sketch profile and sweep curves. Specify these marks:

- 1 = Sketch profile
- 2 = Guide curve, if provided
- 4 = Sweep path

The PathAlign argument is available when TwistCtrlOption is set to swTwistControlType\_e.swTwistControlFollowPath and can take one of these values:

- 0 = None; no correction (default)
- 2 = Direction vector; a plane, planar face, or line defines the path
- 3 = All faces; includes neighboring faces

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

Direction only applies to sketch profiles and only when the sketch profile is not coincident with an end of the path.

Example

[Create Surface-sweep Feature (C#)](Create_Surface-sweep_Feature_Example_CSharp.htm)  
[Create Surface-sweep Feature (VB.NET)](Create_Surface-sweep_Feature_Example_VBNET.htm)  
[Create Surface-sweep Feature (VBA)](Create_Surface-sweep_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::InsertCutSwept5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutSwept5.md)  
[IFeatureManager::InsertProtrusionSwept4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionSwept4.md)  
[IModeler::CreateSweptSurface Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptSurface.md)  
[IModeler::ICreateSweptSurface Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.md)  
[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)
