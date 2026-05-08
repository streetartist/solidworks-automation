# TextScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~TextScale`

Gets or sets the value with which to scale the tolerance font for a hole callout.
Gets or sets the value with which to scale the tolerance font for a hole callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TextScale As System.Double
```

```

Dim instance As ICalloutVariable
Dim value As System.Double
 
instance.TextScale = value
 
value = instance.TextScale
```

```

System.double TextScale {get; set;}
```

```

property System.double TextScale {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 <= value with which to scale the tolerance font <= 10.0

Remarks

Set [ICalloutVariable::UseTextScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~UseTextScale.md) to true to enable setting this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.md)  
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.md)  
[ICalloutVariable::FitTextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextScale.md)  
[ICalloutVariable::FitUseTextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitUseTextScale.md)
