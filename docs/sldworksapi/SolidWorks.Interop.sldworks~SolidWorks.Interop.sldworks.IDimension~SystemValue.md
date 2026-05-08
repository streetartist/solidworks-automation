# SystemValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SystemValue`

Obsolete. Superseded by IDimension::GetSystemValue3, IDimension::IGetSystemValue3, IDimension::SetSystemValue3, and IDimension::ISetSystemValue3.
Obsolete. Superseded by [IDimension::GetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.md), [IDimension::IGetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.md), [IDimension::SetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.md), and [IDimension::ISetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SystemValue As System.Double
```

```

Dim instance As IDimension
Dim value As System.Double
 
instance.SystemValue = value
 
value = instance.SystemValue
```

```

System.double SystemValue {get; set;}
```

```

property System.double SystemValue {
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
