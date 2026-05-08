# IPartExplodeStep Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep`

Allows access to the explode step of an explode view of a multibody part.
Allows access to the explode step of an explode view of a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPartExplodeStep 
```

```

Dim instance As IPartExplodeStep
```

```

public interface IPartExplodeStep 
```

```

public interface class IPartExplodeStep 
```

Remarks

This interface is valid only for an active current explode view of a multibody part. To create an explode view of a multibody part, call [IPartDoc::CreateExplodedView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateExplodedView.md).

The setter properties and methods of this interface:

- Always clear selection lists.
- Do not work if the Explode PropertyManager is open.
- Do not work if any body is being edited in the context of the multibody part.

To edit an explode step:

1. Use [IPartDoc::ShowExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.md) to activate the explode view of interest.
2. Use [IPartDoc::GetExplodedViewConfigurationName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewConfigurationName.md) to get the configuration for the explode view.
3. Call [IConfiguration::GetPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetPartExplodeStep.md) to access the explode step of interest.
4. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select:
   1. Bodies to move with Mark = 1.
   2. An explode direction entity (cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), conical face, linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), or [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)) with Mark = 2.
5. Call [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md) to get the bodies selected in step 4a.
6. Call [IPartExplodeStep::SetBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~SetBodies.md), passing in the bodies gotten in step 4a.
7. Call [IPartExplodeStep::SetExplodeDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~SetExplodeDirection.md), passing in the explode direction entity that was selected in step 4b. See **Notes**.
8. Modify other explode step properties.

**Notes**:

When editing the object entity for the explode direction, please bear in mind:

| If... | Then... |
| --- | --- |
| Both object and manipulator index are valid | Both object and manipulator index are set. |
| Manipulator index is valid, but object is invalid | Manipulator index is set, and object is unchanged. |
| Object is valid, but manipulator index is invalid | Object is set, and the manipulator index is reset to the Z direction index. |
| Both object and manipulator index are invalid | No values change. |

For more information, see **Exploded Views in Multibody Parts** topic in the SOLIDWORKS user-interface help.

To access explode steps of explode views of assemblies, see [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md).

Example

[Add Multibody Part Explode Step (VBA)](Add_Multibody_Part_Explode_Step_Example.htm)  
[Add Multibody Part Explode Step (VB.NET)](Add_Multibody_Part_Explode_Step_Example_VBNET.htm)  
[Add Multibody Part Explode Step (C#)](Add_Multibody_Part_Explode_Step_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
