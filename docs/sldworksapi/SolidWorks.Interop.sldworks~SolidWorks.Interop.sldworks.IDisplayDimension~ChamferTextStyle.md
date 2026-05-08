# ChamferTextStyle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ChamferTextStyle`

Gets or sets the text style for chamfer dimensions.
Gets or sets the text style for chamfer dimensions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ChamferTextStyle As System.Integer
```

```

Dim instance As IDisplayDimension
Dim value As System.Integer
 
instance.ChamferTextStyle = value
 
value = instance.ChamferTextStyle
```

```

System.int ChamferTextStyle {get; set;}
```

```

property System.int ChamferTextStyle {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Text style for chamfer dimensions only as defined by [swDetailingChamferDimLeaderTextStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetailingChamferDimLeaderTextStyle_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
