# ShapeIntensity Property (IBreakLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~ShapeIntensity`

Gets or sets the shape intensity of a jagged cut break line.
Gets or sets the shape intensity of a jagged cut break line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShapeIntensity As System.Integer
```

```

Dim instance As IBreakLine
Dim value As System.Integer
 
instance.ShapeIntensity = value
 
value = instance.ShapeIntensity
```

```

System.int ShapeIntensity {get; set;}
```

```

property System.int ShapeIntensity {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Shape intensity of a jagged cut break line; valid range is 1 (most) to 5 (least) (see **Remarks**)

Remarks

Call [IBreakLine::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Style.md) to determine if this break line is a jagged cut break line.

Example

[Insert Jagged Cut Break (C#)](Insert_Jagged_Cut_Break_Example_CSharp.htm)  
[Insert Jagged Cut Break (VB.NET)](Insert_Jagged_Cut_Break_Example_VBNET.htm)  
[Insert Jagged Cut Break (VBA)](Insert_Jagged_Cut_Break_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.md)  
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.md)
