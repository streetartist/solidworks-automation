# GetNamedViewRotation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetNamedViewRotation`

Gets the specified named view orientation matrix with respect to the Front view.
Gets the specified named view orientation matrix with respect to the Front view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNamedViewRotation( _
   ByVal Name As System.String _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Name As System.String
Dim value As System.Object
 
value = instance.GetNamedViewRotation(Name)
```

```

System.object GetNamedViewRotation( 
   System.string Name
)
```

```

System.Object^ GetNamedViewRotation( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of the named view

#### Return Value

Array of 9 doubles describing the view rotation with respect to the Front view

Remarks

The end-user may have redefined the Front view to be something other than the X-Y plane.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IGetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetNamedViewRotation.md)  
[IModelDoc2::GetStandardViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetStandardViewRotation.md)  
[IModelDoc2::IGetStandardViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetStandardViewRotation.md)  
[IModelDoc2::DeleteNamedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteNamedView.md)  
[IModelDoc2::NameView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~NameView.md)  
[IModelDoc2::ShowNamedView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowNamedView2.md)
