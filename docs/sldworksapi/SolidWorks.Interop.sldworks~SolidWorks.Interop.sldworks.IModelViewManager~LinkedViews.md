# LinkedViews Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~LinkedViews`

Gets or sets whether linking of viewports is enabled in this document.
Gets or sets whether linking of viewports is enabled in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkedViews As System.Boolean
```

```

Dim instance As IModelViewManager
Dim value As System.Boolean
 
instance.LinkedViews = value
 
value = instance.LinkedViews
```

```

System.bool LinkedViews {get; set;}
```

```

property System.bool LinkedViews {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if linking of viewports is enabled in this document, false if not

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
[IModelView::Linked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Linked.md)  
[IModelViewManager::ViewportDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ViewportDisplay.md)
