# ShowParenthesis Property (ICalloutVariable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShowParenthesis`

Gets or sets whether to show parentheses around linear tolerance dimensions in a hole callout.
Gets or sets whether to show parentheses around linear tolerance dimensions in a hole callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowParenthesis As System.Boolean
```

```

Dim instance As ICalloutVariable
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

True to show parentheses around linear tolerance dimensions, false to not

Remarks

This property supports bilateral, symmetric, or fit-with-tolerance types only.

In SOLIDWORKS 2016 and later, use this property to set whether to show parentheses around linear tolerance dimensions in a hole callout. Calling [IDimensionTolerance::ShowParenthesis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~ShowParenthesis.md) to set whether to show parentheses around linear tolerance dimensions in a hole callout does not override this property's setting.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.md)  
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.md)
