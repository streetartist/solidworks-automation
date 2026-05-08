# ConfigurationsToSave Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ConfigurationsToSave`

Sets the subset of configurations to save.
Sets the subset of configurations to save.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

WriteOnly Property ConfigurationsToSave As System.Object
```

```

Dim instance As IAdvancedSaveAsOptions
 
instance.ConfigurationsToSave = value
```

```

System.object ConfigurationsToSave {set;}
```

```

property System.Object^ ConfigurationsToSave {
   void set (    System.Object^ value);
}
```

#### Property Value

Array of configurations to save

Remarks

The active configuration is always saved with the subset of configurations.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md)  
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.md)
