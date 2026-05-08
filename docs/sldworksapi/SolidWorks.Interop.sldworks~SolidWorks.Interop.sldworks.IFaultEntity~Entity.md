# Entity Property (IFaultEntity)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity`

Obsolete. Superseded by IFaultEntity::Entity2.
Obsolete. Superseded by [IFaultEntity::Entity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Entity( _
   ByVal Index As System.Integer _
) As Entity
```

```

Dim instance As IFaultEntity
Dim Index As System.Integer
Dim value As Entity
 
value = instance.Entity(Index)
```

```

Entity Entity( 
   System.int Index
) {get;}
```

```

property Entity^ Entity {
   Entity^ get(System.int Index);
}
```

#### Parameters

*Index*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaultEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity.md)  
[IFaultEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity_members.md)
