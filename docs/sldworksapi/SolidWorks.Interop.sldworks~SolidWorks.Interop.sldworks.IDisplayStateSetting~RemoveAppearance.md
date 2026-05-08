# RemoveAppearance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~RemoveAppearance`

Gets or sets whether to remove appearances for this display state setting.
Gets or sets whether to remove appearances for this display state setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RemoveAppearance As System.Boolean
```

```

Dim instance As IDisplayStateSetting
Dim value As System.Boolean
 
instance.RemoveAppearance = value
 
value = instance.RemoveAppearance
```

```

System.bool RemoveAppearance {get; set;}
```

```

property System.bool RemoveAppearance {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to remove appearances, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md)  
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.md)
