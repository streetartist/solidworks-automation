# Orientation Property (IBreakLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Orientation`

Gets the orientation of this break line in the drawing view.
Gets the orientation of this break line in the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Orientation As System.Integer
```

```

Dim instance As IBreakLine
Dim value As System.Integer
 
value = instance.Orientation
```

```

System.int Orientation {get;}
```

```

property System.int Orientation {
   System.int get();
}
```

#### Property Value

Break orientation as defined in [swBreakLineOrientation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineOrientation_e.html)

Example

[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)  
[Create Break View (VB.NET)](Create_Broken_View_Example_VBNET.htm)  
[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.md)  
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.md)  
[IBreakline::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~GetPosition.md)  
[IBreakline::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~SetPosition.md)
