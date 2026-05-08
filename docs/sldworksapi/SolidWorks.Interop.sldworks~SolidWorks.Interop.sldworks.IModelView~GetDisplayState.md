# GetDisplayState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetDisplayState`

Gets the display state of this model view.
Gets the display state of this model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayState( _
   ByVal DisplayType As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelView
Dim DisplayType As System.Integer
Dim value As System.Boolean
 
value = instance.GetDisplayState(DisplayType)
```

```

System.bool GetDisplayState( 
   System.int DisplayType
)
```

```

System.bool GetDisplayState( 
   System.int DisplayType
) 
```

#### Parameters

*DisplayType*
:   Display setting to check as defined in [swViewDisplayType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewDisplayType_e.html)

#### Return Value

True if the setting specified is turned on, false if not

Remarks

By passing in an available DisplayType option, you can check various display conditions for the view. For example, if you want to know if a view is shaded, you could make the following call in Visual Basic:

res = mView.GetDisplayState( swIsViewShaded )

Example

[Get Display State (VBA)](Get_Display_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
