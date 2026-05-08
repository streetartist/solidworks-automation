# AddExplodeStep2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep2`

Adds a regular (translate and rotate) explode step to the explode view of the active configuration.
Adds a regular (translate and rotate) explode step to the explode view of the active configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddExplodeStep2( _
   ByVal ExplDist As System.Double, _
   ByVal ExplDirIndex As System.Integer, _
   ByVal ReverseDir As System.Boolean, _
   ByVal ExplAng As System.Double, _
   ByVal RotAxisIndex As System.Integer, _
   ByVal ReverseAng As System.Boolean, _
   ByVal RotateAboutOrigin As System.Boolean, _
   ByVal AutoSpaceComponentsOnDrag As System.Boolean, _
   ByRef Error As System.Integer _
) As System.Object
```

```

Dim instance As IConfiguration
Dim ExplDist As System.Double
Dim ExplDirIndex As System.Integer
Dim ReverseDir As System.Boolean
Dim ExplAng As System.Double
Dim RotAxisIndex As System.Integer
Dim ReverseAng As System.Boolean
Dim RotateAboutOrigin As System.Boolean
Dim AutoSpaceComponentsOnDrag As System.Boolean
Dim Error As System.Integer
Dim value As System.Object
 
value = instance.AddExplodeStep2(ExplDist, ExplDirIndex, ReverseDir, ExplAng, RotAxisIndex, ReverseAng, RotateAboutOrigin, AutoSpaceComponentsOnDrag, Error)
```

```

System.object AddExplodeStep2( 
   System.double ExplDist,
   System.int ExplDirIndex,
   System.bool ReverseDir,
   System.double ExplAng,
   System.int RotAxisIndex,
   System.bool ReverseAng,
   System.bool RotateAboutOrigin,
   System.bool AutoSpaceComponentsOnDrag,
   out System.int Error
)
```

```

System.Object^ AddExplodeStep2( 
   System.double ExplDist,
   System.int ExplDirIndex,
   System.bool ReverseDir,
   System.double ExplAng,
   System.int RotAxisIndex,
   System.bool ReverseAng,
   System.bool RotateAboutOrigin,
   System.bool AutoSpaceComponentsOnDrag,
   [Out] System.int Error
) 
```

#### Parameters

*ExplDist*
:   Distance in meters to move the components in this explode step

*ExplDirIndex*
:   Explode direction manipulator index as defined in [swExplodeDirectionIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExplodeDirectionIndex_e.html) (see **Remarks**)

*ReverseDir*
:   True to reverse the explode direction, false to not

*ExplAng*
:   Angle in radians of component rotation (see **Remarks**)

*RotAxisIndex*
:   Rotation manipulator index as defined in [swRotationAxisIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRotationAxisIndex_e.html) (see **Remarks**)

*ReverseAng*
:   True to reverse the direction of ExplAng, false to not

*RotateAboutOrigin*
:   True if each component rotates about its origin, false if not (see **Remarks**)

*AutoSpaceComponentsOnDrag*
:   True to automatically space components on drag, false to not (see **Remarks**)

*Error*
:   Error code as defined in [swCreateExplodeStepError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateExplodeStepError_e.html)

#### Return Value

[Explode step](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)

Remarks

This method:

- Is valid only for an active current explode view. To create an explode view, call [IAssemblyDoc::AutoExplode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.md) or [IAssemblyDoc::CreateExplodedView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateExplodedView.md).
- Always clears the selection list.
- Does not work if the Explode PropertyManager is open.
- Does not work if any component is being edited in the context of the assembly.

If AutoSpaceComponentsOnDrag is set to true, then RotateAboutOrigin is false and ExplAng is 0.0. Set AutoSpaceComponentsOnDrag to false to specify other values for RotateAboutOrigin and ExplAng.

Before calling this method, you must:

1. Use [IConfigurationManager::ActiveConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md) to get the active configuration for the assembly.
2. Call [IAssemblyDoc::ShowExploded2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.md) to activate an explode view.
3. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select:

- Components to move with Mark = 1.
- (Optionally) An explode direction entity (cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), conical face, linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), or [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)) with Mark = 2. Either, both, or neither of the direction entity and ExplDirIndex can be set. If neither, then the Z-direction manipulator index is used.
- (Optionally) A rotation axis with Mark = 32. Valid only if RotateAboutOrigin is set to false. Either, both, or neither of the rotation axis and RotAxisIndex can be set. If neither, then the XY ring index is used.

After calling this method, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md).

For C++, specify VARIANT\_TRUE or VARIANT\_FALSE for ReverseDir, ReverseAng, and RotateAboutOrigin.

To edit a regular explode step, see the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) remarks.

To create an explode step for the explode view of a multibody part, see [IConfiguration::AddPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep.md).

Example

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::AddRadialExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep.md)  
[IConfiguration::DeleteExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.md)  
[IConfiguration::GetExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExplodeStep.md)  
[IConfiguration::GetNumberOfExplodeSteps Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.md)
