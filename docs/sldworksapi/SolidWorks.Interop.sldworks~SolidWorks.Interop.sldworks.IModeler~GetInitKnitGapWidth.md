# GetInitKnitGapWidth Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetInitKnitGapWidth`

Gets the initial gap bound width for knitting a body.
Gets the initial gap bound width for knitting a body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetInitKnitGapWidth() As System.Double
```

```

Dim instance As IModeler
Dim value As System.Double
 
value = instance.GetInitKnitGapWidth()
```

```

System.double GetInitKnitGapWidth()
```

```

System.double GetInitKnitGapWidth(); 
```

#### Return Value

Initial knitting gap width used for body sewing

Remarks

This value is 0 until a call to knit a body is made.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::SetInitKnitGapWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetInitKnitGapWidth.md)
