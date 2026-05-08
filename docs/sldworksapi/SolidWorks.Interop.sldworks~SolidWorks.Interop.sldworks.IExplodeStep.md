# IExplodeStep Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep`

Allows access to an explode step in the explode view of the active assembly configuration.
Allows access to an explode step in the explode view of the active assembly configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IExplodeStep 
```

```

Dim instance As IExplodeStep
```

```

public interface IExplodeStep 
```

```

public interface class IExplodeStep 
```

Remarks

This interface is valid only for assemblies. To access the explode steps of an explode view of multibody parts, see [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md).

If this is a subassembly explode step, then you can call only one method on this interface, [IExplodeStep::GetSubAssemblyExplodeSteps](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetSubAssemblyExplodeSteps.md), to retrieve the nested explode steps of this subassembly explode step.

The setter properties and methods of this interface:

- Always clear selection lists.
- Do not work if the Explode PropertyManager is open.
- Do not work if any component is being edited in the context of the assembly.

To edit an explode step that is not a subassembly explode step:

1. Use [IConfigurationManager::ActiveConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md) to get the active configuration of the assembly.
2. Access the explode step. See the **Accessors** section.
3. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select:
   1. Components to move with Mark = 1.
   2. An explode direction entity (cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), conical face, linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), or [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)) with Mark = 2 (regular explode steps) or Mark = 34 (radial explode steps).
   3. A rotation axis with Mark = 32, if RotateAboutOrigin is set to false (regular explode steps only).
   4. A diverge direction entity with Mark = 64 (radial explode steps only).
4. Call [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md) to get the components selected in step 3a.
5. Call [IExplodeStep::SetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetComponents.md), passing in the components gotten in step 4.
6. Call [IExplodeStep::SetExplodeDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetExplodeDirection.md), passing in the explode direction entity that was selected in step 3b. See **Notes**.
7. Call [IExplodeStep::SetRotationAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetRotationAxis.md), passing in the rotation axis that was selected in step 3c (for regular explode steps only).
8. Set [IExplodeStep::DivergeDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeDirection.md) to the diverge direction entity that was selected in step 3d (for radial explode steps only). See **Notes**.
9. Modify other explode step properties.

**Notes**:

When editing the object entity for the explode direction or rotation axis, please bear in mind:

| If... | Then... |
| --- | --- |
| Both object and manipulator index are valid | Both object and manipulator index are set. |
| Manipulator index is valid, but object is invalid | Manipulator index is set, and object is unchanged. |
| Object is valid, but manipulator index is invalid | Object is set, but the manipulator index is reset to:   - Z direction index for explode direction. - XY ring index for rotation axis. |
| Both object and manipulator index are invalid | No values change. |

When editing the diverge direction object entity or the diverge from axis flag, please bear in mind:

| If... | Then... |
| --- | --- |
| Diverge direction object is valid | IExplodeStep::DivergeDirection properly sets the diverge direction, and [IExplodeStep::DivergeFromAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeFromAxis.md) is set to true. |
| Diverge direction object is null | IExplodeStep::DivergeDirection is set to null, and IExplodeStep::DivergeFromAxis is set to false. |
| Diverge direction object is invalid | Direction object entity is unchanged. |
| IExplodeStep::DivergeFromAxis is set to false | IExplodeStep::DivergeFromAxis is set to false, and the diverge direction object is set to null. |
| IExplodeStep::DivergeFromAxis is set to true | No values change. |

Example

[Add Regular Explode Step (VBA)](Add_Explode_Step_Example_VB.htm)  
[Edit Radial Explode Step (VBA)](Edit_Radial_Explode_Step_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IAssemblyDoc::ShowExploded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded.md)  
[IModelDoc2::IsExploded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsExploded.md)
