# TranslateBy Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~TranslateBy`

Translates the model view in the screen.
Translates the model view in the screen.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub TranslateBy( _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) 
```

```

Dim instance As IModelView
Dim X As System.Double
Dim Y As System.Double
 
instance.TranslateBy(X, Y)
```

```

void TranslateBy( 
   System.double X,
   System.double Y
)
```

```

void TranslateBy( 
   System.double X,
   System.double Y
) 
```

#### Parameters

*X*
:   Translation in X direction, in meters and relative to X,Y axes of the graphics area

*Y*
:   Translation in Y direction, in meters and relative to Windows X,Y axes of the graphics area

Remarks

This method lets you specify a vector by which to translate the current SOLIDWORKS graphics area. This vector is in meters and is relative to the X,Y axes of the graphics area. This vector has no relation to the SOLIDWORKS triad axis that is displayed in the graphics area. This method is equivalent to the user-interface panning of the graphics area.

Example

[Set Viewports (VB.NET)](Set_Viewports_Example_VBNET.htm)  
[Set Viewports (VBA)](Set_Viewports_Example_VB.htm)  
[Set Viewports (C#)](Set_Viewports_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
