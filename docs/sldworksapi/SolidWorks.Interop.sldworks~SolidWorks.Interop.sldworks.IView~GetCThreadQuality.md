# GetCThreadQuality Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreadQuality`

Gets the cosmetic thread display quality in this view.
Gets the cosmetic thread display quality in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCThreadQuality() As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
value = instance.GetCThreadQuality()
```

```

System.bool GetCThreadQuality()
```

```

System.bool GetCThreadQuality(); 
```

#### Return Value

True if precision quality, false if draft quality

Example

See the [IView::SetDisplayMode4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode4.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::SetDisplayMode4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode4.md)
