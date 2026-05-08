# KeepBody Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~KeepBody`

Gets or sets whether to keep the original solid body when converting to sheet metal.
Gets or sets whether to keep the original solid body when converting to sheet metal.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepBody As System.Boolean
```

```

Dim instance As IConvertSolidFeatureData
Dim value As System.Boolean
 
instance.KeepBody = value
 
value = instance.KeepBody
```

```

System.bool KeepBody {get; set;}
```

```

property System.bool KeepBody {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to keep the original solid body, false to let the original body be consumed by the convert solid feature

Example

See the [IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)
