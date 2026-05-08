# BreakSketchBlocks Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~BreakSketchBlocks`

Gets or sets whether to break sketch blocks.
Gets or sets whether to break sketch blocks.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BreakSketchBlocks As System.Boolean
```

```

Dim instance As IBreakLine
Dim value As System.Boolean
 
instance.BreakSketchBlocks = value
 
value = instance.BreakSketchBlocks
```

```

System.bool BreakSketchBlocks {get; set;}
```

```

property System.bool BreakSketchBlocks {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to break sketch blocks, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.md)  
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.md)
