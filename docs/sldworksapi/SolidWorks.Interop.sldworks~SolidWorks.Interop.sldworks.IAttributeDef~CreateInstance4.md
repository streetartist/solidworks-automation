# CreateInstance4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance4`

Obsolete. Superseded by IAttributeDef::CreateInstance5.
Obsolete. Superseded by [IAttributeDef::CreateInstance5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateInstance4( _
   ByVal OwnerDoc As ModelDoc2, _
   ByVal OwnerObj As System.Object, _
   ByVal NameIn As System.String, _
   ByVal Options As System.Integer, _
   ByVal ConfigurationOption As System.Integer _
) As Attribute
```

```

Dim instance As IAttributeDef
Dim OwnerDoc As ModelDoc2
Dim OwnerObj As System.Object
Dim NameIn As System.String
Dim Options As System.Integer
Dim ConfigurationOption As System.Integer
Dim value As Attribute
 
value = instance.CreateInstance4(OwnerDoc, OwnerObj, NameIn, Options, ConfigurationOption)
```

```

Attribute CreateInstance4( 
   ModelDoc2 OwnerDoc,
   System.object OwnerObj,
   System.string NameIn,
   System.int Options,
   System.int ConfigurationOption
)
```

```

Attribute^ CreateInstance4( 
   ModelDoc2^ OwnerDoc,
   System.Object^ OwnerObj,
   System.String^ NameIn,
   System.int Options,
   System.int ConfigurationOption
) 
```

#### Parameters

*OwnerDoc*

*OwnerObj*

*NameIn*

*Options*

*ConfigurationOption*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md)  
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.md)
