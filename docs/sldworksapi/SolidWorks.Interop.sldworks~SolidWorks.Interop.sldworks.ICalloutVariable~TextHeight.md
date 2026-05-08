# TextHeight Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~TextHeight`

Gets or sets the height of the tolerance text in a hole callout.
Gets or sets the height of the tolerance text in a hole callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TextHeight As System.Double
```

```

Dim instance As ICalloutVariable
Dim value As System.Double
 
instance.TextHeight = value
 
value = instance.TextHeight
```

```

System.double TextHeight {get; set;}
```

```

property System.double TextHeight {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Height of the tolerance text

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.md)  
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.md)  
[ICalloutVariable::FitTextHeight Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextHeight.md)
