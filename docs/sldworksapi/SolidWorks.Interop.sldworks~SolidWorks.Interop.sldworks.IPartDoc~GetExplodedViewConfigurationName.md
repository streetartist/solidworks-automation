# GetExplodedViewConfigurationName Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewConfigurationName`

Gets the name of the configuration for the specified explode view of this multibody part.
Gets the name of the configuration for the specified explode view of this multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExplodedViewConfigurationName( _
   ByVal ExplodedViewName As System.String _
) As System.String
```

```

Dim instance As IPartDoc
Dim ExplodedViewName As System.String
Dim value As System.String
 
value = instance.GetExplodedViewConfigurationName(ExplodedViewName)
```

```

System.string GetExplodedViewConfigurationName( 
   System.string ExplodedViewName
)
```

```

System.String^ GetExplodedViewConfigurationName( 
   System.String^ ExplodedViewName
) 
```

#### Parameters

*ExplodedViewName*
:   Name of the explode view whose configuration to get

#### Return Value

Name of the configuration for ExplodedViewName

Example

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::GetExplodedViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewNames.md)  
[IPartDoc::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.md)
