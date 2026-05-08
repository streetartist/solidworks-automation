# InsertGroundPlane Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGroundPlane`

Obsolete. See IFeatureManager::CreateDefinition and IGroundPlaneFeatureData.
Obsolete. See [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md) and [IGroundPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertGroundPlane( _
   ByVal ReverseDirection As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim ReverseDirection As System.Boolean
Dim value As Feature
 
value = instance.InsertGroundPlane(ReverseDirection)
```

```

Feature InsertGroundPlane( 
   System.bool ReverseDirection
)
```

```

Feature^ InsertGroundPlane( 
   System.bool ReverseDirection
) 
```

#### Parameters

*ReverseDirection*
:   True to reverse the alignment of ground faces relative to the ground plane, false to not

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, select the entity to use as the ground plane using [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) or [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

Call this method to insert a ground plane at each level of a plant assembly. Ground planes are used as reference geometry when inserting published assets at each level.

Call [IAssemblyDoc::ActivateGroundPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ActivateGroundPlane.md) to activate the ground plane on the level where you want to insert a published asset; the asset's ground face snaps to the assembly's activated ground plane. Components with magnetic mates snap only to components that are also on the active ground plane.

Only one ground plane can be active at a given time in each assembly configuration.

See **Large Assemblies > Facility Layout** in the SOLIDWORKS user-interface help.

Example

[Insert and Activate Ground Plane (VBA)](Insert_Ground_Plane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IAssemblyDoc::GetActiveGroundPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetActiveGroundPlane.md)
