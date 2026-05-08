# TolerancePrecision Property (ICalloutLengthVariable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable~TolerancePrecision`

Gets or sets number of digits after the decimal point to display the primary tolerance value for the length variable in a hole callout.
Gets or sets number of digits after the decimal point to display the primary tolerance value for the length variable in a hole callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TolerancePrecision As System.Integer
```

```

Dim instance As ICalloutLengthVariable
Dim value As System.Integer
 
instance.TolerancePrecision = value
 
value = instance.TolerancePrecision
```

```

System.int TolerancePrecision {get; set;}
```

```

property System.int TolerancePrecision {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of digits after the decimal point to display the primary tolerance value

Remarks

Call [IDisplayDimension::SetPrecision3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetPrecision3.md) to set the dual tolerance value for a display dimension for a hole callout.

Example

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)  
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)  
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICalloutLengthVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable.md)  
[ICalloutLengthVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable_members.md)  
[ICalloutLengthVariable::Precision Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable~Precision.md)
