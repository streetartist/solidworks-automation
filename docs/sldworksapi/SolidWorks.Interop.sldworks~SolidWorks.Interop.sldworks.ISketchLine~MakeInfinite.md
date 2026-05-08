# MakeInfinite Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~MakeInfinite`

Makes a line infinite.
Makes a line infinite.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeInfinite() As System.Boolean
```

```

Dim instance As ISketchLine
Dim value As System.Boolean
 
value = instance.MakeInfinite()
```

```

System.bool MakeInfinite()
```

```

System.bool MakeInfinite(); 
```

#### Return Value

True if the line is changed to infinite, false if not

Remarks

When you change a line from finite to infinite, you cannot change it back to finite.

Example

[Make Line Infinite (VBA)](Make_Line_Infinite_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)  
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.md)  
[ISketchLine::Infinite Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~Infinite.md)
