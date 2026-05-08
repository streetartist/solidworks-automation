# GetSecondArrow Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetSecondArrow`

Gets whether this diameter display dimension has the second arrow enabled.
Gets whether this diameter display dimension has the second arrow enabled.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSecondArrow() As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.GetSecondArrow()
```

```

System.bool GetSecondArrow()
```

```

System.bool GetSecondArrow(); 
```

#### Return Value

True if the second arrow is displayed, false if the second arrow is not displayed (see **Remarks**)

Remarks

For diameter dimensions, the second outside arrow is the arrow that appears on the opposite side of the arc from the dimension text. This occurs only when the text is outside of the arc.

Display of this arrow is optional, and is controlled by a value stored in one of two places: on the owning document or on the individual display dimension. Use [IDisplayDimension::GetUseDocSecondArrow](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocSecondArrow.md) to determine whether the document or the individual display dimension is controlling the second arrow display.

The return value from this method is not valid when the document is controlling the display of second arrows.

This method applies only to diameter dimensions. If this method is executed on any other type of dimension, SOLIDWORKS returns false.

Use [IDisplayDimension::SetSecondArrow](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetSecondArrow.md) to set the second arrow values.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetUseDocSecondArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocSecondArrow.md)  
[IDisplayDimension::SetSecondArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetSecondArrow.md)  
[IDisplayDimension::ArrowSide Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ArrowSide.md)
