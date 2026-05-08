# ShowExploded Method (IAssemblyDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded`

Obsolete. Superseded by IAssemblyDoc::ShowExploded2.
Obsolete. Superseded by [IAssemblyDoc::ShowExploded2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowExploded( _
   ByVal ShowIt As System.Boolean _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim ShowIt As System.Boolean
Dim value As System.Boolean
 
value = instance.ShowExploded(ShowIt)
```

```

System.bool ShowExploded( 
   System.bool ShowIt
)
```

```

System.bool ShowExploded( 
   System.bool ShowIt
) 
```

#### Parameters

*ShowIt*
:   True if you want to show the existing exploded state for the current assembly configuration, false if you want to show the assembly in the collapsed state

#### Return Value

True if successful in displaying the existing exploded assembly state, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AutoExplode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.md)  
[ViewCollapseAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.md)  
[ViewExplodeAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.md)
