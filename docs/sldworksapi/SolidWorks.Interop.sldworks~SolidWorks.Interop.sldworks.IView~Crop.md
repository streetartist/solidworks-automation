# Crop Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Crop`

Obsolete. Superseded by IView::Crop2.
Obsolete. Superseded by [IView::Crop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Crop2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Crop() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.Crop()
```

```

System.int Crop()
```

```

System.int Crop(); 
```

#### Return Value

Crop view status as defined in [swCropViewErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCropViewErrors_e.html)

Example

[Crop View (VBA)](Crop_View_Example_VB.htm)  
[Crop View (VB.NET)](Crop_View_Example_VBNET.htm)  
[Crop View (C#)](Crop_View_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
