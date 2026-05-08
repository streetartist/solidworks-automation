# IncludeDoNotShowAgain Property (IMessageBarDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~IncludeDoNotShowAgain`

Gets or sets whether to display the "Do not show again" check box for this message bar.
Gets or sets whether to display the "Do not show again" check box for this message bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeDoNotShowAgain As System.Boolean
```

```

Dim instance As IMessageBarDefinition
Dim value As System.Boolean
 
instance.IncludeDoNotShowAgain = value
 
value = instance.IncludeDoNotShowAgain
```

```

System.bool IncludeDoNotShowAgain {get; set;}
```

```

property System.bool IncludeDoNotShowAgain {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True (default) to display the check box, false to not.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.md)  
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.md)
