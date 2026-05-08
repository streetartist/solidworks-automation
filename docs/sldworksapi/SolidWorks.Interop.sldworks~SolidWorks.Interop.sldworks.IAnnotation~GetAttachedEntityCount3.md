# GetAttachedEntityCount3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityCount3`

Gets the number of entities to which this annotation is attached.
Gets the number of entities to which this annotation is attached.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttachedEntityCount3() As System.Integer
```

```

Dim instance As IAnnotation
Dim value As System.Integer
 
value = instance.GetAttachedEntityCount3()
```

```

System.int GetAttachedEntityCount3()
```

```

System.int GetAttachedEntityCount3(); 
```

#### Return Value

Number of entities to which this annotation is attached

Remarks

This method supports all annotation types. See [IAnnotation::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetType.md) to determine the type of annotation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetAttachedEntities3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities3.md)  
[IAnnotation::GetAttachedEntityTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.md)  
[IAnnotation::GetNext3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md)  
[IAnnotation::GetType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetType.md)  
[IAnnotation::IGetAttachedEntityTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetAttachedEntityTypes.md)  
[IAnnotation::ISetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetAttachedEntities.md)  
[IAnnotation::SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.md)
