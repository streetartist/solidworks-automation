# GetAttachedEntities2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2`

Obsolete. Superseded by IAnnotation::GetAttachedEntities3.
Obsolete. Superseded by [IAnnotation::GetAttachedEntities3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttachedEntities2() As System.Object
```

```

Dim instance As IAnnotation
Dim value As System.Object
 
value = instance.GetAttachedEntities2()
```

```

System.object GetAttachedEntities2()
```

```

System.Object^ GetAttachedEntities2(); 
```

#### Return Value

Array of objects

Remarks

This method now supports all annotation types. See [IAnnotation::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetType.md) to determine the type of annotation.

The array returned by this function may contain one or more objects of varying type. To determine the corresponding object type in the IAnnotation::GetAttachedEntites2 array, see [IAnnotation::GetAttachedEntityTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.md). COM applications can use QueryInterface to obtain the specific object from the LPUNKNOWN pointer.

|  |  |
| --- | --- |
| **Object Type** | **Object Returned** |
| swSelFACES | [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) |
| swSelEDGES | [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) |
| swSelVERTICES | [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) |
| swSelSKETCHSEGS | [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) |
| swSelSKETCHPOINTS | [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) |
| swSelNOTHING | NULL (annotation is dangling or unsupported) |

You can associate annotations with some items not listed in the previous table (for example, origins). If this annotation is attached to one or more of those entities, then SOLIDWORKS returns a corresponding NULL in one of the array positions and IAnnotation::GetAttachedEntityTypes indicates the unsupported entity by returning a corresponding swSelNOTHING value. COM applications that call [IAnnotation::GetAttachedEntityCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityCount2.md) include the NULL value in the total count of associated entities.

Likewise, if an annotation has become disassociated from its geometry, then SOLIDWORKS returns a corresponding NULL in one of the array positions and [IAnnotation::GetAttachedEntityTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.md) indicates the dangling item by returning a corresponding swSelNOTHING value.

If this annotation is not associated with any geometry (for example, a note without a leaderline), then SOLIDWORKS returns an empty array.

Example

[Get Types of Entities for Selected Dimension (VBA)](Get_Types_of_Entities_for_Selected_Dimension_Example_VB.htm)  
[Get BOM Balloon Properties (C#)](Get_BOM_Balloon_Properties_Example_CSharp.htm)  
[Get BOM Balloon Properties (VB.NET)](Get_BOM_Balloon_Properties_Example_VBNET.htm)  
[Get BOM Balloon Properties (VBA)](Get_BOM_Balloon_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetAttachedEntityCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityCount2.md)  
[IAnnotation::GetAttachedEntityTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.md)  
[IAnnotation::GetNext3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md)  
[IAnnotation::GetType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetType.md)  
[IAnnotation::SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.md)  
[IAttribute::GetEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntity.md)  
[IAttribute::IGetEntity2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetEntity2.md)  
[IAttribute::GetEntityState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.md)  
[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)  
[IEntity::GetSafeEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetSafeEntity.md)  
[IFaultEntity::Entity2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity2.md)  
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.md)  
[IPartDoc::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityName.md)  
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.md)  
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.md)  
[IAnnotation::SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.md)  
[IAnnotation::ISetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetAttachedEntities.md)
