# GetAttachedEntityTypes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityTypes`

Gets the types of entities attached to this annotation.
Gets the types of entities attached to this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttachedEntityTypes() As System.Object
```

```

Dim instance As IAnnotation
Dim value As System.Object
 
value = instance.GetAttachedEntityTypes()
```

```

System.object GetAttachedEntityTypes()
```

```

System.Object^ GetAttachedEntityTypes(); 
```

#### Return Value

Array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) that indicate the attached entity types as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

Remarks

This method supports all annotation types. Use [IAnnotation::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetType.md) to determine the annotation type.

This method returns an array of longs or integers indicating object types. The list of object types corresponds to the list of objects returned by [IAnnotation::GetAttachedEntities3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities3.md).

You can associate annotations with additional items not listed in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html). If this annotation is attached to one or more entities not listed in swSelectType\_e, then this method and [IAnnotation::IGetAttachedEntityTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetAttachedEntityTypes.md) return swSelNOTHING in a position in the array corresponding to the unlisted item. IAnnotation::GetAttachedEntities3 indicates an unsupported entity by returning a null value in the position in the array corresponding to the unsupported entity. COM applications that call [IAnnotation::GetAttachedEntityCount3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityCount3.md) include the null value in the total count of associated entities.

If an annotation is disassociated from its geometry (i.e., dangling), then IAnnotation::GetAttachedEntities3 returns a null value in the position in the array corresponding to the dangling item, and this method returns swSelNOTHING in the position in the array corresponding to the dangling item.

NOTE: If this annotation is not associated with any geometry, then this method and IAnnotation::GetAttachedEntities3 return empty arrays.

Example

[Attach Annotation to Entity (C#)](Attach_Annotation_to_Entity_Example_CSharp.htm)  
[Attach Annotation to Entity (VB.NET)](Attach_Annotation_to_Entity_Example_VBNET.htm)  
[Attach Annotation to Entity (VBA)](Attach_Annotation_to_Entity_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.md)
