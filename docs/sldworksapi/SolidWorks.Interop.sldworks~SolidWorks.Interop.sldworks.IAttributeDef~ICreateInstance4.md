# ICreateInstance4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~ICreateInstance4`

Obsolete. Superseded by IAttributeDef::CreateInstance5.
Obsolete. Superseded by [IAttributeDef::CreateInstance5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateInstance4( _
   ByVal OwnerDoc As ModelDoc2, _
   ByVal OwnerComp As Component2, _
   ByVal OwnerEntity As Entity, _
   ByVal NameIn As System.String, _
   ByVal Options As System.Integer, _
   ByVal ConfigurationOption As System.Integer _
) As Attribute
```

```

Dim instance As IAttributeDef
Dim OwnerDoc As ModelDoc2
Dim OwnerComp As Component2
Dim OwnerEntity As Entity
Dim NameIn As System.String
Dim Options As System.Integer
Dim ConfigurationOption As System.Integer
Dim value As Attribute
 
value = instance.ICreateInstance4(OwnerDoc, OwnerComp, OwnerEntity, NameIn, Options, ConfigurationOption)
```

```

Attribute ICreateInstance4( 
   ModelDoc2 OwnerDoc,
   Component2 OwnerComp,
   Entity OwnerEntity,
   System.string NameIn,
   System.int Options,
   System.int ConfigurationOption
)
```

```

Attribute^ ICreateInstance4( 
   ModelDoc2^ OwnerDoc,
   Component2^ OwnerComp,
   Entity^ OwnerEntity,
   System.String^ NameIn,
   System.int Options,
   System.int ConfigurationOption
) 
```

#### Parameters

*OwnerDoc*

*OwnerComp*

*OwnerEntity*

*NameIn*

*Options*

*ConfigurationOption*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md)  
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.md)
