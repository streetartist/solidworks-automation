# IsDefeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDefeature`

Gets whether this configuration is a defeature configuration.
Gets whether this configuration is a defeature configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsDefeature() As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
value = instance.IsDefeature()
```

```

System.bool IsDefeature()
```

```

System.bool IsDefeature(); 
```

#### Return Value

True if this configuration is a defeature configuration, false if not

Remarks

A defeature configuration is a type of derived configuration. After using the Defeature tool to remove details from assemblies, multibody parts, and single-body parts, you can save the less-detailed model as a configuration and maintain references to the original part or assembly.

For more information see the **SOLIDWORKS user-interface help > Assemblies > Other Assembly Techniques > Defeature** topic.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::IsDerived Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDerived.md)
