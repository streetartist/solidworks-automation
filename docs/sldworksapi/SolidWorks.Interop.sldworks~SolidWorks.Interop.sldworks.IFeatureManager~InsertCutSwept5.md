# InsertCutSwept5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutSwept5`

Obsolete. See Remarks.
Obsolete. See **Remarks**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCutSwept5( _
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
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal TwistAngle As System.Double, _
   ByVal BMergeSmoothFaces As System.Boolean, _
   ByVal AssemblyFeatureScope As System.Boolean, _
   ByVal AutoSelectComponents As System.Boolean, _
   ByVal PropagateFeatureToParts As System.Boolean, _
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
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim TwistAngle As System.Double
Dim BMergeSmoothFaces As System.Boolean
Dim AssemblyFeatureScope As System.Boolean
Dim AutoSelectComponents As System.Boolean
Dim PropagateFeatureToParts As System.Boolean
Dim CircularProfile As System.Boolean
Dim CircularProfileDiameter As System.Double
Dim Direction As System.Integer
Dim value As Feature
 
value = instance.InsertCutSwept5(Propagate, Alignment, TwistCtrlOption, KeepTangency, BAdvancedSmoothing, StartMatchingType, EndMatchingType, IsThinBody, Thickness1, Thickness2, ThinType, PathAlign, UseFeatScope, UseAutoSelect, TwistAngle, BMergeSmoothFaces, AssemblyFeatureScope, AutoSelectComponents, PropagateFeatureToParts, CircularProfile, CircularProfileDiameter, Direction)
```

```

Feature InsertCutSwept5( 
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
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents,
   System.bool PropagateFeatureToParts,
   System.bool CircularProfile,
   System.double CircularProfileDiameter,
   System.int Direction
)
```

```

Feature^ InsertCutSwept5( 
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
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents,
   System.bool PropagateFeatureToParts,
   System.bool CircularProfile,
   System.double CircularProfileDiameter,
   System.int Direction
) 
```

#### Parameters

*Propagate*
:   True propagates the sweep cut to the next edge, false causes the sweep cut to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge

*Alignment*
:   If the curve used to sweep goes from one face to another or from one edge to another, then true causes the sweep to cut completely through the end faces of the cut, and false causes the cut to begin and end perpendicular to the sweep curve; thus, it cannot break through the two end faces of the body being cut

*TwistCtrlOption*
:   Twist control options as defined in [swTwistControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTwistControlType_e.html)

*KeepTangency*
:   If the sweep section has tangent segments, true to cause the corresponding surfaces in the resulting sweep to be tangent, false to not

*BAdvancedSmoothing*
:   If the sweep section has circular or elliptical arcs, true to approximate the sections and smooth the surfaces, false to not

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

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects (see Remarks)

*TwistAngle*
:   If TwistCtrlOption set to swTwistControlType\_e.swTwistControlConstantTwistAlongPath, then specify end twist angle

*BMergeSmoothFaces*
:   True to merge smooth faces, false to not

*AssemblyFeatureScope*
:   True if the sweep cut affects only selected components in the assembly, false if the sweep cut affects all components in the assembly (**see Remarks**)

*AutoSelectComponents*
:   True to auto-select all affected components in the assembly, false to use manually selected components (**see Remarks**)

*PropagateFeatureToParts*
:   True to extend the sweep cut feature to all affected parts in the assembly, false to just insert the sweep cut into the assembly (**see Remarks**)

*CircularProfile*
:   True to use a circular profile, false to use the selected sketch profile or solid body

*CircularProfileDiameter*
:   If CircularProfile is true, then specify the diameter of the circular profile

*Direction*
:   Direction as defined in [swSweepDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweepDirection_e.html) (see **Remarks**)

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

SOLIDWORKS 2018 introduces a new sweep architecture, making this method obsolete. See [Sweep Features and SweepFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Sweep_Features_and_SweepFeatureData_Objects.htm) to create this cut-sweep feature.

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) multiple times to select the sketch profile or tool body, guide curves, and sweep path for the cut. Specify these marks:

- 1 = Sketch profile or tool body
- 2 = Guide curve, if provided
- 4 = Sweep path

The PathAlign argument is available when TwistCtrlOption is set to swTwistControlType\_e.swTwistControlFollowPath and can take one of these values:

- 0 = None; no correction (default)
- 2 = Direction vector; a plane, planar face, or line defines the path
- 3 = All faces; includes neighboring faces

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

When using cut or cavity features that result in multiple bodies, you cannot select to keep all of the resulting bodies or one or more selected bodies.

Use AssemblyFeatureScope, AutoSelectComponents, and PropagateFeatureToParts to insert sweep cuts into an assembly. AssemblyFeatureScope and AutoSelectComponents perform just like the configuration of the Feature Scope section on the PropertyManager page of the sweep feature:

| **AssemblyFeatureScope setting** | **AutoSelectComponents setting** | **PropertyManager page Feature Scope setting** |
| --- | --- | --- |
| False | Ignored | - All components selected - Auto-select not visible |
| True | If true, affected components are automatically selected  If false, manually select the affected components in the view before calling this method | Selected components selected  If Auto-select is not selected, then manually select affected components in the view |

Direction only applies to sketch profiles and only when the sketch profile is not coincident with an end of the path.

Example

[Create Cut-sweep Feature Using Tool Body (C#)](Create_Cut-sweep_Feature_Using_Tool_Body_Example_CSharp.htm)  
[Create Cut-sweep Feature Using Tool Body (VB.NET)](Create_Cut-sweep_Feature_Using_Tool_Body_Example_VBNET.htm)  
[Create Cut-sweep Feature Using Tool Body (VBA)](Create_Cut-sweep_Feature_Using_Tool_Body_Example_VB.htm)  
[Create Cut-sweep Feature Using Circular Profile (C#)](Create_Cut-sweep_Feature_Using_Circular_Profile_Example_CSharp.htm)  
[Create Cut-sweep Feature Using Circular Profile (VB.NET)](Create_Cut-sweep_Feature_Using_Circular_Profile_Example_VBNET.htm)  
[Create Cut-sweep Feature Using Circular Profile (VBA)](Create_Cut-sweep_Feature_Using_Circular_Profile_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[IFeatureManager::InsertProtrusionSwept4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionSwept4.md)  
[IFeatureManager::InsertSweepSurface3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSweepSurface3.md)  
[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)
