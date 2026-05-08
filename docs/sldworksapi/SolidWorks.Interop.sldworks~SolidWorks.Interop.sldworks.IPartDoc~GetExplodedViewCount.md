# GetExplodedViewCount Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewCount`

Gets the number of explode views in the specified configuration of this multibody part.
Gets the number of explode views in the specified configuration of this multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExplodedViewCount( _
   ByVal ConfigurationName As System.String _
) As System.Integer
```

```

Dim instance As IPartDoc
Dim ConfigurationName As System.String
Dim value As System.Integer
 
value = instance.GetExplodedViewCount(ConfigurationName)
```

```

System.int GetExplodedViewCount( 
   System.string ConfigurationName
)
```

```

System.int GetExplodedViewCount( 
   System.String^ ConfigurationName
) 
```

#### Parameters

*ConfigurationName*
:   Name of the configuration

#### Return Value

Number of explode views in the specified configuration

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.md)  
[IPartDoc::GetExplodedViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewNames.md)  
[IPartDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewConfigurationName.md)  
[IPartDoc::CreateExplodedView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateExplodedView.md)
