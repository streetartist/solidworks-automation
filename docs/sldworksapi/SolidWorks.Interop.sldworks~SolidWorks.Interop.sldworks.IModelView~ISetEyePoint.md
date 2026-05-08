# ISetEyePoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetEyePoint`

Sets the eye position for perspective viewing.
Sets the eye position for perspective viewing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetEyePoint( _
   ByRef Eyept As System.Double _
) As System.Boolean
```

```

Dim instance As IModelView
Dim Eyept As System.Double
Dim value As System.Boolean
 
value = instance.ISetEyePoint(Eyept)
```

```

System.bool ISetEyePoint( 
   ref System.double Eyept
)
```

```

System.bool ISetEyePoint( 
   System.double% Eyept
) 
```

#### Parameters

*Eyept*
:   Array of 3 doubles describing the eye position in screen space

#### Return Value

True if the eye point is set successfully, false if not

Remarks

The values are returned in pixels and are the location of the eye point relative to the screen-space origin (upper-left corner of window). The Z value, in pixels, reflects the distance from the eye point to the object center. These values will be affected by the view scale.

To use these values, you should apply them after you have obtained the current view orientation matrix using [IModelView::Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Transform.md).

The Z value typically are close to

[( [IModelView::GetViewPlaneDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.md) / ("Object Sizes Away")) \* ("Object Sizes Away" + 0.5) ]

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::AddPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~AddPerspective.md)  
[IModelView::GetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetEyePoint.md)  
[IModelView::GetIsoPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetIsoPlaneDistance.md)  
[IModelView::GetViewPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.md)  
[IModelView::HasPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HasPerspective.md)  
[IModelView::IGetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetEyePoint.md)  
[IModelView::SetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetEyePoint.md)  
[IModelView::RemovePerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RemovePerspective.md)  
[IModelView::Scale2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2.md)
