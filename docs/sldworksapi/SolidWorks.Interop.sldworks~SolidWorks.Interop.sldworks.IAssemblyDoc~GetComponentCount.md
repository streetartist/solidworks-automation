# GetComponentCount Method (IAssemblyDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentCount`

Gets the number of components in the active configuration of this assembly.
Gets the number of components in the active configuration of this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentCount( _
   ByVal ToplevelOnly As System.Boolean _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim ToplevelOnly As System.Boolean
Dim value As System.Integer
 
value = instance.GetComponentCount(ToplevelOnly)
```

```

System.int GetComponentCount( 
   System.bool ToplevelOnly
)
```

```

System.int GetComponentCount( 
   System.bool ToplevelOnly
) 
```

#### Parameters

*ToplevelOnly*
:   True to get only the number of components at the top level of the FeatureManager design tree, false to get the number of top level and all child components in the FeatureManager design tree

#### Return Value

Number of components

Remarks

Use this method before using [IAssemblyDoc::IGetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetComponents.md) to determine the size of the array to pass into that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IComponent2::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.md)  
[IComponent2::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.md)  
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.md)  
[IConfiguration::IGetRootComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.md)  
[IConfigurationManager::AddConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration.md)
