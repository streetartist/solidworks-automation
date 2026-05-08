# IExplodeStep Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members`

Allows access to an explode step in the explode view of the active assembly configuration.
The following tables list the members exposed by [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AutoSpaceComponentsOnDrag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~AutoSpaceComponentsOnDrag.md) | Gets or sets whether to automatically space a group of components equally along an axis as you drag them. |
| Property | [DivergeDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeDirection.md) | Gets or sets the diverge direction entity for this radial explode step. |
| Property | [DivergeFromAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeFromAxis.md) | Gets or sets whether to move components at an angle from the explode direction of this radial explode step. |
| Property | [ExplodeDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeDistance.md) | Gets or sets the distance to move components in this regular or radial explode step. |
| Property | [ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.md) | Gets the type of this explode step. |
| Property | [Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~Name.md) | Gets or sets the name of this explode step. |
| Property | [ReverseRotationDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ReverseRotationDirection.md) | Gets or sets whether to reverse the direction of rotation of components in this regular explode step. |
| Property | [ReverseTranslationDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ReverseTranslationDirection.md) | Gets or sets whether to reverse the explode direction in this regular explode step. |
| Property | [RotateAboutEachComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotateAboutEachComponentOrigin.md) | Gets or sets whether components rotate about their origins in this regular explode step. |
| Property | [RotationAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotationAngle.md) | Gets or sets the angle of component rotation in this regular or radial explode step. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponent.md) | Gets the specified component in this explode step. |
| Method | [GetComponentName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentName.md) | Gets the name of the specified component in this explode step. |
| Method | [GetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponents.md) | Gets the components of this explode step. |
| Method | [GetComponentXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentXform.md) | Gets the transform of this explode step. |
| Method | [GetExplodeDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetExplodeDirection.md) | Gets the explode direction (manipulator index and entity) for this explode step. |
| Method | [GetNumOfComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.md) | Gets the number of components in this explode step. |
| Method | [GetRotationAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetRotationAxis.md) | Gets the rotation axis (manipulator index and entity) for this regular explode step. |
| Method | [GetSpecificComponentXForm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetSpecificComponentXForm.md) | Gets the transformation matrix of the specified component in this explode step. |
| Method | [GetSubAssemblyExplodeSteps](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetSubAssemblyExplodeSteps.md) | Gets the explode steps of this subassembly explode step. |
| Method | [IGetComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~IGetComponent.md) | Gets the specified component in this explode step. |
| Method | [IGetComponentXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~IGetComponentXform.md) | Gets the transform for this explode step. |
| Method | [IsSubAssemblyRigid](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~IsSubAssemblyRigid.md) | Gets whether the subassembly is rigid or flexible. |
| Method | [SetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetComponents.md) | Specifies the components of this explode step. |
| Method | [SetExplodeDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetExplodeDirection.md) | Sets the explode direction (manipulator index and entity) for this explode step. |
| Method | [SetRotationAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetRotationAxis.md) | Sets the rotation axis (manipulator index and entity) for this regular explode step. |

[Top](#top)

 

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IAssemblyDoc::ShowExploded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded.md)  
[IModelDoc2::IsExploded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsExploded.md)
