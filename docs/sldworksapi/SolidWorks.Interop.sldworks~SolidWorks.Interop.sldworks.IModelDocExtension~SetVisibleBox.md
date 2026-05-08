# SetVisibleBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox`

Sets the visible bounding box for Zoom to Fit for a part or an assembly.
Sets the visible bounding box for Zoom to Fit for a part or an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetVisibleBox( _
   ByVal UpperLeft As MathPoint, _
   ByVal LowerRight As MathPoint _
) 
```

```

Dim instance As IModelDocExtension
Dim UpperLeft As MathPoint
Dim LowerRight As MathPoint
 
instance.SetVisibleBox(UpperLeft, LowerRight)
```

```

void SetVisibleBox( 
   MathPoint UpperLeft,
   MathPoint LowerRight
)
```

```

void SetVisibleBox( 
   MathPoint^ UpperLeft,
   MathPoint^ LowerRight
) 
```

#### Parameters

*UpperLeft*
:   Upper-left [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of the visible bounding box

*LowerRight*
:   Lower-right [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of the visible bounding box

Remarks

Use:

- [IModelDocExtension::GetVisibleBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.md) to get the visible bounding box for a Zoom to Fit operation.
- [IModelDocExtension::RemoveVisibleBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.md) to remove the visible bounding box  for a Zoom to Fit operation and to return the size of the bounding box to the size calculated by SOLIDWORKS.

Example

[Set Visible Bounding Box for Zoom to Fit (C#)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_CSharp.htm)  
[Set Visible Bounding Box for Zoom to Fit (C#)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_VBNET.htm)  
[Set Visible Bounding Box for Zoom to Fit (VBA)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
