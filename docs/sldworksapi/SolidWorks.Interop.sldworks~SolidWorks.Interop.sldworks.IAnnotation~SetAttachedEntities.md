# SetAttachedEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities`

Attaches this annotation to the specified entities.
Attaches this annotation to the specified entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAttachedEntities( _
   ByVal AttachedEnts As System.Object _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim AttachedEnts As System.Object
Dim value As System.Boolean
 
value = instance.SetAttachedEntities(AttachedEnts)
```

```

System.bool SetAttachedEntities( 
   System.object AttachedEnts
)
```

```

System.bool SetAttachedEntities( 
   System.Object^ AttachedEnts
) 
```

#### Parameters

*AttachedEnts*
:   Array of entities to attach this annotation to (see **Remarks**)

#### Return Value

True if the annotation is attached to the entities, false if not

Remarks

Not all annotations can be attached to a different entity (i.e., face, edge, or vertex). Experiment with this method to determine which annotations can be attached to which entities.

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
[IAnnotation::ISetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetAttachedEntities.md)  
[IAnnotation::GetAttachedEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.md)
