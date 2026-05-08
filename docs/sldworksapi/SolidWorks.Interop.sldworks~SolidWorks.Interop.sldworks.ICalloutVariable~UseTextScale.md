# UseTextScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~UseTextScale`

Gets or sets whether to use the value with which to scale the tolerance text for a hole callout.
Gets or sets whether to use the value with which to scale the tolerance text for a hole callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseTextScale As System.Boolean
```

```

Dim instance As ICalloutVariable
Dim value As System.Boolean
 
instance.UseTextScale = value
 
value = instance.UseTextScale
```

```

System.bool UseTextScale {get; set;}
```

```

property System.bool UseTextScale {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the value with which to scale the tolerance text, false to not

Remarks

Call [ICalloutVariable::TextScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~TextScale.md) to get or set the value with which to scale the tolerance text.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.md)  
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.md)
