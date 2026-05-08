# ResponseAType Property (IMessageBarDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~ResponseAType`

Gets or sets the first response user control for this message bar.
Gets or sets the first response user control for this message bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ResponseAType As System.Integer
```

```

Dim instance As IMessageBarDefinition
Dim value As System.Integer
 
instance.ResponseAType = value
 
value = instance.ResponseAType
```

```

System.int ResponseAType {get; set;}
```

```

property System.int ResponseAType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

First response user control as defined by [swUserMessageBarResponseType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserMessageBarResponseType_e.html)

Remarks

Default value of this property is swUserMessageBarResponseType\_e.swUserMessageBarResponseType\_None.

Example

See the [IMessageBarHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.md)  
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.md)
