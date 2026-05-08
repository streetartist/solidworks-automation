# Infinite Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~Infinite`

Gets whether the line is infinite or finite.
Gets whether the line is infinite or finite.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Infinite As System.Boolean
```

```

Dim instance As ISketchLine
Dim value As System.Boolean
 
value = instance.Infinite
```

```

System.bool Infinite {get;}
```

```

property System.bool Infinite {
   System.bool get();
}
```

#### Property Value

True if the line is infinite, false (finite) if not

Example

[Make Line Infinite (VBA)](Make_Line_Infinite_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)  
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.md)  
[ISketchLine::MakeInfinite Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~MakeInfinite.md)
