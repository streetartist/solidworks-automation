# DeleteNamedView Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteNamedView`

Deletes the specified model view.
Deletes the specified model view.

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

Dim instance As IModelDoc2
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
:   Name of the model view to delete

#### Return Value

True if the named view is deleted, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ShowNamedView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowNamedView2.md)  
[IModelDoc2::NameView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~NameView.md)  
[IModelDocExtension::GetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetNamedViewRotation.md)  
[IModelDocExtension::IGetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetNamedViewRotation.md)
