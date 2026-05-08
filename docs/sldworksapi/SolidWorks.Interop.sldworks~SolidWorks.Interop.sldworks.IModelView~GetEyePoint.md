# GetEyePoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetEyePoint`

Gets the eye position for perspective viewing.
Gets the eye position for perspective viewing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEyePoint() As System.Object
```

```

Dim instance As IModelView
Dim value As System.Object
 
value = instance.GetEyePoint()
```

```

System.object GetEyePoint()
```

```

System.Object^ GetEyePoint(); 
```

#### Return Value

Array of 3 doubles describing the eye position in screen space

Remarks

The values are returned in pixels and are the location of the eyepoint relative to the screen space origin (upper-left corner of window). The Z value reflects the distance from the eye point to the object center. These values are affected by the view scale.

To use these values, you should apply them after you have obtained the current view orientation matrix using ModelView::Xform.

The Z value (in pixels) will typically be close to

[( [IModelView::GetViewPlaneDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.md) / ("Object Sizes Away")) \* ("Object Sizes Away" + 0.5) ]

The perspective view is created based on the value entered by the end-user for Object Sizes Away. If the user specifies 3 objects away, then the eye point is positioned 3 body diameters from the view plane, where the view plane is located at the front of the body as seen from this particular orientation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::AddPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~AddPerspective.md)  
[IModelView::IGetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetEyePoint.md)  
[IModelView::ISetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetEyePoint.md)  
[IModelView::SetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetEyePoint.md)  
[IModelView::GetViewPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.md)  
[IModelView::HasPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HasPerspective.md)  
[IModelView::RemovePerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RemovePerspective.md)  
[IModelView::Scale2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2.md)
