# ICreateInstance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~ICreateInstance`

Obsolete. Superseded by IAttributeDef::CreateInstance5.
Obsolete. Superseded by [IAttributeDef::CreateInstance5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateInstance( _
   ByVal OwnerDoc As ModelDoc, _
   ByVal OwnerEntity As Entity, _
   ByVal NameIn As System.String _
) As Attribute
```

```

Dim instance As IAttributeDef
Dim OwnerDoc As ModelDoc
Dim OwnerEntity As Entity
Dim NameIn As System.String
Dim value As Attribute
 
value = instance.ICreateInstance(OwnerDoc, OwnerEntity, NameIn)
```

```

Attribute ICreateInstance( 
   ModelDoc OwnerDoc,
   Entity OwnerEntity,
   System.string NameIn
)
```

```

Attribute^ ICreateInstance( 
   ModelDoc^ OwnerDoc,
   Entity^ OwnerEntity,
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
