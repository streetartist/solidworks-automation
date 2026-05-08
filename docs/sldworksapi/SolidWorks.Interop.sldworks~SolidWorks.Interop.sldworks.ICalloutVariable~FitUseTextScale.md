# FitUseTextScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitUseTextScale`

Gets or sets whether to use the fit tolerance font scale value in a hole callout.
Gets or sets whether to use the fit tolerance font scale value in a hole callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FitUseTextScale As System.Boolean
```

```

Dim instance As ICalloutVariable
Dim value As System.Boolean
 
instance.FitUseTextScale = value
 
value = instance.FitUseTextScale
```

```

System.bool FitUseTextScale {get; set;}
```

```

property System.bool FitUseTextScale {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the fit tolerance font scale value, false to not

Remarks

Use [ICalloutVariable::FitTextScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextScale.md) to get or set the fit tolerance font scale value in a hole callout.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.md)  
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.md)  
[ICalloutVariable::TextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~TextScale.md)  
[ICalloutVariable::UseTextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~UseTextScale.md)  
[ICalloutVariable::HoleFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~HoleFit.md)  
[ICalloutVariable::ShaftFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShaftFit.md)
