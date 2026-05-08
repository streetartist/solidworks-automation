# GetComponentSuppressionState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetComponentSuppressionState`

Gets the suppression state of the specified component in this configuration.
Gets the suppression state of the specified component in this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentSuppressionState( _
   ByVal CompName As System.String _
) As System.Boolean
```

```

Dim instance As IConfiguration
Dim CompName As System.String
Dim value As System.Boolean
 
value = instance.GetComponentSuppressionState(CompName)
```

```

System.bool GetComponentSuppressionState( 
   System.string CompName
)
```

```

System.bool GetComponentSuppressionState( 
   System.String^ CompName
) 
```

#### Parameters

*CompName*
:   Component name

#### Return Value

True if the configuration is suppressed, false if not

Remarks

SOLIDWORKS 2001Plus SP1, Revision Number 10.1

Example

[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)  
[Get Whether Components Are Laoded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)  
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
