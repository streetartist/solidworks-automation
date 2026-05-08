# TextVisible Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~TextVisible`

Obsolete. Superseded by ISketchBlockInstance::TextDisplay.
Obsolete. Superseded by [ISketchBlockInstance::TextDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~TextDisplay.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TextVisible As System.Boolean
```

```

Dim instance As ICustomSymbol
Dim value As System.Boolean
 
instance.TextVisible = value
 
value = instance.TextVisible
```

```

System.bool TextVisible {get; set;}
```

```

property System.bool TextVisible {
   System.bool get();
   void set (    System.bool value);
}
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.md)  
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.md)
