# ShowExploded Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded`

Displays the specified explode view for this multibody part.
Displays the specified explode view for this multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowExploded( _
   ByVal ShowIt As System.Boolean, _
   ByVal ExplodeViewName As System.String _
) As System.Boolean
```

```

Dim instance As IPartDoc
Dim ShowIt As System.Boolean
Dim ExplodeViewName As System.String
Dim value As System.Boolean
 
value = instance.ShowExploded(ShowIt, ExplodeViewName)
```

```

System.bool ShowExploded( 
   System.bool ShowIt,
   System.string ExplodeViewName
)
```

```

System.bool ShowExploded( 
   System.bool ShowIt,
   System.String^ ExplodeViewName
) 
```

#### Parameters

*ShowIt*
:   True to show ExplodeViewName in its exploded state, false to show it in its collapsed state

*ExplodeViewName*
:   Name of the explode view to show

#### Return Value

True if the explode view displays correctly, false if not

Remarks

This method only works with explode views in the current, active configuration.

Example

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewConfigurationName.md)  
[IPartDoc::GetExplodedViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewNames.md)
