# Severity Property (IMessageBarDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~Severity`

Gets or sets the severity level of this message bar.
Gets or sets the severity level of this message bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Severity As System.Integer
```

```

Dim instance As IMessageBarDefinition
Dim value As System.Integer
 
instance.Severity = value
 
value = instance.Severity
```

```

System.int Severity {get; set;}
```

```

property System.int Severity {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Severity level as defined by [swUserMessageBarSeverity\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserMessageBarSeverity_e.html)

Remarks

The default value of this property is swUserMessageBarSeverity\_e.swUserMessageBarSeverity\_Information.

Example

See the [IMessageBarHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.md)  
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.md)
