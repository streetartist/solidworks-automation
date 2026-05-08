# Unlink Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Unlink`

Unlinks a previously linked display dimension.
Unlinks a previously linked display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Unlink() As System.Integer
```

```

Dim instance As IDisplayDimension
Dim value As System.Integer
 
value = instance.Unlink()
```

```

System.int Unlink()
```

```

System.int Unlink(); 
```

#### Return Value

Error code as defined by [swLinkDimensionError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLinkDimensionError_e.html)

Example

[Unlink Dimensions (VBA)](Unlink_Dimensions_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetLinkedText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLinkedText.md)  
[IDisplayDimension::SetLinkedText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLinkedText.md)  
[IDisplayDimension::IsLinked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsLinked.md)
