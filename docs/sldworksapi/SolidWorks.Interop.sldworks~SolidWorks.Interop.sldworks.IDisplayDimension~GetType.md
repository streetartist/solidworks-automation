# GetType Method (IDisplayDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetType`

Obsolete. Superseded by IDisplayDimension::Type2.
Obsolete. Superseded by [IDisplayDimension::Type2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Type2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetType() As System.Integer
```

```

Dim instance As IDisplayDimension
Dim value As System.Integer
 
value = instance.GetType()
```

```

System.int GetType()
```

```

System.int GetType(); 
```

#### Return Value

Dimension type as defined in [swDimensionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionType_e.html)

Remarks

Radial and diametric dimensions both return swRadialDimension. To determine how this radial dimension is currently displayed, use [IDisplayDimension::Diametric](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Diametric.md) and [IDisplayDimension::DisplayAsLinear](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsLinear.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::Type2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Type2.md)  
[IDisplayDimension::Diametric Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Diametric.md)
