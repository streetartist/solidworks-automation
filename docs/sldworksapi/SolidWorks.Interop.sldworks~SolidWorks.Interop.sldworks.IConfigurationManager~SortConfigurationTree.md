# SortConfigurationTree Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SortConfigurationTree`

Specifies the order in which to list configurations in the ConfigurationManager.
Specifies the order in which to list configurations in the ConfigurationManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SortConfigurationTree( _
   ByVal InSelType As System.Integer _
) 
```

```

Dim instance As IConfigurationManager
Dim InSelType As System.Integer
 
instance.SortConfigurationTree(InSelType)
```

```

void SortConfigurationTree( 
   System.int InSelType
)
```

```

void SortConfigurationTree( 
   System.int InSelType
) 
```

#### Parameters

*InSelType*
:   Order in which to list configurations in the ConfigurationManager as defined in [swConfigTreeSortType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConfigTreeSortType_e.html)

Example

[Specify Order of Configurations (C#)](Specify_Order_of_Configurations_Example_CSharp.htm)  
[Specify Order of Configurations (VB.NET)](Specify_Order_of_Configurations_Example_VBNET.htm)  
[Specify Order of Configurations (VBA)](Specify_Order_of_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)
