# ToleranceMin Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceMin`

Gets or sets the minimum tolerance for a hole callout.
Gets or sets the minimum tolerance for a hole callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ToleranceMin As System.Double
```

```

Dim instance As ICalloutVariable
Dim value As System.Double
 
instance.ToleranceMin = value
 
value = instance.ToleranceMin
```

```

System.double ToleranceMin {get; set;}
```

```

property System.double ToleranceMin {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Minimum tolerance

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.md)  
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.md)  
[ICalloutVariable::ToleranceMax Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceMax.md)
