# AddPartExplodeStep Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep`

Adds an explode step to the specified explode view of a multibody part.
Adds an explode step to the specified explode view of a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddPartExplodeStep( _
   ByVal ExplodeView As System.String, _
   ByVal ExplDist As System.Double, _
   ByVal ExplDirIndex As System.Integer, _
   ByVal ReverseDir As System.Boolean, _
   ByVal AutoSpaceBodiesOnDrag As System.Boolean, _
   ByRef Error As System.Integer _
) As System.Object
```

```

Dim instance As IConfiguration
Dim ExplodeView As System.String
Dim ExplDist As System.Double
Dim ExplDirIndex As System.Integer
Dim ReverseDir As System.Boolean
Dim AutoSpaceBodiesOnDrag As System.Boolean
Dim Error As System.Integer
Dim value As System.Object
 
value = instance.AddPartExplodeStep(ExplodeView, ExplDist, ExplDirIndex, ReverseDir, AutoSpaceBodiesOnDrag, Error)
```

```

System.object AddPartExplodeStep( 
   System.string ExplodeView,
   System.double ExplDist,
   System.int ExplDirIndex,
   System.bool ReverseDir,
   System.bool AutoSpaceBodiesOnDrag,
   out System.int Error
)
```

```

System.Object^ AddPartExplodeStep( 
   System.String^ ExplodeView,
   System.double ExplDist,
   System.int ExplDirIndex,
   System.bool ReverseDir,
   System.bool AutoSpaceBodiesOnDrag,
   [Out] System.int Error
) 
```

#### Parameters

*ExplodeView*
:   Name of the explode view to which to add this explode step

*ExplDist*
:   Distance in meters to move the selected bodies in this explode step

*ExplDirIndex*
:   Explode direction manipulator index as defined in [swExplodeDirectionIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExplodeDirectionIndex_e.html) (see **Remarks**)

*ReverseDir*
:   True to reverse the explode direction, false to not

*AutoSpaceBodiesOnDrag*
:   True to automatically space selected bodies on drag, false to not

*Error*
:   Error code as defined in [swCreatePartExplodeStepError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreatePartExplodeStepError_e.html)

#### Return Value

[IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md)

Remarks

This method:

- Is valid only for an active, current explode view of a multibody part.
- Always clears the selection list.
- Does not work if the Explode PropertyManager is open.
- Does not work if any body is being edited in the context of the part.

Before calling this method, you must:

1. Create an explode view in the active, current configuration of the multibody part. To create an explode view, call [IPartDoc::CreateExplodedView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateExplodedView.md).
2. Populate ExplodeView with [IConfiguration::GetCurrentPartExplodeViewName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCurrentPartExplodeViewName.md).
3. Call [IPartDoc::ShowExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.md) to activate the explode view to which to add an explode step.
4. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select:

- Bodies to move with Mark = 1.
- (Optionally) An explode direction entity (cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), conical face, linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), or [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)) with Mark = 2. Either, both, or neither of the direction entity and ExplDirIndex can be set. If neither, then the Z-direction manipulator index is used.

After calling this method, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md).

For C++, specify VARIANT\_TRUE or VARIANT\_FALSE for ReverseDir.

To edit an explode step, see the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md) remarks.

To create an explode step for the explode view of an assembly, see [IConfiguration::AddExplodeStep2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep2.md) and [IConfiguration::AddRadialExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep.md).

Example

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::DeleteExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.md)  
[IConfiguration::GetNumberOfPartExplodeSteps Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfPartExplodeSteps.md)  
[IConfiguration::GetPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetPartExplodeStep.md)
