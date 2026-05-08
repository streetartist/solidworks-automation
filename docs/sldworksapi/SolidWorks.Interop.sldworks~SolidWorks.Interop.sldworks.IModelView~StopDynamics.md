# StopDynamics Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StopDynamics`

Ends dynamic model view motion.
Ends dynamic model view motion.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub StopDynamics() 
```

```

Dim instance As IModelView
 
instance.StopDynamics()
```

```

void StopDynamics()
```

```

void StopDynamics(); 
```

Remarks

Use this method with [IModelView::StartDynamics](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StartDynamics.md) at the end of dynamic view motion. This method returns the view to its previous HLR,  HLV, or shaded mode and recalculates the display.

After calling this method, you must call [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) or [IModelDoc2::WindowRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~WindowRedraw.md) to update the display for the end-user.

If the SOLIDWORKS file is in view-only mode and is not displaying a shaded image, then you cannot perform any view rotations. Do not call any of the view rotation functions.

To determine if the file is in view-only mode and is not displaying a shaded image, use [IModelDoc2::IsOpenedViewOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedViewOnly.md) and [IModelView::GetDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetDisplayState.md).

Example

[Dynamic View Rotation (C++)](Dynamic_View_Rotation_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::RotateAboutAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutAxis.md)  
[IModelView::RotateAboutCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutCenter.md)  
[IModelView::RotateAboutPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutPoint.md)  
[IModelView::DynamicMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DynamicMode.md)  
[IModelView::HlrQuality Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HlrQuality.md)
