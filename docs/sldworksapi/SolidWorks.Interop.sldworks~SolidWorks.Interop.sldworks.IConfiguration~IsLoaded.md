# IsLoaded Method (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsLoaded`

Gets whether a configuration is loaded.
Gets whether a configuration is loaded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsLoaded() As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
value = instance.IsLoaded()
```

```

System.bool IsLoaded()
```

```

System.bool IsLoaded(); 
```

#### Return Value

True if the configuration is loaded, false if not

Remarks

When a configuration is activated, SOLIDWORKS loads it. For example, if a part or assembly document has three configurations named DC1, DC2, and DC3, and DC1 is the active configuration when you open the document, then this method will return true for DC1 and false for DC2 and DC3.

If you activate the configuration named DC2, then this method will return true for DC1 and DC2 because DC1 was previously loaded. If you activate the configuration named DC3, then this method will return true for DC1, DC2, and DC3 because DC1 and DC2 were previously loaded and DC3 is now loaded.

Example

[Are the Assembly Configurations Loaded (VB.NET)](Are_the_Assembly_Configurations_Loaded_Example_VBNET.htm)  
[Are the Assembly Configurations Loaded (VBA)](Are_the_Assembly_Configurations_Loaded_Example_VB.htm)  
[Are the Assembly Configurations Loaded (C#)](Are_the_Assembly_Configurations_Loaded_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
