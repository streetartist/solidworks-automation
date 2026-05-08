# SetDual Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetDual`

Obsolete. Superseded by IDisplayDimension::SetDual2.
Obsolete. Superseded by [IDisplayDimension::SetDual2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetDual2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDual( _
   ByVal UseDoc As System.Boolean _
) 
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
 
instance.SetDual(UseDoc)
```

```

void SetDual( 
   System.bool UseDoc
)
```

```

void SetDual( 
   System.bool UseDoc
) 
```

#### Parameters

*UseDoc*
:   True uses the document setting, false uses the opposite of the document setting (see **Remarks**)

Remarks

Dual dimensions can use either the same top, bottom, right, or left setting as the document or an opposite top, bottom, right, or left setting. This method allows you to set a dual dimension to use the current document setting or the opposite setting.

Use [IDisplayDimension::GetUseDocDual](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocDual.md) to get the current value of this setting.

After using this method, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::Split Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Split.md)
