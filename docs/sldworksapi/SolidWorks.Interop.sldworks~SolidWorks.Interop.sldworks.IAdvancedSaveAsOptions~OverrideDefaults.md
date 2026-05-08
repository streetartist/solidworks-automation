# OverrideDefaults Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~OverrideDefaults`

Sets whether to override defaults only when saving an assembly as a part.
Sets whether to override defaults only when saving an assembly as a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

WriteOnly Property OverrideDefaults As System.Boolean
```

```

Dim instance As IAdvancedSaveAsOptions
 
instance.OverrideDefaults = value
```

```

System.bool OverrideDefaults {set;}
```

```

property System.bool OverrideDefaults {
   void set (    System.bool value);
}
```

#### Property Value

True to override defaults, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md)  
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.md)
