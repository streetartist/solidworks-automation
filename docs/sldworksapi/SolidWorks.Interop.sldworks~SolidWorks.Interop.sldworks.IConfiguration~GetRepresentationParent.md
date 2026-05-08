# GetRepresentationParent Method (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRepresentationParent`

Gets the Physical Product represented by this configuration.
Gets the Physical Product represented by this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRepresentationParent() As System.String
```

```

Dim instance As IConfiguration
Dim value As System.String
 
value = instance.GetRepresentationParent()
```

```

System.string GetRepresentationParent()
```

```

System.String^ GetRepresentationParent(); 
```

#### Return Value

Physical Product/Family member name

Remarks

This method is valid only:

- For SOLIDWORKS Connected

    - and -

- If [IConfiguration::Get3DExperienceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Get3DExperienceType.md) is not 0

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
