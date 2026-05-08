# SetSecondArrow Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetSecondArrow`

Sets the second arrow characteristics of this diameter display dimension.
Sets the second arrow characteristics of this diameter display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetSecondArrow( _
   ByVal UseDoc As System.Boolean, _
   ByVal SecondArrow As System.Boolean _
) 
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim SecondArrow As System.Boolean
 
instance.SetSecondArrow(UseDoc, SecondArrow)
```

```

void SetSecondArrow( 
   System.bool UseDoc,
   System.bool SecondArrow
)
```

```

void SetSecondArrow( 
   System.bool UseDoc,
   System.bool SecondArrow
) 
```

#### Parameters

*UseDoc*
:   True uses the document setting for second arrows, false uses the setting specified by the SecondArrow argument

*SecondArrow*
:   Enables or disables the display of the second arrow on this display dimension if UseDoc is false

Remarks

For diameter dimensions, the second outside arrow is the arrow that appears on the opposite side of the arc from the dimension text. This occurs only when the text is outside of the arc.

Display of this arrow is optional, and is controlled by a value stored in one of two places: on the owning document or on the individual display dimension. This method allows you to determine which setting to use: the document default or the value specified in the secondArrow argument.

The UseDoc argument indicates whether to use the document default setting for second arrows. If it is false, then the SecondArrow argument indicates whether or not the second arrow is enabled.

Use [IDisplayDimension::GetUseDocSecondArrow](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocSecondArrow.md) and [IDisplayDimension::GetSecondArrow](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetSecondArrow.md) to get the current values for these settings.

This method applies to only diameter dimensions. If you execute this method with any other types of dimensions, SOLIDWORKS returns false.

After using this method, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::ArrowSide Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ArrowSide.md)
