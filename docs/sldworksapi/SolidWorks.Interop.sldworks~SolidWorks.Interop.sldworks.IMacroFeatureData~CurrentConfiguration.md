# CurrentConfiguration Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~CurrentConfiguration`

Gets the macro feature configuration being rebuilt.
Gets the macro feature configuration being rebuilt.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CurrentConfiguration As Configuration
```

```

Dim instance As IMacroFeatureData
Dim value As Configuration
 
value = instance.CurrentConfiguration
```

```

Configuration CurrentConfiguration {get;}
```

```

property Configuration^ CurrentConfiguration {
   Configuration^ get();
}
```

#### Property Value

[Configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md) being rebuilt

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)
