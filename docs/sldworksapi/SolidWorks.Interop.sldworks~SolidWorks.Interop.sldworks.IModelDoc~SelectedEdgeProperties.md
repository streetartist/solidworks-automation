# SelectedEdgeProperties Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectedEdgeProperties`

Obsolete. Superseded by IModelDoc2::SelectedEdgeProperties.
Obsolete. Superseded by [IModelDoc2::SelectedEdgeProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedEdgeProperties.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectedEdgeProperties( _
   ByVal EdgeName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim EdgeName As System.String
Dim value As System.Boolean
 
value = instance.SelectedEdgeProperties(EdgeName)
```

```

System.bool SelectedEdgeProperties( 
   System.string EdgeName
)
```

```

System.bool SelectedEdgeProperties( 
   System.String^ EdgeName
) 
```

#### Parameters

*EdgeName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
