# DAssemblyDocEvents_DynamicHighlightNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DynamicHighlightNotifyEventHandler`

Post-notifies the application when dynamic highlighting of the selected object changes from on to off, and vice versa.
Post-notifies the application when dynamic highlighting of the selected object changes from on to off, and vice versa.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_DynamicHighlightNotifyEventHandler( _
   ByVal bHighlightState As System.Boolean _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_DynamicHighlightNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_DynamicHighlightNotifyEventHandler( 
   System.bool bHighlightState
)
```

```

public delegate System.int DAssemblyDocEvents_DynamicHighlightNotifyEventHandler( 
   System.bool bHighlightState
)
```

#### Parameters

*bHighlightState*
:   True if highlighting is on, false if it is off

Remarks

If developing a C++ application, use [swAssemblyDynamicHighlightNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

To send this notification, specify -1 for the index for any of the [ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md) methods. See **Example**.

Example

**' VBA**

Private Function assy\_DynamicHighlightNotify() As Long

Dim one As Object

Dim x As Integer

Dim pt As Variant

Set one = mgr.GetSelectedObject5(-1)

If Not one Is Nothing Then

    Debug.Print mgr.GetSelectedObjectType2(-1)

    one.Select True

    pt = mgr.GetSelectionPoint(-1)

    If Not IsEmpty(pt) Then

        Debug.Print pt(0), pt(1), pt(2)

    Else

        Debug.Print "Object selected in FeatureManager design tree, so no points."

    End If

Else

    Debug.Print "Dynamic highlighting is now off."

End If

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_DynamicHighlightNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DynamicHighlightNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
