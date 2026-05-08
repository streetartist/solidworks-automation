# ZoomByFactor Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ZoomByFactor`

Modifies the zoom factor for the model view.
Modifies the zoom factor for the model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ZoomByFactor( _
   ByVal Factor As System.Double _
) 
```

```

Dim instance As IModelView
Dim Factor As System.Double
 
instance.ZoomByFactor(Factor)
```

```

void ZoomByFactor( 
   System.double Factor
)
```

```

void ZoomByFactor( 
   System.double Factor
) 
```

#### Parameters

*Factor*
:   Zoom factor

Remarks

The zoom factor should be in the range 0.0 < factor < 2.0. For factor greater than 1, the model view is zoomed in, for factor less than 1 the model view is zoomed out.

Example

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
