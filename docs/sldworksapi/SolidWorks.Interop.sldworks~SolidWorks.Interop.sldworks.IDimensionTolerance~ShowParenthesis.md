# ShowParenthesis Property (IDimensionTolerance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~ShowParenthesis`

Indicates whether to show parentheses around linear tolerance dimensions.
Indicates whether to show parentheses around linear tolerance dimensions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowParenthesis As System.Boolean
```

```

Dim instance As IDimensionTolerance
Dim value As System.Boolean
 
instance.ShowParenthesis = value
 
value = instance.ShowParenthesis
```

```

System.bool ShowParenthesis {get; set;}
```

```

property System.bool ShowParenthesis {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to show parentheses around linear tolerance dimensions, false to not

Remarks

This property supports bilateral, symmetric, or fit-with-tolerance types only.

In SOLIDWORKS 2016 and later, use [ICalloutVariable::ShowParenthesis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShowParenthesis.md) to set whether to show parentheses in a hole's display dimension with multiple values in a callout. Calling IDimensionTolerance::ShowParenthesis to set whether to show parentheses in a hole's display dimension with multiple values in a callout does not override ICalloutVariable::ShowParenthesis' setting.

To see the effects of changing this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)  
[IDimensionTolerance::ShowParenthesis Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShowParenthesis.md)
