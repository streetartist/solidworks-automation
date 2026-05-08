# CreateInstance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance`

Obsolete. Superseded by IAttributeDef::CreateInstance5.
Obsolete. Superseded by [IAttributeDef::CreateInstance5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateInstance( _
   ByVal OwnerDoc As System.Object, _
   ByVal OwnerEntity As System.Object, _
   ByVal NameIn As System.String _
) As System.Object
```

```

Dim instance As IAttributeDef
Dim OwnerDoc As System.Object
Dim OwnerEntity As System.Object
Dim NameIn As System.String
Dim value As System.Object
 
value = instance.CreateInstance(OwnerDoc, OwnerEntity, NameIn)
```

```

System.object CreateInstance( 
   System.object OwnerDoc,
   System.object OwnerEntity,
   System.string NameIn
)
```

```

System.Object^ CreateInstance( 
   System.Object^ OwnerDoc,
   System.Object^ OwnerEntity,
   System.String^ NameIn
) 
```

#### Parameters

*OwnerDoc*

*OwnerEntity*

*NameIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md)  
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.md)
