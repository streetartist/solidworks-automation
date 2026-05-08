# TextDisplay Property (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~TextDisplay`

Gets or sets whether to display text for this block instance.
Gets or sets whether to display text for this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TextDisplay As System.Integer
```

```

Dim instance As ISketchBlockInstance
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

#### Property Value

Display state as defined in [swBlockInstanceTextDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBlockInstanceTextDisplay_e.html)

Example

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)
