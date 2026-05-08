# IsModelLoaded Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelLoaded`

Gets whether the model is loaded in this drawing view.
Gets whether the model is loaded in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsModelLoaded() As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
value = instance.IsModelLoaded()
```

```

System.bool IsModelLoaded()
```

```

System.bool IsModelLoaded(); 
```

#### Return Value

True if the model has been loaded, false if not

Remarks

If the drawing document was loaded as Detached, then the return value will be false. To load the model, use [IView::LoadModel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~LoadModel.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IsModelOutOfDate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelOutOfDate.md)
