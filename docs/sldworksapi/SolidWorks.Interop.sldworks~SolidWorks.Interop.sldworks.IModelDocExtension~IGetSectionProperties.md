# IGetSectionProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSectionProperties`

Obsolete. Superseded by IModelDocExtension::IGetSectionProperties2.
Obsolete. Superseded by [IModelDocExtension::IGetSectionProperties2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSectionProperties2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSectionProperties( _
   ByVal Count As System.Integer, _
   ByRef Sections As System.Object _
) As System.Double
```

```

Dim instance As IModelDocExtension
Dim Count As System.Integer
Dim Sections As System.Object
Dim value As System.Double
 
value = instance.IGetSectionProperties(Count, Sections)
```

```

System.double IGetSectionProperties( 
   System.int Count,
   ref System.object Sections
)
```

```

System.double IGetSectionProperties( 
   System.int Count,
   System.Object^% Sections
) 
```

#### Parameters

*Count*

*Sections*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
