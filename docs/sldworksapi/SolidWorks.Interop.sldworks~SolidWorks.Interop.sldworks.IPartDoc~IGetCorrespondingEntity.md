# IGetCorrespondingEntity Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetCorrespondingEntity`

Obsolete. Superseded by IModelDocExtension::GetCorrespondingEntity.
Obsolete. Superseded by [IModelDocExtension::GetCorrespondingEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.md).

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

Dim instance As IPartDoc
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

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
