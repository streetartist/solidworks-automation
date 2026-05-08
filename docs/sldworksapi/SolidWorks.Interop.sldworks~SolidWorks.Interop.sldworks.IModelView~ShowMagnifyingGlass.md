# ShowMagnifyingGlass Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ShowMagnifyingGlass`

Shows the Magnifying Glass tool at the specified coordinates.
Shows the Magnifying Glass tool at the specified coordinates.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ShowMagnifyingGlass( _
   ByVal Ptx As System.Double, _
   ByVal Pty As System.Double, _
   ByVal Ptz As System.Double, _
   ByVal ZoomFactor As System.Double, _
   ByVal HideOnClick As System.Boolean, _
   ByVal FollowMouse As System.Boolean _
) 
```

```

Dim instance As IModelView
Dim Ptx As System.Double
Dim Pty As System.Double
Dim Ptz As System.Double
Dim ZoomFactor As System.Double
Dim HideOnClick As System.Boolean
Dim FollowMouse As System.Boolean
 
instance.ShowMagnifyingGlass(Ptx, Pty, Ptz, ZoomFactor, HideOnClick, FollowMouse)
```

```

void ShowMagnifyingGlass( 
   System.double Ptx,
   System.double Pty,
   System.double Ptz,
   System.double ZoomFactor,
   System.bool HideOnClick,
   System.bool FollowMouse
)
```

```

void ShowMagnifyingGlass( 
   System.double Ptx,
   System.double Pty,
   System.double Ptz,
   System.double ZoomFactor,
   System.bool HideOnClick,
   System.bool FollowMouse
) 
```

#### Parameters

*Ptx*
:   x coordinate

*Pty*
:   y coordinate

*Ptz*
:   z coordinate

*ZoomFactor*
:   Zoom factor

*HideOnClick*
:   True to hide the Magnifying Glass tool when the mouse is right-clicked, false to not

*FollowMouse*
:   True to have the Magnifying Glass tool follow the pointer, false to not

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
[IModelView::HideMagnifyingGlass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HideMagnifyingGlass.md)  
[IModelView::MoveMagnifyingGlass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~MoveMagnifyingGlass.md)
