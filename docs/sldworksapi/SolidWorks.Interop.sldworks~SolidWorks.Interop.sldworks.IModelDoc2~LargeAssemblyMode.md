# LargeAssemblyMode Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LargeAssemblyMode`

Gets or sets Large Assembly Mode for this document.
Gets or sets Large Assembly Mode for this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LargeAssemblyMode As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
instance.LargeAssemblyMode = value
 
value = instance.LargeAssemblyMode
```

```

System.bool LargeAssemblyMode {get; set;}
```

```

property System.bool LargeAssemblyMode {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True enables Large Assembly Mode, false disables it

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
