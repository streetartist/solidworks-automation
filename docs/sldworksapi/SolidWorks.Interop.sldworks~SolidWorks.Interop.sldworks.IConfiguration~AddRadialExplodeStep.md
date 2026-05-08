# AddRadialExplodeStep Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep`

Adds a radial explode step to the explode view of the active configuration.
Adds a radial explode step to the explode view of the active configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddRadialExplodeStep( _
   ByVal ExplDist As System.Double, _
   ByVal ExplAng As System.Double, _
   ByVal DivergeFromAxis As System.Boolean, _
   ByRef Error As System.Integer _
) As System.Object
```

```

Dim instance As IConfiguration
Dim ExplDist As System.Double
Dim ExplAng As System.Double
Dim DivergeFromAxis As System.Boolean
Dim Error As System.Integer
Dim value As System.Object
 
value = instance.AddRadialExplodeStep(ExplDist, ExplAng, DivergeFromAxis, Error)
```

```

System.object AddRadialExplodeStep( 
   System.double ExplDist,
   System.double ExplAng,
   System.bool DivergeFromAxis,
   out System.int Error
)
```

```

System.Object^ AddRadialExplodeStep( 
   System.double ExplDist,
   System.double ExplAng,
   System.bool DivergeFromAxis,
   [Out] System.int Error
) 
```

#### Parameters

*ExplDist*
:   Distance in meters to move the components in this explode step

*ExplAng*
:   Angle in radians of rotation about component origins

*DivergeFromAxis*
:   True to move components at an angle from the selected explode direction, false to not (see **Remarks**)

*Error*
:   Error code as defined in [swCreateExplodeStepError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateExplodeStepError_e.html)

#### Return Value

[Explode step](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)

Remarks

This method:

- Is valid only for an active current explode view. To create an explode view, call [IAssemblyDoc::AutoExplode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.md) or [IAssemblyDoc::CreateExplodedView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateExplodedView.md).
- Always clears the selection list.
- Does not work if the Explode PropertyManager is open.
- Does not work if any component is being edited in the context of the assembly.

Before calling this method, you must:

1. Use [IConfigurationManager::ActiveConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md) to get the active configuration for the assembly.
2. Call [IAssemblyDoc::ShowExploded2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.md) to activate an explode view.
3. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select:

- Components to move with Mark = 1.
- An explode direction entity (cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), conical face, linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), or [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)) with Mark = 34.
- A diverge direction entity (cylindrical face, conical face, linear edge, or axis) with Mark = 64. The selected entity must form an angle with the direction entity. If DivergeFromAxis is set to true and an invalid diverge direction is selected, then DivergeFromAxis is set to false, and the direction entity is set to null. If DivergeFromAxis is set to false, then the direction entity is set to null.

After calling this method, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md).

For C++, specify VARIANT\_TRUE or VARIANT\_FALSE for ReverseDir and DivergeFromAxis.

To edit a radial explode step, see the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) remarks.

To create an explode step for the explode view of a multibody part, see [IConfiguration::AddPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::GetNumberOfExplodeSteps Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.md)  
[IConfiguration::GetExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExplodeStep.md)  
[IConfiguration::DeleteExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.md)  
[IConfiguration::AddExplodeStep2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep2.md)
