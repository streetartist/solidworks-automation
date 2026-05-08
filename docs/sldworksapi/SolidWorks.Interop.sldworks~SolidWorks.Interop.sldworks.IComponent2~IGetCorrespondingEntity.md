# IGetCorrespondingEntity Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity`

Gets the entity that corresponds with the Dispatch pointer in the context of the component.
Gets the entity that corresponds with the Dispatch pointer in the context of the component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCorrespondingEntity( _
   ByVal PEntity As Entity _
) As Entity
```

```

Dim instance As IComponent2
Dim PEntity As Entity
Dim value As Entity
 
value = instance.IGetCorrespondingEntity(PEntity)
```

```

Entity IGetCorrespondingEntity( 
   Entity PEntity
)
```

```

Entity^ IGetCorrespondingEntity( 
   Entity^ PEntity
) 
```

#### Parameters

*PEntity*
:   Pointer to the [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object (vertex, face, or edge)

#### Return Value

Pointer to the corresponding object in the context of the component

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorresponding.md)  
[IComponent2::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.md)  
[IModelDocExtension::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding.md)  
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.md)
