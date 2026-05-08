# IgnoreMultiple Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~IgnoreMultiple`

Gets and sets whether to create balloons for multiple instances of an item.
Gets and sets whether to create balloons for multiple instances of an item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IgnoreMultiple As System.Boolean
```

```

Dim instance As IAutoBalloonOptions
Dim value As System.Boolean
 
instance.IgnoreMultiple = value
 
value = instance.IgnoreMultiple
```

```

System.bool IgnoreMultiple {get; set;}
```

```

property System.bool IgnoreMultiple {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to create a balloon for only one instance of an item, false to create multiple balloons for multiple instances of an item

Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

Example

See [IAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)  
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.md)
