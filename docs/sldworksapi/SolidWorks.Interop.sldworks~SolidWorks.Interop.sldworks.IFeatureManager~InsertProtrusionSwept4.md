# InsertProtrusionSwept4 Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionSwept4`

Obsolete. See Remarks.
Obsolete. See **Remarks**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertProtrusionSwept4( _
   ByVal Propagate As System.Boolean, _
   ByVal Alignment As System.Boolean, _
   ByVal TwistCtrlOption As System.Integer, _
   ByVal KeepTangency As System.Boolean, _
   ByVal BAdvancedSmoothing As System.Boolean, _
   ByVal StartMatchingType As System.Integer, _
   ByVal EndMatchingType As System.Integer, _
   ByVal IsThinBody As System.Boolean, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ThinType As System.Integer, _
   ByVal PathAlign As System.Integer, _
   ByVal Merge As System.Boolean, _
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
Dim Alignment As System.Boolean
Dim TwistCtrlOption As System.Integer
Dim KeepTangency As System.Boolean
Dim BAdvancedSmoothing As System.Boolean
Dim StartMatchingType As System.Integer
Dim EndMatchingType As System.Integer
Dim IsThinBody As System.Boolean
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim ThinType As System.Integer
Dim PathAlign As System.Integer
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim TwistAngle As System.Double
Dim BMergeSmoothFaces As System.Boolean
Dim CircularProfile As System.Boolean
Dim CircularProfileDiameter As System.Double
Dim Direction As System.Integer
Dim value As Feature
 
value = instance.InsertProtrusionSwept4(Propagate, Alignment, TwistCtrlOption, KeepTangency, BAdvancedSmoothing, StartMatchingType, EndMatchingType, IsThinBody, Thickness1, Thickness2, ThinType, PathAlign, Merge, UseFeatScope, UseAutoSelect, TwistAngle, BMergeSmoothFaces, CircularProfile, CircularProfileDiameter, Direction)
```

```

Feature InsertProtrusionSwept4( 
   System.bool Propagate,
   System.bool Alignment,
   System.int TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.int ThinType,
   System.int PathAlign,
   System.bool Merge,
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

Feature^ InsertProtrusionSwept4( 
   System.bool Propagate,
   System.bool Alignment,
   System.int TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.int ThinType,
   System.int PathAlign,
   System.bool Merge,
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
:   True propagates the swept protrusion to the next tangent edge, false does not

*Alignment*
:   True causes the swept protrusion to go through the end faces if the curve used for the sweep goes from one face to another or from one edge to another, false causes the swept protrusion to begin and end perpendicular to the sweep curve; thus, it cannot break through the two end faces of the body

*TwistCtrlOption*
:   Twist control options as defined in [swTwistControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTwistControlType_e.html)

*KeepTangency*
:   If the sweep section has tangent segments, then true to cause the corresponding surfaces in the resulting sweep to be tangent, false to not

*BAdvancedSmoothing*
:   If the sweep section has circular or elliptical arcs, then true to approximate the sections and smooth the surfaces, false to not

*StartMatchingType*
:   Tangency type as defined in [swTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html)

*EndMatchingType*
:   Tangency type as defined in swTangencyType\_e

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
:   If TwistCtrlOption is swTwistControlType\_e.swTwistControlConstantTwistAlongPath, then specify end twist angle

*BMergeSmoothFaces*
:   True to merge smooth faces, false to not

*CircularProfile*
:   True to use a circular profile, false to use the selected sketch profile or solid body

*CircularProfileDiameter*
:   If CircularProfile is true, then specify the diameter of the circular profile

*Direction*
:   Direction as defined in [swSweepDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweepDirection_e.html) (see **Remarks**)

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

SOLIDWORKS 2018 introduces a new sweep architecture, making this method obsolete. See [Sweep Features and SweepFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Sweep_Features_and_SweepFeatureData_Objects.htm) to create this swept-boss or base feature.

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

[Get Guide Curves in Sweep Feature (C#)](Get_Guide_Curves_in_Sweep_Feature_Example_CSharp.htm)  
[Get Guide Curves in Sweep Feature (VB.NET)](Get_Guide_Curves_in_Sweep_Feature_Example_VBNET.htm)  
[Get Guide Curves in Sweep Feature (VBA)](Get_Guide_Curves_in_Sweep_Feature_Example_VB.htm)  
[Select Mulitple Sketches for Sweep Path (C#)](Select_Multiple_Paths_for_Sweep_Path_Example_CSharp.htm)  
[Select Mulitple Sketches for Sweep Path (VB.NET)](Select_Multiple_Paths_for_Sweep_Path_Example_VBNET.htm)  
[Select Mulitple Sketches for Sweep Path (VBA)](Select_Multiple_Paths_for_Sweep_Path_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::InsertCutSwept5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutSwept5.md)  
[IFeatureManager::InsertSweepSurface3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSweepSurface3.md)  
[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)
