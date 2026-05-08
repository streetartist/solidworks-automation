# GetComponentConfigName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetComponentConfigName`

Gets the referenced configuration name of the specified component in this configuration.
Gets the referenced configuration name of the specified component in this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentConfigName( _
   ByVal CompName As System.String _
) As System.String
```

```

Dim instance As IConfiguration
Dim CompName As System.String
Dim value As System.String
 
value = instance.GetComponentConfigName(CompName)
```

```

System.string GetComponentConfigName( 
   System.string CompName
)
```

```

System.String^ GetComponentConfigName( 
   System.String^ CompName
) 
```

#### Parameters

*CompName*
:   Component name

#### Return Value

Referenced configuration name

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
