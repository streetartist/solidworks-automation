# ISetAttachedEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetAttachedEntities`

Attaches this annotation to the specified entities.
Attaches this annotation to the specified entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetAttachedEntities( _
   ByVal Count As System.Integer, _
   ByRef LpArr As System.Object _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim Count As System.Integer
Dim LpArr As System.Object
Dim value As System.Boolean
 
value = instance.ISetAttachedEntities(Count, LpArr)
```

```

System.bool ISetAttachedEntities( 
   System.int Count,
   ref System.object LpArr
)
```

```

System.bool ISetAttachedEntities( 
   System.int Count,
   System.Object^% LpArr
) 
```

#### Parameters

*Count*
:   Number of entities to which to attach this annotation

*LpArr*
:   - in-process, unmanaged C++: Pointer to an array of entities to attach this annotation to (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if the annotation is attached to the entities, false if not

Remarks

Not all annotations can be attached to a different entity (i.e., face, edge, or vertex). Experiment with this method to determine which annotations can be attached to which entities.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetAttachedEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.md)  
[SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.md)
