# Value Property (IDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~Value`

Obsolete. Superseded by IDimension::GetValue3, IDimension::IGetValue3, IDimension::ISetValue3, and IDimension::SetValue3.
Obsolete. Superseded by [IDimension::GetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.md), [IDimension::IGetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.md), [IDimension::ISetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.md), and [IDimension::SetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Value As System.Double
```

```

Dim instance As IDimension
Dim value As System.Double
 
instance.Value = value
 
value = instance.Value
```

```

System.double Value {get; set;}
```

```

property System.double Value {
   System.double get();
   void set (    System.double value);
}
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)
