# Position Property (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Position`

Gets or sets the X and Y location of the model view's geometric center, relative to the drawing sheet origin.
Gets or sets the X and Y location of the model view's geometric center, relative to the drawing sheet origin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Position As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
instance.Position = value
 
value = instance.Position
```

```

System.object Position {get; set;}
```

```

property System.Object^ Position {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of 2 doubles (see **Remarks**)

Remarks

Any view alignments that might affect this view are handled the same way as if you were using the SOLIDWORKS user interface to draw the view to move it. If it is aligned with another view, it will only be allowed to move along the alignment vector. If it has child views that are aligned with it, those views will also be moved along with this view.

Changing this property can cause changes to the graphics of the drawing. After making all the view-related changes, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) to regenerate the drawing to see these changes.

Example

[Insert and Position DXF File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)  
[Reposition Drawing Views to Avoid Overlap (VBA)](Reposition_Drawing_Views_to_Avoid_Overlap_Example_VB.htm)  
[Get View Bounding Box and Position (C#)](Get_View_Bounding_Box_and_Position_Example_CSharp.htm)  
[Get View Bounding Box and Position (VB.NET)](Get_View_Bounding_Box_and_Position_Example_VBNET.htm)  
[Get View Bounding Box and Position (VBA)](Get_View_Bounding_Box_and_Position_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IPosition.md)  
[IView::ModelToViewTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ModelToViewTransform.md)  
[IView::SetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetXform.md)  
[IView::ISetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetXform.md)  
[IView::IGetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.md)  
[IView::IGetViewXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetViewXform.md)  
[IView::GetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.md)  
[IView::GetViewXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetViewXform.md)  
[IView::PositionLocked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~PositionLocked.md)
