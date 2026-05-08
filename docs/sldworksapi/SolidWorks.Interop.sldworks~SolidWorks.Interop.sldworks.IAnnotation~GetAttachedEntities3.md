# GetAttachedEntities3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities3`

Gets the entities to which this annotation is attached.
Gets the entities to which this annotation is attached.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttachedEntities3() As System.Object
```

```

Dim instance As IAnnotation
Dim value As System.Object
 
value = instance.GetAttachedEntities3()
```

```

System.object GetAttachedEntities3()
```

```

System.Object^ GetAttachedEntities3(); 
```

#### Return Value

Array of objects

Remarks

This method now supports all annotation types. See [IAnnotation::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetType.md) to determine the type of annotation.

The array returned by this function may contain one or more objects of varying type. To determine the corresponding object type in the IAnnotation::GetAttachedEntites3 array, see [IAnnotation::GetAttachedEntityTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.md) or [IAnnotation::IGetAttachedEntityTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetAttachedEntityTypes.md). COM applications can use QueryInterface to obtain the specific object from the LPUNKNOWN pointer.

|  |  |
| --- | --- |
| **Object Type** | **Object Returned** |
| swSelFACES | [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) |
| swSelEDGES | [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) |
| swSelVERTICES | [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) |
| swSelSKETCHSEGS | [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) |
| swSelSKETCHPOINTS | [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) |
| swSelSilhouettes | [ISilhouetteEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.md) |
| swSelNOTHING | NULL (annotation is dangling or unsupported) |

You can associate annotations with some items not listed in the previous table (for example, origins). If this annotation is attached to one or more of those entities, then SOLIDWORKS returns a corresponding NULL in one of the array positions and IAnnotation::GetAttachedEntityTypes indicates the unsupported entity by returning a corresponding swSelNOTHING value. COM applications that call [IAnnotation::GetAttachedEntityCount3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityCount3.md) include the NULL value in the total count of associated entities.

Likewise, if an annotation has become disassociated from its geometry, then SOLIDWORKS returns a corresponding NULL in one of the array positions and [IAnnotation::GetAttachedEntityTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.md) indicates the dangling item by returning a corresponding swSelNOTHING value.

If this annotation is not associated with any geometry (for example, a note without a leaderline), then SOLIDWORKS returns an empty array.

Example

[Get Types of Entities Attached to Selected Annotation (VBA)](Get_Types_of_Entities_for_Selected_Dimension_Example_VB.htm)  
[Get Types of Entities Attached to Selected Annotation (VB.NET)](Get_Types_of_Entities_for_Selected_Dimension_Example_VBNET.htm)  
[Get Types of Entities Attached to Selected Annotation (C#)](Get_Types_of_Entities_for_Selected_Dimension_Example_CSharp.htm)  
[Select Silhouette Edge Attached to Note (C#)](Select_Silhouette_Edge_Attached_to_Note_Example_CSharp.htm)  
[Select Silhouette Edge Attached to Note (VB.NET)](Select_Silhouette_Edge_Attached_to_Note_Example_VBNET.htm)  
[Select Silhouette Edge Attached to Note (VBA)](Select_Silhouette_Edge_Attached_to_Note_Example_VB.htm)  
[Attach Annotation to Entity (C#)](Attach_Annotation_to_Entity_Example_CSharp.htm)  
[Attach Annotation to Entity (VB.NET)](Attach_Annotation_to_Entity_Example_VBNET.htm)  
[Attach Annotation to Entity (VBA)](Attach_Annotation_to_Entity_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetNext3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md)  
[IAnnotation::ISetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetAttachedEntities.md)  
[IAnnotation::SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.md)
