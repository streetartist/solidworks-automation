# HideMagnifyingGlass Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HideMagnifyingGlass`

Hides the Magnifying Glass tool.
Hides the Magnifying Glass tool.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub HideMagnifyingGlass() 
```

```

Dim instance As IModelView
 
instance.HideMagnifyingGlass()
```

```

void HideMagnifyingGlass()
```

```

void HideMagnifyingGlass(); 
```

Example

**Visual Basic for Applications (VBA)**

'----------------------------------------  
'  
' Preconditions: Model document is open.  
'  
' Postconditions: None  
'  
'----------------------------------------  
Option Explicit

Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swModelView As SldWorks.ModelView  
Sub main()

Set swApp = Application.SldWorks  
Set swModel = swApp.**ActiveDoc**  
Set swModelView = swModel.**ActiveView**

swModelView.**ShowMagnifyingGlass** -0.01928933522023, 0.004431675106825, -0.001816629754713, 2, True, True  
swModelView.**MoveMagnifyingGlass** -0.01928933522023, 0.004431675106825, -0.004  
swModelView.**MoveMagnifyingGlass** -0.01928933522023, 0.004431675106825, -0.016  
swModelView.**HideMagnifyingGlass**

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::MoveMagnifyingGlass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~MoveMagnifyingGlass.md)  
[IModelView::ShowMagnifyingGlass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ShowMagnifyingGlass.md)
