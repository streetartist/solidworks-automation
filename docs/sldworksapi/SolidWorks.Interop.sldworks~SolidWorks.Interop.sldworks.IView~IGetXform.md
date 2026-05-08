# IGetXform Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform`

Gets the matrix used for displaying this drawing view.
Gets the matrix used for displaying this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetXform() As System.Double
```

```

Dim instance As IView
Dim value As System.Double
 
value = instance.IGetXform()
```

```

System.double IGetXform()
```

```

System.double IGetXform(); 
```

#### Return Value

Array of 3 doubles that describe the location and scale of the drawing view (see **Remarks**)

Remarks

The first two values returned are the X and Y locations of the view relative to the sheet origin, and the third value returned is the scale of the drawing view.

Because of a Microsoft compilation issue, the Dispatch name generated in the **swdisp.h** and **swdisp.cpp** files for the Dispatch version of this method is GetXform (with a lower-case letter f). To work around this:

- Use GetXform in your code instead of GetXForm.  
    
  - or -
- Modify the swdisp.h and swdisp.cpp files so that the declaration for GetXForm in the [IView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) object is changed to GetXform. Remember to change it when you upgrade the SOLIDWORKS software.

[IView::GetViewXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetViewXform.md) and [IView::IGetViewXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetViewXform.md) get the transform from model space origin to drawing space origin.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.md)  
[IView::ISetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetXform.md)  
[IView::SetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetXform.md)  
[IView::ModelToViewTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ModelToViewTransform.md)
