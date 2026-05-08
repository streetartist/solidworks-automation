# ViewportDisplay Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ViewportDisplay`

Sets the model's viewport arrangement.
Sets the model's viewport arrangement.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

WriteOnly Property ViewportDisplay As System.Integer
```

```

Dim instance As IModelViewManager
 
instance.ViewportDisplay = value
```

```

System.int ViewportDisplay {set;}
```

```

property System.int ViewportDisplay {
   void set (    System.int value);
}
```

#### Property Value

Viewport arrangement as defined by [swViewportDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewportDisplay_e.html)

Example

[Set Viewports (VB.NET)](Set_Viewports_Example_VBNET.htm)  
[Set Viewports (VBA)](Set_Viewports_Example_VB.htm)  
[Set Viewports (C#)](Set_Viewports_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::LinkedViews Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~LinkedViews.md)  
[IModelView::Linked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Linked.md)
