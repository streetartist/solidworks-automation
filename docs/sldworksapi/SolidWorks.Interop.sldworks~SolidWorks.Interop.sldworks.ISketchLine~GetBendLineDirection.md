# GetBendLineDirection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~GetBendLineDirection`

Gets whether the sketch line is a bendline, and, if it is, the direction of the bendline.
Gets whether the sketch line is a bendline, and, if it is, the direction of the bendline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBendLineDirection() As System.Integer
```

```

Dim instance As ISketchLine
Dim value As System.Integer
 
value = instance.GetBendLineDirection()
```

```

System.int GetBendLineDirection()
```

```

System.int GetBendLineDirection(); 
```

#### Return Value

Bendline direction as defined in [swBendLineDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendLineDirection_e.html)

Example

[Get Direction of Bendline (C#)](Get_Direction_of_Bendline_Example_CSharp.htm)  
[Get Direction of Bendline (VB.NET)](Get_Direction_of_Bendline_Example_VBNET.htm)  
[Get Direction of Bendline (VBA)](Get_Direction_of_Bendline_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)  
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.md)
