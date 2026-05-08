# VisibilityViewTools Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~VisibilityViewTools`

Gets or sets the visibility of the Heads-up View Toolbar for this model view.
Gets or sets the visibility of the Heads-up View Toolbar for this model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property VisibilityViewTools As System.Boolean
```

```

Dim instance As IModelView
Dim value As System.Boolean
 
instance.VisibilityViewTools = value
 
value = instance.VisibilityViewTools
```

```

System.bool VisibilityViewTools {get; set;}
```

```

property System.bool VisibilityViewTools {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the Heads-up View toolbar is visible, false if not

Remarks

After setting this property to false, call [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) or [IModelView::IGraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.md) to repaint the entire graphics window.

Example

'-----------------------------------------

'

' Preconditions: Drawing document is open and

'                Heads-up View toolbar is visible.

'

' Postcondition: Heads-up View toolbar is hidden.

'

'------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swModelView As SldWorks.ModelView

Dim vRect as Variant

Sub main()

Set swApp = Application.SldWorks

Set swModel = swApp.ActiveDoc

Set swModelView = swModel.ActiveView

' Assume Heads-up View toolbar is visible (True)

Debug.Print "Heads-up View toolbar visible: " & swModelView.VisibilityViewTools

' Hide Heads-up View toolbar (False)

swModelView.VisibilityViewTools = False

Debug.Print "Hands-up View toolbar visible: " & swModelView.VisibilityViewTools

swModelView.GraphicsRedraw(vRect)

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
