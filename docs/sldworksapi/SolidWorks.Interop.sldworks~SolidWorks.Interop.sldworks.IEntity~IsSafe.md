# IsSafe Property (IEntity)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IsSafe`

Gets whether this IEntity object survived a rebuild.
Gets whether this [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object survived a rebuild.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsSafe As System.Boolean
```

```

Dim instance As IEntity
Dim value As System.Boolean
 
value = instance.IsSafe
```

```

System.bool IsSafe {get;}
```

```

property System.bool IsSafe {
   System.bool get();
}
```

#### Property Value

True if the [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object survived the rebuild, false if not

Remarks

The IEntity::IsSafe property is read-only and does not persist from session to session. To make an entity safe, use [IEntity::GetSafeEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetSafeEntity.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)  
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.md)
