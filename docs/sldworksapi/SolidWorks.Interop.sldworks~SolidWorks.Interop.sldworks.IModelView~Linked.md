# Linked Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Linked`

Gets whether or not this viewport is linked or not.
Gets whether or not this viewport is linked or not.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Linked As System.Boolean
```

```

Dim instance As IModelView
Dim value As System.Boolean
 
value = instance.Linked
```

```

System.bool Linked {get;}
```

```

property System.bool Linked {
   System.bool get();
}
```

#### Property Value

True if this viewport is linked, false if not

Example

[Set Viewports (VB.NET)](Set_Viewports_Example_VBNET.htm)  
[Set Viewports (VBA)](Set_Viewports_Example_VB.htm)  
[Set Viewports (C#)](Set_Viewports_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelViewManager::LinkedViews Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~LinkedViews.md)  
[IModelViewManager::ViewportDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ViewportDisplay.md)
