# GetUseDocArrowHeadStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocArrowHeadStyle`

Gets whether this display dimension uses the document default setting for dimension arrowhead style.
Gets whether this display dimension uses the document default setting for dimension arrowhead style.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUseDocArrowHeadStyle() As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.GetUseDocArrowHeadStyle()
```

```

System.bool GetUseDocArrowHeadStyle()
```

```

System.bool GetUseDocArrowHeadStyle(); 
```

#### Return Value

True if this display dimension uses the document setting, false if it uses the local display dimension setting

Remarks

The arrowhead style for a display dimension is controlled by a value stored in one of two places: on the owning document or on the individual display dimension. This method gets the setting that indicates which setting is currently in use.

Use [IDisplayDimension::SetArrowHeadStyle2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetArrowHeadStyle2.md) to set this value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetArrowHeadStyle2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetArrowHeadStyle2.md)
