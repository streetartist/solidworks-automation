# LoadModel Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~LoadModel`

Loads the model if the model has not already been loaded for this drawing view.
Loads the model if the model has not already been loaded for this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadModel() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.LoadModel()
```

```

System.int LoadModel()
```

```

System.int LoadModel(); 
```

#### Return Value

0 if the model was loaded, -1 if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IsModelLoaded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelLoaded.md)  
[IView::IsModelOutOfDate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelOutOfDate.md)
