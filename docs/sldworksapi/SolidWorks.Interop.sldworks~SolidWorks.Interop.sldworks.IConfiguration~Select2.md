# Select2 Method (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Select2`

Selects the configuration.
Selects the configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select2( _
   ByVal AppendFlag As System.Boolean, _
   ByVal SelectData As SelectData _
) As System.Boolean
```

```

Dim instance As IConfiguration
Dim AppendFlag As System.Boolean
Dim SelectData As SelectData
Dim value As System.Boolean
 
value = instance.Select2(AppendFlag, SelectData)
```

```

System.bool Select2( 
   System.bool AppendFlag,
   SelectData SelectData
)
```

```

System.bool Select2( 
   System.bool AppendFlag,
   SelectData^ SelectData
) 
```

#### Parameters

*AppendFlag*
:   True appends the configuration to the selection list, false replaces the selection  
    list with the configuration

*SelectData*
:   Pointer to the [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the configuration is selected, false if not

Example

[Add Derived Configurations (VBA)](Add_Derived_Configurations_Example_VB.htm)  
[Add Derived Configurations (VB.NET)](Add_Derived_Configurations_Example_VBNET.htm)  
[Add Derived Configurations (C#)](Add_Derived_Configurations_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
