# IComponentReload3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IComponentReload3`

Obsolete. Superseded by IAssemblyDoc::ReplaceComponents.
Obsolete. Superseded by [IAssemblyDoc::ReplaceComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IComponentReload3( _
   ByVal Component As Component2, _
   ByVal ReadOnly As System.Boolean, _
   ByVal Options As System.Integer _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim Component As Component2
Dim ReadOnly As System.Boolean
Dim Options As System.Integer
Dim value As System.Integer
 
value = instance.IComponentReload3(Component, ReadOnly, Options)
```

```

System.int IComponentReload3( 
   Component2 Component,
   System.bool ReadOnly,
   System.int Options
)
```

```

System.int IComponentReload3( 
   Component2^ Component,
   System.bool ReadOnly,
   System.int Options
) 
```

#### Parameters

*Component*

*ReadOnly*

*Options*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
