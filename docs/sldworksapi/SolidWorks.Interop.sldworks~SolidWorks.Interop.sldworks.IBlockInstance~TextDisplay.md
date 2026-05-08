# TextDisplay Property (IBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance~TextDisplay`

Obsolete. Superseded by ISketchBlockInstance::TextDisplay.
Obsolete. Superseded by [ISketchBlockInstance::TextDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~TextDisplay.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TextDisplay As System.Integer
```

```

Dim instance As IBlockInstance
Dim value As System.Integer
 
instance.TextDisplay = value
 
value = instance.TextDisplay
```

```

System.int TextDisplay {get; set;}
```

```

property System.int TextDisplay {
   System.int get();
   void set (    System.int value);
}
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance.md)  
[IBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance_members.md)
