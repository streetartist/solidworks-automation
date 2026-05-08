# DeleteNamedView Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~DeleteNamedView`

Obsolete. Superseded by IModelDoc2::DeleteNamedView.
Obsolete. Superseded by [IModelDoc2::DeleteNamedView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteNamedView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteNamedView( _
   ByVal ViewName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim ViewName As System.String
Dim value As System.Boolean
 
value = instance.DeleteNamedView(ViewName)
```

```

System.bool DeleteNamedView( 
   System.string ViewName
)
```

```

System.bool DeleteNamedView( 
   System.String^ ViewName
) 
```

#### Parameters

*ViewName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
