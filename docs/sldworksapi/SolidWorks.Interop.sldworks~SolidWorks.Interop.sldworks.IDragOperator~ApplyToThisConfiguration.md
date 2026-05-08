# ApplyToThisConfiguration Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ApplyToThisConfiguration`

Gets or sets the configurations to which to apply the movement of the components.
Gets or sets the configurations to which to apply the movement of the components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ApplyToThisConfiguration As System.Boolean
```

```

Dim instance As IDragOperator
Dim value As System.Boolean
 
instance.ApplyToThisConfiguration = value
 
value = instance.ApplyToThisConfiguration
```

```

System.bool ApplyToThisConfiguration {get; set;}
```

```

property System.bool ApplyToThisConfiguration {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True applies the movement of the components only to the active configuration, false applies it to all configurations

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)
