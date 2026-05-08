# SaveAllAsCopy Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAllAsCopy`

Sets whether to save all component references as copies.
Sets whether to save all component references as copies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

WriteOnly Property SaveAllAsCopy As System.Boolean
```

```

Dim instance As IAdvancedSaveAsOptions
 
instance.SaveAllAsCopy = value
```

```

System.bool SaveAllAsCopy {set;}
```

```

property System.bool SaveAllAsCopy {
   void set (    System.bool value);
}
```

#### Property Value

True to save all as a copy, false (default) to not

Example

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md)  
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.md)
