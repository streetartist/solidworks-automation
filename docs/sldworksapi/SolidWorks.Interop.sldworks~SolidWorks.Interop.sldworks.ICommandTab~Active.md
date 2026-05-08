# Active Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~Active`

Gets or sets whether this CommandManager tab is active.
Gets or sets whether this CommandManager tab is active.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Active As System.Boolean
```

```

Dim instance As ICommandTab
Dim value As System.Boolean
 
instance.Active = value
 
value = instance.Active
```

```

System.bool Active {get; set;}
```

```

property System.bool Active {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if this CommandManager tab is active, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.md)  
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.md)
