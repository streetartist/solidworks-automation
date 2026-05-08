# PreserveGeometryReferences Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~PreserveGeometryReferences`

Sets whether to preserve geometry references only when saving an assembly as a part.
Sets whether to preserve geometry references only when saving an assembly as a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

WriteOnly Property PreserveGeometryReferences As System.Boolean
```

```

Dim instance As IAdvancedSaveAsOptions
 
instance.PreserveGeometryReferences = value
```

```

System.bool PreserveGeometryReferences {set;}
```

```

property System.bool PreserveGeometryReferences {
   void set (    System.bool value);
}
```

#### Property Value

True to preserve geometry references, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md)  
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.md)
