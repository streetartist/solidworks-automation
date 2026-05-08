# GetCorrespondingEntity Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity`

Gets the entity that corresponds with the Dispatch pointer in the context of the component.
Gets the entity that corresponds with the Dispatch pointer in the context of the component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCorrespondingEntity( _
   ByVal Entity As System.Object _
) As System.Object
```

```

Dim instance As IComponent2
Dim Entity As System.Object
Dim value As System.Object
 
value = instance.GetCorrespondingEntity(Entity)
```

```

System.object GetCorrespondingEntity( 
   System.object Entity
)
```

```

System.Object^ GetCorrespondingEntity( 
   System.Object^ Entity
) 
```

#### Parameters

*Entity*
:   Pointer to the Dispatch object of an entity (vertex, face, or edge)

#### Return Value

Pointer to the corresponding object in the context of the component

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorresponding.md)  
[IComponent2::IGetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity.md)  
[IModelDocExtension::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding.md)  
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.md)
