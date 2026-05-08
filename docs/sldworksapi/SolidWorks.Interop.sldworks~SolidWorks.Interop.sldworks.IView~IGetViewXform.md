# IGetViewXform Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetViewXform`

Gets the transform from model space origin to drawing space origin.
Gets the transform from model space origin to drawing space origin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetViewXform() As System.Double
```

```

Dim instance As IView
Dim value As System.Double
 
value = instance.IGetViewXform()
```

```

System.double IGetViewXform()
```

```

System.double IGetViewXform(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is formatted as the following array of 13 doubles:

- [0-8] is a 3x3 matrix of the view rotation
- [9-11] is a 1x3 vector of translation
- [12] is the scaling of the transformation

[IView::GetXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.md) and [IView::IGetXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.md) return the location of the drawing view center with respect to the drawing origin.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetViewXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetViewXform.md)  
[IView::ModelToViewTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ModelToViewTransform.md)
