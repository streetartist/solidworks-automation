# FixProjectedLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~FixProjectedLength`

Gets or sets whether to fix the projected length for this jog feature.
Gets or sets whether to fix the projected length for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FixProjectedLength As System.Boolean
```

```

Dim instance As IJogFeatureData
Dim value As System.Boolean
 
instance.FixProjectedLength = value
 
value = instance.FixProjectedLength
```

```

System.bool FixProjectedLength {get; set;}
```

```

property System.bool FixProjectedLength {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True fixes the projected length, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)  
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.md)
